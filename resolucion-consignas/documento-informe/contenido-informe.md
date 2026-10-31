# TRABAJO PRÁCTICO INTEGRADOR: LEGISLACIÓN E INTELIGENCIA ARTIFICIAL APLICADA

**Materia:** Legislación  
**Carrera:** Tecnicatura Universitaria en Programación  
**Comisión:** Comisión 5  
**Título del Trabajo:** Análisis Jurídico y Técnico de Incidente de Seguridad: Caso Elías Ezequiel Nuñes Pinheiro (SIM Swapping, Acceso Ilegítimo y Preservación de Evidencia Digital)  
**Integrantes:**  
* Mateo Serafini  
* Hugo Tcach  
* Farid Salomon  
* Gonzalo Vega  

**Docentes:** [COMPLETAR: docentes]  
**Fecha de Entrega:** [COMPLETAR: fecha de entrega]  
**Enlace a Video de Presentación:** [COMPLETAR: link del video en YouTube]  

> **Nota académica:** Este trabajo fue elaborado con fines exclusivamente educativos por estudiantes de la Tecnicatura Universitaria en Programación y no constituye asesoramiento jurídico profesional.

---

## RESUMEN EJECUTIVO

En este trabajo analizamos el caso real de Elías Ezequiel Nuñes Pinheiro, oriundo de Eldorado (Misiones), quien realizó maniobras de duplicación no autorizada de tarjetas SIM (*SIM swapping*) contra el exministro de Seguridad porteño Marcelo D'Alessandro y el entonces diputado Diego Santilli [F1, F2, F4, F7]. A partir de datos personales obtenidos mediante consultas al RENAPER, a Nosis y al sitio "Dark PFA", gestionó en forma remota ante Movistar el cambio de chip e insertó tarjetas SIM "blancas" adquiridas a Comtel S.A., dejando sin línea a los titulares y recibiendo los códigos de verificación para ingresar a sus cuentas de WhatsApp y Telegram [F1, F2, F4, F7]. En la justicia de la Ciudad de Buenos Aires, la jueza María Araceli Martínez (Juzgado Penal 29) homologó un acuerdo de juicio abreviado imponiéndole tres años de prisión en suspenso y reglas de conducta [F1, F2]. Examinamos las normas penales y de protección de datos aplicables, elaboramos una matriz cualitativa con siete riesgos y proponemos medidas simples de prevención, junto con un protocolo básico de cinco pasos y modelos de práctica con datos ficticios para documentar la cadena de custodia y el cálculo de hash SHA-256.

---

## ETAPA 1 – PRESENTACIÓN DEL CASO Y ALCANCE

### 1.1. Descripción de los Hechos
El caso analizado tiene como protagonista a Elías Ezequiel Nuñes Pinheiro, radicado en la localidad de Eldorado, provincia de Misiones (tenía 22 años cuando declaró en marzo y abril de 2023 [F4, F5, F6, F7] y 25 años en julio de 2026 [F1]). En octubre de 2022 ejecutó ataques de reemplazo no autorizado de tarjeta SIM (*SIM swapping*) contra distintas figuras públicas, entre ellas el entonces diputado nacional Diego Santilli —atacado el 14 de octubre de 2022, según La Nación [F2]— y el entonces ministro de Seguridad porteño Marcelo D'Alessandro —atacado el 19 de octubre de 2022 [F1, F2, F4, F7], entre las 14:17 y las 15:43 según Infobae [F1], aunque el epígrafe de una fotografía en otra nota de Infobae menciona el 18 de octubre de 2022 [F6]—.

La maniobra técnica de *SIM swapping* consiste en lograr que la empresa de telefonía móvil asigne el número de teléfono de la víctima a un nuevo chip físico en poder del atacante [F1, F2, F4]. Para reunir los datos que exigía la operadora, Nuñes Pinheiro realizaba consultas previas en el Registro Nacional de las Personas (RENAPER) y en informes comerciales de la firma Nosis (mediante la aplicación "Mi Nosis") [F1, F2, F4, F7], además de recurrir al sitio "Dark PFA" [F2, F7, F8, F9]. Con esa información gestionaba por vía remota ante la empresa **Movistar** el cambio de chip: en su declaración explicó que la plataforma de autogestión pedía únicamente el número de línea, el número de DNI y el número de trámite del DNI [F1, F4, F7]. Luego colocaba en un teléfono una tarjeta SIM "blanca" (sin número asignado de fábrica) comprada a través de Mercado Libre a la firma **Comtel S.A.** [F1, F4, F7].

Al activarse el nuevo chip en una antena de Eldorado, se interrumpía la conectividad de la línea original de la víctima y el atacante recibía los mensajes con códigos de verificación, tomando el control de las cuentas de WhatsApp y Telegram [F1, F2, F4]. En sus declaraciones ante la fiscal Daniela Dupuy [F3, F4, F5, F6, F7], Nuñes Pinheiro sostuvo que actuaba a pedido de un usuario de Telegram identificado como **"ElJuanxd"** [F1, F4, F5, F6, F7, F9] y que cobraba entre $12.000 y $15.000 por cada objetivo mediante billeteras virtuales o criptomonedas [F1, F3, F5, F6, F7] (en una de las notas se indica "$15 mil por cada objetivo" [F4] y en otra se menciona un pago de $46.000 el 17/10/2022 por tres objetivos [F5]). Asimismo, se acreditó que destruyó el teléfono celular utilizado para las maniobras [F2, F5]: según Infobae [F5], declaró que le prendió fuego y lo arrojó al río Paraná porque se asustó al ver la repercusión pública del caso.

