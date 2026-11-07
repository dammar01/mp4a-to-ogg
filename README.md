# mp4a-to-ogg

A simple Python script for batch-converting audio files to **OGG Vorbis** using FFmpeg. Place your files in `sources/`, run the script, and find the converted files in `output/`.

Although the project name refers to MP4A, the script attempts to process **every file** in `sources/`. Formats such as M4A, MP3, WAV, and audio in MP4 files can be used as long as your FFmpeg installation supports them and they contain an audio stream.

## Features

- Converts files sequentially with a single command.
- Produces `.ogg` files using the `libvorbis` encoder at VBR quality `5`.
- Excludes video when converting files that contain video streams.
- Creates the `output/` directory automatically.
- Displays an `[OK]` or `[ERR]` status for each conversion attempt.
- Uses only the Python standard library, with no additional pip packages.

## Requirements

- **Python 3**, preferably version 3.10 or later.
- **FFmpeg**, available as the `ffmpeg` command and built with the `libvorbis` encoder.

Download Python from [python.org](https://www.python.org/downloads/) and FFmpeg from the [official FFmpeg download page](https://ffmpeg.org/download.html). On Windows, add the directory containing `ffmpeg.exe` (usually `bin/`) to your `PATH`, then open a new terminal. On macOS or Linux, FFmpeg is also available through your system's package manager.

Check your installation:

```sh
python --version
ffmpeg -version
ffmpeg -encoders
```

Make sure the encoder list includes `libvorbis`. If your system uses the `python3` command, substitute `python3` in all Python commands below.

## Usage

1. Clone or download this repository, then open a terminal in the project directory containing `main.py`.
2. Create the input directory if it does not already exist:

   ```sh
   mkdir sources
   ```

3. Copy the audio files you want to convert into `sources/`. Keep nonmedia files out of this directory.
4. Run:

   ```sh
   python main.py
   ```

5. Find the converted files in `output/`.

Example file layout after conversion:

```text
mp4a-to-ogg/
├── main.py
├── README.md
├── LICENCE
├── CONTRIBUTING.md
├── .gitignore
├── sources/              # Local input files, excluded from Git
│   ├── recording.m4a
│   └── music.wav
└── output/               # Converted files, excluded from Git
    ├── recording.ogg
    └── music.ogg
```

Example output for successful conversions; file order may vary. The script currently prints its completion and error messages in Indonesian:

```text
[OK] recording.m4a → recording.ogg
[OK] music.wav → music.ogg

Selesai.
```

`Selesai.` means "Done." The `sources/` and `output/` directories are not tracked by Git. After a fresh clone, create `sources/` yourself; the script creates `output/` when it runs.

## How it works and configuration

For each input file, the script runs the equivalent of:

```sh
ffmpeg -y -i "sources/recording.m4a" -vn -c:a libvorbis -q:a 5 "output/recording.ogg"
```

| Setting | Behavior |
| --- | --- |
| `SRC_DIR = Path("./sources")` | Reads input from `sources/`, relative to the terminal's working directory. |
| `OUT_DIR = Path("./output")` | Saves output to `output/`, relative to the terminal's working directory. |
| `-y` | Overwrites existing output files without confirmation. |
| `-vn` | Excludes video streams. |
| `-c:a libvorbis` | Encodes audio using Vorbis in an OGG container. |
| `-q:a 5` | Uses VBR quality `5`; bitrate and output size depend on the input audio. |

To change directories or quality, edit the corresponding values in [main.py](main.py). There are currently no CLI arguments for these settings. See the [FFmpeg documentation](https://ffmpeg.org/ffmpeg.html) and [libvorbis encoder options](https://ffmpeg.org/ffmpeg-codecs.html#libvorbis) for parameter details.

## Behavior and limitations

- **Existing output is overwritten.** Move any files you want to keep before running the script again.
- Output names use the input file's stem. Both `song.m4a` and `song.wav` produce `song.ogg`; whichever file is processed later overwrites the earlier result. The script does not sort the processing order.
- Only files directly inside `sources/` are processed; subdirectories are not traversed.
- File extensions are not filtered. Files without audio or in unsupported formats may fail to convert.
- Vorbis encoding is **lossy**; converting from another lossy format does not improve the source quality.
- The script suppresses detailed FFmpeg logs. Conversion failures reported by FFmpeg produce `[ERR]`, and the script then attempts the next file.
- The `Selesai.` message indicates that the processing loop has ended; it does not guarantee that every file converted successfully. The script does not set a failure exit code for conversions that produce `[ERR]`.
- Failed conversions may leave partial output files. Check the results before using them.
- The script does not delete input files.

## Troubleshooting

| Symptom | What to do |
| --- | --- |
| `Folder ./sources tidak ditemukan` (sources directory not found) | Run from the project directory and create `sources/`. |
| `Tidak ada file di ./sources` (no files in sources) | Place audio files directly in `sources/`, outside any subdirectory. |
| `FileNotFoundError` when calling FFmpeg | Make sure `ffmpeg -version` works in the same terminal. Check your installation and `PATH`. |
| `[ERR] gagal convert: ...` (conversion failed) | Run the example FFmpeg command above with the affected filename to see the detailed error. That command also overwrites the corresponding output. |
| `Unknown encoder 'libvorbis'` | Use an FFmpeg build that includes `libvorbis`, then check `ffmpeg -encoders` again. |
| `PermissionError` | Make sure the input directory is readable and the output directory is writable. |

## Contributing

Bug reports, documentation improvements, and pull requests are welcome. See the [contribution guide](CONTRIBUTING.md) for manual checks and the information to include in a bug report.

## License

This project's code and documentation are licensed under the [MIT License](LICENCE), using the license text published by the [Open Source Initiative](https://opensource.org/license/mit). FFmpeg is separate software with its [own licensing terms](https://ffmpeg.org/legal.html). This project's license does not grant rights to third-party media files.
