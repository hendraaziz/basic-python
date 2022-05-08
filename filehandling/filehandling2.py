import csv
data = open('filehandling/nilai.csv','r')
nama = input(f"masukan nama: ")
nilai1= input(f"nilai1: ")
if data.read()=='':
    data = open('filehandling/nilai.csv','a')
    data.write(nama+','+nilai1)
else:
    data = open('filehandling/nilai.csv','a')
    data.write('\n'+nama+','+nilai1)
data = open('filehandling/nilai.csv','r') 
read_file = csv.reader(data)
for cetak in read_file:
    print('Nama: '+cetak[0])
    print('Nilai: '+cetak[1])
    print('--------')
data.close()

"""

data.write(nama+','+nilai1)
"""