### 1.2. Actores Involucrados
* **Sujeto Activo (Imputado):** Elías Ezequiel Nuñes Pinheiro, quien ejecutó las maniobras de *SIM swapping* desde Eldorado, Misiones [F1, F2, F3, F4].
* **Contacto en Telegram y Proveedores de Datos Ilícitos:** El usuario de Telegram "ElJuanxd", señalado como quien encargaba los objetivos y realizaba los pagos [F1, F4, F5, F6, F7, F9]. Además, en la investigación se identificó a Tomás Patricio Hválica como creador y administrador del sitio "Dark PFA" [F2, F8, F9], a quien La Nación [F9] vincula con el usuario de Telegram `@pr1sox`.
* **Víctimas en el Caso Analizado:** Marcelo D'Alessandro [F1, F2, F4, F7] y Diego Santilli [F2, F7], cuyas líneas celulares y cuentas de mensajería fueron intervenidas desde el mismo código IMEI en Eldorado [F7].
* **Empresas de Telecomunicaciones y Comercializadoras:** La operadora Movistar, ante la cual se gestionó de forma remota el cambio de chip con validación basada en línea, DNI y número de trámite, y la firma Comtel S.A., vendedora de las tarjetas SIM "blancas" empleadas [F1, F4, F7].
* **Autoridades Judiciales:** En el tramo inicial de la investigación en la Ciudad de Buenos Aires intervino la fiscal Daniela Dupuy [F3, F4, F5, F6, F7]. Posteriormente, el acuerdo de juicio abreviado fue homologado por la jueza María Araceli Martínez, a cargo del Juzgado Penal 29 de CABA [F1, F2]. En paralelo, en el fuero federal de Comodoro Py interviene el juez Marcelo Martínez de Giorgi [F1, F2, F8, F9].

### 1.3. Sistemas y Servicios Tecnológicos Analizados
1. **Gestión de Tarjetas SIM en la Red Móvil:** El proceso remoto de reposición de SIM en la operadora Movistar, que permitía asociar una línea existente a una tarjeta SIM "blanca" de Comtel S.A. ingresando número de línea, DNI y número de trámite [F1, F4, F7].
2. **Códigos de Verificación Vinculados a la Línea Telefónica:** El envío de códigos de activación a la línea celular para habilitar cuentas en otro dispositivo, mecanismo que falla cuando un tercero toma el control de la tarjeta SIM [F1, F4].
3. **Sistemas de Consulta de Datos Personales:** El acceso a información del RENAPER, informes de Nosis (aplicación "Mi Nosis") y el sitio "Dark PFA" para obtener el número de trámite del DNI y otros datos de las víctimas [F1, F2, F4, F7].
4. **Aplicaciones de Mensajería Instantánea:** WhatsApp y Telegram, cuyas cuentas fueron abiertas en el dispositivo del atacante una vez desviada la línea telefónica [F1, F2, F4].

### 1.4. Alcance, Diferencias entre Fuentes y Límites del Análisis
Nuestro trabajo se centra en la **condena en juicio abreviado homologado** en la justicia de la Ciudad Autónoma de Buenos Aires por la jueza María Araceli Martínez (Juzgado Penal 29), mediante la cual se impuso a Nuñes Pinheiro la pena de **tres años de prisión en suspenso**, la obligación de fijar residencia, someterse al cuidado del Patronato de Liberados y realizar **150 horas de tareas comunitarias no remuneradas** [F1, F2], luego de certificar con el juzgado federal que no se vulneraba la garantía contra el doble juzgamiento (*non bis in idem*) [F1, F2].

Al reconstruir el caso exclusivamente con fuentes periodísticas públicas abiertas y leídas el 30/10/2026 (cuyas copias completas se acompañan en `anexos-para-zip/10_Evidencia_Fuentes/`), dejamos constancia expresa de las siguientes discrepancias y límites informativos:
1. **Fecha de publicación y terminología procesal:** La Nación [F2] publicó la noticia el 08/06/2026 indicando que el acuerdo se formalizó ese día, y lo describe como un juicio abreviado con condena en suspenso. Infobae [F1] publicó su nota el 18/07/2026 y en el título y parte del texto emplea los términos *"probation"* y *"suspensión de juicio a prueba"*, aunque en el mismo cuerpo afirma que la jueza *"homologó un acuerdo de juicio abreviado"* y *"condenó"* a tres años de prisión en suspenso.
2. **Unificación de penas y decomiso:** Únicamente La Nación [F2] informa que la pena de tres años en suspenso fue una pena unificada que absorbió una condena previa de dos años y seis meses dictada en 2024 por el Tribunal Oral Federal N° 2, y que abarcó los ataques contra D'Alessandro y Santilli. Por su parte, únicamente Infobae [F1] menciona que se dispuso el decomiso directo de la totalidad de los elementos incautados.
3. **Datos que no surgen de las fuentes:** Ninguna de las notas consultadas afirma que la condena se encuentre **firme**, ni informa el número de expediente, los números de artículo del Código Penal aplicados por el juzgado ni el detalle de las actas de cadena de custodia del expediente.
4. **Causa federal paralela en trámite:** Queda fuera del alcance de una sentencia definitiva el expediente conexo que tramita en Comodoro Py ante el juez federal Marcelo Martínez de Giorgi por presunto espionaje ilegal a jueces federales e integrantes de la Corte Suprema (entre febrero de 2022 y mayo de 2023), en el cual Nuñes Pinheiro fue procesado por asociación ilícita en agosto de 2026 [F9] y apeló dicho procesamiento en septiembre de 2026 [F8].

---

## ETAPA 2 – MARCO JURÍDICO APLICABLE

