# Bitácora de Registro y Trazabilidad de Interacción con IA

> **Asignatura:** Legislación – Tecnicatura Universitaria en Programación (UTN)  
> **Eje Temático:** Eje 1 – Cibercrimen, evidencia digital y cadena de custodia  
> **Estudiante:** Gonzalo Vega  
> **Finalidad:** Cumplir con las directrices de la consigna oficial (Sección 5 - Etapa 5 y Sección 7 - Uso de IA Generativa), garantizando transparencia, trazabilidad, verificación jurídica humana y análisis propio sin copia acrítica.

---

## 1. Protocolo de Gobernanza y Validación de IA
1. **No Carga de Datos Confidenciales:** No se cargan a las herramientas de IA datos personales reales no públicos ni credenciales.
2. **Principio de Verificación Cruzada:** Ninguna afirmación jurídica, cita legal o número de artículo emitido por un modelo de IA se asume como verdadero hasta ser contrastado con el texto oficial del Código Penal de la Nación Argentina, leyes especiales (ej. Ley 26.388, Ley 25.326) o jurisprudencia confirmada.
3. **Registro de Descarte y Corrección:** Todo error conceptual, alucinación jurídica o sesgo detectado en las respuestas de los modelos debe registrarse en la bitácora junto con la corrección humana realizada.

---

## 2. Matriz de Registro de Interacciones

| ID | Fecha | Herramienta / Modelo | Objetivo / Consigna | Prompt Utilizado (Resumen) | Respuesta / Aporte Aprovechado | Errores / Descartes / Correcciones | Fuente de Verificación Humana |
|:---|:---|:---|:---|:---|:---|:---|:---|
| **#001** | 2026-10-30 | Antigravity / Gemini | Verificación inicial de entorno y herramientas ofimáticas | *Verificación de entorno del sistema operativo y extensiones del IDE para manejo de suites ofimáticas.* | Detección de LibreOffice 26.2.6 en Linux, pdftotext y extensión PDF en el IDE. Definición del flujo técnico de trabajo. | Ninguno (análisis de entorno de sistema). | Ejecución de comandos del sistema operativo (`which`, `libreoffice --version`, inspección de caché de extensiones). |
| **#002** | 2026-10-30 | Antigravity / Gemini | Selección del caso y configuración de entregables | *Descarte del caso Vélez Cheratto y selección de un caso real argentino con sentencia firme para el Eje 1.* | Confirmación del **Caso Ezequiel Nuñes Pinheiro (SIM Swapping, Acceso Ilegítimo y Fraude Informático)** con condena firme en juicio abreviado (octubre 2023). Configuración de estructura de entregables en `resolucion-consignas/` y guion para 4 integrantes. | Ninguno. Se adoptaron los requerimientos del estudiante y se actualizó la guía para Claude. | Fallo del Juzgado PCyF N° 29 de CABA (Jueza Martínez), causas UFEDECO/UFECI, Ley 26.388 y Ley 25.326. |
| **#003** | 2026-10-30 | Claude Sonnet *(Planificador)* | Arquitectura y planificación del informe del TPI | *Diseño del plan integral de ejecución (`plan-ejecucion-tpi.md`), corrección de datos fácticos y fijación de reglas de estilo y tono para estudiantes.* | Detección de inconsistencias en tipificación previa (se descartó condena por art. 173 inc. 16 y 157). Pautado de fuentes mínimas, estructura de 6 etapas, guion para 4 integrantes y paquete de anexos. | Descarte de citas sin respaldo periodístico. Prohibición de soluciones técnicas poco realistas ("fancy") y de alusiones al material de la cátedra en el cuerpo. | Búsqueda cruzada en Infobae y La Nación sobre la causa porteña. |
| **#004** | 2026-10-30 | Antigravity / Gemini Flash *(Ejecutor)* | Ejecución técnica y producción de todos los entregables | *Ejecución metodológica de las 8 fases del plan: relevamiento de fuentes, redacción del informe, generación de DOCX/PDF, guion y anexos.* | Generación de: `fuentes-material.md`, `fuentes-caso.md`, `contenido-informe.md`, `Informe_TPI_Eje1.docx`, `Informe_TPI_Eje1.pdf` (9 págs.), `Presentacion_TPI_Eje1.pptx` (10 diapositivas), `guion-video-4-integrantes.md` (10:30 min) y los 10 componentes de `anexos-para-zip/`. | Se eliminaron términos como "consigna" o "cátedra" del cuerpo; se ajustó el script de hashes para usar solo librería estándar `hashlib`. | Código Penal Argentino (Ley 26.388), Ley 25.326, InfoLEG y fuentes periodísticas [F1] a [F8]. |

