from pytube import YouTube
import os

def download_video(url, desired_size):
    try:
        # Get YouTube video details
        yt = YouTube(url)
        video_title = yt.title
        video_stream = yt.streams.filter(file_extension='mp4').first()

        # Download video
        video_stream.download()

        # Check actual file size
        file_size_mb = os.path.getsize(video_title + ".mp4") / (1024 * 1024)

        print(f"Actual file size: {file_size_mb:.2f} MB")

        # Check if the actual size is greater than the desired size
        if file_size_mb > desired_size:
            recommended_size = file_size_mb * 1.1  # Suggest 10% more than the actual size
            print(f"Recommended size: {recommended_size:.2f} MB")
            print("Consider choosing a larger size for better quality.")

        else:
            print("Video downloaded successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Get user input
    video_url = input("Enter YouTube video URL: ")
    desired_size = float(input("Enter desired size of the video in MB: "))

    # Download the video
    download_video(video_url, desired_size)