A continuación analizamos las normas jurídicas y estándares técnicos aplicables al caso y explicamos por qué se vinculan con cada conducta.

### 2.1. Código Penal de la Nación Argentina (según texto de la Ley 26.388)
Según Infobae [F1], la condena dictada en la justicia porteña fue por **"acceder ilegítimamente a datos informáticos restringidos, sustraer documento público y entorpecer las comunicaciones"**, mientras que según La Nación [F2] la destrucción del celular utilizado derivó en una imputación adicional por **"destrucción de medios de prueba"**. Dado que las notas periodísticas no citan números de artículo, la correspondencia con el articulado del Código Penal (modificado por la Ley 26.388) que desarrollamos a continuación constituye una **interpretación propia del equipo** contrastada con el texto legal:

* **Artículo 153 bis del Código Penal (Acceso Ilegítimo a Sistemas o Datos Informáticos):**  
  * *Qué establece la norma:* Reprime con prisión de quince días a seis meses, si no resultare un delito más severamente penado, al que a sabiendas accediere por cualquier medio, sin la debida autorización o excediendo la que posea, a un sistema o dato informático de acceso restringido. La pena se eleva de un mes a un año de prisión cuando el acceso fuese en perjuicio de un sistema o dato informático de un organismo público estatal o de un proveedor de servicios públicos o financieros.  
  * *Por qué aplica al caso:* Es la figura que encuadra el *"acceder ilegítimamente a datos informáticos restringidos"* reseñado por Infobae [F1]. Nuñes Pinheiro ingresó a sabiendas y sin autorización a las cuentas de WhatsApp y Telegram de las víctimas valiéndose de los códigos de verificación obtenidos tras el cambio de SIM, y también se valió de consultas no autorizadas a sistemas con datos restringidos (RENAPER y Nosis) [F1, F2, F4].
* **Artículo 153 del Código Penal (Violación, Apoderamiento e Interceptación de Comunicaciones Electrónicas):**  
  * *Qué establece la norma:* Reprime con prisión de quince días a seis meses al que abriere o accediere indebidamente a una comunicación electrónica, una carta, un pliego cerrado, un despacho telegráfico, telefónico o de otra naturaleza que no le esté dirigido; o se apoderare indebidamente de ellos; o indebidamente suprimiere o desviare de su destino una correspondencia o una comunicación electrónica que no le esté dirigida. En la misma pena incurre quien interceptare o captare comunicaciones electrónicas o telecomunicaciones provenientes de cualquier sistema de carácter privado o de acceso restringido (con agravante de un mes a un año si comunicare a otro o publicare el contenido).  
  * *Por qué aplica al caso:* Describe de forma directa el efecto del *SIM swapping* sobre los mensajes de la víctima: al activar la tarjeta SIM en otro aparato, el atacante desvió de su destino e interceptó comunicaciones electrónicas y mensajes de verificación dirigidos exclusivamente al titular de la línea [F1, F2, F4].
* **Artículo 197 del Código Penal (Interrupción o Entorpecimiento de Comunicaciones):**  
  * *Qué establece la norma:* Reprime con prisión de seis meses a dos años al que interrumpiere o entorpeciere la comunicación telegráfica, telefónica o de otra naturaleza, o resistiere violentamente el restablecimiento de la comunicación interrumpida.  
  * *Por qué aplica al caso:* Corresponde a la figura de *"entorpecer las comunicaciones"* indicada por Infobae [F1]. Como señala esa nota, al gestionar ante Movistar el cambio no autorizado de tarjeta SIM, la maniobra *"interrumpió la conectividad de la línea"* del titular legítimo, impidiéndole utilizar su servicio telefónico [F1, F4].
* **Artículo 255 del Código Penal (Sustracción, Ocultación o Destrucción de Documentos y Objetos de Prueba):**  
  * *Qué establece la norma:* Reprime con prisión de un mes a cuatro años al que sustrajere, alterare, ocultare, destruyere o inutilizare en todo o en parte objetos destinados a servir de prueba ante la autoridad competente, registros o documentos confiados a la custodia de un funcionario público o de otra persona en el interés del servicio público (recordando además que el art. 77 del Código Penal, según Ley 26.388, establece que el término *"documento"* comprende toda representación de actos o hechos con independencia del soporte utilizado para su fijación, almacenamiento, archivo o transmisión).  
  * *Por qué aplica al caso (interpretación del equipo):* Este artículo permite explicar dos datos publicados en la prensa sobre la causa. En primer lugar, la figura de *"sustraer documento público"* mencionada por Infobae [F1] dentro de la condena, en tanto el teléfono intervenido pertenecía a quien se desempeñaba como ministro de Seguridad porteño y contenía comunicaciones y documentos digitales vinculados a su función. En segundo lugar, la imputación adicional por *"destrucción de medios de prueba"* que señala La Nación [F2], originada en que Nuñes Pinheiro destruyó el teléfono celular empleado en los ataques [F2] (prendiéndole fuego y arrojándolo al río Paraná, según su declaración reseñada en Infobae [F5]).

