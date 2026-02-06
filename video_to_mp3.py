import os
import subprocess

VIDEOS_DIR = "videos"
AUDIOS_DIR = "audios"

# create audios folder if not exists
os.makedirs(AUDIOS_DIR, exist_ok=True)

files = os.listdir(VIDEOS_DIR)

for file in files:
    # only process mp4 files
    if not file.lower().endswith(".mp4"):
        continue

    # extract tutorial number safely
    try:
        tutorial_number = file.split("#")[1].split(".")[0]
    except IndexError:
        print(f"Skipping (tutorial number not found): {file}")
        continue

    # output audio filename
    output_audio = f"{tutorial_number}_{file.replace('.mp4','')}.mp3"

    print(f"Processing Tutorial #{tutorial_number}")

    subprocess.run([
        "ffmpeg",
        "-y",  # overwrite if file exists
        "-i", f"{VIDEOS_DIR}/{file}",
        f"{AUDIOS_DIR}/{output_audio}"
    ])

print("✅ All possible videos processed successfully")
