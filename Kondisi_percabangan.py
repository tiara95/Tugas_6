try:
    skor = float(input("Masukkan skor (0–100): "))

    if skor < 0 or skor > 100:
        print("Error: Skor harus antara 0 sampai 100.")
    else:
        if skor >= 90:
            print("Nilai Huruf: A")
            print("Predikat   : Dengan Pujian")
        elif skor >= 80:
            print("Nilai Huruf: B")
            print("Predikat   : Sangat Memuaskan")
        elif skor >= 70:
            print("Nilai Huruf: C")
            print("Predikat   : Memuaskan")
        elif skor >= 60:
            print("Nilai Huruf: D")
            print("Predikat   : Tidak Memuaskan")
        else:
            print("Nilai Huruf: E")
            print("Predikat   : Tidak LULUS")

except ValueError:
    print("Input tidak valid! Harus berupa angka.")