#### Subsección: Figuras Conexas Analizadas (Interpretación Académica)
Como equipo analizamos también otras dos figuras incorporadas por la Ley 26.388 para distinguir su alcance técnico:
* **Artículo 157 bis del Código Penal (Acceso Ilegítimo a Bancos de Datos Personales):** Sanciona con prisión de un mes a dos años a quien, a sabiendas e ilegítimamente o violando sistemas de confidencialidad y seguridad, accediere de cualquier forma a un banco de datos personales, o revelare información registrada cuyo secreto estuviere obligado a preservar por ley. Consideramos que esta figura guarda estrecha relación con la etapa preparatoria del ataque, consistente en extraer datos personales de registros como el RENAPER, Nosis o el sitio "Dark PFA" [F1, F2, F4, F7].
* **Artículo 173 inciso 16 del Código Penal (Defraudación Informática):** Sanciona al que defraudare a otro mediante cualquier técnica de manipulación informática que altere el normal funcionamiento de un sistema informático o la transmisión de datos. Si bien existió un engaño en el trámite remoto de autogestión de la operadora y Nuñes Pinheiro recibió pagos de terceros por cada encargo [F1, F4], el ataque contra los titulares de las líneas no tuvo por finalidad provocarles un perjuicio patrimonial directo (como ocurre cuando se usa el *SIM swapping* para vaciar cuentas bancarias), sino acceder a sus comunicaciones privadas, razón por la cual resulta coherente que la condena reseñada en [F1] no haya encuadrado el hecho como estafa o defraudación informática.

### 2.2. Constitución Nacional
* **Artículo 18 de la Constitución Nacional:**  
  Establece la inviolabilidad del domicilio, la correspondencia epistolar y los papeles privados, principio que alcanza a las comunicaciones telefónicas y a los mensajes digitales (WhatsApp, Telegram, correos electrónicos). Asimismo, consagra la garantía del debido proceso y el principio *non bis in idem* (que prohíbe juzgar o sancionar dos veces a una persona por el mismo hecho), el cual tuvo aplicación práctica directa en el caso cuando el Juzgado Penal 29 certificó el expediente federal del juez Martínez de Giorgi antes de homologar el acuerdo [F1, F2].

### 2.3. Ley 25.326 de Protección de los Datos Personales
* **Artículo 9 (Seguridad de los Datos):** Obliga al responsable o usuario de archivos y bancos de datos a adoptar las medidas técnicas y organizativas necesarias para garantizar la seguridad y confidencialidad de los datos personales, evitando su adulteración, pérdida, consulta o tratamiento no autorizado. En el caso analizado, tanto la obtención previa de datos en bases públicas y privadas como la aprobación remota de un cambio de SIM pidiendo solo línea, DNI y número de trámite [F1, F4, F7] exponen debilidades frente a este deber legal.
* **Artículo 10 (Deber de Confidencialidad):** Impone el deber de secreto profesional a todas las personas que intervengan en cualquier fase del tratamiento de datos personales, obligación que se quebranta cuando se facilitan accesos o consultas para fines ajenos a la función autorizada.

### 2.4. Estándares Técnicos, Protocolos y Jurisprudencia sobre Evidencia Digital
* **Norma Internacional ISO/IEC 27037:2012:**  
  Es un estándar internacional de buenas prácticas técnicas (no una ley) que orienta cómo identificar, recolectar, adquirir y preservar evidencia digital potencial para mantener su confiabilidad y permitir que el procedimiento pueda ser revisado por terceros.
* **Resolución 232/2023 del Ministerio de Seguridad:**  
  Aprueba el protocolo argentino que ordena el tratamiento de la evidencia digital en cinco etapas: identificación, recolección, preservación, procesamiento y presentación, definiendo la cadena de custodia como el registro cronológico de las personas que tomaron contacto con el elemento y de las operaciones realizadas.
* **Convenio de Budapest sobre Ciberdelito (aprobado por Ley 27.411):**  
  Brinda herramientas procesales de cooperación internacional frente a delitos cometidos mediante sistemas informáticos. Sus artículos 16 y 17 contemplan la **preservación rápida de datos informáticos almacenados y de datos de tráfico** cuando existe riesgo de que se pierdan o modifiquen mientras se tramita la orden judicial para obtenerlos, junto con una red de contacto permanente las 24 horas (art. 35). Esto resulta clave cuando los ataques se coordinan mediante plataformas extranjeras como Telegram [F1, F4].
* **Jurisprudencia sobre Cadena de Custodia y Hash (Cámara de Apelaciones en lo PPJCyF de CABA, Sala III, Causa N° 41459/2019-3, resolución del 05/10/2021):**  
  En ese precedente, la defensa pidió la nulidad de la evidencia digital porque el código hash anotado en el acta de resguardo no coincidía. El Ministerio Público Fiscal explicó que el personal del Cuerpo de Investigaciones Judiciales había realizado una videograbación de la pantalla del celular y calculado su hash, pero por un error involuntario de tipeo había consignado en el acta el hash perteneciente a un modelo de acta anterior, circunstancia que fue advertida y subsanada dejando constancia. Por mayoría (voto de los jueces Marum y Vázquez; con disidencia del juez Delgado), la Cámara confirmó el rechazo de la nulidad, sosteniendo que las nulidades procesales son de carácter excepcional, que requieren demostrar un perjuicio concreto, que la medida era reproducible y que un error material de tipeo subsanado y explicado no implicaba que la evidencia hubiera sido manipulada.

---

## ETAPA 3 – MATRIZ DE RIESGOS LEGALES Y DE CUMPLIMIENTO

Construimos la siguiente matriz con siete riesgos vinculados al caso y al desarrollo y operación de sistemas. Los niveles de probabilidad, impacto y criticidad responden a una **valoración cualitativa realizada por el equipo** (no se calculan mediante fórmulas matemáticas) y coinciden con la planilla `04_Matriz_Riesgos.xlsx` incluida en los anexos.

