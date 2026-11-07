import subprocess
from pathlib import Path

SRC_DIR = Path("./sources")
OUT_DIR = Path("./output")

# pastikan folder output ada
OUT_DIR.mkdir(exist_ok=True)

def convert_to_ogg(input_path: Path, output_path: Path):
    cmd = [
        "ffmpeg",
        "-y",
        "-i", str(input_path),
        "-vn",
        "-c:a", "libvorbis",
        "-q:a", "5",
        str(output_path)
    ]

    try:
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"[OK] {input_path.name} → {output_path.name}")
    except subprocess.CalledProcessError:
        print(f"[ERR] gagal convert: {input_path.name}")


def main():
    if not SRC_DIR.exists():
        print("Folder ./sources tidak ditemukan")
        return

    files = [f for f in SRC_DIR.iterdir() if f.is_file()]

    if not files:
        print("Tidak ada file di ./sources")
        return

    for file in files:
        output_file = OUT_DIR / (file.stem + ".ogg")
        convert_to_ogg(file, output_file)

    print("\nSelesai.")


if __name__ == "__main__":
    main()