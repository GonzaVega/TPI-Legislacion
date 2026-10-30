# Plan de Ejecución del TPI – Eje 1 (para Gemini 3.8 Flash)

> Autor del plan: Claude Sonnet 5.5 (planificador). Ejecutor: Gemini 3.8 Flash (High).
> Insumos: `consignas/TP legislacion.pdf`, `actividad-IA/guia-planificador-claude.md`, `material/Plantilla entrega de trabajos ok.docx`, `consignas/Modelo_Presentacion_TPI_Legislacion.pptx`.
> **Regla del usuario:** ante cualquier duda, PREGUNTAR antes de suponer.

## 0. CORRECCIONES OBLIGATORIAS a la guía previa (hechos verificados)

La guía `guia-planificador-claude.md` contiene datos NO respaldados. Verificado en prensa (Infobae, La Nación):

| Dato en la guía | Realidad verificada | Acción |
|---|---|---|
| "Ezequiel Nuñes Pinheiro" | **Elías Ezequiel Nuñes Pinheiro**, de Eldorado (Misiones) | Corregir nombre |
| Condena por art. 173 inc. 16 (fraude) y art. 157 | Condenado por **acceso ilegítimo a datos informáticos restringidos (art. 153 bis), sustracción de documentos y entorpecimiento de comunicaciones** | **No afirmar** 173 inc.16 ni 157 como condena. Pueden mencionarse solo como "figuras que *podrían* analizarse" y rotuladas como análisis propio |
| Víctimas: "magistrados de la Corte" | Víctimas citadas: exministro porteño Marcelo D'Alessandro, diputado Diego Santilli, funcionarios | Usar solo lo citable |
| Condena firme sin matices | Juicio abreviado ante la jueza **María Araceli Martínez** (fuero PCyF CABA): **3 años en suspenso**, pautas de conducta, tareas comunitarias. Existe además causa **federal paralela** (Comodoro Py, juez Martínez De Giorgi; Zanchetta) **en trámite** | Aclarar en Etapa 1 el alcance: se analiza la condena porteña; la causa federal no tiene sentencia |
| Cellebrite, hashes SHA-256, antenas BTS, UFEDECO/UFECI, "15 SIM", fecha 6/oct/2023, "decomiso" | **No verificados** | Buscar fuente; si no hay, redactar como "procedimiento típico/ilustrativo" y NO como hecho del caso |

## 0 ter. PRIMERA FUENTE: el material de la cátedra (decisión del usuario, obligatorio)

Antes de salir a buscar en la web, Gemini debe **leer y extraer** lo relevante de los PDF de `material/` (con `pdftotext "archivo.pdf" -`). Orden de fuentes: **1) material de la cátedra → 2) normas oficiales (infoleg) → 3) fuentes periodísticas/jurídicas web.** La web solo completa lo que el material no cubre.

| Archivo en `material/` | Usar para |
|---|---|
| `arg_ley26388 (1).pdf` | Texto de la Ley 26.388 y artículos del CP (153 bis, etc.): citar desde acá antes que de la web |
| `SEMANA 2 - DELITOS INFORMATICOS.pdf`, `JURISPRUDENCIA DELITOS INFORMATICOS.pdf` | Conceptos de delitos informáticos y fallos |
| `Unidad_3_Evidencia digital tup.pdf` | Qué es la evidencia digital y el hash (explicar simple) |
| `Unidad 4 cadena de custodia TUP a distancia.pdf` | Cadena de custodia, protocolos, ISO/IEC 27037 |
| `000099168.pdf` | Fallo sobre cadena de custodia y discrepancia de hash (ejemplo, NO es el caso elegido) |
| `UNIDAD 1 ...`, `PRESENTACION UNIDAD 1...`, `Programa_Legislacion_V1.2.pdf` | Conceptos generales y marco de la materia |
| `referencia-fallo-velez-c.md` | Es el caso que NO se usa; solo puede servir de apoyo conceptual sobre cadena de custodia, sin desarrollarlo |

