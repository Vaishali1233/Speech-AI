import yt_dlp
import whisper
import json
import os

#audio downloaded in wav format
def download_audio(youtube_video_url, output_path="audio.wav"):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
        'outtmpl': "%(title)s.%(ext)s" 
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(youtube_video_url, download=True)
        filename = ydl.prepare_filename(info_dict).rsplit(".", 1)[0] + ".wav"  
    return filename

#transcribes audio using OpenAI whisper
def transcribe_audio(audio_path):
    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    model = whisper.load_model("base") 
    result = model.transcribe(audio_path)

    transcript = []
    for segment in result["segments"]:
        transcript.append({
            "start": segment["start"],
            "end": segment["end"],
            "text": segment["text"]
        })

    return transcript

def save_transcript(transcript, filename="transcript.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(transcript, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    youtube_video_url = "https://www.youtube.com/watch?v=C4QMPhiF_as"
    audio_file = download_audio(youtube_video_url)
    print(f"Downloaded audio: {audio_file}")

    transcript_data = transcribe_audio(audio_file)
    save_transcript(transcript_data)

    print("Your file saved as transcript.json")
