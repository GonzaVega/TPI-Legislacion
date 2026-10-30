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

---

## RESUMEN EJECUTIVO

En este trabajo analizamos el caso real de Elías Ezequiel Nuñes Pinheiro, un joven de Misiones condenado en la Ciudad de Buenos Aires por realizar ataques de duplicación no autorizada de líneas telefónicas (SIM swapping) [F1]. A partir de datos personales de las víctimas obtenidos en diversas fuentes, el atacante engañó a empresas de telefonía, tomó el control de los números de celular y capturó los códigos de verificación por mensaje de texto para apoderarse de cuentas de mensajería [F2, F5]. El hecho derivó en una condena de tres años de prisión en suspenso en juicio abreviado por acceso ilegítimo a sistemas informáticos, sustracción de documentos y entorpecimiento de comunicaciones [F1, F3]. Evaluamos las normas penales aplicables, construimos una matriz con siete riesgos críticos y proponemos medidas de seguridad concretas y accesibles para evitar estas intrusiones. Finalmente, presentamos un protocolo básico de cadena de custodia para resguardar evidencia digital de manera confiable y reflexionamos sobre la responsabilidad ética que tenemos como futuros programadores en la protección de sistemas y datos personales.

---

## ETAPA 1 – PRESENTACIÓN DEL CASO Y ALCANCE

### 1.1. Descripción de los Hechos
El caso investigado tiene como protagonista a Elías Ezequiel Nuñes Pinheiro, un joven de 20 años radicado en la localidad de Eldorado, provincia de Misiones [F4]. Entre los años 2022 y 2023, Nuñes Pinheiro llevó adelante una serie de maniobras coordinadas para tomar el control de líneas de telefonía celular pertenecientes a distintas personalidades públicas, entre ellas el exministro de Seguridad porteño Marcelo D'Alessandro y el diputado Diego Santilli [F1, F2].

La maniobra se basó en una técnica conocida como **SIM swapping** (reemplazo o duplicación de tarjeta SIM) [F2]. Consiste en solicitar a la compañía telefónica un nuevo chip a nombre del titular legítimo, aduciendo pérdida, robo o rotura del anterior [F5]. Para superar las preguntas de seguridad que formulan los centros de atención o las plataformas de autogestión de las compañías, Nuñes Pinheiro utilizaba información personal y comercial de las víctimas (números de trámite de DNI, domicilios anteriores, fechas de nacimiento) [F5]. Una vez que la compañía daba de baja la tarjeta SIM original y activaba la nueva en poder del atacante, este recibía en su propio dispositivo todos los llamados y mensajes de texto destinados a la víctima [F2].

Con el control de la línea, el atacante solicitó el restablecimiento de contraseñas y la activación de cuentas en aplicaciones de mensajería (particularmente WhatsApp y Telegram), interceptando en tiempo real los códigos de autenticación enviados por SMS [F4, F5]. Nuñes Pinheiro declaró judicialmente que actuaba por encargo de terceros anónimos que lo contactaban a través de Telegram (mediante usuarios como "Eljuanxd" o "Pr1sox"), quienes le indicaban qué números intervenir a cambio de pagos mediante billeteras virtuales o criptomonedas [F4, F5].

### 1.2. Actores Involucrados
* **Sujeto Activo (Imputado):** Elías Ezequiel Nuñes Pinheiro, confeso ejecutor técnico de las maniobras de SIM swapping desde la provincia de Misiones [F1, F4].
* **Terceros Instigadores:** Usuarios anónimos de la aplicación Telegram que contrataban los servicios ilícitos y proveían listados de personas a intervenir [F4].
* **Víctimas Directas:** Titulares de las líneas telefónicas intervenidas (funcionarios públicos porteños y particulares) cuya privacidad y comunicaciones resultaron vulneradas [F1, F2].
* **Prestadoras de Telecomunicaciones:** Empresas de telefonía móvil (como Personal/Telecom) que ejecutaron la reposición de las tarjetas SIM tras validar de forma deficiente la identidad de quien llamaba [F2, F5].
* **Organismos Judiciales y de Investigación:** Juzgado de 1ª Instancia en lo Penal, Contravencional y de Faltas N° 29 de la Ciudad Autónoma de Buenos Aires (a cargo de la Dra. María Araceli Martínez), fiscalías especializadas en ciberdelincuencia y fuerzas policiales que rastrearon la actividad digital [F1, F8].

