YouTube Video Downloader (yt_dlp)

A simple Python script for downloading YouTube videos – built just for fun and experimentation with `yt_dlp`

## Features

- Downloads YouTube videos directly using URL
- Saves videos in MP4 format for easy playback
- Combines best quality video and audio streams
- Customizable download directory

## Requirements

- Python 3.7+
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) library

To install `yt-dlp`, run:
```sh
pip install yt-dlp
```

## Usage

1. **Edit the Script**
   - Add your target YouTube video URLs to the `URLS` list.
   - Set the `save_path` to your desired directory for downloads.

2. **Run the Script**
   - Execute in your terminal:
     ```sh
     python your_script_name.py
     ```

3. **Example**
```python
URLS = [
    "https://www.youtube.com/watch?v=EXAMPLE_VIDEO_ID"
]
save_path = r"C:\Downloads"
```
The script will download each video in the list and save it as MP4 to the specified folder.

## How It Works

- Uses `yt_dlp` to fetch the best video (MP4) and audio streams, then merges them
- Prints status messages for progress and any errors
- Each downloaded video will be named after its YouTube title for easier organization

## Notes

- This project is for **educational and personal use only**.
- Avoid downloading content you do not own or have permission to download.
- Features can be easily extended, such as batch downloading, playlist support, or adding a GUI.
