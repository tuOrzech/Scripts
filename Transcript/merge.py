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