### 1.3. Sistemas y Servicios Tecnológicos Analizados
1. **Red de Telefonía Móvil y Tarjetas SIM:** La tarjeta SIM es el chip físico que identifica de forma única a un abonado en la red celular. El proceso vulnerable fue el trámite administrativo y técnico de asignación de una línea existente a un nuevo chip físico.
2. **Mensajes de Texto (SMS) como Segundo Factor (2FA):** El uso de mensajes de texto para enviar códigos de un solo uso (OTP). El SMS viaja en texto plano a través de la red celular y llega a quien posea el chip activo, lo que lo convierte en un método inseguro frente a la clonación de SIM.
3. **Bases de Datos de Información Personal:** Registros crediticios y comerciales públicos o privados de donde se extraían las respuestas a las preguntas de seguridad de las operadoras telefónicas [F5].
4. **Plataformas de Mensajería Instantánea:** Aplicaciones como WhatsApp y Telegram, cuyo mecanismo inicial de vinculación de cuenta depende del número de teléfono celular del usuario.

### 1.4. Alcance y Límites del Análisis
El presente trabajo se circunscribe al análisis de la sentencia condenatoria dictada en el marco del **juicio abreviado homologado en octubre de 2023 por el Juzgado PCyF N° 29 de CABA**, donde recayó condena firme sobre Nuñes Pinheiro a la pena de tres años de prisión en suspenso y reglas de conducta [F1, F3]. 

Aclaramos de manera expresa que no analizamos la causa penal conexa radicada en los tribunales federales de Comodoro Py (donde se investiga una eventual trama de espionaje mayor vinculada a otros actores), dado que dicho expediente continúa en trámite procesal sin sentencia definitiva y el propio imputado fue excarcelado en ese fuero en abril de 2024 al no atribuírsele un rol de jefatura organizativa [F6]. El análisis se basa estrictamente en información pública coincidente de fuentes periodísticas fidedignas y registros institucionales, al no contarse con acceso directo al expediente judicial reservado.

---

## ETAPA 2 – MARCO JURÍDICO APLICABLE

A continuación explicamos cada una de las normas nacionales e internacionales que resultan aplicables al caso y fundamentamos por qué corresponden a las conductas analizadas.

### 2.1. Código Penal de la Nación Argentina (con reformas de la Ley 26.388)
La Ley 26.388 incorporó y actualizó diversas figuras en el Código Penal para sancionar los delitos informáticos. En este caso aplican de forma directa:

* **Artículo 153 bis del Código Penal (Acceso Ilegítimo a Sistemas Informáticos):**  
  * *Texto y concepto:* Sanciona a quien, a sabiendas y sin la debida autorización o excediendo la que posea, acceda por cualquier medio a un sistema o dato informático de acceso restringido.  
  * *Por qué aplica:* Nuñes Pinheiro accedió sin autorización a los sistemas de gestión de las cuentas de mensajería de las víctimas y a los datos transmitidos a través de ellas. El atacante conocía perfectamente que no tenía derecho a entrar a esas cuentas ("a sabiendas") y utilizó medios fraudulentos para vulnerar el acceso restringido.
* **Artículo 153 del Código Penal (Violación de Comunicaciones Electrónicas):**  
  * *Texto y concepto:* Castiga a quien abriere o accediere indebidamente a una comunicación electrónica, una carta, un despacho telegráfico o telefónico que no le esté dirigido, o se apoderare indebidamente de ellos.  
  * *Por qué aplica:* Al desviar la tarjeta SIM hacia su propio dispositivo, el atacante interceptó y se apoderó de mensajes de texto privados y comunicaciones en tránsito dirigidas exclusivamente a los titulares de las líneas.
* **Artículo 197 del Código Penal (Entorpecimiento de Servicios y Comunicaciones):**  
  * *Texto y concepto:* Reprime a quien interrumpiere o entorpeciere las comunicaciones telegráficas, telefónicas o de otra naturaleza.  
  * *Por qué aplica:* Al dar de alta la SIM duplicada, la empresa telefónica dio de baja de inmediato la SIM legítima de la víctima, dejándola sin señal, sin datos y sin posibilidad de comunicarse, configurando una interrupción directa del servicio de telecomunicaciones.
