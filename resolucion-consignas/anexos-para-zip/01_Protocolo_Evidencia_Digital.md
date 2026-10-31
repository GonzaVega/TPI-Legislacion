# PROTOCOLO BÁSICO DE PRESERVACIÓN Y DOCUMENTACIÓN DE EVIDENCIA DIGITAL

> **Materia:** Legislación – Tecnicatura Universitaria en Programación (UTN)  
> **Equipo:** Mateo Serafini, Hugo Tcach, Farid Salomon, Gonzalo Vega (Comisión 5)  
> **Finalidad:** guía simple de pasos para cuidar la evidencia digital y que no pierda valor probatorio. Es una propuesta académica del equipo, pensada para un programador que debe resguardar archivos o registros; no reemplaza el trabajo del personal especializado.

---

## 1. Principio básico
No se trabaja sobre la evidencia original. Toda revisión se hace sobre una copia, y se comprueba con un código hash que la copia es igual al original.

---

## 2. Cinco pasos

### Paso 1: Identificar y anotar
* Anotar qué elementos hay: computadoras, celulares, chips SIM, discos, pendrives o archivos de registro.
* Registrar marca, modelo, número de serie o IMEI, y sacar fotos del estado antes de tocarlos.

### Paso 2: Aislar
* Un dispositivo apagado se deja apagado.
* Si un celular está encendido, no se lo revisa: se lo pone en modo avión para que no reciba mensajes ni órdenes de borrado remoto, y se anota la hora y quién lo hizo.

### Paso 3: Copiar
* No tocar el original: se trabaja sobre una copia.
* El original se guarda en un lugar seguro.
* *(En casos reales, el personal especializado puede usar herramientas más avanzadas; aquí nos quedamos en los pasos básicos).*

### Paso 4: Calcular el hash
* Se calcula el hash SHA-256 del original y de la copia (por ejemplo con el script `05_calcular_hashes.py`).
* Si los dos valores coinciden, la copia es idéntica. El valor se anota con fecha, hora y firma.

### Paso 5: Registrar la cadena de custodia
* Cada vez que el elemento cambia de manos se completa el formulario (modelo en el anexo 02): fecha, hora, motivo y firmas.
* Si hay un error en el formulario, se corrige dejando constancia de la rectificación.
