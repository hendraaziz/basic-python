try:
    f = open("filehandling/hello1.txt",'r')
    if f.read()=='':
        print('data kosong')
        #f = open("filehandling/hello.txt",'a')
        #f.write("append pesan")
        
    else:
        print('data isi')
        #f = open("filehandling/hello.txt",'a')
        #f.write("\nappend pesan")
except Exception as exception:
    print("Error: %s!\n\n" % exception)
f = open("filehandling/hello1.txt",'r')
print(f.read())
f.close()