| ID | Riesgo Detectado | Tipo | Norma o Principio Vinculado | Probabilidad | Impacto | Criticidad | Medida Propuesta |
|:---|:---|:---|:---|:---|:---|:---|:---|
| **R1** | Cambio de SIM aprobado con datos personales fáciles de conseguir. En el caso, la plataforma pedía número de línea, DNI y número de trámite [F4, F7]. | Técnico / Operativo | Ley 25.326 (art. 9) | Alta | Muy alto | **Crítica** | Pedir un paso más de verificación: trámite presencial con DNI o confirmación por otro canal ya registrado del titular. |
| **R2** | Códigos de verificación por SMS: los recibe quien tenga la SIM, aunque no sea el titular. | Técnico / Seguridad | Ley 25.326 (art. 9) y buenas prácticas de seguridad | Alta | Muy alto | **Crítica** | Ofrecer una app autenticadora de códigos (TOTP) u otro método que no dependa del SMS. |
| **R3** | Acceso indebido a cuentas de mensajería (WhatsApp, Telegram) y a conversaciones privadas [F1]. | Penal | Código Penal, arts. 153 bis y 153 | Alta | Alto | **Alta** | Activar la verificación en dos pasos con PIN propio de la aplicación, independiente de la línea. |
| **R4** | Pérdida de señal del titular al darse de baja su SIM [F1]. | Operativo / Penal | Código Penal, art. 197 | Alta | Medio | **Media** | Avisar por correo o notificación y dar un tiempo para frenar el trámite antes de dar de baja la SIM. |
| **R5** | Pérdida de valor de la prueba digital por fallas en la cadena de custodia. | Procesal / Legal | Art. 18 CN, ISO/IEC 27037 y jurisprudencia de la Cámara PCyF CABA (Sala III, 05/10/2021) | Media | Muy alto | **Alta** | Aplicar el protocolo de 5 pasos: aislar, copiar, calcular hash SHA-256 y registrar la custodia. |
| **R6** | Responsabilidad de la empresa por no cuidar los datos personales de sus clientes. | Administrativo / Civil | Ley 25.326 (arts. 9 y 31) | Alta | Medio | **Media** | Registrar quién autorizó cada cambio de SIM, con fecha, hora y dirección IP. |
| **R7** | Riesgo ético y penal para programadores que participen en accesos no autorizados. | Ético / Penal | Código Penal, art. 153 bis | Media | Alto | **Media** | Formarse en ética y legislación, no vender credenciales ni acceder sin autorización y rechazar pedidos dudosos. |

---

## ETAPA 4 – MEDIDAS, DOCUMENTOS Y PROTOCOLOS PROPUESTOS

A partir de los riesgos detectados, proponemos medidas simples y accesibles para los sistemas involucrados, junto con un protocolo básico de preservación de evidencia digital y dos modelos documentales de práctica.

### 4.1. Medidas Simples de Prevención para Sistemas y Operadoras
1. **Un Paso Adicional para Aprobar un Cambio de SIM:** No habilitar el reemplazo remoto de una tarjeta SIM pidiendo únicamente datos estáticos como el número de línea, el DNI y el número de trámite [F4, F7]. Exigir el trámite presencial con DNI o una confirmación adicional por otro canal ya registrado del titular.
2. **Aviso Previo y Tiempo para Cancelar el Trámite:** Antes de dar de baja la tarjeta SIM activa, enviar un aviso por correo electrónico o notificación al titular e incorporar una demora prudencial que le permita frenar la operación si no fue solicitada por él.
3. **Autenticación con Aplicaciones de Códigos Temporales y PIN Propio:** En el diseño de aplicaciones, evitar que el código enviado por SMS sea la única barrera de ingreso. Promover el uso de aplicaciones autenticadoras de códigos temporales (TOTP) que funcionan en el propio teléfono sin depender de la señal celular, y activar el PIN de verificación en dos pasos dentro de WhatsApp y Telegram.
4. **Registro Básico de Operaciones (Logs):** Guardar en los sistemas un registro claro de cada solicitud de cambio de SIM o acceso a datos, indicando fecha, hora, dirección IP de origen y qué operador o método aprobó la gestión.

---

### 4.2. Protocolo Básico de Preservación y Documentación de Evidencia Digital (Anexo 01)
Para que los archivos o dispositivos vinculados a un incidente conserven su identidad, integridad y trazabilidad, proponemos una guía simple de cinco pasos (desarrollada en `01_Protocolo_Evidencia_Digital.md` y `.docx`):

```
[Paso 1: Identificar] ──> [Paso 2: Aislar] ──> [Paso 3: Copiar] ──> [Paso 4: Calcular Hash] ──> [Paso 5: Registrar]
```

1. **Paso 1 – Identificar y anotar:** Anotar qué elementos hay (computadoras, celulares, tarjetas SIM, discos, pendrives o archivos de registro), registrando marca, modelo, número de serie o IMEI y tomando fotografías de su estado antes de tocarlos.
2. **Paso 2 – Aislar:** Si un equipo está apagado, se lo deja apagado. Si un teléfono celular está encendido, no se lo revisa ni se abren sus aplicaciones: se lo coloca en **modo avión** para evitar que reciba mensajes o indicaciones remotas de borrado, anotando la hora y quién lo hizo.
3. **Paso 3 – Copiar:** Nunca se trabaja sobre la evidencia original. Toda revisión se realiza sobre una copia de trabajo, mientras el original se guarda sin modificar en un lugar seguro.
4. **Paso 4 – Calcular el hash:** Se calcula el código hash SHA-256 del archivo original y de la copia (por ejemplo, mediante nuestro script `05_calcular_hashes.py`). Si ambos valores coinciden, se comprueba que la copia es idéntica al original.
5. **Paso 5 – Registrar la cadena de custodia:** En cada entrega o traslado se completa el formulario de cadena de custodia con fecha, hora, nombres, motivo y firmas. Si se comete un error material al anotar un dato (como un código hash mal copiado), no se borra ni se oculta: se corrige dejando constancia expresa de la rectificación con fecha y firma.

