#!/usr/bin/env python
import cgi
import os
import cgitb
import re
import io
import shutil

import urllib.request
cgitb.enable()

print ("Content-Type: text/html")
print ()

form = cgi.FieldStorage()

# Get filename here.
fileitem = form['sentFile']

# Test if the file was uploaded
if fileitem.filename:
   fn = os.path.basename(fileitem.filename)
   open('/tmp/' + fn, 'wb+').write(fileitem.file.read())

   message = 'File "' + fn + '" was upload'
   
else:
   message = u'Where is a file? :('

   
print ("""

<html>
<head>
    <link rel="stylesheet" href="main.css">
    <title> Protein converter </title>
</head>
<body>
   <p>%s</p>
   <form method="post">
       <a href="script/script.py"> Download </a>
   </form>
</body>
</html>
""" % (message,))

x = []
y = []
z = []
r = []
g = []
b = []
protein = []
size = []

# Подключение к БД
import pymysql
conn = pymysql.connect(
db='protein',
user='root',
passwd='Eyara',
host='localhost')
c = conn.cursor()


#Парсинг строк
word = u'ATOM'
with io.open('/tmp/' + fn, 'r', encoding='utf-8') as file:
    for line in file:
        if word in line:
            x.append(float(line [31:38]))
            y.append(float(line [41:47]))
            z.append(float(line [48:54]))
            protein.append(line[13:16])


#Работаем с красным цветом
for i in protein:
    protname = str(i)
    c.execute("SELECT R FROM colors WHERE name = \"%s\" " %protname)
    data = c.fetchall()
    examp = str(data)
    numb = str(re.findall(r'\d+',examp))
    numb = numb.replace('\'', '').replace('[', '').replace(']', '').replace(' ', '')
    if numb == '':
        numb = '0'
    numb = float(int(numb) / 255)
    numb = round(numb, 10)
    r.append(numb)

#Работаем с зелёным цветом

for i in protein:
    protname = str(i)
    c.execute("SELECT G FROM colors WHERE name = \"%s\" " %protname)
    data = c.fetchall()
    examp = str(data)
    numb = str(re.findall(r'\d+',examp))
    numb = numb.replace('\'', '').replace('[', '').replace(']', '').replace(' ', '')
    if numb == '':
        numb = '0'
    numb = float(int(numb) / 255)
    numb = round(numb, 10)
    g.append(numb)

#Работаем с синим цветом

for i in protein:
    protname = str(i)
    c.execute("SELECT B FROM colors WHERE name = \"%s\" " %protname)
    data = c.fetchall()
    examp = str(data)
    numb = str(re.findall(r'\d+',examp))
    numb = numb.replace('\'', '').replace('[', '').replace(']', '').replace(' ', '')
    if numb == '':
        numb = '0'
    numb = float(int(numb) / 255)
    numb = round(numb, 10)
    b.append(numb)


#Работаем с радиусом

for i in protein:
    protname = str(i)
    c.execute("SELECT VW FROM colors WHERE name = \"%s\" " %protname)
    data = c.fetchall()
    examp = str(data)
    numb = str(re.findall(r'\d+',examp))
    numb = numb.replace('\'', '').replace('[', '').replace(']', '').replace(' ', '').replace(',' , '.')
    if numb == '':
        numb = '0'
    numb = ((float(numb)) / 255)
    numb = round(numb, 10)
    size.append(numb)


#изменение координаты Z

min_value = min(z)

for i in z:
    new_value = round((float(i) - float(min_value)),3)
    j = z.index(i)
    z.remove(i)
    z.insert(j, new_value)


#Создание скрипта для Blender
f = open('/var/www/test/script/script.py' , 'w+')

f.write('import bpy' + '\n' +  'def makeMaterial(diffuse, alpha):' + '\n')
f.write('    mat = bpy.data.materials.new(\'materialchik\')' + '\n')
f.write('    mat.diffuse_color = diffuse' + '\n' + '    mat.diffuse_shader = \'LAMBERT\'')
f.write('\n' + '    mat.diffuse_intensity = 1.0' + '\n' + '    mat.specular_color = (1,1,1)')
f.write('\n' + '    mat.specular_shader = \'COOKTORR\'' + '\n')
f.write('    mat.specular_intensity = 0.5' + '\n' + '    mat.alpha = alpha' + '\n')
f.write('    mat.ambient = 1' + '\n' + '    return mat' + '\n')
f.write('def setMaterial(ob, mat):' + '\n' + '    me1 = ob.data' + '\n')
f.write('    me1.materials.append(mat)' + '\n' + 'def my():' + '\n')


for i in x:
    j = x.index(i)
    f.write('    red = makeMaterial((')
    f.write(str(r[j]) + ', ')
    f.write(str(g[j]) + ', ')
    f.write(str(b[j]))
    f.write('), 1)' + '\n')
    f.write('    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=3,size=')
    f.write(str(size[j]) + ', location=(')
    f.write(str(i) + ', ')
    f.write(str(y[j]) + ', ')
    f.write(str(z[j]) + '))'+ '\n')
    f.write('    setMaterial(bpy.context.object, red)' + '\n')

f.close()

print ('Done!')
