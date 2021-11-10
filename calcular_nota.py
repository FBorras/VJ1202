def calcular_nota(ec, examen):
    if ec >= 5 and examen >= 5:
        nota = ec*0.6 + examen*0.4
        if nota >= 9:
            return "SOBRESALIENTE"
        elif nota >= 7:
            return "NOTABLE"
        elif nota >= 5:
            return "SUFICIENTE"
    return "NO SUPERA"

