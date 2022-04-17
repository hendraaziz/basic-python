print("==== Program mengecek status lulus siswa ====")
nTeori = int(input(f"Masukkan nilai ujian Teori (maks 100): "))
nPraktek = int(input(f"Masukkan nilai ujian Praktek (maks 100): "))
if nTeori >=70 and nPraktek >= 70:
    print(f"Selamat, anda lulus!")
elif nTeori >= 70 and nPraktek < 70:
    print(f"Anda harus mengulang ujian praktek.")
elif nTeori < 70 and nPraktek >= 70:
    print(f"Anda harus mengulang ujian teori.")
else:
    print(f"Anda harus mengulang ujian teori dan praktek.")