* **Artículo 255 del Código Penal (Sustracción de Documentos):**  
  * *Por qué aplica:* Formó parte de la imputación admitida en la justicia porteña vinculada a la sustracción y apropiación de constancias y registros documentales reservados que se encontraban bajo la custodia de funcionarios públicos [F1, F3].

#### Subsección: Figuras Conexas Analizadas (Análisis Académico)
Como estudiantes de programación, evaluamos si correspondía aplicar también el **Artículo 173 inciso 16 del Código Penal** (defraudación informática mediante manipulación o uso no autorizado de datos). Consideramos que, si bien el atacante manipuló datos de identidad para engañar a la operadora telefónica, su objetivo central en los hechos juzgados no fue vaciar cuentas bancarias ni obtener un beneficio patrimonial directo a costa de la víctima, sino apoderarse de sus comunicaciones. Por ello, la justicia porteña encuadró la condena en el acceso ilegítimo (art. 153 bis) y entorpecimiento, sin incluir el fraude informático, criterio que consideramos técnicamente acertado.

### 2.2. Constitución Nacional
* **Artículo 18 de la Constitución Nacional:**  
  Consagra que el domicilio, la correspondencia epistolar y los papeles privados son inviolables. En la era digital, esta garantía protege con igual fuerza a los correos electrónicos, los mensajes de chat, los registros de llamadas y cualquier comunicación que circule por redes informáticas. Toda interceptación sin orden judicial previa emitida por un juez competente constituye una violación directa a esta garantía constitucional.

### 2.3. Ley 25.326 de Protección de los Datos Personales
Esta ley regula el tratamiento de datos personales para garantizar el honor y la intimidad de las personas:
* **Artículo 9 (Seguridad de los Datos):** Obliga a quienes administran bases de datos (tanto empresas de telefonía como plataformas web) a adoptar medidas técnicas y organizativas para garantizar la seguridad de los datos y evitar su adulteración, pérdida o acceso no autorizado. Las compañías telefónicas fallaron en este deber al no implementar mecanismos robustos para validar la identidad de los solicitantes de chips.
* **Artículo 10 (Deber de Confidencialidad):** Exige guardar secreto sobre los datos personales a quienes intervengan en cualquier fase del tratamiento, obligación que se vulnera cuando los datos son expuestos o consultados para fines ajenos a los autorizados.

### 2.4. Estándares Técnicos y Protocolos de Evidencia Digital
* **Norma ISO/IEC 27037:**  
  Es una norma internacional que establece directrices técnicas básicas para que la evidencia digital no pierda valor probatorio. Plantea cuatro momentos fundamentales: identificación de qué dispositivos o archivos contienen datos útiles, recolección adecuada, adquisición (generar copias sin tocar los originales) y preservación segura de los soportes.
* **Resolución 232/2023 del Ministerio de Seguridad:**  
  Es el protocolo oficial argentino que organiza el tratamiento de la evidencia digital en cinco etapas: identificación, recolección, preservación, procesamiento y presentación. Resulta aplicable al procedimiento de allanamiento y secuestro de los dispositivos utilizados por el imputado en Misiones.
* **Convenio de Budapest sobre Ciberdelincuencia (Ley 27.411):**  
  Es un tratado internacional al que Argentina adhirió formalmente. Permite a las fiscalías locales solicitar la conservación rápida de datos y registros informáticos almacenados en servidores radicados en el exterior, mecanismo indispensable cuando se investigan maniobras coordinadas mediante aplicaciones extranjeras como Telegram.

---

## ETAPA 3 – MATRIZ DE RIESGOS LEGALES Y DE CUMPLIMIENTO

Para evaluar las debilidades del caso desde el punto de vista del desarrollo de software y la gestión de sistemas, elaboramos la siguiente matriz con siete riesgos concretos, ordenados por nivel de criticidad.

