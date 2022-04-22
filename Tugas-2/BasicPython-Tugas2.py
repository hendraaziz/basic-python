#daftar contact
contact = {
    'nama': ('Fawwaz', 'John'),
    'telp': ('0812345678', '0823456781')
    }
nama = list(contact['nama'])
telp = list(contact['telp'])

def menu():
    print(f"\n=== Menu ===")
    print(f"1. Daftar Kontak")
    print(f"2. Tambah Kontak")
    print(f"3. Keluar")
    pilih = int(input("\nInput pilihan Anda: "))
    opsiMenu(pilih)

def opsiMenu(pilih):
    if pilih == 1:
        #menu listContact
        listContact()
    elif pilih == 2:
        #menu addContact
        addContact()
    elif pilih == 3:
        #End Program
        print(f"---------------")
        print(f"Program selesai!\nSampai jumpa!")
        print(f"---------------")
    else:
        print(f"\nMenu tidak tersedia")
        print(f"Silahkan Pilih Menu lainnya")
        menu()

def listContact():
    print(f"\nDaftar Kontak")
    print(f"--------------")
    for a, b in zip(nama, telp):
        print(f"Nama: {a}\nNo.Telp: {b}\n")
    menu()

def addContact():
    #menambahkan contact
    print(f"masukkan nama dan nomor telp yang ingin ditambahkan:")
    add_nama = input("Nama: ")
    add_telp = input("No. Telp: ")
    nama.append(add_nama)
    telp.append(add_telp)
    print(f"Kontak baru berhasil ditambahkan.\n")
    menu()

print(f"\nSelamat datang!")
menu()