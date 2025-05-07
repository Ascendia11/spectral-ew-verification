import hashlib, pathlib

DATA_DIR = pathlib.Path(__file__).resolve().parent / "data"
OUT_FILE = pathlib.Path(__file__).resolve().parent / "verification.txt"

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    lines = [
        f"{sha256(p)}  {p.name}\n"
        for p in sorted(DATA_DIR.iterdir()) if p.is_file()
    ]
    OUT_FILE.write_text("".join(lines))
    print("Wrote", OUT_FILE)

if __name__ == "__main__":
    main()
