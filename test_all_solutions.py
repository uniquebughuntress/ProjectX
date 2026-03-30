"""
test_all_solutions.py.py
Created: 26.03.26 13:18
Author: natalya
Project: ProjectX_Natalya

HIER teste ich meine Lösungen
"""

import sys
from pathlib import Path

# Importiere deine Lösungen
from my_solutions.meine_Loesungen_1_10 import *
from my_solutions.meine_Loesungen_81_90 import aufgabe_087_bubble_sort

# Füge das Hauptverzeichnis zum Python-Pfad hinzu
sys.path.insert(0, str(Path(__file__).parent))




def test_aufgabe_001():
    """Teste Text spiegeln"""
    assert aufgabe_001_spiegle_text("Hallo") == "ollaH"
    assert aufgabe_001_spiegle_text("Python") == "nohtyP"
    assert aufgabe_001_spiegle_text("") == ""
    print("✓ Aufgabe 001: Text spiegeln - OK")


def test_aufgabe_002():
    """Teste Vokale zählen"""
    assert aufgabe_002_zaehle_vokale("Hallo Welt") == 3
    assert aufgabe_002_zaehle_vokale("Python") == 1
    assert aufgabe_002_zaehle_vokale("AEIOU") == 5
    print("✓ Aufgabe 002: Vokale zählen - OK")


def test_aufgabe_003():
    """Teste, ob der Text ein Palindrom ist (Groß/Klein ignorieren)"""
    assert aufgabe_003_ist_palindrom("Hallo World") == False
    assert aufgabe_003_ist_palindrom("Rentner") == True
    assert aufgabe_003_ist_palindrom(" ") == True
    assert aufgabe_003_ist_palindrom("Das ist kein Palindrom") == False
    assert aufgabe_003_ist_palindrom("Reliefpfeiler") == True
    print("✓ Aufgabe 003: Palindrom Prüfung - OK")


def test_aufgabe_004():
    """Teste, ob alles großgeschrieben ist"""
    assert aufgabe_004_zu_grossbuchstaben("Code is in the air!") == "CODE IS IN THE AIR!"
    assert aufgabe_004_zu_grossbuchstaben("") == ""
    print("✓ Aufgabe 004: alles großgeschrieben - OK")


def test_aufgabe_005():
    """Teste, ob alles kleingeschrieben ist"""
    assert aufgabe_005_zu_kleinbuchstaben("Code is in the air!") == "code is in the air!"
    assert aufgabe_005_zu_kleinbuchstaben("") == ""
    print("✓ Aufgabe 005: alles kleingeschrieben - OK")


def test_aufgabe_006():
    """Test, ob erste Buchstaben jedes Satzes in Großbuchstaben umgewandelt"""
    assert aufgabe_006_capitalize_saetze("was für ein schöner Tag!") == "Was für ein schöner Tag!"
    assert aufgabe_006_capitalize_saetze("ariella") == "Ariella"
    assert aufgabe_006_capitalize_saetze("hallo. wie geht es dir? gut!") == "Hallo. Wie geht es dir? Gut!"
    assert aufgabe_006_capitalize_saetze("hello world!how are you?") == "Hello world! How are you?"
    assert aufgabe_006_capitalize_saetze("hello world!   how are you?") == "Hello world! How are you?"
    print("✓ Aufgabe 006: erster Buchstabe jedes Satzes großgeschrieben - OK")


def test_aufgabe_007():
    """Teste, ob alle Vorkommen von alt durch neu in text ersetzt sind"""
    assert aufgabe_007_ersetze_zeichen("Hello World!", "World", "Python") == "Hello Python!"
    assert aufgabe_007_ersetze_zeichen("Love is in the air!", "Love", "Code") == "Code is in the air!"
    assert aufgabe_007_ersetze_zeichen("Hello World?", "?", "!") == "Hello World!"
    print("✓ Aufgabe 007: Ersetze alle Vorkommen von alt durch neu in text  - OK")


def test_aufgabe_008():
    """Teste, ob alle Wort Vorkommen im Text richtig gezählt sind"""
    assert aufgabe_008_zaehle_wort("Wir kämpfen, wir hoffen, wir siegen.", "Wir") == 3
    assert aufgabe_008_zaehle_wort("Ich ging schnell in den Wald. Im Wald war es schnell dunkel. Die Dunkelheit im Wald machte mir Angst, aber ich ging weiter in den Wald...", "Bahnhof") == 0
    assert aufgabe_008_zaehle_wort("Sie will alles, sie kriegt alles!", "alles") == 2
    assert aufgabe_008_zaehle_wort("Ich ging schnell in den Wald. Im Wald war es schnell dunkel. Die Dunkelheit im Wald machte mir Angst, aber ich ging weiter in den Wald. Ein Baum stand im Weg. Hinter dem Baum sah ich einen anderen Baum. Der Wald war mein Ziel, doch der Wald war unheimlich", "Wald") == 6
    print("✓ Aufgabe 008: Zähle, wie oft wort im Text vorkommt (wortgenau)  - OK")


def test_aufgabe_009():
    """Teste, ob der Text nach limit Zeichen abgeschnitten und fall nötig, '...' eingefügt"""
    assert aufgabe_009_kuerze_text("Ich ging schnellen Schrittes in den Forst. Dort wurde es rasch dunkel. Die düstere Atmosphäre im Gehölz flößte mir Angst ein, dennoch ging ich weiter. Ein Baum versperrte den Weg, hinter dem sich ein weiteres Gewächs abzeichnete. Das Waldgebiet war mein Ziel, doch es wirkte unheimlich.", 100) == "Ich ging schnellen Schrittes in den Forst. Dort wurde es rasch dunkel. Die düstere Atmosphäre im Geh..."
    # Test 2: Text kürzer als limit
    assert aufgabe_009_kuerze_text("Hallo Welt",100) == "Hallo Welt"
    # Test 3: Text genau limit lang
    assert aufgabe_009_kuerze_text("Hallo Welt", 10)
    print("✓ Aufgabe 009: Schneide den Text nach limit Zeichen ab und füge '...' an, falls nötig.  - OK")


def test_aufgabe_010():
    """Teste, ob ein Satz in Wörter, getrennt nach Leerzeichen, zerlegt und in einer Liste ist"""
    assert aufgabe_010_teile_worte("Was für ein schöner Tag!") == ['Was', 'für', 'ein', 'schöner', 'Tag!']


def run_all_tests():
    """Führe alle Tests aus"""
    print("\n🧪 Teste meine Lösungen...\n")

    test_aufgabe_001()
    test_aufgabe_002()
    test_aufgabe_003()
    test_aufgabe_004()
    test_aufgabe_005()
    test_aufgabe_006()
    test_aufgabe_007()
    test_aufgabe_008()
    test_aufgabe_009()
    test_aufgabe_010()

    print("\n🎉 Alle getesteten Aufgaben bestanden!")


if __name__ == "__main__":
    run_all_tests()