---

## 3. Registro Detallado de Sesiones

### Sesión #001: Preparación del Entorno y Análisis de Factibilidad
* **Fecha:** 30 de octubre de 2026
* **Herramientas activas:** Antigravity (Ejecutor local)
* **Objetivo:** Auditar el entorno de ejecución, plantillas disponibles y contrastar la viabilidad de casos reales para el Eje 1 (LibreFútbol vs. Caso Vélez Cheratto).
* **Decisiones adoptadas:**
  * Configuración del flujo de trabajo en dos capas: **Planeamiento estratégico (Claude Sonnet)** y **Ejecución operativa / pericial / documental (Antigravity)**.
  * Adopción de la plantilla oficial del estudiante (`material/Plantilla entrega de trabajos ok.docx`).

### Sesión #002: Elección de Caso con Sentencia Firme y Especificación de Entregables
* **Fecha:** 30 de octubre de 2026
* **Herramientas activas:** Antigravity (Ejecutor local)
* **Objetivo:** Definición de un caso real argentino no enseñado en clase, con sentencia judicial firme y todos los entregables formalizados.
* **Decisiones adoptadas:**
  * Elección definitiva del **Caso Elías Ezequiel Nuñes Pinheiro**: cumple con el Eje 1 (cibercrimen, SIM swapping, acceso indebido, entorpecimiento), tiene sentencia condenatoria en juicio abreviado (Juzgado PCyF N° 29 de CABA, octubre 2023).
  * Creación de la rama `desarrollo` en git.
  * Definición de la carpeta `resolucion-consignas/` con subcarpetas para el informe escrito, la presentación con guion para 4 integrantes (8 a 12 min) y la carpeta con contenidos para el archivo ZIP de anexos.

### Sesión #003: Planificación Estratégica y Reglas de Trazabilidad
* **Fecha:** 30 de octubre de 2026
* **Herramientas activas:** Claude Sonnet (Planificador)
* **Objetivo:** Formular el plan de trabajo detallado (`plan-ejecucion-tpi.md`) y fijar los filtros de rigor fáctico y estilo.
* **Decisiones adoptadas:**
  * Corrección crítica: Se constató que Nuñes Pinheiro fue condenado por arts. 153 bis, 197 y 255 CPA, pero no por fraude informático (173 inc. 16), el cual se reserva como análisis doctrinario propio.
  * Reglas de estilo: Tono de estudiantes de programación (español rioplatense, sin jerga forzada, soluciones simples y realistas).
  * Prohibición absoluta de decir "según la guía" o "la cátedra" en el texto final.

### Sesión #004: Ejecución Operativa Completa de Entregables
* **Fecha:** 30 de octubre de 2026
* **Herramientas activas:** Antigravity / Gemini Flash (Ejecutor)
* **Objetivo:** Ejecutar integralmente el plan y generar todos los entregables en `resolucion-consignas/`.
* **Decisiones adoptadas:**
  * Relevamiento de 9 fuentes del material oficial en `actividad-IA/fuentes-material.md`.
  * Relevamiento de 8 fuentes externas (Infobae, Clarín, La Nación, Perfil, Página/12, Primera Edición, El Territorio, JusBaires) en `actividad-IA/fuentes-caso.md`.
  * Redacción del informe escrito en Markdown (`contenido-informe.md`) y generación automatizada de `Informe_TPI_Eje1.docx` respetando la portada oficial con marcadores editables, compilando el PDF oficial de 9 páginas mediante LibreOffice headless.
  * Armado del guion para 4 integrantes en `guion-video-4-integrantes.md` (cronometrado en 10:30 min con preguntas probables).
  * Adaptación de la presentación en diapositivas `Presentacion_TPI_Eje1.pptx` (10 diapositivas).
  * Construcción de la carpeta de anexos para el ZIP (`resolucion-consignas/anexos-para-zip/`) con 10 componentes (protocolo, formulario de cadena de custodia, plantilla pericial TUP, matriz XLSX y MD, script Python de hashes probado, bitácoras de IA, constancias de sentencia y evidencia de prensa).

*(Se irán agregando las sucesivas sesiones a medida que avancemos en cada etapa del TPI).*
