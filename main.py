import yt_dlp

def download_youtube_video(video_url, save_path="downloads"):
    try:
        # Prefer video and audio streams that are compatible with mp4
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',
            'merge_output_format': 'mp4',
        }

        print("Downloading...")

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])

        print(f"Video downloaded successfully and saved in: {save_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    URLS = [
        "-----VIDEO-URL-----"
        ]
    for video_url in URLS:
        save_path = r"DEST-DIRECTORY"
        download_youtube_video(video_url, save_path)
