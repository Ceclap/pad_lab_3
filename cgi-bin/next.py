import cgi
print('''
<!DOCTYPE HTML>
<html>
<head>
 <meta charset="utf-8">
 <title>Contor</title>
</head>
<body>
 <br>
 <br>
 <br>
 <br>
''')
# Cerem obiectul care contine parametrii de intrare
params = cgi.FieldStorage()
# Obtinem valoarea parametrului x. Daca nu exista, functia va returna valoarea
# transmisa ca al 2-lea argument.
x = params.getfirst('x', '')
x = int(x)
print('<font size="7"><b>')
print('<p align="center"><a href="/cgi-bin/counter.py?x=' + str(x + 1) + '">' + str(x) + '</a></p>')
print('</b></font>')
print('''
</body>
</html>
''')
