#F Beni Oktopiansahinal Project - Basic Python by
#Program untuk mengirimkan email kepada beberapa penerima
#Menggunakan smtp GMAIL, sebelumnya email pengirim di setting untuk menerima low security.

# Imports Library smtplib
import smtplib,getpass

# SETUP EMAIL LOGIN 
gmail_user = input(str("Masukkan akun gmail: "))
gmail_app_password = getpass.getpass(prompt = "Pass email pengirim(Hidden): \n")

# SETUP PENERIMA EMAIL
#with open('receiver_list.txt', 'r') as file:
	#penerima = file.read().replace('\n', ',')

# SETUP Pengirim, penerima, judul dan isi email
sent_from = gmail_user
sent_to = input(str("Masukkan gmail penerima lalu akhiri dengan enter: "))
sent_subject = input(str("Masukkan  subjek atau judul lalu akhiri dengan enter: "))
sent_body = input(str("Masukkan pesan yang akan dikirim lalu akhiri dengan enter: "))

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(sent_to), sent_subject, sent_body)

# =============================================================================
# Mengirim Email atau Gagal
# Detail Sumber: http://www.samlogic.net/articles/smtp-commands-reference.htm
# =============================================================================

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_app_password)
    server.sendmail(sent_from, sent_to, email_text)
    server.close()

    print('Email sent!')
except Exception as exception:
    print("Error: %s!\n\n" % exception)

#sumber : https://stackoverflow.com/questions/10147455/how-to-send-an-email-with-gmail-as-provider-using-python