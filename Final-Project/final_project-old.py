#Final Project
#Program untuk mengirimkan email kepada beberapa penerima
#Menggunakan smtp GMAIL, sebelumnya email pengirim di setting untuk menerima low security.

# Imports Library smtplib, ssl, csv, getpass

import smtplib,ssl,csv,getpass
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# SETUP EMAIL LOGIN 

def kirim_email():
    judul_pesan = input(f"Masukan Subject Email: ")
    user_email =input(f"Email Pengirim: ")
    user_pass=getpass.getpass(prompt = "Pass email pengirim(Hidden): \n")
    try:
        data= open('Final-Project/receiver_list.txt','r')
        read_file = csv.reader(data)
        if data=='':
            print('Data Tujuan Masih Kosong')
        for penerima in read_file:
            #message
            pesan = MIMEMultipart("alternative")
            pesan['Subject']=judul_pesan
            pesan['From']= user_email
            pesan['To']=penerima[1]
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
                server.sendmail(user_email, penerima[1], msg=pesan.as_string())
                server.close()
                print('Email Kepada '+penerima[0]+' Terkirim!')
            except Exception as exception:
                print("Error: %s!\n\n" % exception)
                print('Belum Membuat daftar penerima!!\n\n')
        data.close()
    except Exception as exception:
        print("Error: %s!\n" % exception) 
def menu():
    print(f"\n=== Menu ===")
    print(f"1. Setup Penerima Email")
    print(f"2. Kirim Email")
    print(f"3. Keluar")
    pilih = int(input("\nInput pilihan Anda: "))
    opsiMenu(pilih)

def opsiMenu(pilih):
    if pilih == 1:
        #menu Setup Email
        
        menu()
    elif pilih == 2:
        #menu Kirim Email
        kirim_email()
        menu()
    elif pilih == 3:
        #End Program
        print(f"---------------")
        print(f"Program selesai!\nSampai jumpa!")
        print(f"---------------")
    else:
        print(f"\nMenu tidak tersedia")
        print(f"Silahkan Pilih Menu lainnya")
        menu()
menu()

#sumber : https://stackoverflow.com/questions/10147455/how-to-send-an-email-with-gmail-as-provider-using-python