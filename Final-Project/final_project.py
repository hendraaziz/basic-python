from cgitb import text
from email.mime import base
from fileinput import filename
from itertools import tee
from json import encoder
from multiprocessing import context
import smtplib,ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass
import csv

#1.tampil tujuan
def listTujuan():
    try:
        data= open('Final-Project/receiver_list.txt','r')
        read_file = csv.reader(data)
        if data=='':
            print('Data Kosong')
        else:
            print('\n\nDaftar Email Tujuan')
            print('-----------------')
            for cetak in read_file:
                print('Nama: '+cetak[0])
                print('Email: '+cetak[1])
                print('--------')
        data.close()
    except Exception as exception:
        print("Error: %s!\n" % exception)
    mainMenu()

#2.Tambah Tujuan
def tambahTujuan():
    try:
        data = open('Final-Project/receiver_list.txt','r')
        nama = input(f"Masukkan Nama Tujuan: ")
        tujuan= input(f"Masukkan Email Tujuan: ")
        if data.read()=='':
            data = open('Final-Project/receiver_list.txt','a')
            data.write(nama+','+tujuan)
        else:
            data = open('Final-Project/receiver_list.txt','a')
            data.write('\n'+nama+','+tujuan)
        data.close()
    except Exception as exception:
        nama = input(f"Masukkan Nama Tujuan: ")
        tujuan= input(f"Masukkan Email Tujuan: ")
        data = open('Final-Project/receiver_list.txt','a')
        data.write(nama+','+tujuan)
        data.close()
    print('\nData Tujuan Berhasil Ditambah!\n')
    mainMenu()

#3.Over Write Tujuan
def owTujuan():
    nama = input(f"Masukkan Nama Tujuan: ")
    tujuan= input(f"Masukkan Email Tujuan: ")
    data = open('Final-Project/receiver_list.txt','w')
    data.write(nama+','+tujuan)
    data.close()
    print('\nData Tujuan Berhasil Ditambah!\n')
    mainMenu()

#Main Menu
def mainMenu():
    try:
        print(f"\n======================")
        print(f"== Menu Kirim Email ==")
        print(f"======================\n")
        print(f"1. Tampil Tujuan")
        print(f"2. Hanya Tambah Tujuan")
        print(f"3. Hapus & Tambah Tujuan")
        print(f"4. Kirim Email")
        print(f"5. Keluar")
        pilih = int(input("\nInput pilihan Anda: "))
        opsiMenu(pilih)
    except Exception as exception:
        print("Error: %s!\n\n" % exception)

def opsiMenu(pilih):
    if pilih == 1:
        #menu listTujuan
        listTujuan()
    elif pilih == 2:
        #menu tambahTujuan
        tambahTujuan()
    elif pilih == 3:
        #menu addContact
        owTujuan()
    elif pilih == 4:
        #menu addContact
        kirimEmail()
    elif pilih == 5:
        #End Program
        print(f"---------------")
        print(f"Program selesai!\nSampai jumpa!")
        print(f"---------------")
    else:
        print(f"\nMenu tidak tersedia")
        print(f"Silahkan Pilih Menu lainnya")
        mainMenu()

#Kirim Email
def kirimEmail():
    judul_pesan = input(f"Masukan Subject Email: ")
    user_email =input(f"Email Pengirim: ")
    user_pass=getpass.getpass(prompt = "Pass email pengirim(Hidden): \n")
    try:
        data= open('Final-Project/receiver_list.txt','r')
        read_file = csv.reader(data)
        if data=='':
            print('Data Tujuan Masih Kosong')
        for cetak in read_file:
            #message
            pesan = MIMEMultipart("alternative")
            pesan['Subject']=judul_pesan
            pesan['From']= user_email
            pesan['To']=cetak[1]

            #template
            html = open("Final-Project/template.html")
            template = MIMEText(html.read(),"html") #membaca file sebagai HTML
            pesan.attach(template) #masukan template ke pesan

            #attach file
            filenameCV='Final-Project/cv.pdf'
            with open(filenameCV,'rb') as lampiran:
                pdf=MIMEBase("application","octet-stream")
                pdf.set_payload(lampiran.read())
                encoders.encode_base64(pdf)
                pesan.attach(pdf)
                pdf.add_header(
                    "Content-Disposition",
                    "attachment",
                    filename=filenameCV
                )

            #send email
            context = ssl.create_default_context()

            try:
                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.ehlo()
                server.login(user_email, user_pass)
                server.sendmail(user_email, cetak[1], msg=pesan.as_string())
                server.close()

                print('Email Kepada '+cetak[0]+' Terkirim!')
            except Exception as exception:
                print("Error: %s!\n\n" % exception)
                print('Belum Membuat daftar penerima!!\n\n')
        data.close()
    except Exception as exception:
        print("Error: %s!\n" % exception) 
    mainMenu()
    

mainMenu()

#sumber 1: https://stackoverflow.com/questions/10147455/how-to-send-an-email-with-gmail-as-provider-using-python
#sumber 2: http://www.samlogic.net/articles/smtp-commands-reference.htm
#sumber 3: https://drive.google.com/file/d/1WhRNf16HOmbXm47xlUxucd_y2t-Cf-tP/view
#sumber 4: https://www.youtube.com/watch?v=q0yAR04avXk
#sumber 5: https://stackoverflow.com/questions/9202224/getting-a-hidden-password-input