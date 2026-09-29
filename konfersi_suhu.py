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
        return None


suhu = float(input("Masukkan nilai suhu: "))
satuan = input("Masukkan satuan (C/F): ")

hasil = convert_temperature(suhu, satuan)

if hasil is None:
    print("Satuan tidak valid! Gunakan 'C' atau 'F'.")
elif satuan.upper() == 'C':
    print(f"{suhu} °C = {hasil:.2f} °F")
else:
    print(f"{suhu} °F = {hasil:.2f} °C")