"""Esta función siempre va a guardr en un archivo el paramentro que se le mande"""

def printsDate(information, nameFile):
    with open(f"{nameFile}.txt", "w", encoding="utf-8") as f:
            f.write(f"{information}\n")
    print(f"Informacion guardada en {nameFile}.txt ✅")