#1. Dictionary
mydict = {"nama":"aziz","alamat":"yogya","usia":"30"}
print(mydict)

#akses item
print(mydict["nama"])
print(mydict["alamat"])

#ubah value
mydict["nama"] = "hendra"
mydict["alamat"] = "sleman"
mydict["usia"] = "20"
print("Nama: {}\n Alamat: {}\n Usia: {}".format(mydict["nama"], mydict["alamat"],mydict["usia"]))

#looping in dict
for x in mydict:
    print(mydict[x])

for x in mydict:
    print(f"{x} : {mydict[x]}")

#nesteed
nested_dict = {"nama":[]}