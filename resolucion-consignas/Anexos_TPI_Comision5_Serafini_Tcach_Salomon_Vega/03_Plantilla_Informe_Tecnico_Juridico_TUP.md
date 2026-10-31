# MODELO DE INFORME TÉCNICO-JURÍDICO PARA EL PROGRAMADOR (TUP)

> **EJEMPLO – DATOS FICTICIOS. No corresponde a la causa del caso analizado ni a ninguna causa real.** Se usa el archivo de práctica `05_ejemplo_registro_ficticio.txt`, creado por el equipo. Las direcciones IP son de rangos reservados para documentación y el número de línea es inexistente.  
> **Materia:** Legislación – Tecnicatura Universitaria en Programación (UTN)  
> **Estructura:** identificación, objeto, origen, procedimiento, hallazgos y conclusión, escritas de forma objetiva.

---

### INFORME TÉCNICO (MODELO)

#### 1. Identificación
* **Profesional:** [Nombre y apellido del profesional – a completar]
* **Rol:** Técnico Universitario en Programación (TUP).
* **Expediente de referencia:** [EJEMPLO] Expediente X-0000/0000 (ficticio).
* **Fecha del informe:** [EJEMPLO] 10/01/2025.

#### 2. Objeto
Revisar el archivo de registro `05_ejemplo_registro_ficticio.txt` para verificar su integridad y describir qué eventos figuran sobre una línea de ejemplo.

#### 3. Origen de la evidencia
* **Origen:** archivo de texto de práctica creado por el equipo (no proviene de ninguna empresa real).
* **Forma de obtención:** copia del archivo; el original se conserva sin modificar.
* **Medidas de preservación:** el análisis se hace sobre la copia.

#### 4. Verificación de integridad
* **Archivo:** `05_ejemplo_registro_ficticio.txt` (731 bytes).
* **Hash SHA-256:** `40b4ae55313c6236cb881819d70514e1891faf4d6aa68d7975c72b42749c57a4`
* **Cómo se obtuvo:** con el script `05_calcular_hashes.py` del paquete de anexos.
* **Resultado:** el hash calculado antes y después de la revisión es el mismo, por lo que el archivo no cambió.

#### 5. Procedimiento
Se abrió la copia en modo lectura y se leyeron los eventos en orden de fecha y hora. No se modificó ningún dato.

#### 6. Hallazgos (descripción objetiva del archivo de ejemplo)
1. Línea de ejemplo: `11-0000-0000` (inexistente).
2. 10/01/2025 14:18:22: se inicia una solicitud de reposición de SIM desde la IP de ejemplo `192.0.2.10`.
3. 14:18:40: la validación se aprueba con tres datos (línea, DNI y número de trámite).
4. 14:19:05: se da de baja la SIM anterior.
5. 14:21:40: se envía un código por SMS a la SIM nueva.
6. 14:30:12: una consulta de estado de solo lectura desde otra IP de ejemplo (`198.51.100.7`).

#### 7. Conclusión técnica
1. **Integridad:** el archivo mantuvo el mismo hash durante la revisión.
2. **Lo que muestra el registro de ejemplo:** la reposición se aprobó solo con datos personales, y el código por SMS fue a la SIM nueva. Esto ilustra por qué proponemos validar la identidad con un paso adicional y no usar SMS como único método (ver Etapas 3 y 4 del informe).
3. **Límite:** es un archivo inventado; no permite sacar conclusiones sobre ningún caso real.

---

**Firma:** [Nombre y apellido del profesional – a completar]