**Reglas:**
1. Leer primero todos los PDF relevantes y armar `actividad-IA/fuentes-material.md`: archivo | página o fragmento | concepto extraído (resumido con palabras propias) | dónde se usó en el informe.
2. Cada concepto o norma del informe debe usar primero lo que dice el material. Si el material no lo cubre, recién ahí se busca afuera, y se anota en `fuentes-caso.md`.
3. **En el texto del informe, la presentación y el guion NO se menciona que viene del material** (ver sección 5). Los conceptos se explican directamente. La constancia vive únicamente en `fuentes-material.md`, la bitácora de IA y la **bibliografía**, donde pueden figurar los documentos como referencias (ej. título del documento, unidad, año si consta).
4. Si el material contradice una fuente web, prevalece el texto de la norma oficial y se avisa al usuario.
5. Si algún PDF no extrae texto (escaneado), avisar al usuario antes de seguir; no suponer su contenido.
6. Incluir `fuentes-material.md` en `anexos-para-zip/08_Fuentes_Caso.md` como sección aparte ("Fuentes de estudio").



## 0 bis. PROTOCOLO DE INVESTIGACIÓN Y FUENTES SOBRE EL CASO (decisión del usuario, obligatorio)

Si el usuario consigue la sentencia, la aportará y será la fuente primaria. Si no, el caso se reconstruye **solo con datos coincidentes entre fuentes confiables**. Prohibido inventar, suponer o completar con "lo típico".

**Fuentes a consultar (mínimo 8, al menos 3 medios distintos):** Infobae, La Nación, Clarín, Página 12, Perfil, medios misioneros (Primera Edición, El Territorio, Misiones Online), Fiscales.gob.ar / MPF CABA / Poder Judicial CABA (jusbaires.gob.ar), Palabras del Derecho, Microjuris, elDial, Abogados.com.ar, Infobae/La Nación para la causa federal.

**Reglas de uso de los datos (clasificar cada dato):**
- **Confirmado:** aparece en ≥2 fuentes independientes, o en una fuente oficial. Se afirma sin reservas.
- **Reportado:** aparece en una sola fuente confiable. Se redacta como "según [medio]".
- **Contradictorio:** las fuentes difieren. Se declara la discrepancia, no se elige una.
- **No hallado:** se omite o se marca explícitamente como "no surge de las fuentes consultadas".
Ejemplos ya detectados como discrepantes: "decomiso" y "unificación de condenas".

**Registro (cumple las reglas de interacción con IA):**
1. Crear `actividad-IA/fuentes-caso.md` con tabla: ID | Medio | Título | URL | Fecha de publicación | Fecha de consulta | Datos extraídos | Estado (Confirmado/Reportado/Contradictorio). Debe incluir también las búsquedas realizadas (consulta literal) y las que no dieron resultado.
2. Registrar en `registro-trazabilidad-ia.md` cada consulta web como entrada nueva (prompt, qué se aprovechó, qué se descartó, cómo se verificó = contraste entre fuentes).
3. Incorporar las URL consultadas en: la **Bibliografía/fuentes** del informe (con fecha de consulta), la **Etapa 5** (evidencia de verificación) y el anexo `08_Fuentes_Caso.md`.
4. Guardar copia de respaldo de cada nota usada en `anexos-para-zip/10_Evidencia_Fuentes/` (texto extraído en .md con URL y fecha; PDF solo si es de acceso libre). Es la "prueba de la investigación".
5. Cada afirmación fáctica del informe lleva marca de fuente (ej. `[F3]` = ID de la tabla). Antes de maquetar, auditar que ninguna afirmación quede sin marca.
6. Nunca cargar a la IA datos personales no públicos. Usar solo lo publicado por los medios.

**Sentencia:** intentar localizarla (JusBaires, Fiscales.gob.ar, sitios jurídicos). Si no aparece, el anexo `09_Sentencia_Abreviado_CABA/LEEME.txt` explica que no fue hallada y remite a las reseñas de `10_Evidencia_Fuentes/`. Si el usuario la aporta, se agrega ahí y se actualizan los datos "Reportado" a "Confirmado".

**Tarea 0 (previa a todo):** ejecutar este protocolo, completar `fuentes-caso.md`, mostrar al usuario un resumen de datos Confirmados/Reportados/Contradictorios y recién entonces pasar a la redacción.


## 1. Datos confirmados por el usuario (NO volver a preguntar)

