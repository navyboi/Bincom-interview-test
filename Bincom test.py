#!C:\Users\user\AppData\Local\Programs\Python\Python38-32\python.exe 

print("content-type: text/html\n\n" )
print ("<html>")
print ("<head>")
print ("<title>Bincom Interview Test</title>")
print ("</head>")
print ("<body>")
for i in range(0,100000,5):
    print ("<h2><b>%s</b></h2>" % (i))
for j in range(0,100,3):
    print("<h2><i>%s</i></h2>" % (j))
for k in range(0,100):
    if k > 1:
        for l in range(2,k):
            if k % l == 0:
                break
        else:
            print("<h2><u>%s</u></h2>" % (k))
print ("</body>")
print ("</html>")