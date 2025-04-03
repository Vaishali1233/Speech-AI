import json
from deep_translator import GoogleTranslator

def load_transcript(filename="transcript.json"):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

#using google translate to translate the json file
def translate_text(text, target_language="hi"):
    return GoogleTranslator(source="auto", target=target_language).translate(text)

def translate_transcript(transcript, target_language="hi"):
    translated_transcript = []
    
    for segment in transcript:
        translated_text = translate_text(segment["text"], target_language)
        translated_transcript.append({
            "start": segment["start"],
            "end": segment["end"],
            "text": translated_text
        })
    
    return translated_transcript

def save_translated(transcript, filename="translated.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(transcript, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    transcript_data = load_transcript()
    translated_data = translate_transcript(transcript_data, target_language="hi")
    save_translated(translated_data)
    
    print("Your file saved as translated.json")
