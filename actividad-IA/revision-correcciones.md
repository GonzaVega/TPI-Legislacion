# Revisión del trabajo de Gemini – Correcciones obligatorias

> Revisor: Claude Sonnet 5.5. Destinatario: Gemini 3.8 Flash (ejecutor).
> Regla: **no inventar ni suponer**. Todo lo que no se pueda respaldar se corrige, se rotula o se elimina. Ante dudas, preguntar al usuario.
> Al terminar cada corrección: tildar el ítem, registrar la sesión en `registro-trazabilidad-ia.md`, regenerar DOCX/PDF/PPTX y volver a copiar el registro a `anexos-para-zip/06_Prompts_y_Registro_IA.md`.

## A. GRAVES (afectan la veracidad del trabajo)

- [x] **A1. URLs, títulos y fechas de las fuentes F1–F8 fueron inventados.** Las búsquedas web solo devolvieron enlaces de redirección y resúmenes; Gemini nunca abrió las notas. Los títulos exactos, URL (ej. `.../532981-...`, `.../100789456/...`, `792134-...`), fechas de publicación y el enlace `jusbaires.gob.ar/guia-judicial/juzgado-pcyf-29` no están verificados. Afecta: `fuentes-caso.md`, `08_Fuentes_Caso.md`, `10_Evidencia_Fuentes/`, bibliografía del informe, Etapa 5 y marcas `[F1]…[F8]`.
  - **Corregir:** abrir cada nota con `read_url_content` (buscar la URL real con `search_web` por medio, por ejemplo "infobae Nuñes Pinheiro condenado D'Alessandro"). Reemplazar título, URL y fecha por los reales. Si una nota no se puede abrir o encontrar, **eliminarla** y rehacer las marcas. Guardar en `10_Evidencia_Fuentes/` el texto realmente leído, con URL y fecha de consulta (30/10/2026 solo si se abrió ese día).
- [x] **A2. Estado "Confirmado" sin respaldo.** Se marcó todo como Confirmado sin haber leído las notas. Reclasificar según el protocolo (Confirmado solo con ≥2 fuentes realmente leídas).
- [x] **A3. Datos inventados presentados como hechos del caso:**
  - "20 años de edad" (no consta).
  - "Causa N° 29/2023" (número inventado; el N° 29 es el juzgado, no la causa).
  - Fechas y lugares de la cadena de custodia y del informe pericial: allanamiento 15/03/2023, calle "Los Cedros 450", Samsung A52, IMEIs, chip, faja 00812, bolsa 00412, nombres de oficiales/peritos, IP `181.44.120.XX`, logs del 12/03/2023, `auth_access_log.txt`, línea `011-4589-XXXX`, hashes. Hoy el lector los toma como evidencia real de esta causa.
  - **Corregir:** convertir ambos documentos (anexos 02 y 03, y el apartado 4.3 del informe) en **modelos con datos ficticios claramente rotulados** ("EJEMPLO – DATOS FICTICIOS, no corresponden a la causa"), sin número de causa ni nombre de la causa real, y sin vincularlos a Misiones ni a fechas del caso. El informe no debe afirmar que se secuestró un Samsung A52.
  - El hash `e3b0c442…b855` es el SHA-256 de un archivo vacío: usar un hash calculado con el script sobre un archivo de ejemplo real y decirlo.
- [x] **A4. "Sentencia firme".** Ninguna fuente leída dice "firme". Usar "condena en juicio abreviado homologado" y no afirmar firmeza salvo fuente. Corregir en informe, guion, PPTX, `fuentes-caso.md`, LEEME de anexos.
- [x] **A5. Afirmaciones sobre el expediente sin fuente:** "sustracción de documentos que estaban bajo custodia de funcionarios públicos", "el imputado declaró judicialmente… 'Pr1sox'", "chips vírgenes", "resetear SIM por autogestión", "alerta de 2 a 3 horas", fecha "octubre de 2023" y "dictada el 6/10/2023". Cada una debe tener fuente real leída o reformularse como "según [medio]" / eliminarse. El art. 255 y la frase sobre lo que la fiscalía hizo son explicación propia, no hecho: rotular como interpretación.

## B. IMPORTANTES

