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


# Füge hier weitere Tests hinzu, während du die Aufgaben löst

def run_all_tests():
    """Führe alle Tests aus"""
    print("\n🧪 Teste meine Lösungen...\n")

    test_aufgabe_001()
    test_aufgabe_002()
    # test_aufgabe_003()  # Aktiviere wenn gelöst
    # test_aufgabe_004()  # Aktiviere wenn gelöst

    print("\n🎉 Alle getesteten Aufgaben bestanden!")


if __name__ == "__main__":
    run_all_tests()