| ID | Riesgo Detectado | Tipo de Riesgo | Norma / Principio Vinculado | Probabilidad | Impacto | Criticidad (P × I) | Medida Propuesta |
|:---|:---|:---|:---|:---|:---|:---|:---|
| **R1** | **Reposición fraudulenta de tarjetas SIM por validación débil de identidad.** Se entregan chips a terceros atacantes usando solo datos personales públicos o fáciles de conseguir. | Técnico / Operativo | Ley 25.326 (Art. 9) y normas de telecomunicaciones. | Alta | Muy Alto | **Crítica** | Exigir validación biométrica en la app de la compañía o trámite presencial con DNI físico para duplicar una SIM, eliminando cuestionarios estáticos. |
| **R2** | **Vulneración de cuentas de usuario por utilizar SMS como segundo factor de autenticación.** Los códigos de verificación viajan sin cifrar y llegan al chip clonado. | Técnico / Seguridad | Art. 18 de la Constitución Nacional y buenas prácticas de seguridad. | Alta | Muy Alto | **Crítica** | Reemplazar el SMS por aplicaciones autenticadoras de códigos temporales (TOTP) o llaves de seguridad físicas. |
| **R3** | **Acceso indebido a cuentas de mensajería y exfiltración de conversaciones privadas.** El atacante entra al perfil de la víctima y lee sus mensajes. | Penal | Código Penal (Art. 153 bis y Art. 153). | Alta | Alto | **Alta** | Incorporar una contraseña o PIN interno en la aplicación (verificación en dos pasos nativa de WhatsApp/Telegram) independiente de la línea celular. |
| **R4** | **Pérdida de señal e interrupción total del servicio de comunicaciones del titular legítimo.** La víctima queda incomunicada sin saber por qué. | Operativo / Penal | Código Penal (Art. 197). | Alta | Medio | **Media** | Enviar una alerta inmediata por correo electrónico y notificación push antes de desactivar la SIM original, otorgando un período de gracia para cancelar el trámite. |
| **R5** | **Nulidad de la prueba digital por fallas en la cadena de custodia.** Dispositivos secuestrados encendidos, alterados o sin registro de quién los manipuló. | Procesal / Legal | Art. 18 CN (debido proceso) e ISO/IEC 27037. | Media | Muy Alto | **Alta** | Aplicar el protocolo oficial de secuestro: colocar teléfonos en modo avión o bolsas de Faraday, calcular hash SHA-256 de cada archivo y registrar firmas de entrega. |
| **R6** | **Responsabilidad legal de empresas por falta de medidas de seguridad en el tratamiento de datos.** Sanciones administrativas y demandas civiles por entregar líneas sin control. | Administrativo / Civil | Ley 25.326 (Art. 9 y 31) y Ley de Defensa del Consumidor. | Alta | Medio | **Media** | Implementar auditorías internas de seguridad, registro estricto de qué empleado autoriza cada reemplazo de SIM y sanciones por incumplimiento de protocolos. |
| **R7** | **Riesgo ético y penal para programadores por participar en maniobras informáticas ilegales.** Desarrolladores que prestan servicios o crean herramientas para terceros sin medir las consecuencias penales. | Ético / Penal | Código Penal (Art. 153 bis, participación criminal). | Media | Alto | **Media** | Formación profesional sólida en ética y legislación informática; abstenerse de manipular accesos, vender credenciales o colaborar con servicios no autorizados. |

---

## ETAPA 4 – MEDIDAS, DOCUMENTOS Y PROTOCOLOS PROPUESTOS

A partir de los riesgos identificados, proponemos un conjunto de soluciones concretas, realistas y no sofisticadas, tanto para la prevención en sistemas como para el manejo correcto de evidencia digital.

### 4.1. Medidas Prácticas de Mitigación para Sistemas y Empresas
1. **Verificación Reforzada en Trámites de SIM:** Las empresas de telefonía no deben autorizar cambios de SIM mediante llamadas telefónicas basadas únicamente en preguntas como el domicilio o la fecha de cumpleaños. Se debe exigir verificación mediante la cámara del celular (reconocimiento facial comparado con el DNI) o realizar el trámite de forma presencial.
2. **Aviso Previo por Canales Alternativos:** Cuando se solicite un reemplazo de SIM, el sistema debe enviar de inmediato un correo electrónico al titular registrado alertando: *"Se solicitó un nuevo chip para su línea. Si no fue usted, ingrese a este enlace de inmediato para frenar la operación"*. Debe existir una ventana de espera mínima de 2 a 3 horas antes del corte definitivo de la línea original.
3. **Abandono del SMS como Método Seguro de Verificación:** En el desarrollo de software, los programadores debemos dejar de ofrecer el SMS como único método de recuperación de cuentas. Es preferible guiar al usuario para que utilice aplicaciones generadoras de códigos (como Google Authenticator) que se ejecutan dentro del dispositivo y no dependen de la red telefónica.
4. **Registro Inmutable de Eventos (Logs Básicos):** Los sistemas que administran líneas y usuarios deben guardar un registro claro que indique: fecha, hora, dirección IP, número de documento consultado y qué operador autorizó la operación. Estos registros son los que luego permiten a la justicia reconstruir lo ocurrido.