- **Integrantes (4):** Mateo Serafini, Hugo Tcach, Farid Salomon, Gonzalo Vega. **Comisión 5** (todos). Entrega grupal real.
- **Portada:** reemplazar TODOS los datos de la plantilla (Metodología de Sistemas 1, 2024, etc.). Materia: Legislación. Título: caso Nuñes Pinheiro. Campos con marcador editable visible, por ejemplo `[COMPLETAR: fecha de entrega]`, `[COMPLETAR: docentes]` y `[COMPLETAR: link del video en YouTube]` (este último como línea propia en la portada). El usuario los edita después.
- **Sentencia del abreviado (CABA):** debe acompañarse en `anexos-para-zip/`. Una búsqueda previa NO encontró PDF público del texto íntegro (la JusBaires exige gestión oficial). Gemini debe: (a) intentar `search_web` sobre Poder Judicial CABA/MPF CABA/Fiscales.gob.ar/Infobae/La Nación y descargar cualquier PDF o texto de la resolución; (b) si no aparece, **no inventarla ni reconstruirla**. Crear `09_Sentencia_Abreviado_CABA/LEEME.txt` con: fuentes periodísticas que la reseñan (URL y fecha), datos que se conocen y la indicación de que el texto íntegro debe solicitarse al Juzgado PCyF N° 29 vía JusBaires; y **avisar al usuario**. Preguntarle si prefiere que se cite la reseña periodística como sustituto.
- Ojo: una fuente menciona "decomiso" y "unificación de condenas"; contrastar antes de afirmarlo.

## 1 bis. Preguntas pendientes (usar `ask_question` solo si surgen)

1. Extensión del informe (sugerido 15–25 páginas).
2. Formato de citas (APA o libre).


## 2. Estructura de carpetas (ya creada)

```
resolucion-consignas/
├── documento-informe/        Informe_TPI_Eje1.docx + .pdf
├── presentacion-y-guion/     Presentacion_TPI_Eje1.pptx + guion-video-4-integrantes.md
└── anexos-para-zip/          ← contenido del ZIP (el usuario lo comprime)
```
No incluir en el ZIP datos personales reales no públicos (consigna 6.2). Para ejemplos usar datos sintéticos.

## 3. Herramientas

- No hay python-docx/pptx instalados. **Pedir permiso** para `pip install --user python-docx python-pptx openpyxl` (necesita red) o, alternativa: generar con LibreOffice headless (`soffice --headless --convert-to pdf`), escribiendo el contenido en `.fodt`/HTML y convirtiendo.
- Para respetar la plantilla: copiar `material/Plantilla entrega de trabajos ok.docx`, abrir con python-docx, reemplazar campos de portada y volcar contenido con los estilos de la plantilla. Si la plantilla no tiene estilos de Heading/tabla, definirlos sin alterar fuente/márgenes base.
- Validar cada entregable: convertir a PDF y revisar visualmente (`pdftoppm -png` y ver imagen).

## 4. Orden de trabajo (cada paso se registra en `registro-trazabilidad-ia.md`)

### Paso A – Tarea 0 y preguntas (sección 0 y 1).
### Paso B – Redactar el contenido fuente en Markdown (`resolucion-consignas/documento-informe/contenido-informe.md`) y que el usuario lo revise antes de maquetar. Contenido:

**Resumen ejecutivo:** 8–12 líneas exactas.

**Etapa 1 – Caso y alcance:** hechos verificados (SIM swapping desde Eldorado, ingeniería social ante operadoras, accesos no autorizados, uso de Telegram, pedidos de terceros, pagos menores); actores; sistemas (red móvil, procesos de reposición de SIM, 2FA por SMS, bases de datos consultadas); datos (personales, comunicaciones); sentencia (juicio abreviado, 3 años en suspenso); aclaración de causa federal abierta y límites del análisis (basado en fuentes públicas, sin acceso al expediente).

**Etapa 2 – Marco jurídico (explicar POR QUÉ aplica cada norma):**
- CP arts. 153 bis (acceso ilegítimo), 153 (comunicaciones/entorpecimiento: verificar redacción exacta y art. 197 sobre interrupción de comunicaciones), 255 (sustracción de documentos) – **verificar numeración contra infoleg antes de citar**.
- Ley 26.388; Ley 25.326 (arts. 9 y 10); art. 18 CN (inviolabilidad de comunicaciones y debido proceso); Ley 25.873/Ley 19.798 de telecomunicaciones y normas ENACOM sobre portabilidad/ SIM solo si se verifican; Convenio de Budapest (Ley 27.411); ISO/IEC 27037 (mención breve, ver nota de estándares); guías de evidencia digital del MPF/Protocolo de actuación en evidencia digital (verificar nombre exacto).

