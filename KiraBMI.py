berat = float(input("Sila masukkan berat anda: "))
tinggi = float(input("Sila masukkan tinggi anda(Dalam unit meter): "))
nilai_bmi = berat / (tinggi * tinggi)
two_decimal_bmi = "{:.2f}".format(nilai_bmi)

if nilai_bmi < 18.5:
    print("Nilai bmi anda adalah", two_decimal_bmi)
    print("Kategori bmi anda adalah kurang berat badan")
    print("Menu cadangan adalah Lobak merah, tomato, barli, susu, yogurt, keju, roti, mi")
elif 18.5 <= nilai_bmi <= 24.9:
    print("Nilai bmi anda adalah", two_decimal_bmi)
    print("Kategori bmi anda adalah normal")
    print("Menu cadangan adalah Epal, pisang, anggur, roti, kacang soya, bebola ikan")
elif 25.0 <= nilai_bmi <= 29.9:
    print("Nilai bmi anda adalah", two_decimal_bmi)
    print("Kategori bmi anda adalah berat badan berlebihan")
    print("Menu cadangan adalah Oat, barli, air kelapa, bebola ikan, epal hijau, pisang, oren")
else:
    print("Nilai bmi anda adalah", two_decimal_bmi)
    print("Kategori bmi anda adalah obesiti")
    print("Menu cadangan adalah beras perang, roti gandum, brokoli, kekacang dan bayam, tauhu")