---

### 4.2. Protocolo Básico de Relevamiento y Preservación de Evidencia Digital
Para que la evidencia informática obtenida en un incidente tenga validez y no pueda ser cuestionada en un juicio, proponemos un procedimiento sencillo de cinco pasos:

```
[Paso 1: Identificar] ──> [Paso 2: Aislar] ──> [Paso 3: Duplicar] ──> [Paso 4: Calcular Hash] ──> [Paso 5: Registrar]
```

1. **Paso 1 – Identificación:** Anotar de forma clara qué elementos existen en el lugar (marca, modelo y número de serie de computadoras, teléfonos celulares, chips SIM, memorias o routers).
2. **Paso 2 – Aislamiento:** No encender dispositivos que estén apagados. Si un teléfono celular está encendido, no revisarlo manualmente: colocarlo de inmediato en "modo avión" o guardarlo en una funda metálica protectora (tipo Faraday) para evitar que reciba mensajes, llamadas o comandos remotos de borrado a través de internet.
3. **Paso 3 – Copia de Trabajo:** Nunca trabajar sobre el archivo o dispositivo original. Se debe realizar una copia digital completa de los datos para que los análisis y peritajes se hagan sobre el duplicado, preservando intacto el original.
4. **Paso 4 – Cálculo de Integridad (Hash):** Sobre cada archivo o imagen copiada, se debe calcular su código hash utilizando el algoritmo estándar SHA-256 mediante un programa simple. Este código alfanumérico funciona como una "huella digital": si el archivo se modifica en un solo espacio o letra, el hash cambia por completo, demostrando si hubo o no alteración.
5. **Paso 5 – Documentación y Cadena de Custodia:** Completar un formulario de papel o digital donde conste quién secuestró el elemento, quién lo recibió, fecha, hora, motivo del traslado y firmas de las partes involucradas.

---

### 4.3. Formulario Modelo de Registro y Cadena de Custodia
Este documento acompaña físicamente a la evidencia desde que es secuestrada hasta que se presenta en el juzgado:

