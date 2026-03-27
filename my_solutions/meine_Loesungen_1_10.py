"""
meine_Loesungen_1_10.py
Created: 26.03.26 12:55
Author: natalya
Project: ProjectX_Natalya

100 Basis-Aufgaben für die Studierenden.

Jede Funktion ist nur als Stub angelegt und soll von euch implementiert
werden. Nutzt Docstring und Parameternamen als Leitplanke. Schreibt sauberen,
getesteten Code und haltet euch an PEP 8.
"""

from typing import Any, Optional


# Gruppe: Alexander, Erik, Jan B
def aufgabe_001_spiegle_text(text: str) -> str:
    """Gib den Text rückwärts zurück."""
    return text[::-1]


# Gruppe: Alexander, Erik, Jan B
def aufgabe_002_zaehle_vokale(text: str) -> int:
    """Zähle die Anzahl der Vokale im Text (a, e, i, o, u)."""
    vokale = {"a", "e", "i", "o", "u"}  # Set (O(1) lookup)
    counter = 0
    for char in text.lower():
        if char in vokale:
            counter += 1
    return counter

"""
Fortgeschrittene Loesung:

def aufgabe_002_zaehle_vokale(text: str) -> int:
    vokale = set("aeiou")
    return sum(1 for char in text.lower() if char in vokale)
"""


# Gruppe: Alexander, Erik, Jan B
def aufgabe_003_ist_palindrom(text: str) -> bool:
    """Prüfe, ob der Text ein Palindrom ist (Groß/Klein ignorieren)."""
    if not text:  # Leerer Text
        return True  # Ein leerer Text ist per Definition ein Palindrom
    bereinigter_text = text.lower().replace(" ", "")
    return bereinigter_text == bereinigter_text[::-1]



# Gruppe: Alexander, Erik, Jan B
def aufgabe_004_zu_grossbuchstaben(text: str) -> str:
    """Wandle alle Zeichen in Großbuchstaben um."""
    return text.upper()


# Gruppe: Alexander, Erik, Jan B
def aufgabe_005_zu_kleinbuchstaben(text: str) -> str:
    """Wandle alle Zeichen in Kleinbuchstaben um."""
    return text.lower()


# Gruppe: Alexander, Erik, Jan B
def aufgabe_006_capitalize_saetze(text: str) -> str:
    """Setze den ersten Buchstaben jedes Satzes auf Großbuchstaben."""
    if not text:
        return text

    # Prüfen, ob Satzzeichen im Text sind
    satzzeichen = set(".!?")

    if not any(char in satzzeichen for char in text):
        # Fall 1: Keine Satzzeichen → nur ein Satz
        return text[0].upper() + text[1:]

    # Fall 2: Mit Satzzeichen -> mehrere Sätze
    result = []
    satz = ""

    for char in text:
        satz += char
        if char in satzzeichen:
            # Satzende: großschreiben und speichern
            satz = satz.strip()
            if satz:
                satz = satz[0].upper() + satz[1:]
                result.append(satz)
            satz = ""  # Zurücksetzen für nächsten Satz

    # Letzten Satz (falls ohne Satzzeichen)
    if satz.strip():
        satz = satz.strip()
        satz = satz[0].upper() + satz[1:]
        result.append(satz)

    return " ".join(result)


# Gruppe: Alexander, Erik, Jan B
def aufgabe_007_ersetze_zeichen(text: str, alt: str, neu: str) -> str:
    """Ersetze alle Vorkommen von alt durch neu in text."""
    return text.replace(alt, neu)


# Gruppe: Alexander, Erik, Jan B
def aufgabe_008_zaehle_wort(text: str, wort: str) -> int:
    """Zähle, wie oft wort im Text vorkommt (wortgenau)."""
    pass


# Gruppe: Alexander, Erik, Jan B
def aufgabe_009_kuerze_text(text: str, limit: int) -> str:
    """Schneide den Text nach limit Zeichen ab und füge '...' an, falls nötig."""
    pass


# Gruppe: Alexander, Erik, Jan B
def aufgabe_010_teile_worte(text: str) -> list[str]:
    """Zerlege einen Satz in Wörter, getrennt nach Leerzeichen."""
    pass


