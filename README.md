# Wypożyczalnia Sprzętu Narciarskiego

## Opis projektu  
Projekt to aplikacja do zarządzania wypożyczalnią sprzętu narciarskiego.  
Został napisany w języku Python i wykorzystuje XML do przechowywania danych oraz XSD do ich walidacji.  
Aplikacja umożliwia użytkownikowi dodawanie klientów, sprzętu, karnetów, wypożyczeń oraz wyszukiwanie klientów.

## Autorzy  
- Osoba 1: Natalia Świderska
- Osoba 2: Patrycja Zachara

## Wymagane środowisko  
- **Python 3.x** (zalecana wersja 3.9+)  
- **PyCharm** (lub inne środowisko Python, np. VS Code)  
- **System operacyjny**: Windows / Linux / macOS  

## Wykorzystane biblioteki  
- **lxml** – do przetwarzania i walidacji XML względem XSD  
- **xml.etree.ElementTree** – do operacji na plikach XML  
- **re** – do walidacji numeru PESEL  
- **datetime** – do walidacji poprawności formatu dat  

## Struktura plików  
- `main.py` – Główny plik programu  
- `WypozyczalniaSprzetuNarciarskiego.xml` – Baza danych w formacie XML  
- `WypozyczalniaSprzetuNarciarskiego.xsd` – Plik XSD do walidacji struktury XML  

## Jak uruchomić?
1. Zainstaluj wymagane biblioteki:
   ```bash
   pip install lxml
   pip install datetime
   pip install re
   pip install xml.etree.ElementTree 