* **Número de Caso / Causa:** Causa CABA N° 29/2023.
* **Fecha y Hora de Recepción:** 30 de octubre de 2026 – 10:30 hs.
* **Descripción del Elemento:** Teléfono celular smartphone marca Samsung modelo Galaxy A52, color negro, pantalla sana, con tarjeta SIM de la empresa Personal colocada en la ranura 1.
* **Número de Serie / IMEI:** 358912093847120.
* **Estado al Momento del Secuestro:** Encendido, colocado en modo avión y guardado en bolsa de resguardo N° 00412.
* **Cálculo de Hash SHA-256 del Volcado Lógico:** `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
* **Historial de Movimientos:**
  * *Entregado por:* Oficial Ayudante Gómez (Fuerza Policial interviniente).
  * *Recibido por:* Lic. Martínez (Perito Informático Oficial).
  * *Motivo:* Traslado al laboratorio para extracción de registros de llamadas y mensajes.
  * *Firmas:* [Firmas de entrega y recepción].

---

### 4.4. Estructura de Informe Técnico para el Programador que Colabora en una Pericia
Cuando a un técnico o programador se le solicita colaborar en el análisis de un incidente, su informe debe seguir una estructura simple y ordenada:
1. **Identificación:** Datos del técnico, fecha y número de expediente.
2. **Objeto:** Explicación clara de qué se solicitó revisar (por ejemplo: *"determinar si hubo accesos no autorizados a la cuenta de mensajería desde direcciones IP desconocidas"*).
3. **Origen de la Evidencia:** De qué archivo, base de datos o dispositivo provienen los registros analizados.
4. **Procedimiento Empleado:** Explicar con palabras sencillas qué operaciones se hicieron (ejemplo: *"se extrajo el archivo de texto con los registros del servidor y se calculó su código hash SHA-256 para constatar su integridad"*).
5. **Hallazgos:** Detalle objetivo de lo encontrado, sin conjeturas (ejemplo: *"el día 15 de marzo a las 14:22 hs se registró un inicio de sesión exitoso desde una dirección IP asignada a una conexión de Eldorado, Misiones, solicitando restablecimiento de clave"*).
6. **Conclusión Técnica:** Resumen final sobre la integridad de los datos y el resultado de la observación.

---

## ETAPA 5 – DECLARACIÓN DE USO DE INTELIGENCIA ARTIFICIAL Y REFLEXIÓN CRÍTICA

### 5.1. Declaración de Herramientas y Finalidad
En cumplimiento de las pautas de integridad académica, declaramos de forma transparente las herramientas de Inteligencia Artificial empleadas en este trabajo:

| Herramienta / Modelo | Finalidad Específica | Contenido Aprovechado | Contenido Descartado o Corregido (Alucinaciones) | Método de Verificación Humana |
|:---|:---|:---|:---|:---|
| **Claude Sonnet** | Planificación inicial y diseño de la estructura argumentativa. | Esquema de las seis etapas del informe y sugerencias para la matriz de riesgos. | Se corrigió la atribución errónea de los artículos penales de la condena: el modelo sugería condena por fraude informático (art. 173 inc. 16) y revelación de secretos (art. 157), datos que fueron descartados al no coincidir con las fuentes periodísticas judiciales reales. | Cotejo directo contra notas de prensa de Infobae, Clarín y La Nación [F1, F2, F3]. |
| **Antigravity / Gemini Flash** | Asistencia en redacción, maquetación sobre plantilla Word y confección de scripts. | Automatización de la plantilla documental, armado de tablas comparativas y código Python simple para cálculo de hashes. | Se descartaron propuestas técnicas sofisticadas e irreales (como implementar llaves FIDO2 corporativas obligatorias o servidores de registros blockchain), adoptando medidas simples y accesibles. | Revisión y adaptación por parte de los cuatro integrantes del equipo. |

### 5.2. Reflexión Crítica sobre el Uso de IA
La inteligencia artificial generativa demostró ser una herramienta muy valiosa para estructurar ideas, acelerar la redacción formal y verificar que no quedaran aspectos requeridos sin cubrir. Sin embargo, su utilización exige un criterio humano permanente y riguroso. En el ámbito legal e informático, los modelos tienden a "rellenar" lagunas de información inventando números de artículos, fechas o detalles periciales que suenan verosímiles pero son falsos.

Para neutralizar ese riesgo, aplicamos un principio estricto: **ningún dato fáctico ni norma jurídica se incluyó en el trabajo sin haber sido contrastado previamente con el texto de la ley o con al menos dos fuentes periodísticas independientes**. Asimismo, no se cargaron a los sistemas de IA datos personales reales que no fueran los estrictamente públicos reportados en las noticias del caso judicial.

---

## ETAPA 6 – CONCLUSIONES Y ROL PROFESIONAL DEL PROGRAMADOR

El análisis del caso Nuñes Pinheiro nos deja aprendizajes fundamentales para nuestro futuro desempeño como Técnicos Universitarios en Programación:

1. **La Seguridad debe ser pensada desde el Diseño:** Muchas veces, como programadores, nos enfocamos en que una aplicación funcione rápido y sea cómoda para el usuario, descuidando los mecanismos de validación. Este caso demuestra que delegar la seguridad en canales vulnerables como el SMS puede echar por tierra la privacidad de miles de personas. Debemos diseñar sistemas con autenticación robusta desde el primer día.
2. **El Valor Probatorio de los Registros (Logs):** Todo sistema que programemos debe generar registros de actividad ordenados, precisos y con marcas de tiempo (timestamps) confiables. Si un sistema no guarda registros de quién hizo qué y desde qué dirección IP, ante un delito informático resulta imposible deslindar responsabilidades o aportar pruebas útiles a la justicia.
3. **Límites Profesionales y Deber Ético:** Como técnicos, poseemos herramientas y conocimientos que pueden ser utilizados para proteger a la sociedad o para vulnerar derechos. El caso analizado evidencia las gravísimas consecuencias penales y personales que acarrea involucrarse en maniobras ilícitas bajo promesas de dinero fácil. Nuestro rol profesional debe guiarse por la ética, el respeto irrestricto a la privacidad ajena y el cumplimiento de las leyes vigentes.
4. **Trabajo en Equipo:** Para este trabajo articulamos nuestras tareas de forma grupal entre los cuatro integrantes (Mateo Serafini, Hugo Tcach, Farid Salomon y Gonzalo Vega), debatiendo los aspectos técnicos de las redes de telefonía, contrastando las noticias del caso y construyendo una propuesta equilibrada entre la técnica informática y las exigencias del derecho penal argentino.

---

## BIBLIOGRAFÍA Y FUENTES CONSULTADAS

### Normativa Oficial y Fuentes Jurídicas
1. **Código Penal de la Nación Argentina.** Ley N° 11.179 (texto ordenado por Decreto 399/1995, con modificaciones introducidas por la Ley 26.388 de Delitos Informáticos). Disponible en: InfoLEG.
2. **Ley N° 25.326.** Protección de los Datos Personales. Sancionada el 4 de octubre de 2000. Disponible en: InfoLEG.
3. **Ley N° 27.411.** Aprobación del Convenio sobre la Ciberdelincuencia del Consejo de Europa (Convenio de Budapest). Sancionada el 20 de septiembre de 2017. Disponible en: InfoLEG.
4. **Constitución de la Nación Argentina.** Artículo 18 (Garantías del debido proceso e inviolabilidad de la correspondencia).
5. **Ministerio de Seguridad de la Nación.** Resolución 232/2023: Protocolo general para la identificación, recolección, preservación, procesamiento y presentación de evidencia digital. Boletín Oficial de la República Argentina.
6. **Norma Internacional ISO/IEC 27037:2012.** Tecnología de la información — Técnicas de seguridad — Directrices para la identificación, recolección, adquisición y preservación de evidencia digital. Organización Internacional de Normalización (ISO).
7. **Poder Judicial de la Ciudad Autónoma de Buenos Aires (JusBaires).** Guía Judicial: Juzgado de 1ª Instancia en lo Penal, Contravencional y de Faltas N° 29. Disponible en: `https://jusbaires.gob.ar`.

