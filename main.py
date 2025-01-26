import xml.etree.ElementTree as ET
import lxml.etree as etree
import re
from datetime import datetime

# Ścieżki do plików
xml_file = "wypozyczalniaSprzetuNarciarskiego.xml"
xsd_file = "wypozyczalniaSprzetuNarciarskiego.xsd"

#walidacja xml za pomoca xsd
def validate_xml():
    try:
        xml_doc = etree.parse(xml_file)
        xsd_doc = etree.parse(xsd_file)
        xsd_schema = etree.XMLSchema(xsd_doc)

        if xsd_schema.validate(xml_doc):
            print("XML jest poprawny względem XSD.")
        else:
            print("Błąd walidacji XML:")
            print(xsd_schema.error_log)
    except Exception as e:
        print(f"Błąd walidacji: {e}")
# walidacja pesel
def validate_pesel(pesel):
    return re.fullmatch(r"\d{11}", pesel) is not None

# walidacja daty
def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# walidacja id
def is_unique_id(root, element_name, id_value):
    return all(item.find(element_name).text != id_value for item in root.findall(f".//{element_name}"))

# wyszukiwanie klienta
def find_client():
    tree = ET.parse(xml_file)
    root = tree.getroot()

    pesel = input("Podaj PESEL klienta do wyszukania: ")

    for klient in root.findall(".//klient"):
        if klient.find("pesel").text == pesel:
            xml_string = ET.tostring(klient, encoding="utf-8").decode()
            print("\nZnaleziony klient w formacie XML:")
            print(xml_string)
            return

    print("Nie znaleziono klienta o podanym PESEL.")

# nowy klinet
def add_client():
    tree = ET.parse(xml_file)
    root = tree.getroot()

    imie = input("Podaj imię klienta: ")
    nazwisko = input("Podaj nazwisko klienta: ")
    pesel = input("Podaj PESEL klienta: ")

    if not validate_pesel(pesel):
        print("BŁĄD: PESEL musi składać się z 11 cyfr.")
        return

    for klient in root.findall(".//klient"):
        if klient.find("pesel").text == pesel:
            print("BŁĄD: Klient z tym numerem PESEL już istnieje.")
            return

    klienci = root.find("klienci")
    nowy_klient = ET.Element("klient")
    ET.SubElement(nowy_klient, "imie").text = imie
    ET.SubElement(nowy_klient, "nazwisko").text = nazwisko
    ET.SubElement(nowy_klient, "pesel").text = pesel

    klienci.append(nowy_klient)
    tree.write(xml_file, encoding="utf-8", xml_declaration=True)
    print(f"Dodano nowego klienta: {imie} {nazwisko} ({pesel})")

# nowy sprzet
def add_equipment():
    tree = ET.parse(xml_file)
    root = tree.getroot()

    id_sprzetu = input("Podaj ID sprzętu: ")
    rodzaj = input("Podaj rodzaj sprzętu (narty/snowboard): ")
    specyfikacja = input("Podaj specyfikację sprzętu: ")
    rozmiar = input("Podaj rozmiar sprzętu: ")
    cena = input("Podaj cenę za dzień wypożyczenia: ")

    sprzety = root.find("sprzety")
    nowy_sprzet = ET.Element("sprzet")
    ET.SubElement(nowy_sprzet, "idSprzetu").text = id_sprzetu
    ET.SubElement(nowy_sprzet, "rodzaj").text = rodzaj
    ET.SubElement(nowy_sprzet, "specyfikacja").text = specyfikacja
    ET.SubElement(nowy_sprzet, "rozmiar").text = rozmiar
    ET.SubElement(nowy_sprzet, "cenaZaDzien").text = cena

    sprzety.append(nowy_sprzet)
    tree.write(xml_file, encoding="utf-8", xml_declaration=True)
    print(f"Dodano nowy sprzęt: {rodzaj}, Specyfikacja: {specyfikacja}")

# dodaj karnet
def add_pass():
    tree = ET.parse(xml_file)
    root = tree.getroot()

    id_karnetu = input("Podaj ID karnetu: ")
    rodzaj = input("Podaj rodzaj karnetu (ulgowy/normalny): ")
    czas_trwania = input("Podaj czas trwania (dzienny/tygodniowy): ")
    cena = input("Podaj cenę karnetu: ")

    karnety = root.find("karnety")
    nowy_karnet = ET.Element("karnet")
    ET.SubElement(nowy_karnet, "idKarnetu").text = id_karnetu
    ET.SubElement(nowy_karnet, "rodzaj").text = rodzaj
    ET.SubElement(nowy_karnet, "czasTrwania").text = czas_trwania
    ET.SubElement(nowy_karnet, "cena").text = cena

    karnety.append(nowy_karnet)
    tree.write(xml_file, encoding="utf-8", xml_declaration=True)
    print(f"Dodano nowy karnet: {rodzaj}, Czas trwania: {czas_trwania}")

# nowe wypozyczenie
def add_rental():
    tree = ET.parse(xml_file)
    root = tree.getroot()

    id_sprzetu = input("Podaj ID wypożyczonego sprzętu: ")
    pesel = input("Podaj PESEL wypożyczającego: ")
    data_wypozyczenia = input("Podaj datę wypożyczenia (YYYY-MM-DD): ")
    data_zwrotu = input("Podaj datę zwrotu (YYYY-MM-DD): ")
    cena = input("Podaj cenę wypożyczenia: ")

    if not validate_pesel(pesel):
        print("BŁĄD: PESEL musi składać się z 11 cyfr.")
        return

    if not validate_date(data_wypozyczenia) or not validate_date(data_zwrotu):
        print("BŁĄD: Niepoprawny format daty. Wymagany format: YYYY-MM-DD.")
        return

    wypozyczenia = root.find("wypozyczonia")
    nowe_wypozyczenie = ET.Element("wypozyczenie")
    ET.SubElement(nowe_wypozyczenie, "idSprzetu").text = id_sprzetu
    ET.SubElement(nowe_wypozyczenie, "dataWypozyczenia").text = data_wypozyczenia
    ET.SubElement(nowe_wypozyczenie, "dataZwrotu").text = data_zwrotu
    ET.SubElement(nowe_wypozyczenie, "cena").text = cena
    ET.SubElement(nowe_wypozyczenie, "peselWypozyczajacego").text = pesel

    wypozyczenia.append(nowe_wypozyczenie)
    tree.write(xml_file, encoding="utf-8", xml_declaration=True)
    print(f"Dodano nowe wypożyczenie: Sprzęt ID {id_sprzetu}, Wypożyczający: {pesel}")

# ====== MENU ======
def menu():
    while True:
        print("\n=== Wypożyczalnia Sprzętu Narciarskiego ===")
        print("1. Dodaj nowego klienta")
        print("2. Dodaj nowy sprzęt")
        print("3. Dodaj nowy karnet")
        print("4. Dodaj nowe wypożyczenie sprzętu")
        print("5. Wyszukaj klienta i zwróć jego dane w XML")
        print("6. Waliduj XML")
        print("7. Wyjdź")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            add_client()
        elif wybor == "2":
            add_equipment()
        elif wybor == "3":
            add_pass()
        elif wybor == "4":
            add_rental()
        elif wybor == "5":
            find_client()
        elif wybor == "6":
            validate_xml()
        elif wybor == "7":
            break
        else:
            print("Wybierz poprwna opcje!")

menu()
