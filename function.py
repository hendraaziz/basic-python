def luas_lingkaran(jari):
    print("===Program menghitung Luas Lingkaran===")
    luas = float((22/7)*jari**2)
    return luas

def biodata(nama, alamat, usia=" tanpa data"):
    print("===Tampil Biodata===")
    print(f"nama: {nama}\nalamat: {alamat}\nusia: {usia}")


nama = str(input(f"Masukkan nama: "))
alamat = str(input(f"Masukkan Alamat: "))
usia = str(input(f"Masukkan Usia: "))
lebar = int(input(f"Masukkan jari-jari lingkaran: "))

biodata(alamat,nama,)
print(f"Luas lingkaran dengan jari-jari {lebar} cm adalah {luas_lingkaran(lebar):.2f} cm².")



