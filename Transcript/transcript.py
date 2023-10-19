import os
import openai

print("Rozpoczynam transkrypcję...")

system_prompt = "Jesteś asystentem do transkrypcji. Twoim głównym zadaniem jest przekształcanie mowy z pliku audio w format tekstowy. Twoim zadaniem jest korygowanie wszelkich nieścisłości ortograficznych w przepisanym tekście. Dodawaj tylko niezbędną interpunkcję, taką jak kropki, przecinki i wielkie litery, i korzystaj wyłącznie z podanego kontekstu."


def transcribe(audio_file_path, options):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    print("Przetwarzanie pliku audio...")
    with open(audio_file_path, "rb") as audio_file:
        response = openai.Audio.transcribe("whisper-1", audio_file)
    print("Transkrypcja pliku audio zakończona.")    
    return response['text']


  
filepath = 'path_to_your_file.mp3'

def generate_corrected_transcript(temperature, system_prompt, audio_file):
    print("Poprawianie transkrypcji przy użyciu modelu GPT-4...")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        temperature=temperature,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": transcribe(audio_file, "")
            }
        ]
    )
    print("Poprawianie transkrypcji zakończone.")
    return response['choices'][0]['message']['content']
    


corrected_text = generate_corrected_transcript(0, system_prompt, filepath)

# print(corrected_text)


# Zapisz transkrypcję w pliku o takiej samej nazwie jak plik mp3, ale z rozszerzeniem .txt
base_name = os.path.basename(filepath)  # uzyskaj nazwę bazową pliku mp3
name_without_extension = os.path.splitext(base_name)[0]  # usuń rozszerzenie
txt_filename = name_without_extension + '.txt'  # dodaj rozszerzenie .txt

print("Zapisywanie transkrypcji do pliku...")
with open(txt_filename, 'w', encoding='utf-8') as file:
    file.write(corrected_text)
print("Zapisywanie zakończone.")