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
| **#006** | 2026-10-31 | Gemini | Conversión universal a PDF de anexos documentales y ajuste de roles en guion y presentación | *Conversión a PDF con fidelidad textual estricta (100% palabras coincidentes, sin agregar ni quitar contenido) de todos los archivos Markdown y texto de la carpeta de anexos (`01` a `09`), y actualización de guion y diapositivas (asignación de Bloque 2 a Gonzalo Vega y Bloque 4 a Hugo Tcach, eliminación de sección de preguntas).* | 1) Generación mediante LibreOffice y Flat ODF de los PDFs correspondientes a la totalidad de anexos documentales: `01_Protocolo_Evidencia_Digital.pdf`, `02_Formulario_Cadena_Custodia.pdf`, `03_Plantilla_Informe_Tecnico_Juridico_TUP.pdf`, `04_Matriz_Riesgos.pdf`, `05_ejemplo_registro_ficticio.pdf`, `06_Prompts_y_Registro_IA.pdf`, `07_Declaracion_Uso_IA.pdf`, `08_Fuentes_Caso.pdf` y `09_Sentencia_Abreviado_CABA/LEEME.pdf`.<br>2) Garantía de lectura universal sin requerir visores de Markdown específicos por parte de los docentes evaluadores.<br>3) Adecuación del guion del video a los 4 integrantes definitivos y eliminación de preguntas probables por ser modalidad video. | Se evitó cualquier distorsión tipográfica o desborde de tablas mediante generación controlada en Flat ODF (`.fodt`), asegurando 0 palabras faltantes o añadidas (verificación automatizada con `pdftotext`). | Verificación automatizada con scripts en Python (`pdftotext`, conteo de palabras e intersección léxica), inspección de metadatos (`pdfinfo`) y renderizado visual con `pdftoppm -png`. |
| **#007** | 2026-11-02 | Gemini | Depuración final de archivos intermedios en carpeta de anexos y unificación de referencias a `.pdf` (ítem C6) | *Ejecución de la directriz "Listo para entregar": eliminación de los 8 archivos intermedios `.md`/`.txt` (`01` al `08`) y de los 3 `.docx` (`01` al `03`) de la carpeta de anexos, eliminación de scripts auxiliares en la carpeta del informe, actualización de referencias en el informe `.docx`/`.pdf`, `Presentacion_TPI_Eje1.pptx` y `LEEME.txt` para que apunten a los `.pdf` definitivos, y registro de campos pendientes.* | Eliminación de archivos intermedios en `Anexos_TPI_Comision5_Serafini_Tcach_Salomon_Vega/` y `Documento_entregable_TPI_Comision5_Serafini_Tcach_Salomon_Vega/`, conservando únicamente las versiones definitivas en `.pdf`, `04_Matriz_Riesgos.xlsx`, el script `05_calcular_hashes.py` y las subcarpetas `09_Sentencia_Abreviado_CABA/` y `10_Evidencia_Fuentes/`. Unificación de todas las referencias cruzadas hacia los archivos `.pdf` y conservación de `Oscar Londero - Martín Mangini` en la portada. | Se corrigieron las alusiones que apuntaban a `.md`, `.txt`, `.docx`, `anexos-para-zip/` y `material/` dentro de `TPI_Legislacion_Comision5_Serafini_Tcach_Salomon_Vega.docx` y se dejaron marcados los 2 campos pendientes de completar antes de la exportación final a PDF (`[COMPLETAR: fecha de entrega]` y `[COMPLETAR: link del video en YouTube]`). | Verificación de estructura de carpetas (`ls -la`), lectura de párrafos y tablas de `TPI_Legislacion_Comision5_Serafini_Tcach_Salomon_Vega.docx` y reexportación con LibreOffice headless. |

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

### Sesión #006: Conversión Universal a PDF de Anexos y Ajustes Finales de Roles
* **Fecha:** 31 de octubre de 2026
* **Herramientas activas:** Gemini
* **Objetivo:** 
  1. Convertir la totalidad de los archivos Markdown y texto de la carpeta de anexos (`01` a `09`) a formato PDF con fidelidad textual absoluta (100% idénticos, sin agregar ni suprimir información), garantizando que los docentes evaluadores puedan visualizarlos e imprimirlos sin depender de extensiones o visores de Markdown.
  2. Reasignar roles en el guion del video y la presentación: Bloque 2 (Marco Jurídico) a Gonzalo Vega y Bloque 4 (Buenas Prácticas Técnicas y Organizacionales) a Hugo Tcach.
  3. Eliminar la sección de preguntas probables del guion y actualizar la diapositiva final de la presentación, dado que la entrega es un video pregrabado sin instancia sincrónica de preguntas.
