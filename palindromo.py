
# -*- coding: utf-8 -*- #
import re
import datetime

def is_par(x):
    if (x % 2 == 0):
        return True
    return False

def is_palindromo(frase):
    frase_original = frase
    # Limpieza frase
    frase = frase.strip()
    frase = frase.lower()
    # Limpiar caracteres no ascii
    frase = frase.decode('utf-8').encode('utf-8')
    # Acentos
    frase = re.sub("á", "a", frase)
    frase = re.sub("é", "e", frase)
    frase = re.sub("í", "i", frase)
    frase = re.sub("ó", "o", frase)
    frase = re.sub("ú", "u", frase)
    # Remover newline y símbolos
    frase = re.sub(r'(\\n+)', "", frase)
    frase = re.sub("[^\w\d@]", "", frase)
    # Metricas frase
    largo_frase = len(frase)
    mitad = int(largo_frase/2)
    par = is_par(largo_frase)
    # Casos basicos
    if (largo_frase <= 1):
        return False
    # Contadores derecho y revés
    i = 0
    j = largo_frase-1
    while (i <= j):
        if (not par):
            if (i==mitad):
                return True
        if (frase[i] != frase[j]):
            return False
        i+=1
        j-=1
    return True

### Main
archivo = open("InputPruebas.txt", mode="r")
salida = open("OutputPruebas.txt", mode="w")
# Leer archivo y extraer frase
lineas = archivo.readlines()
nCaso=1
for linea in lineas:
    palindromo = False
    string_palindromo = "No"
    frase = linea.rstrip("\n")
    if is_palindromo(frase):
         palindromo = True
         string_palindromo = "Si"
    # Logear resultados en Output
    # Formato: [DD/MM/YYYY HH:MM:SS] Caso de prueba id #id - Resultado: “Si/No”
    tiempo_actual = datetime.datetime.now()
    tiempo_a_imprimir = tiempo_actual.strftime("[%d/%m/%Y %H:%M:%S]")
    linea_a_escribir = tiempo_a_imprimir+' Caso de prueba id '+str(nCaso)+' - Resultado: '+string_palindromo+"\n"
    salida.write(linea_a_escribir)
    nCaso += 1
# Limpiar caracter de sobra en logs
salida.seek(0, 1)
salida.seek(salida.tell() - 1, 0)
salida.truncate()
archivo.close()
salida.close()