---

### 4.3. Modelo de Formulario de Cadena de Custodia – EJEMPLO CON DATOS FICTICIOS (Anexo 02)
> **ACLARACIÓN IMPORTANTE – EJEMPLO CON DATOS FICTICIOS:** En el caso real de Nuñes Pinheiro, el propio imputado declaró que destruyó el teléfono utilizado [F2, F5] y las fuentes públicas no contienen actas de secuestro ni números de expediente. Por ello, para no inventar hechos sobre la causa, diseñamos un **modelo de práctica con datos ficticios** (`02_Formulario_Cadena_Custodia.md` y `.docx`) aplicado sobre el archivo de ejemplo `05_ejemplo_registro_ficticio.txt` incluido en nuestros anexos:

* **Número de expediente / causa:** `[EJEMPLO] Expediente X-0000/0000` (ficticio, no corresponde a la causa real).
* **Carátula y lugar:** `[EJEMPLO] Incidente informático de práctica` – Oficina de práctica, sin dirección real.
* **Fecha y hora del procedimiento:** `[EJEMPLO] 10/01/2025 – 10:00 hs.`
* **Elemento identificado (Ítem N° 01):** Archivo de registro de eventos en formato de texto llamado `05_ejemplo_registro_ficticio.txt` (731 bytes), creado por el equipo para probar el flujo de trabajo.
* **Verificación de integridad (Hash SHA-256 real del archivo de práctica):**  
  `40b4ae55313c6236cb881819d70514e1891faf4d6aa68d7975c72b42749c57a4`  
  *(Valor calculado con el script `05_calcular_hashes.py` sobre `05_ejemplo_registro_ficticio.txt`)*.
* **Registro de movimientos:** Tabla donde se asienta cada cambio de manos entre personas ficticias (`Persona A`, `Persona B`, `Persona C`), con fecha, hora, motivo (entrega, copia para análisis y verificación de hash, devolución del original) y firmas.

---

### 4.4. Modelo de Informe Técnico-Jurídico para el Programador – EJEMPLO CON DATOS FICTICIOS (Anexo 03)
> **ACLARACIÓN IMPORTANTE – EJEMPLO CON DATOS FICTICIOS:** Del mismo modo, acompañamos en `03_Plantilla_Informe_Tecnico_Juridico_TUP.md` (y `.docx`) un modelo de informe técnico completado con datos de práctica sobre el archivo `05_ejemplo_registro_ficticio.txt`, utilizando direcciones IP reservadas para documentación (`192.0.2.10` y `198.51.100.7`) y un número de línea inexistente (`11-0000-0000`):

1. **Identificación:** Datos del Técnico Universitario en Programación, expediente ficticio `[EJEMPLO] Expediente X-0000/0000` y fecha `[EJEMPLO] 10/01/2025`.
2. **Objeto:** Revisar el archivo de práctica `05_ejemplo_registro_ficticio.txt` para comprobar su integridad y describir de forma objetiva los eventos registrados sobre una línea de ejemplo.
3. **Origen y medidas de preservación:** Archivo de texto creado para práctica; se conserva el original sin tocar y se analiza una copia de trabajo.
4. **Verificación de integridad:** Comprobación del hash SHA-256 (`40b4ae55313c6236cb881819d70514e1891faf4d6aa68d7975c72b42749c57a4`) antes y después de la lectura mediante `05_calcular_hashes.py`.
5. **Procedimiento y hallazgos objetivos:** Apertura de la copia en modo de solo lectura y descripción cronológica de los cinco eventos de ejemplo (solicitud de reposición de SIM a las 14:18:22, aprobación con línea, DNI y trámite a las 14:18:40, baja de la SIM anterior a las 14:19:05, envío de SMS a la SIM nueva a las 14:21:40 y consulta de estado a las 14:30:12).
6. **Conclusión técnica y límites:** Constancia de que el archivo no sufrió alteraciones durante la revisión y aclaración expresa de que, por tratarse de un archivo ficticio de práctica, solo ilustra el mecanismo técnico y no prueba hechos de ninguna causa real.

---

## ETAPA 5 – DECLARACIÓN DE USO DE INTELIGENCIA ARTIFICIAL Y REFLEXIÓN CRÍTICA

### 5.1. Declaración de Herramientas, Aportes y Corrección de Errores
Durante el desarrollo del trabajo utilizamos herramientas de Inteligencia Artificial generativa bajo supervisión humana y dejamos registro completo de las sesiones, errores detectados y correcciones en `anexos-para-zip/06_Prompts_y_Registro_IA.md` y `07_Declaracion_Uso_IA.md`:

