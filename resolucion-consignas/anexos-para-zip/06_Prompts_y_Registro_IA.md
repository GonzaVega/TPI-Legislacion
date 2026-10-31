# Bitácora de Registro y Trazabilidad de Interacción con IA

> **Asignatura:** Legislación – Tecnicatura Universitaria en Programación (UTN)  
> **Eje Temático:** Eje 1 – Cibercrimen, evidencia digital y cadena de custodia  
> **Equipo (Comisión 5):** Mateo Serafini, Hugo Tcach, Farid Salomon, Gonzalo Vega  
> **Finalidad:** Documentar con transparencia las consultas realizadas a herramientas de Inteligencia Artificial, los aportes aprovechados, los errores o alucinaciones detectadas y corregidas, y los métodos de verificación humana aplicados.

---

## 1. Protocolo de Gobernanza y Validación de IA
1. **No Carga de Datos Confidenciales:** No se cargan a las herramientas de IA datos personales reales no públicos ni credenciales.
2. **Principio de Verificación Documental:** Ninguna afirmación jurídica, cita legal, número de artículo ni hecho del caso emitido por un modelo de IA se asume como verdadero sin ser contrastado con el texto completo de la normativa argentina (Ley 26.388, Código Penal, Ley 25.326, Ley 27.411) y con las notas periodísticas realmente abiertas y leídas.
3. **Registro de Descarte y Corrección:** Todo error conceptual, alucinación jurídica o dato sin respaldo detectado en las respuestas de los modelos se registra en esta bitácora junto con la corrección realizada.

---

## 2. Matriz de Registro de Interacciones

| ID | Fecha | Herramienta / Modelo | Objetivo | Prompt Utilizado (Resumen) | Respuesta / Aporte Aprovechado | Errores / Descartes / Correcciones | Fuente de Verificación Humana |
|:---|:---|:---|:---|:---|:---|:---|:---|
| **#001** | 2026-10-30 | Gemini | Verificación inicial del entorno y herramientas ofimáticas | *Verificación de herramientas instaladas en el sistema operativo para edición y conversión de documentos.* | Detección de LibreOffice 26.2.6 en Linux y `pdftotext`. Definición del flujo técnico de trabajo. | Ninguno (relevamiento de entorno). | Comandos del sistema (`which`, `libreoffice --version`). |
| **#002** | 2026-10-30 | Gemini | Selección preliminar del caso y armado de guía inicial | *Selección de un caso real argentino para el Eje 1 y redacción de guía preliminar (`guia-planificador-claude.md`).* | Elección del **Caso Elías Ezequiel Nuñes Pinheiro (SIM Swapping y acceso ilegítimo)** y definición de la estructura de carpetas en `resolucion-consignas/`. | En ese borrador preliminar Gemini incluyó sin verificar: condena por fraude informático (art. 173 inc. 16) y art. 157, "sentencia firme del 06/10/2023", UFEDECO/UFECI y Cellebrite. Todos esos datos fueron descartados en las sesiones #003 y #005. | Contraste posterior en sesiones #003 y #005 contra las notas periodísticas reales y el texto de la Ley 26.388. |
| **#003** | 2026-10-30 | Claude Sonnet *(Planificador)* | Planificación del trabajo y reglas de verificación | *Diseño del plan de ejecución (`plan-ejecucion-tpi.md`), corrección de errores de la guía inicial y fijación de reglas de estilo.* | Descarte de la condena por arts. 173 inc. 16 y 157 CP. Definición del protocolo de clasificación de datos (Confirmado, Reportado, Contradictorio, No hallado), estructura en 6 etapas, guion para 4 integrantes y paquete de anexos. | Prohibición de proponer medidas técnicas sofisticadas y de incluir afirmaciones sin respaldo documental. | Contraste preliminar con prensa sobre la causa porteña y la causa federal. |
| **#004** | 2026-10-30 | Gemini *(Ejecutor)* | Primera ejecución de los entregables | *Generación inicial de `fuentes-material.md`, `fuentes-caso.md`, `contenido-informe.md`, DOCX/PDF, PPTX, guion y anexos.* | Estructura base del script `05_calcular_hashes.py` con la librería estándar `hashlib` y armado inicial de las carpetas de entrega. | Gemini no abrió las notas periodísticas (solo usó resúmenes de búsqueda) e inventó URLs, títulos y fechas (`06/10/2023`, Clarín, Perfil, Primera Edición, El Territorio), además de inventar "20 años", "Causa N° 29/2023", un Samsung A52 secuestrado, el hash de un archivo vacío (`e3b0c442...`) y números de página inexactos de los PDFs. | Auditoría completa en la Sesión #005 (`revision-correcciones.md`). |
| **#005** | 2026-10-30 / 2026-10-31 | Claude Sonnet *(Revisor)* y Gemini *(Ejecutor)* | Auditoría de veracidad (`revision-correcciones.md`) y corrección integral de entregables (ítems A1–C5) | *Apertura y lectura real de las notas periodísticas del caso, releído página por página de los PDFs con `pdftotext`, reemplazo de datos inventados por modelos ficticios rotulados y regeneración de DOCX, PDF y PPTX.* | 1) Apertura y descarga de 9 notas reales (`[F1]` a `[F9]`) en `10_Evidencia_Fuentes/`.<br>2) Clasificación rigurosa de hechos en `fuentes-caso.md` y `08_Fuentes_Caso.md`.<br>3) Creación de `05_ejemplo_registro_ficticio.txt` (hash real `40b4ae55...57a4`) y rotulado de los anexos 02 y 03 como ejemplos ficticios.<br>4) Corrección de `fuentes-material.md`, informe (DOCX/PDF), anexos DOCX con tablas reales, matriz (XLSX/MD), guion (~1.305 palabras, 10 min) y diapositivas (PPTX). | Se eliminaron todas las fuentes no verificadas, la afirmación de "sentencia firme", "20 años", "Causa N° 29/2023", "Personal/Telecom", el supuesto secuestro del Samsung A52 y las medidas sofisticadas (biometría facial, bolsa de Faraday, bloqueador de escritura, llaves físicas). Se rotuló que la numeración de los artículos penales es interpretación propia. | Lectura directa de `[F1]` a `[F9]`, lectura página por página con `pdftotext` de `arg_ley26388 (1).pdf`, `Unidad_3...pdf`, `Unidad 4...pdf`, `000099168.pdf`, `SEMANA 2...pdf` y `JURISPRUDENCIA...pdf`, e inspección visual de páginas renderizadas con `pdftoppm -png`. |

