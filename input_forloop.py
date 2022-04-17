jumlah = int(input("masukkan jumlah nama yang mau dimasukan: "))
print(f"Jumlah nama, {jumlah} !")
i = 1
nama = []
while i <= jumlah:
    nama.append(input(f"masukkan nama ke-{i}: "))
    i += 1
for x,y in enumerate(nama):
    print(f"Nama ke- {x+1} adalah: {y} ")