import os
import sys
import subprocess

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

SOURCE_DIR = r"C:\Users\rexpak\Desktop\code\raco_soundboard\sounds\新增資料夾"
OUTPUT_DIR = r"C:\Users\rexpak\Desktop\code\raco_soundboard\sounds\新增資料夾_output"

os.makedirs(OUTPUT_DIR, exist_ok=True)

for file in os.listdir(SOURCE_DIR):
    if file.lower().endswith(".mp4"):
        input_path = os.path.join(SOURCE_DIR, file)
        output_name = os.path.splitext(file)[0] + ".mp3"
        output_path = os.path.join(OUTPUT_DIR, output_name)

        cmd = [
            "ffmpeg",
            "-i", input_path,
            "-vn",
            "-acodec", "mp3",
            output_path
        ]

        print(f"轉換中: {file} -> {output_name}")

        subprocess.run(
            cmd,
            check=True,
            encoding="utf-8",
            errors="replace"
        )

print("✅ 全部 mp4 已轉成 mp3！")
