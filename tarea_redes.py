import csv

meses = ["ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO"]

datos = []

archivo = open("datos_redes_sociales (1).csv", "r", encoding="utf-8-sig")

lector = csv.reader(archivo)

encabezados = next(lector)

for fila in lector:
    datos.append(fila)

archivo.close()

print("Archivo leído correctamente")
print("\n--- Diferencia de seguidores de Twitter ---")

for fila in datos:
    if fila[0] == "TWITTER" and fila[1] == "SEGUIDORES (FOLLOWERS)":
        seguidores_enero = int(fila[3])
        seguidores_junio = int(fila[8])

diferencia = seguidores_junio - seguidores_enero

print("Seguidores en enero:", seguidores_enero)
print("Seguidores en junio:", seguidores_junio)
print("Diferencia:", diferencia)
print("\n--- Diferencia de visualizaciones de YouTube ---")

mes1 = input("Escribe el primer mes: ").upper()
mes2 = input("Escribe el segundo mes: ").upper()

if mes1 in meses and mes2 in meses:
    posicion1 = encabezados.index(mes1)
    posicion2 = encabezados.index(mes2)

    for fila in datos:
        if fila[0] == "YOUTUBE" and fila[1] == "VISUALIZACIONES":
            vistas1 = int(fila[posicion1])
            vistas2 = int(fila[posicion2])

    diferencia_vistas = abs(vistas2 - vistas1)

print("Visualizaciones en", mes1, ":", vistas1)
print("Visualizaciones en", mes2, ":", vistas2)
print("Diferencia:", diferencia_vistas)
print("\n--- Promedio de crecimiento ---")

suma_facebook = 0
suma_twitter = 0

for fila in datos:
    if fila[0] == "FACEBOOK" and fila[1] == "CRECIMIENTO (seguidores)":
        for i in range(3, 9):
            suma_facebook = suma_facebook + int(fila[i])

    if fila[0] == "TWITTER" and fila[1] == "CRECIMIENTO DE FOLLOWERS":
        for i in range(3, 9):
            suma_twitter = suma_twitter + int(fila[i])

promedio_facebook = suma_facebook / 6
promedio_twitter = suma_twitter / 6

print("Promedio de crecimiento de Facebook:", promedio_facebook)
print("Promedio de crecimiento de Twitter:", promedio_twitter)
print("\n--- Promedio de Me gusta ---")

suma_youtube = 0
suma_twitter_megusta = 0
suma_facebook_megusta = 0

for fila in datos:
    if fila[0] == "YOUTUBE" and fila[1] == "ME GUSTA":
        for i in range(3, 9):
            suma_youtube = suma_youtube + int(fila[i])

    if fila[0] == "TWITTER" and fila[1] == "ME GUSTA":
        for i in range(3, 9):
            suma_twitter_megusta = suma_twitter_megusta + int(fila[i])

    if fila[0] == "FACEBOOK" and fila[1] == "ME GUSTA EN PUBLICACIONES":
        for i in range(3, 9):
            suma_facebook_megusta = suma_facebook_megusta + int(fila[i])

promedio_youtube = suma_youtube / 6
promedio_twitter_megusta = suma_twitter_megusta / 6
promedio_facebook_megusta = suma_facebook_megusta / 6

print("Promedio Me gusta YouTube:", promedio_youtube)
print("Promedio Me gusta Twitter:", promedio_twitter_megusta)
print("Promedio Me gusta Facebook:", promedio_facebook_megusta)