---

## 3. Registro Detallado de Sesiones

### Sesión #001: Preparación del Entorno
* **Fecha:** 30 de octubre de 2026
* **Herramientas activas:** Gemini
* **Objetivo:** Auditar las herramientas disponibles para generar y verificar documentos ofimáticos y PDFs.
* **Decisiones adoptadas:**
  * Uso de plantilla base (`material/Plantilla entrega de trabajos ok.docx`) y conversión a PDF con LibreOffice headless.

### Sesión #002: Selección Preliminar del Caso y Borrador de Guía
* **Fecha:** 30 de octubre de 2026
* **Herramientas activas:** Gemini
* **Objetivo:** Seleccionar un caso real argentino para el Eje 1 y estructurar los entregables en `resolucion-consignas/`.
* **Decisiones adoptadas y errores luego corregidos:**
  * Se eligió el **Caso Elías Ezequiel Nuñes Pinheiro**.
  * *Nota de corrección:* En esta sesión preliminar el modelo había incluido datos no verificados (como atribuir la condena al fraude informático del art. 173 inc. 16 y al art. 157, afirmar que la sentencia era firme de octubre de 2023 y mencionar UFEDECO/UFECI y Cellebrite), los cuales fueron descartados y corregidos en las sesiones #003 y #005.

### Sesión #003: Planificación y Reglas de Verificación
* **Fecha:** 30 de octubre de 2026
* **Herramientas activas:** Claude Sonnet (Planificador)
* **Objetivo:** Formular el plan de ejecución (`plan-ejecucion-tpi.md`) y fijar reglas de rigor fáctico y lenguaje sencillo.
* **Decisiones adoptadas:**
  * Descarte de la condena por fraude informático (art. 173 inc. 16), reservándolo como análisis académico comparativo.
  * Creación del protocolo de clasificación de datos: *Confirmado* (≥2 fuentes leídas), *Reportado* (1 fuente, citando el medio), *Contradictorio* (declarar la discrepancia) y *No hallado* (no afirmar).

