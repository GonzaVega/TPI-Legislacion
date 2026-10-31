# Declaración Formal de Uso de Inteligencia Artificial

> **Documento:** Declaración de uso ético, trazable y responsable de herramientas de IA  
> **Asignatura:** Legislación – Tecnicatura Universitaria en Programación (UTN)  
> **Equipo (Comisión 5):** Mateo Serafini, Hugo Tcach, Farid Salomon, Gonzalo Vega  
> **Sección vinculada en el Informe:** Etapa 5 – Declaración de Uso de IA y Reflexión Crítica

---

## 1. Declaración de Integridad Académica
En el marco de nuestra formación profesional en la Tecnicatura Universitaria en Programación (TUP), dejamos constancia de los siguientes principios aplicados en este trabajo:

1. **Uso como Asistente Bajo Control Humano:** Las herramientas de Inteligencia Artificial generativa se utilizaron como apoyo para estructurar secciones, redactar borradores iniciales, programar el script de cálculo de hashes en Python y dar formato a los documentos entregables.
2. **Autoría y Responsabilidad del Equipo:** El análisis jurídico de los tipos penales, la valoración cualitativa de la matriz de riesgos, el diseño del protocolo de cinco pasos, la elaboración de los modelos con datos ficticios de práctica y la revisión final son responsabilidad directa de los integrantes del equipo.
3. **Verificación Documental Directa:** Ninguna afirmación fáctica ni cita legal generada por un modelo fue aceptada sin contrastarla con el texto completo de la normativa argentina (Ley 26.388, Código Penal, Ley 25.326, Ley 27.411) y con las nueve notas periodísticas reales abiertas y leídas el 30/10/2026 (`[F1]` a `[F9]`).

---

## 2. Herramientas Utilizadas, Roles y Límites

| Herramienta / Modelo | Rol en el Trabajo | Finalidad Específica | Límites y Controles Aplicados |
|:---|:---|:---|:---|
| **Gemini (Guía inicial y ejecución operativa)** | Asistente de búsqueda preliminar, programación y maquetación | Armado del script `05_calcular_hashes.py` con la librería estándar `hashlib`, generación de archivos DOCX, PDF, XLSX y PPTX, y descarga de los textos completos de las notas periodísticas reales durante la corrección. | Sus primeros borradores contenían errores de atribución penal y datos fácticos no verificados que fueron detectados y eliminados por completo en la etapa de revisión. |
| **Claude Sonnet (Planificación y revisión crítica)** | Diseño metodológico y auditoría de veracidad | Estructuración del plan de trabajo (`plan-ejecucion-tpi.md`), reglas de clasificación de datos según respaldo documental y revisión crítica de errores (`revision-correcciones.md`). | Sus observaciones se ejecutaron verificando cada documento normativo página por página y abriendo cada nota periodística antes de corregir el informe. |

---

## 3. Detección de Alucinaciones y Mitigación de Riesgos

* **Corrección de Alucinaciones Jurídicas y Fácticas:**  
  Durante el proceso comprobamos que los modelos de lenguaje tienden a completar vacíos informativos inventando datos de apariencia verosímil. En concreto:
  1. En la guía preliminar (`guia-planificador-claude.md`), Gemini había incluido como delitos de la condena el fraude informático (art. 173 inc. 16 CP) y la violación de secretos (art. 157 CP), además de mencionar organismos y herramientas forenses (UFEDECO/UFECI, Cellebrite) que no surgían de las notas del caso.
  2. En la primera ejecución del informe, Gemini había generado títulos, fechas (como una supuesta sentencia del 06/10/2023) y URLs periodísticas sin haber abierto las notas, y había presentado datos inventados de cadena de custodia (como una "Causa N° 29/2023", un teléfono Samsung A52 y el hash SHA-256 de un archivo vacío) como si pertenecieran al expediente real.  
  Todos esos elementos fueron eliminados, reemplazando las fuentes por las nueve notas efectivamente abiertas y leídas el 30/10/2026 (`10_Evidencia_Fuentes/`) y convirtiendo los anexos 02 y 03 en modelos de práctica claramente rotulados con datos ficticios sobre el archivo `05_ejemplo_registro_ficticio.txt`.
* **Protección de Datos Personales:**  
  En cumplimiento de la Ley 25.326, no se ingresaron en las herramientas de IA datos personales no públicos ni información confidencial de terceros.
* **Trazabilidad Completa:**  
  El registro cronológico de sesiones, prompts, aportes aprovechados y correcciones obra en `actividad-IA/registro-trazabilidad-ia.md` y su copia `anexos-para-zip/06_Prompts_y_Registro_IA.md`.
