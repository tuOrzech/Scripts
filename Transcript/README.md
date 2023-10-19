# Dokumentacja Transkrypcji Audio

## Wstęp

Ten skrypt służy do transkrypcji plików audio na tekst przy użyciu API OpenAI. Skrypt przetwarza plik audio, a następnie koryguje transkrypcję przy użyciu modelu GPT-4.

## Importowane biblioteki

```python
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



filepath = 'your_file_path'

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

```

## Opis działania

Skrypt rozpoczyna transkrypcję i wyświetla odpowiedni komunikat.
Ustalany jest systemowy monit, który instruuje model GPT-4, jak ma działać.
Skrypt zawiera dwie główne funkcje: `transcribe` i `generate_corrected_transcript`.

## Funkcja `transcribe`

Przyjmuje ścieżkę do pliku audio i opcje.
Ustawia klucz API dla OpenAI.
Otwiera plik audio i przetwarza go przy użyciu funkcji `openai.Audio.transcribe`.
Zwraca przetworzony tekst.

## Funkcja `generate_corrected_transcript`

Przyjmuje temperaturę, systemowy monit i ścieżkę do pliku audio.
Poprawia transkrypcję przy użyciu modelu GPT-4.
Zwraca poprawiony tekst.

Skrypt następnie zapisuje poprawioną transkrypcję w pliku tekstowym o tej samej nazwie co plik audio, ale z rozszerzeniem `.txt`.

## Jak używać

Upewnij się, że masz zainstalowane wymagane biblioteki i że masz dostęp do API OpenAI.
Zmień ścieżkę `filepath` na ścieżkę do twojego pliku audio.
Uruchom skrypt.
Po zakończeniu działania skryptu, sprawdź folder, w którym znajduje się skrypt - powinien tam być plik tekstowy z transkrypcją.

## Uwagi

Upewnij się, że masz odpowiednie uprawnienia do czytania pliku audio i zapisywania pliku tekstowego w wybranej lokalizacji.

```bash
pip3 install openai
```

Klucz API OpenAI powinien być przechowywany w zmiennej środowiskowej OPENAI_API_KEY.

```bash
export OPENAI_API_KEY='your_api_key_here'
```

## Podział dużych plików audio

Jeśli plik audio przekracza limit 25MB, możemy podzielić go na mniejsze kawałki, aby przetworzyć każdy fragment osobno.
Poniżej znajduje się kod, który pozwala podzielić plik audio na fragmenty o długości 12 minut (720 sekund) każdy:

```python

from pydub import AudioSegment

def split_mp3(file_path, chunk_length_in_sec=720):  # Ustawienie na 12 minut (720 sekund)
    audio = AudioSegment.from_mp3(file_path)

    # Długość pliku audio w milisekundach
    length_audio = len(audio)

    # Liczba fragmentów
    num_chunks = int(length_audio / (chunk_length_in_sec * 1000)) + 1

    chunks = []

    for i in range(num_chunks):
        start_time = i * chunk_length_in_sec * 1000
        end_time = (i + 1) * chunk_length_in_sec * 1000

        # Tworzenie fragmentu
        chunk = audio[start_time:end_time]

        # Zapisanie fragmentu do pliku
        chunk_name = f"chunk{i}.mp3"
        chunk.export(chunk_name, format="mp3")
        chunks.append(chunk_name)

    return chunks


```

## Pamiętaj, aby zainstalować bibliotekę pydub oraz ffmpeg przed użyciem powyższego kodu.

## Podział dużych plików audio

Jeśli plik audio przekracza limit 25MB, możemy podzielić go na mniejsze kawałki, aby przetworzyć każdy fragment osobno. Poniżej znajduje się kod, który pozwala podzielić plik audio na fragmenty o długości 12 minut (720 sekund) każdy:

```python
from pydub import AudioSegment

def split_mp3(file_path, chunk_length_in_sec=720):  # Ustawienie na 12 minut (720 sekund)
    audio = AudioSegment.from_mp3(file_path)

    # Długość pliku audio w milisekundach
    length_audio = len(audio)

    # Liczba fragmentów
    num_chunks = int(length_audio / (chunk_length_in_sec * 1000)) + 1

    chunks = []

    for i in range(num_chunks):
        start_time = i * chunk_length_in_sec * 1000
        end_time = (i + 1) * chunk_length_in_sec * 1000

        # Tworzenie fragmentu
        chunk = audio[start_time:end_time]

        # Zapisanie fragmentu do pliku
        chunk_name = f"chunk{i}.mp3"
        chunk.export(chunk_name, format="mp3")
        chunks.append(chunk_name)

    return chunks

# Użyj funkcji, aby podzielić plik
chunks = split_mp3("your_file_path_to_audio.mp3")

print(f"Plik został podzielony na {len(chunks)} fragmentów.")

```

## Łączenie fragmentów transkryptu w jedną całość

Jeśli masz kilka fragmentów transkryptu zapisanych w różnych plikach tekstowych i chcesz je połączyć w jedną całość, możesz użyć poniższego skryptu:

```python
# Lista plików .txt, które chcesz połączyć
files_to_merge = ['chunk0.txt', 'chunk1.txt', 'chunk2.txt', 'chunk3.txt']

# Nazwa pliku wyjściowego
output_file = 'caly_transkrypt.txt'

# Otwórz plik wyjściowy w trybie zapisu
with open(output_file, 'w', encoding='utf-8') as outfile:
    # Przejrzyj każdy plik w liście
    for fname in files_to_merge:
        # Otwórz każdy plik w trybie odczytu
        with open(fname, 'r', encoding='utf-8') as infile:
            # Kopiuj zawartość do pliku wyjściowego
            outfile.write(infile.read())
            # Dodaj nową linię po każdym pliku, aby oddzielić treść
            outfile.write("\n")
```

Po uruchomieniu powyższego skryptu otrzymasz plik o nazwie `caly_transkrypt.txt`, który zawiera połączoną treść wszystkich plików z listy `files_to_merge.`

# Instrukcje dotyczące `ffmpeg`

## Instalacja `ffmpeg` Dla macOS (zakładając, że masz zainstalowane Homebrew):

Aby zainstalować `ffmpeg`, możesz użyć następujących poleceń w terminalu:

```bash
brew install ffmpeg
```

### Pomniejszanie pliku audio

Jeśli chcesz pomniejszyć rozmiar pliku audio, możesz użyć następujących poleceń:

```bash
ffmpeg -i input_filename.mp3 -ab 128k output_filename.mp3
```

```bash
ffmpeg -i input_filename.mp3 -ab 96k output_filename.mp3
```

```bash
ffmpeg -i input_filename.mp3 -ab 64k output_filename.mp3
```
