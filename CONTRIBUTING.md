# Contributing

Thank you for helping improve mp4a-to-ogg. You can submit documentation improvements, bug reports, and code changes through this repository's Issues or pull requests.

## Setting up your environment

1. Fork and clone the repository, then create a branch for your changes.
2. Install Python 3 and FFmpeg with the `libvorbis` encoder, as described in the [README](README.md#requirements).
3. Create a `sources/` directory and add test audio you have permission to use. There are no pip dependencies to install.

Run all commands from the project directory containing `main.py`. Use `python3` if that is the Python executable name on your system.

## Checking your changes

There is currently no automated test suite. For documentation changes, check that the instructions match the code's behavior and that relative links resolve correctly.

For code changes, use a separate working copy with nonsensitive test input to avoid overwriting your personal conversions. Relevant manual checks include:

1. Run `python main.py` without a `sources/` directory and verify the missing-directory message.
2. Create an empty `sources/` directory and run again; verify the empty-directory message.
3. Add one valid audio file and run again; verify that `[OK]` appears, an `.ogg` file is created, and the audio plays.
4. Add a text file to `sources/`; verify that it produces `[ERR]` and that valid audio files are still processed.
5. Create a subdirectory inside `sources/`; verify that files inside it are skipped, unless the change intentionally adds recursive processing.
6. Check output overwriting and input filename collisions if the change affects file naming.

If FFprobe is available with your FFmpeg installation, inspect the converted file's codec:

```sh
ffprobe -v error -select_streams a:0 -show_entries stream=codec_name -of default=noprint_wrappers=1 "output/recording.ogg"
```

The expected result is `codec_name=vorbis`. The script can currently exit with a success status even when a conversion produces `[ERR]`; do not judge success by the exit code alone.

## Reporting bugs

Include the following information in your Issue:

- Your operating system and Python version from `python --version`.
- Your FFmpeg version from `ffmpeg -version`.
- The command you ran, the expected result, and the actual result.
- The input format and concise steps to reproduce the problem.
- Logs from a direct FFmpeg command if the script only displays `[ERR]`.

Remove personal information from logs before sharing them. Use synthetic media or samples you have permission to publish.

## Submitting pull requests

- Keep each change focused on one clear purpose.
- Follow the existing code style and explain any new dependencies.
- Update the README if usage or behavior changes.
- Describe the checks you actually ran and their results, including any checks you could not complete.
- Exclude private media, converted files, credentials, and local environment files. The `sources/` and `output/` directories are already excluded through `.gitignore`.

Contributions submitted to this project are covered by its [MIT License](LICENCE).