### Sesión #004: Primera Ejecución de Entregables (con defectos detectados en revisión)
* **Fecha:** 30 de octubre de 2026
* **Herramientas activas:** Gemini (Ejecutor)
* **Objetivo:** Generar la primera versión del informe, presentación, guion y anexos.
* **Problemas detectados posteriormente:**
  * Las búsquedas web solo habían devuelto enlaces de redirección y resúmenes; el modelo completó sin abrir las notas, inventando URLs, títulos y fechas, números de causa y datos periciales (Samsung A52, hash de archivo vacío) presentados como si fueran reales.

### Sesión #005: Auditoría Crítica y Corrección Integral (A1 a C5)
* **Fecha:** 30 y 31 de octubre de 2026
* **Herramientas activas:** Claude Sonnet (Revisor en `revision-correcciones.md`) y Gemini (Ejecución de correcciones)
* **Objetivo:** Cumplir íntegramente las correcciones obligatorias A1–A5, B1–B6 y C1–C5 sin inventar ni suponer ningún dato.
* **Acciones y verificaciones ejecutadas:**
  1. **Fuentes reales del caso (A1 y A2):** Se siguieron las redirecciones de búsqueda, se abrieron y descargaron las 9 notas periodísticas reales (`F1_Infobae.md` a `F9_LaNación.md` en `anexos-para-zip/10_Evidencia_Fuentes/`) y se reescribieron `actividad-IA/fuentes-caso.md`, `08_Fuentes_Caso.md` y `Resumen_Notas_Periodisticas_Caso.md`. Se eliminaron las fuentes inexistentes o no verificables (Clarín, Perfil, Primera Edición, El Territorio y JusBaires).
  2. **Eliminación de datos inventados y rotulado de modelos (A3, A4 y A5):** Se eliminaron "20 años", "Causa N° 29/2023", "sentencia firme", "octubre de 2023", "Personal/Telecom" y el supuesto secuestro de un Samsung A52. Se incorporaron los datos reales verificados (Movistar, SIM "blanca" de Comtel S.A., consultas a RENAPER, Nosis y Dark PFA, contacto "ElJuanxd", destrucción del celular quemándolo y arrojándolo al río Paraná [F2, F5], condena en juicio abreviado homologado en el Juzgado Penal 29 de CABA a 3 años en suspenso y 150 hs de tareas [F1, F2], y discrepancias entre [F1] y [F2]). Se creó `05_ejemplo_registro_ficticio.txt`, se calculó su hash SHA-256 real (`40b4ae55313c6236cb881819d70514e1891faf4d6aa68d7975c72b42749c57a4`) con `05_calcular_hashes.py` y se rehicieron los anexos 02 y 03 y los apartados 4.3 y 4.4 del informe como modelos con datos ficticios claramente rotulados.
  3. **Verificación de documentos de estudio y articulado penal (B1 y B2):** Se leyeron todas las páginas de `arg_ley26388 (1).pdf`, `Unidad_3_Evidencia digital tup.pdf`, `Unidad 4 cadena de custodia TUP a distancia.pdf`, `000099168.pdf`, `SEMANA 2 - DELITOS INFORMATICOS.pdf` y `JURISPRUDENCIA DELITOS INFORMATICOS.pdf` con `pdftotext`, corrigiendo números de página y secciones en `fuentes-material.md` y ajustando el texto de los arts. 153 bis, 153, 197, 255, 157 bis y 173 inc. 16 CP, aclarando que la numeración de artículos aplicada al caso es interpretación propia del equipo.
  4. **Estilo, medidas simples y coherencia entre archivos (B3, B4, B5 y B6):** Se quitaron las medidas sofisticadas y las alusiones a material de estudio o consignas, se aclaró que la matriz es una valoración cualitativa sin fórmulas y se alinearon informe, anexos, guion y presentación.
  5. **Verificación visual y de formato (C1 a C5):** Se regeneraron los anexos `.docx` 01 a 03 con tablas reales de Word, se corrigió la alineación y paginación de `Informe_TPI_Eje1.docx` / `.pdf` (10 páginas, sin páginas en blanco y con la matriz completa en la página 6), se rehizo `Presentacion_TPI_Eje1.pptx` con tabla completa de los 7 riesgos en la diapositiva 5 y sin texto residual, se verificó la extensión del guion (~1.305 palabras habladas para 10 minutos) y se inspeccionaron las imágenes renderizadas con `pdftoppm -png`.