**Nota de estándares (ISO/IEC 27037 y RFC 3227) – simplificar y dejar constancia del origen:**
- **ISO/IEC 27037:** verificado en `material/Unidad 4 cadena de custodia TUP a distancia.pdf` (aparece como norma sobre identificación, recolección y preservación de evidencia digital). Usar solo la idea general en 2–3 líneas ("es una norma internacional con buenas prácticas para identificar, recolectar y conservar evidencia digital"). No detallar fases ni cláusulas. En el texto NO decir que viene del material; la constancia va en `fuentes-caso.md` (ID de fuente, archivo y página/línea) y en la bitácora de IA.
- **RFC 3227:** NO aparece en ningún PDF del material (buscado con `pdftotext`). Antes de incluirlo, Gemini debe verificarlo en fuente externa (rfc-editor.org / ietf.org), guardar el link y la fecha de consulta en `fuentes-caso.md` y explicarlo en 1–2 líneas ("recomienda recolectar primero la evidencia que más rápido se pierde, como la memoria"). Si no puede verificarlo, **omitirlo**.
- Regla general: todo estándar o norma citada debe tener constancia de dónde se obtuvo (archivo del material con ubicación, o link con fecha de consulta). Sin constancia, no se cita.
- Subsección "Figuras conexas analizadas" (fraude informático art. 173 inc. 16, 157 bis) rotulada como análisis académico, no condena.

**Etapa 3 – Matriz (≥6 riesgos), columnas obligatorias:** Riesgo | Tipo | Norma/principio | Probabilidad | Impacto | Medida propuesta (+ columna Criticidad). Riesgos sugeridos: (1) reposición fraudulenta de SIM por validación débil; (2) acceso ilegítimo a bases de datos con credenciales de terceros; (3) 2FA por SMS vulnerable; (4) nulidad/pérdida de valor probatorio por cadena de custodia deficiente; (5) responsabilidad civil/administrativa de operadoras y proveedores de datos (Ley 25.326, Defensa del Consumidor); (6) riesgo ético-penal del técnico que participa sin cuidado (instigación/participación, deber de confidencialidad); (7) daño reputacional/extorsión a víctimas. Escala Baja/Media/Alta + criticidad = P×I.

**Etapa 4 – Medidas y documentos (los dos primeros son entregables en anexos):**
1. Protocolo simple de relevamiento, preservación y documentación de evidencia digital: pasos numerados y cortos (identificar qué hay, no tocar ni modificar el original, hacer una copia, calcular el hash para comprobar que no cambió, guardar todo en un lugar seguro, anotar quién lo manejó y cuándo). Sin términos forenses avanzados.
2. Formulario de Cadena de Custodia.
3. Plantilla de Informe técnico-jurídico para el TUP que colabora en una pericia (identificación, objeto, metodología, hallazgos, hashes, limitaciones, conclusiones, firma, declaración de imparcialidad).
4. Medidas simples para empresas (ver sección 5: nada sofisticado): verificación de identidad más estricta al reponer una SIM, aviso al titular por otro medio, autenticación con app en lugar de SMS, guardar registros de lo que pasa y un plan básico de qué hacer ante un incidente.
5. Comentario sobre cooperación internacional/Budapest si hay servicios en el extranjero (Telegram).

**Etapa 5 – Uso de IA:** tabla herramientas/finalidad/qué se adoptó/qué se descartó (incluir la corrección de la sección 0 como ejemplo real de alucinación detectada y corregida) / cómo se verificó. Remitir a anexos.

**Etapa 6 – Conclusiones y rol del TUP.**

**Bibliografía:** solo fuentes realmente consultadas (periodísticas con URL y fecha, normas con infoleg, ISO, RFC).

### Paso C – Maquetar `documento-informe/Informe_TPI_Eje1.docx` sobre la plantilla → exportar PDF → verificar páginas con imágenes.
Orden: Portada, Resumen ejecutivo, Etapas 1–6 (con matriz como tabla), Declaración de IA y evidencia de verificación, Conclusiones, Bibliografía.

### Paso D – Anexos en `anexos-para-zip/` (nombres numerados):
- `01_Protocolo_Evidencia_Digital.docx`
- `02_Formulario_Cadena_Custodia.docx` (campos: nº de caso, ítem, descripción, hash, fecha/hora, responsable, estado, firmas)
- `03_Plantilla_Informe_Tecnico_Juridico_TUP.docx`
- `04_Matriz_Riesgos.xlsx` (o .docx)
- `05_calcular_hashes.py` (stdlib: hashlib SHA-256 de archivos/carpeta, salida CSV con fecha UTC; probarlo ejecutándolo sobre archivos sintéticos)
- `06_Prompts_y_Registro_IA.md` (copia de `actividad-IA/registro-trazabilidad-ia.md` + prompts)
- `07_Declaracion_Uso_IA.md` (copia de `declaracion-uso-ia.md`)
- `08_Fuentes_Caso.md` (copia de `fuentes-caso.md`)
- `LEEME.txt` con índice.
Con ejemplos únicamente sintéticos.

