# ---------- Soal 1: Konversi suhu ----------
def convert_temperature(value, unit):
    """Konversi suhu. unit 'C' = dari Celsius ke Fahrenheit,
    unit 'F' = dari Fahrenheit ke Celsius."""
    unit = unit.upper()
    if unit == 'C':
        return (value * 9 / 5) + 32
    elif unit == 'F':
        return (value - 32) * 5 / 9
    else:
        return "Unit tidak valid! Gunakan 'C' atau 'F'."

print(convert_temperature(100, 'C'))  
print(convert_temperature(212, 'F'))  
print(convert_temperature(50, 'D'))  #output : unit tidak valid