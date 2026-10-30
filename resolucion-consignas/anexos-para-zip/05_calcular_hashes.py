#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script simple de verificación de integridad y cálculo de hashes (SHA-256)
Autor: Mateo Serafini, Hugo Tcach, Farid Salomon, Gonzalo Vega
Materia: Legislación - Tecnicatura Universitaria en Programación (UTN)

Finalidad:
Calcular de manera rápida y reproducible el código hash SHA-256 de uno o más
archivos para garantizar su integridad digital sin alterar el contenido original.
No requiere librerías externas (utiliza únicamente la librería estándar de Python).
"""

import sys
import os
import hashlib
from datetime import datetime, timezone

def calcular_hash_sha256(ruta_archivo):
    """
    Lee un archivo en bloques de 64 KB y calcula su código hash SHA-256.
    Retorna la cadena hexadecimal representativa.
    """
    sha256 = hashlib.sha256()
    try:
        # Abrimos en modo binario de solo lectura para no alterar ningún byte
        with open(ruta_archivo, 'rb') as f:
            while True:
                bloque = f.read(65536)  # Lectura en bloques de 64 KB
                if not bloque:
                    break
                sha256.update(bloque)
        return sha256.hexdigest()
    except Exception as e:
        return f"ERROR: {str(e)}"

def procesar_ruta(ruta_objetivo):
    """
    Procesa un archivo individual o todos los archivos dentro de un directorio.
    Imprime en pantalla y genera un archivo CSV con los resultados.
    """
    if not os.path.exists(ruta_objetivo):
        print(f"Error: La ruta '{ruta_objetivo}' no existe.")
        return

    archivos_a_procesar = []
    if os.path.isfile(ruta_objetivo):
        archivos_a_procesar.append(ruta_objetivo)
    elif os.path.isdir(ruta_objetivo):
        for raiz, _, ficheros in os.walk(ruta_objetivo):
            for fichero in ficheros:
                archivos_a_procesar.append(os.path.join(raiz, fichero))

    archivo_salida = "registro_hashes_verificacion.csv"
    fecha_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    print(f"Iniciando cálculo de hashes SHA-256 [{fecha_utc}]")
    print("-" * 80)
    print(f"{'Archivo':<45} | {'Hash SHA-256':<32}")
    print("-" * 80)

    with open(archivo_salida, "w", encoding="utf-8") as salida:
        salida.write("Fecha_UTC,Ruta_Archivo,Tamanio_Bytes,Hash_SHA256\n")
        
        for ruta in archivos_a_procesar:
            hash_calculado = calcular_hash_sha256(ruta)
            tamanio = os.path.getsize(ruta) if os.path.exists(ruta) else 0
            nombre_mostrar = os.path.basename(ruta)
            if len(nombre_mostrar) > 42:
                nombre_mostrar = nombre_mostrar[:39] + "..."
            
            print(f"{nombre_mostrar:<45} | {hash_calculado}")
            salida.write(f'"{fecha_utc}","{ruta}",{tamanio},"{hash_calculado}"\n')

    print("-" * 80)
    print(f"Proceso finalizado. Se generó el archivo de constancia: {archivo_salida}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        ruta = sys.argv[1]
    else:
        # Por defecto procesa el directorio actual
        ruta = "."
    procesar_ruta(ruta)