* **Acciones y verificaciones ejecutadas:**
  1. **Generación de PDFs con fidelidad 100%:** Se implementó una canalización de generación mediante Flat OpenDocument (`.fodt`) procesado por LibreOffice headless con perfil aislado de usuario. Se generaron con éxito:
     * `01_Protocolo_Evidencia_Digital.pdf` (1 página)
     * `02_Formulario_Cadena_Custodia.pdf` (1 página con tabla estructurada)
     * `03_Plantilla_Informe_Tecnico_Juridico_TUP.pdf` (1 página ejecutiva)
     * `04_Matriz_Riesgos.pdf` (2 páginas apaisadas con la tabla completa)
     * `05_ejemplo_registro_ficticio.pdf` (1 página en tipografía monoespaciada)
     * `06_Prompts_y_Registro_IA.pdf` (documento completo de bitácora)
     * `07_Declaracion_Uso_IA.pdf` (declaración formal de uso de IA)
     * `08_Fuentes_Caso.pdf` (detalle de las 9 fuentes y su contrastación)
     * `09_Sentencia_Abreviado_CABA/LEEME.pdf` (instrucciones de acceso al fallo)
  2. **Validación algorítmica de texto:** Para cada archivo se ejecutó extracción con `pdftotext` comparando el conjunto léxico contra el archivo Markdown/texto original, corroborando cero palabras faltantes (`set()`).
  3. **Inspección visual:** Se renderizaron todas las páginas a imágenes PNG de alta resolución (`pdftoppm -png -r 150`) para auditar paginación, contraste, alineación de tablas y ausencia de desbordes o páginas huérfanas.
  4. **Ajuste de roles y guion:** Se modificó `guion-video-4-integrantes.md` asignando el Bloque 2 a Gonzalo Vega y el Bloque 4 a Hugo Tcach, adaptando las transiciones entre oradores y suprimiendo la sección 3 ("Preguntas Probables"). Se actualizó el título de la diapositiva 10 en `Presentacion_TPI_Eje1.pptx` a "Cierre de la Presentación".

### Sesión #007: Depuración Final de Anexos Intermedios y Unificación de Referencias a PDF ("Listo para Entregar" – Ítem C6)
* **Fecha:** 2 de noviembre de 2026
* **Herramientas activas:** Gemini
* **Objetivo:** Ejecutar la directriz de depuración final establecida en `plan-ejecucion-tpi.md` (Sección 6) y `revision-correcciones.md` (Ítem C6), unificar todas las referencias hacia los archivos `.pdf` definitivos y dejar registrado qué campos restan completar antes de la exportación final del informe.
* **Acciones y verificaciones ejecutadas:**
  1. **Eliminación de archivos intermedios y duplicados:**
     * En `resolucion-consignas/Anexos_TPI_Comision5_Serafini_Tcach_Salomon_Vega/`: se eliminaron los 8 archivos fuente `.md` y `.txt` (`01` al `08`) y los 3 archivos `.docx` (`01_Protocolo_Evidencia_Digital.docx`, `02_Formulario_Cadena_Custodia.docx` y `03_Plantilla_Informe_Tecnico_Juridico_TUP.docx`), conservando únicamente las versiones definitivas en `.pdf`, la planilla `04_Matriz_Riesgos.xlsx`, el script `05_calcular_hashes.py` y las subcarpetas `09_Sentencia_Abreviado_CABA/` y `10_Evidencia_Fuentes/`.
     * En `resolucion-consignas/Documento_entregable_TPI_Comision5_Serafini_Tcach_Salomon_Vega/`: se eliminaron los insumos auxiliares `contenido-informe.md` y `generar_informe_docx.py`, dejando únicamente el documento final `TPI_Legislacion_Comision5_Serafini_Tcach_Salomon_Vega.docx` y su versión `.pdf`.
  2. **Unificación de referencias hacia los archivos `.pdf`:** Se actualizaron todas las referencias cruzadas en `TPI_Legislacion_Comision5_Serafini_Tcach_Salomon_Vega.docx` (Etapas 1.4, 3, 4.2, 4.3, 4.4, 5 y Bibliografía), en `LEEME.txt`, en `09_Sentencia_Abreviado_CABA/LEEME.txt` y en `Presentacion_TPI_Eje1.pptx` para que apunten exclusivamente a los documentos `.pdf` del paquete de anexos (`01_Protocolo_Evidencia_Digital.pdf`, `02_Formulario_Cadena_Custodia.pdf`, `03_Plantilla_Informe_Tecnico_Juridico_TUP.pdf`, `04_Matriz_Riesgos.pdf`, `05_ejemplo_registro_ficticio.pdf`, `06_Prompts_y_Registro_IA.pdf`, `07_Declaracion_Uso_IA.pdf` y `08_Fuentes_Caso.pdf`).
  3. **Registro de campos pendientes de completar por el estudiante antes de generar el PDF definitivo de entrega:**
     * Se conservó la edición ya realizada por el usuario en la portada (`Profesores: Oscar Londero - Martín Mangini`).
     * Quedan pendientes únicamente 2 marcadores en la portada de `TPI_Legislacion_Comision5_Serafini_Tcach_Salomon_Vega.docx`:
       1. `Fecha de Entrega: [COMPLETAR: fecha de entrega]`
       2. `Video de Exposición (YouTube): [COMPLETAR: link del video en YouTube]`