### Fuentes Periodísticas de Investigación del Caso
8. **[F1] Infobae (06/10/2023):** *Condenaron al hacker que admitió haber intervenido el teléfono de Marcelo D’Alessandro*. Disponible en: `https://www.infobae.com/politica/2023/10/06/condenaron-al-hacker-que-admitio-haber-intervenido-el-telefono-de-marcelo-dalessandro/` (Consultado el 30/10/2026).
9. **[F2] Clarín (06/10/2023):** *SIM swapping: condenaron a tres años de prisión en suspenso al hacker misionero que duplicó el celular de D’Alessandro*. Disponible en: `https://www.clarin.com/politica/sim-swapping-condenaron-hacker-misionero-celular-dalessandro` (Consultado el 30/10/2026).
10. **[F3] La Nación (07/10/2023):** *Juicio abreviado: condenaron al joven de Eldorado que hackeó las comunicaciones de funcionarios*. Disponible en: `https://www.lanacion.com.ar/seguridad/juicio-abreviado-condenaron-al-joven-de-eldorado-que-hackeo-las-comunicaciones-de-funcionarios` (Consultado el 30/10/2026).
11. **[F4] Perfil (12/06/2023):** *Quién es Ezequiel Nuñes Pinheiro, el hacker de Eldorado que confesó el SIM swapping a políticos y jueces*. Disponible en: `https://www.perfil.com/noticias/politica/quien-es-ezequiel-nunes-pinheiro-el-hacker-de-eldorado-confeso-sim-swapping.phtml` (Consultado el 30/10/2026).
12. **[F5] Página/12 (15/06/2023):** *La declaración del hacker de Eldorado: cómo funcionaba la duplicación de chips*. Disponible en: `https://www.pagina12.com.ar/532981-la-declaracion-del-hacker-de-eldorado-como-funcionaba-la-duplicacion` (Consultado el 30/10/2026).
13. **[F6] Primera Edición de Misiones (18/04/2024):** *Eldorado: excarcelaron al joven implicado en maniobras informáticas contra funcionarios*. Disponible en: `https://www.primeraedicion.com.ar/nota/100789456/eldorado-excarcelaron-al-joven-implicado-en-maniobras-informaticas/` (Consultado el 30/10/2026).
14. **[F7] El Territorio de Misiones (14/06/2023):** *Los rastros digitales de los hackeos telefónicos que condujeron a Eldorado*. Disponible en: `https://www.elterritorio.com.ar/noticias/2023/06/14/792134-los-rastros-digitales-de-los-hackeos` (Consultado el 30/10/2026).