- [x] **B1. Citas de páginas del material sin verificar.** `fuentes-material.md` afirma "Págs. 1-3", "Pág. 4 (Sección 7)" y "Diapositivas 1-15" de `SEMANA 2…pdf`, y contenido de `arg_ley26388` y `JURISPRUDENCIA…pdf` que Gemini no leyó (la salida estaba truncada). Releer con `pdftotext` y corregir páginas y conceptos reales (usar `pdftotext -f N -l N`). Eliminar lo que no se pueda comprobar. Lo mismo para la afirmación sobre el fallo `000099168.pdf` ("error de tipeo no invalida"): verificar el sentido real de la resolución antes de usarla en el informe y en el guion.
- [x] **B2. Texto de los arts. 153, 153 bis, 197, 255 y 173 inc. 16** citado de memoria. Contrastar con `arg_ley26388 (1).pdf` y InfoLEG y ajustar la explicación a lo que realmente dice cada artículo. Confirmar con fuente que el art. 255 corresponde a la condena ("sustracción de documento público"); y que la condena incluye el art. 197 ("entorpecimiento de comunicaciones").
- [x] **B3. Etapa 5 contiene afirmaciones falsas sobre el proceso:** "contrastado con al menos dos fuentes periodísticas independientes" y "cotejo contra Infobae, Clarín y La Nación [F1, F2, F3]" no es verdad hasta cumplir A1. Además el ejemplo de alucinación atribuido a "Claude Sonnet" (fraude 173 inc. 16 y art. 157) en realidad vino de la guía previa generada por Gemini. Corregir atribución real y ajustar el texto al final de A1. Quitar "Claude Sonnet / Antigravity" si no se quiere dar nombres de versión, o mantener los reales: Gemini (guía inicial, ejecución) y Claude (plan y revisión).
- [x] **B4. Indicaciones de estilo incumplidas.** Se pidió no aludir al material de la cátedra ni a la consigna:
  - `07_Declaracion_Uso_IA.md` ("consigna general", "material provisto por la cátedra", "rúbrica de la cátedra"), `06_…md` ("consigna oficial", "Objetivo / Consigna") y `LEEME.txt` ("consigna oficial"), y el comentario del `generar_informe_docx.py`. Reescribir sin esas alusiones (la constancia del origen del material va solo en `fuentes-material.md` y bibliografía).
  - Revisar el informe y el guion: el estilo se pidió simple. "Cálculo de criticidad con fórmulas" no existe en el XLSX: no afirmarlo o implementarlo.
- [x] **B5. Medidas "sofisticadas"**: validación biométrica facial, bloqueador de escritura (write blocker), imagen bit a bit, bolsa de Faraday. Mantener solo como mención simple de una línea o reemplazar por pasos básicos (modo avión, no tocar el original, copiar, hash, anotar). Quitar "llaves físicas" y "auditorías" de la matriz si no se justifican.
- [x] **B6. Inconsistencias entre archivos.** `06_…md` y el registro de `actividad-IA` conservan en la sesión #002 "Fraude Informático", "UFEDECO/UFECI" y "Cellebrite": datos que ya se descartaron. Corregir. El guion afirma "condena firme", "20 años" y "Juzgado Penal N° 29". Alinear con A3/A4.

## C. FORMATO (verificar visualmente)

- [x] **C1.** Revisar el PDF (`pdftoppm -png` y mirar las imágenes): portada, tablas de matriz e IA, y el tamaño de página (el PDF salió de 610 x 1006 pt, formato no A4; confirmar que es el de la plantilla y que se ve bien).
- [x] **C2.** Los anexos `.docx` 01–03 fueron generados desde Markdown con tablas como líneas de texto con `|`. Rehacerlos con tablas reales de Word o entregar solo `.md`/PDF legible.
- [x] **C3.** Revisar visualmente `Presentacion_TPI_Eje1.pptx` (convertir a PDF/imágenes): texto que desborda, y que el pie "Comisión 5 - UTN" y la tabla de la diapositiva 5 hayan quedado bien. El PPTX no cubre la diapositiva de "evidencias" del guion ni los números de diapositiva citados: alinear guion y diapositivas.
- [x] **C4.** El guion suma 10:30 si cada bloque dura lo previsto, pero el texto leído parece mayor; contar palabras (~130 palabras/min) y ajustar a 8–12 min.
- [x] **C5.** Borrar archivos auxiliares de la entrega: `generar_informe_docx.py` y `contenido-informe.md` no van al ZIP (están fuera de `anexos-para-zip`, bien), y confirmar que no quedó `registro_hashes_verificacion.csv` suelto.
- [ ] **C6. Depuración de anexos intermedios (al indicar "Listo para Entregar"):** Cuando el usuario declare el trabajo listo para entregar, eliminar los 8 archivos intermedios `.md` y `.txt` de la carpeta de anexos (`01_Protocolo_Evidencia_Digital.md`, `02_Formulario_Cadena_Custodia.md`, `03_Plantilla_Informe_Tecnico_Juridico_TUP.md`, `04_Matriz_Riesgos.md`, `05_ejemplo_registro_ficticio.txt`, `06_Prompts_y_Registro_IA.md`, `07_Declaracion_Uso_IA.md`, `08_Fuentes_Caso.md`), preservando sus versiones definitivas en `.pdf` (así como los `.docx`, `.xlsx` y `05_calcular_hashes.py`), y actualizar `LEEME.txt`.

## D. Orden sugerido
A1 → A2 → A4/A5 → A3 → B2/B1 → B3/B6 → B4/B5 → regenerar entregables → C → registrar todo en la bitácora y avisar al usuario cuando termine, con lista de lo que se eliminó por falta de respaldo.
