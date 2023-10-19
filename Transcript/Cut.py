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
chunks = split_mp3("/Users/Kaczor/Desktop/Test/131.mp3")

print(f"Plik został podzielony na {len(chunks)} fragmentów.")
