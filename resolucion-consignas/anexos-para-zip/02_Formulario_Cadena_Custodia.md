# MODELO DE FORMULARIO DE CADENA DE CUSTODIA DE EVIDENCIA DIGITAL

> **EJEMPLO – DATOS FICTICIOS. No corresponde a la causa del caso analizado ni a ninguna causa real.** Todos los nombres, números, fechas y lugares son inventados por el equipo solo para mostrar cómo se completa el formulario.  
> **Materia:** Legislación – Tecnicatura Universitaria en Programación (UTN)

---

## 1. Datos generales (ejemplo)
* **Número de expediente / causa:** [EJEMPLO] Expediente X-0000/0000
* **Carátula:** [EJEMPLO] Incidente informático de práctica
* **Fecha y hora del procedimiento:** [EJEMPLO] 10/01/2025 – 10:00 hs.
* **Lugar:** [EJEMPLO] Oficina de práctica, sin dirección real
* **Autoridad que interviene:** [EJEMPLO] Autoridad ficticia

---

## 2. Elemento secuestrado (ejemplo)
* **Ítem N°:** 01
* **Tipo de elemento:** Archivo de registro de eventos (log) en formato de texto.
* **Nombre del archivo:** `05_ejemplo_registro_ficticio.txt` (archivo de práctica incluido en este paquete de anexos).
* **Tamaño:** 731 bytes.
* **Estado al obtenerlo:** copia de trabajo; el original se guarda sin modificar.
* **Rótulo / código del elemento:** [EJEMPLO] ITEM-01

---

## 3. Verificación de integridad (hash)
* **Algoritmo:** SHA-256.
* **Valor calculado:** `40b4ae55313c6236cb881819d70514e1891faf4d6aa68d7975c72b42749c57a4`
* **Cómo se calculó:** con el script `05_calcular_hashes.py` de este paquete, sobre el archivo de práctica `05_ejemplo_registro_ficticio.txt`. El valor es real para ese archivo; si alguien modifica una sola letra del archivo, el hash cambia.

---

## 4. Registro de movimientos (ejemplo)

| Fecha y hora | Entrega | Recibe | Motivo | Firma entrega | Firma recepción |
|:---|:---|:---|:---|:---|:---|
| [EJEMPLO] 10/01/2025 10:30 | Persona A (ficticia) | Persona B (ficticia) | Entrega del archivo para su análisis | [firma] | [firma] |
| [EJEMPLO] 10/01/2025 15:00 | Persona B (ficticia) | Persona C (ficticia) | Copia para el análisis y verificación del hash | [firma] | [firma] |
| [EJEMPLO] 10/01/2025 17:00 | Persona C (ficticia) | Persona B (ficticia) | Devolución del original, hash verificado | [firma] | [firma] |

---

## 5. Observaciones (ejemplo)
Si se detecta un error al completar el formulario (por ejemplo, un hash mal copiado), se corrige dejando constancia de la rectificación, con fecha y firma, sin borrar lo anterior.