| Herramienta / Modelo | Rol en el Trabajo | Contenido Aprovechado | Errores o Alucinaciones Detectadas y Corregidas | Método de Verificación Humana |
|:---|:---|:---|:---|:---|
| **Gemini (Guía inicial y ejecución operativa)** | Relevamiento preliminar, redacción de borradores, programación del script de hashes en Python y maquetación de archivos DOCX, PDF, XLSX y PPTX. | Estructura del código `05_calcular_hashes.py` con la librería estándar `hashlib`, generación automatizada de documentos y descarga de textos de las notas reales en la etapa de corrección. | 1) En la guía inicial (`guia-planificador-claude.md`) había incluido como parte de la condena el fraude informático (art. 173 inc. 16) y la violación de secretos (art. 157), además de mencionar UFEDECO/UFECI y Cellebrite sin respaldo.<br>2) En la primera versión del informe había inventado URLs, títulos y fechas de notas periodísticas (como una supuesta condena del 06/10/2023), la edad de "20 años", la "Causa N° 29/2023", el secuestro de un Samsung A52 y el hash de un archivo vacío (`e3b0c442...`). Todo ello fue eliminado y corregido. | Apertura y lectura directa de las nueve notas reales (`[F1]` a `[F9]`) el 30/10/2026, lectura página por página de la Ley 26.388 con `pdftotext` y prueba del script Python sobre `05_ejemplo_registro_ficticio.txt`. |
| **Claude Sonnet (Planificación y revisión crítica)** | Diseño del plan de trabajo (`plan-ejecucion-tpi.md`), protocolo de clasificación de fuentes y revisión crítica de veracidad (`revision-correcciones.md`). | Esquema de las seis etapas, reglas de lenguaje claro y sencillo, tabla de clasificación de datos (confirmados, reportados, contradictorios y no hallados) y lista puntual de correcciones obligatorias. | Ninguna afirmación fáctica de la revisión se incorporó sin antes abrir las notas periodísticas reales y contrastar el texto completo de los documentos normativos. | Control cruzado por los integrantes del equipo entre el informe, los anexos, el guion y las diapositivas. |

### 5.2. Reflexión Crítica sobre el Uso de IA en Temas Legales y Técnicos
La experiencia de este trabajo mostró de forma concreta tanto la utilidad como los riesgos de la Inteligencia Artificial generativa. Para tareas como estructurar secciones, escribir un script en Python o dar formato a tablas y documentos, la IA ahorra mucho tiempo. Sin embargo, cuando se le pide reconstruir un caso judicial o resumir noticias sin obligarla a leer el texto completo de cada fuente, tiende a completar los vacíos inventando fechas, enlaces web, números de expediente, modelos de teléfonos secuestrados o artículos penales que parecen creíbles pero no existen en las fuentes reales.

Por esa razón, la revisión crítica resultó indispensable: descartamos todas las notas cuya URL no pudo abrirse ni verificarse, conservamos en `10_Evidencia_Fuentes/` el texto completo de las nueve notas efectivamente leídas (`[F1]` a `[F9]`), distinguimos con claridad qué datos están confirmados por dos o más medios, cuáles fueron reportados por uno solo y en qué puntos las notas difieren, y rotulamos de manera explícita que la numeración de los artículos del Código Penal es una interpretación propia del equipo y que los formularios de cadena de custodia e informe pericial contienen datos ficticios de práctica. Asimismo, en ningún momento se cargaron a las herramientas de IA datos personales no públicos.

---

## ETAPA 6 – CONCLUSIONES Y ROL PROFESIONAL DEL PROGRAMADOR

El estudio del caso Nuñes Pinheiro nos deja cuatro conclusiones principales para nuestra formación como Técnicos Universitarios en Programación:

1. **La Seguridad en el Diseño de los Procesos de Autenticación:** El caso muestra que una aplicación o servicio no es seguro si el proceso para recuperar una línea o una cuenta depende de unos pocos datos personales (como el número de línea, el DNI y el número de trámite [F4, F7]) que pueden obtenerse en bases de datos o filtraciones. Como programadores, debemos evitar que el mensaje de texto (SMS) sea la única barrera de seguridad y priorizar métodos como las aplicaciones generadoras de códigos temporales (TOTP) y la verificación en dos pasos con PIN propio.
2. **Importancia de los Registros del Sistema (Logs):** Contar con registros claros que guarden fecha, hora, dirección IP, identificador del dispositivo y qué usuario o canal autorizó un cambio permite reconstruir un incidente y aportar elementos verificables ante una investigación judicial.
3. **Cuidado de la Evidencia Digital y Trazabilidad:** Un archivo digital o un registro de eventos solo conserva su valor probatorio si se puede explicar su origen, demostrar que no fue alterado mediante el cálculo de su código hash SHA-256, trabajar siempre sobre copias sin modificar el original y documentar cada entrega en la cadena de custodia.
4. **Responsabilidad Ética y Legal del Programador:** Los conocimientos técnicos que adquirimos en la carrera nos dan acceso a sistemas, bases de datos y herramientas sensibles. Involucrarse en accesos ilegítimos o aceptar encargos anónimos a cambio de dinero acarrea consecuencias penales reales, como la condena analizada en la justicia porteña y el procesamiento penal en el fuero federal [F1, F2, F8, F9]. Ejercer la profesión con ética implica proteger la privacidad de las personas y respetar las leyes vigentes.

---

## BIBLIOGRAFÍA Y FUENTES CONSULTADAS