### Paso E – Presentación `Presentacion_TPI_Eje1.pptx` (adaptar el modelo de 10 diapositivas; reemplazar el caso SaaS de ejemplo, mantener el orden: contexto, caso, marco jurídico, matriz, medidas, IA, evidencias, conclusiones, cierre). Poco texto, tabla breve de riesgos.

### Paso F – Guion `guion-video-4-integrantes.md`: 10–11 min total; tabla de tiempos y texto literal por integrante con diapositivas indicadas.
- Int. 1 (2:30): apertura, caso y alcance (Etapa 1).
- Int. 2 (2:30): marco jurídico (Etapa 2).
- Int. 3 (3:00): matriz y medidas (Etapas 3–4).
- Int. 4 (2:30): IA, conclusiones y rol TUP (Etapas 5–6) + cierre.
Incluir transiciones y 3 preguntas probables del docente con respuesta.

### Paso G – Control de calidad (checklist contra rúbrica y consigna 6.1/6.2):
- [ ] Portada con materia, caso, comisión, integrantes, fecha
- [ ] Resumen 8–12 líneas · [ ] 6 etapas · [ ] matriz con campos mínimos y ≥5 riesgos
- [ ] Documento/protocolo propuesto · [ ] Declaración IA + evidencia de verificación
- [ ] Bibliografía real · [ ] Sin datos personales no públicos · [ ] Ningún dato de la sección 0 sin fuente
- [ ] Todo hecho jurídico citado verificado en fuente primaria
- [ ] Advertencia: trabajo académico, no asesoramiento jurídico.

### Paso H – Actualizar bitácora (sesiones nuevas, errores corregidos) y hacer commit en rama `desarrollo` **solo si el usuario lo pide**.

## 5. Tono, lenguaje y estilo (OBLIGATORIO en todos los entregables, incluido el guion)

- **Quiénes escriben:** estudiantes de la Tecnicatura en Programación. Español rioplatense, claro, sencillo y prolijo. Redacción en primera persona del plural ("analizamos", "creemos") cuando corresponda.
- **Nada demasiado específico ni técnico:** explicar los conceptos de forma simple, como los explicaría un estudiante que los entendió, sin jerga forense o pericial avanzada. Si se nombra un término técnico (hash, log, 2FA, SIM swapping), definirlo en una línea.
- **Sin soluciones "fancy":** las medidas propuestas deben ser realistas y básicas (verificación de identidad más estricta, avisos al usuario, autenticación con app en lugar de SMS, guardar registros, ordenar el manejo de evidencia). No proponer herramientas, arquitecturas ni tecnología sofisticada o poco realista para el nivel del trabajo.
- **Anexos acordes:** el script de hashes (`05_calcular_hashes.py`) debe ser simple (pocas líneas, solo `hashlib`, bien comentado). Formularios y plantillas sencillos.
- **Prohibido aludir al material de la cátedra:** no escribir "según el material", "la guía", "la consigna", "lo visto en clase", "la cátedra nos indica", "el modelo provisto", etc. Se exponen directamente los conceptos y la información como conocimiento propio del equipo. Esto vale también para el guion y las diapositivas. (Los términos "etapa 1…6" pueden usarse como títulos de secciones del informe, sin decir que provienen de una consigna.)
- **Fuentes:** las únicas referencias permitidas son las fuentes reales consultadas (normas, notas periodísticas, sitios jurídicos) con su link, según el protocolo de la sección 0 bis.
- **Estructura de ideas:** distinguir *hechos / norma / interpretación / propuesta*. No copiar textos de las notas periodísticas: reformular con palabras propias y citar la fuente.
- **Extensión y formato:** oraciones cortas, párrafos breves, tablas simples. Sin adornos innecesarios.
- **Control final:** antes de entregar, buscar en todos los archivos las expresiones "material", "guía", "consigna", "cátedra", "clase" y "docente" fuera de la portada, y reescribir donde aludan a material de estudio.

