Konwersja Stron PDF na Obrazy przy Użyciu ImageMagick (macOS)
Wstęp
Poniżej znajduje się instrukcja, jak utworzyć i uruchomić skrypt do konwersji poszczególnych stron pliku PDF na obrazy (format PNG lub JPG) przy użyciu narzędzia ImageMagick na macOS.

Wymagania
ImageMagick: Aby zainstalować ImageMagick przy użyciu Homebrew, otwórz Terminal i wpisz:

brew install imagemagick

Krok po Kroku

1. Tworzenie Skryptu
Otwórz Terminal.
Utwórz nowy plik skryptu za pomocą edytora tekstu, na przykład nano:

nano convert_pdf.sh

Skopiuj poniższy skrypt i wklej go do edytora:

#!/bin/bash

# Lokalizacja pliku PDF
pdf_file="ścieżka/do/pliku.pdf"

# Folder wyjściowy
output_folder="ścieżka/do/katalogu/wyjściowego"

# Sprawdzenie, czy folder wyjściowy istnieje, jeśli nie - utworzenie
[ -d "$output_folder" ] || mkdir -p "$output_folder"

# Liczba stron
page_count=22

# Konwersja
for i in $(seq 1 $page_count); do
    convert -density 300 "$pdf_file[$((i-1))]" -quality 100 "$output_folder/page_$i.png"
done

Zapisz i zamknij edytor (dla nano, użyj Ctrl+X, potwierdź zapisanie zmian Y, a następnie wciśnij Enter).

2. Nadawanie Uprawnień
Nadaj uprawnienia wykonawcze do skryptu, aby można go było uruchomić:

chmod +x convert_pdf.sh

3. Uruchomienie Skryptu
Teraz możesz uruchomić skrypt, wpisując:

./convert_pdf.sh

Obrazy zostaną wygenerowane w określonym folderze wyjściowym.

Notatki Końcowe

Ścieżki: Pamiętaj, aby zastąpić "ścieżka/do/pliku.pdf" i "ścieżka/do/katalogu/wyjściowego" rzeczywistymi ścieżkami do pliku źródłowego i folderu wyjściowego.
Format Obrazu: Skrypt zapisuje obrazy jako pliki .png dla zachowania wysokiej jakości. Jeśli preferujesz format .jpg, zmień "$output_folder/page_$i.png" na "$output_folder/page_$i.jpg" i dostosuj parametry jakości obrazu.
Liczba Stron: Zmien zmienną page_count na rzeczywistą liczbę stron w twoim pliku PDF.