### 1. Normativa, Documentos de Estudio y Jurisprudencia
1. **Código Penal de la Nación Argentina.** Ley N° 11.179 y modificatorias, en especial la **Ley N° 26.388** de Delitos Informáticos (sancionada el 04/06/2008 y promulgada de hecho el 24/06/2008; arts. 77, 153, 153 bis, 157 bis, 173 inc. 16, 183, 184, 197 y 255). Documento consultado: `material/arg_ley26388 (1).pdf` (págs. 1–4) e InfoLEG.
2. **Constitución de la Nación Argentina.** Artículo 18 (inviolabilidad de la correspondencia y los papeles privados, debido proceso y garantía contra el doble juzgamiento).
3. **Ley N° 25.326.** Protección de los Datos Personales (arts. 9 y 10). InfoLEG.
4. **Ley N° 27.411.** Aprobación del Convenio sobre la Ciberdelincuencia del Consejo de Europa (Convenio de Budapest, arts. 16, 17, 18, 19 y 35). InfoLEG y `material/Unidad 4 cadena de custodia TUP a distancia.pdf` (pág. 4).
5. **Ministerio de Seguridad de la Nación.** Resolución 232/2023: Protocolo para la identificación, recolección, preservación, procesamiento y presentación de evidencia digital. Documentos consultados: `material/Unidad_3_Evidencia digital tup.pdf` (pág. 2) y `material/Unidad 4 cadena de custodia TUP a distancia.pdf` (pág. 3).
6. **Norma Internacional ISO/IEC 27037:2012.** Directrices para la identificación, recolección, adquisición y preservación de evidencia digital potencial. Documento consultado: `material/Unidad 4 cadena de custodia TUP a distancia.pdf` (pág. 3).
7. **Cámara de Apelaciones en lo Penal, Penal Juvenil, Contravencional y de Faltas de la CABA, Sala III.** Causa N° 41459/2019-3, *"Incidente de apelación en autos NN, NN sobre 131 – Contactar menor de edad por intermedio de tecnologías para cometer delitos de integridad sexual"*, resolución del 05/10/2021. Documento consultado: `material/000099168.pdf` (págs. 1–15).
8. **Apuntes de estudio verificados:** *Unidad N° 3: Evidencia digital: concepto, integridad, trazabilidad y hash* (`material/Unidad_3_Evidencia digital tup.pdf`, págs. 1–4); *Unidad N° 4: Cadena de custodia y protocolos para evidencia digital* (`material/Unidad 4 cadena de custodia TUP a distancia.pdf`, págs. 1–6); *Semana 2 – Delitos Informáticos* (`material/SEMANA 2 - DELITOS INFORMATICOS.pdf`, págs. 1–15); y *Jurisprudencia – Delitos Informáticos* (`material/JURISPRUDENCIA DELITOS INFORMATICOS.pdf`, págs. 1–4).

### 2. Fuentes Periodísticas del Caso (Abiertas y Leídas el 30/10/2026)
9. **[F1] Infobae (18/07/2026):** *La Justicia concedió la probation a un acusado por intervenir el teléfono de Marcelo D’Alessandro*. Disponible en: `https://www.infobae.com/judiciales/2026/07/18/la-justicia-concedio-la-probation-a-un-acusado-por-intervenir-el-telefono-de-marcelo-dalessandro/` (Consultado el 30/10/2026).
10. **[F2] La Nación (08/06/2026):** *Alarma en Comodoro Py: la Justicia porteña unificó las condenas contra el hacker que atacó a D’Alessandro y Santilli*. Disponible en: `https://www.lanacion.com.ar/politica/alarma-en-comodoro-py-la-justicia-portena-unifico-las-condenas-contra-el-hacker-que-ataco-a-nid08062026/` (Consultado el 30/10/2026).
11. **[F3] Página/12 (29/03/2023):** *El joven que hackeó el celular de Marcelo D'Alessandro contó cómo fue la operación* (por Raúl Kollmann). Disponible en: `https://www.pagina12.com.ar/535939-el-joven-que-hackeo-el-celular-de-marcelo-dalessandro-conto-` (Consultado el 30/10/2026; titular y bajada).
12. **[F4] Infobae (28/03/2023):** *El hacker de D’Alessandro dijo que le pagaron $15 mil “por cada objetivo” y que sus jefes serían misioneros*. Disponible en: `https://www.infobae.com/judiciales/2023/03/28/el-hacker-de-dalessandro-dijo-que-le-pagaron-15-mil-por-cada-objetivo-y-que-sus-jefes-serian-misioneros/` (Consultado el 30/10/2026).
13. **[F5] Infobae (11/04/2023):** *El joven que hackeó a D’Alessandro declaró que prendió fuego su teléfono y lo tiró al río Paraná porque se asustó*. Disponible en: `https://www.infobae.com/judiciales/2023/04/11/el-joven-que-hackeo-a-dalessandro-declaro-que-prendio-fuego-su-telefono-y-lo-tiro-al-rio-parana-porque-se-asusto/` (Consultado el 30/10/2026).
14. **[F6] Infobae (05/04/2023):** *La Justicia recibió un informe clave y avanza con la ruta del dinero que se utilizó para financiar al hacker de D’Alessandro*. Disponible en: `https://www.infobae.com/judiciales/2023/04/05/la-justicia-recibio-un-informe-clave-y-avanza-con-la-ruta-del-dinero-que-se-utilizo-para-financiar-al-hacker-de-dalessandro/` (Consultado el 30/10/2026).
15. **[F7] Infobae (30/03/2023):** *Investigan al padre del hacker que espió a Marcelo D’Alessandro por un misterioso viaje a Chile*. Disponible en: `https://www.infobae.com/judiciales/2023/03/30/investigan-al-padre-del-hacker-que-espio-a-marcelo-dalessandro-por-un-misterioso-viaje-a-chile/` (Consultado el 30/10/2026).
16. **[F8] Infobae (10/09/2026):** *Los tres hackers acusados de espiar a jueces federales apelaron el procesamiento*. Disponible en: `https://www.infobae.com/judiciales/2026/09/10/los-tres-hackers-acusados-de-espiar-a-jueces-federales-apelaron-el-procesamiento/` (Consultado el 30/10/2026).
17. **[F9] La Nación (21/08/2026):** *Procesaron a un exagente de inteligencia y dos hackers por espiar a miembros de la Corte y jueces*. Disponible en: `https://www.lanacion.com.ar/politica/procesaron-a-un-exagente-de-inteligencia-y-dos-hackers-por-espiar-a-miembros-de-la-corte-y-jueces-nid21082026/` (Consultado el 30/10/2026).
