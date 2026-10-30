# GUION ESTRUCTURADO PARA PRESENTACIÓN EN VIDEO (4 INTEGRANTES)

> **Materia:** Legislación – Tecnicatura Universitaria en Programación (UTN)  
> **Eje Temático:** Eje 1 – Cibercrimen, evidencia digital y cadena de custodia  
> **Caso:** Elías Ezequiel Nuñes Pinheiro (SIM Swapping, Acceso Ilegítimo y Preservación de Evidencia)  
> **Comisión:** Comisión 5  
> **Duración Total Estimada:** 10 minutos y 30 segundos (dentro del rango reglamentario de 8 a 12 minutos)  
> **Apoyo Visual:** Diapositivas correspondientes al archivo `Presentacion_TPI_Eje1.pptx`

---

## 1. Tabla General de Tiempos y Distribución

| Bloque | Integrante | Temas Asignados | Diapositivas de Apoyo | Tiempo Estimado |
|:---|:---|:---|:---|:---|
| **Bloque 1** | **Mateo Serafini** | Apertura, presentación del equipo, resumen ejecutivo y descripción fáctica del caso Nuñes Pinheiro (Etapa 1). | Diapositivas 1, 2 y 3 | **00:00 a 02:30 (2:30 min)** |
| **Bloque 2** | **Hugo Tcach** | Marco jurídico aplicable: Ley 26.388 (arts. 153 bis, 153, 197 CPA), Ley 25.326, garantías del art. 18 CN y Convenio de Budapest (Etapa 2). | Diapositiva 4 | **02:30 a 05:00 (2:30 min)** |
| **Bloque 3** | **Farid Salomon** | Exposición de la matriz de riesgos priorizada y medidas prácticas de mitigación para sistemas y operadoras (Etapas 3 y 4). | Diapositivas 5 y 6 | **05:00 a 08:00 (3:00 min)** |
| **Bloque 4** | **Gonzalo Vega** | Cadena de custodia, cálculo de hash SHA-256, uso responsable de IA, conclusiones profesionales y cierre del equipo (Etapas 4, 5 y 6). | Diapositivas 7, 8, 9 y 10 | **08:00 a 10:30 (2:30 min)** |

---

## 2. Guion Literal por Integrante

### BLOQUE 1: APERTURA Y PRESENTACIÓN DEL CASO
**Expositor:** Mateo Serafini  
**Tiempo:** 00:00 – 02:30 (2 minutos y 30 segundos)  
**Diapositivas:** 1, 2 y 3

*(Diapositiva 1: Portada institucional en pantalla)*
> *"Buenas tardes, profesores y compañeros. Somos el grupo de la Comisión 5, integrado por Hugo Tcach, Farid Salomon, Gonzalo Vega y quien les habla, Mateo Serafini. En este Trabajo Práctico Integrador de Legislación, analizamos un incidente real y sumamente actual ocurrido en nuestro país: el caso de Elías Ezequiel Nuñes Pinheiro, vinculado a maniobras de duplicación ilegítima de tarjetas SIM, acceso no autorizado a comunicaciones y tratamiento de evidencia digital."*

*(Transición a Diapositiva 2: Estructura general de la exposición)*
> *"Organizamos nuestro análisis en torno a la realidad que nos toca vivir como futuros programadores. Muchas veces pensamos que la seguridad es solo un problema de código, pero este caso demuestra cómo las fallas en los procesos de autenticación y la falta de recaudos legales pueden poner en riesgo la privacidad de miles de personas. Vamos a recorrer el caso, las normas penales aplicables, los riesgos detectados, las medidas que proponemos y cómo cuidamos la evidencia."*

*(Transición a Diapositiva 3: Presentación del Caso Nuñes Pinheiro)*
> *"El caso ocurrió entre los años 2022 y 2023. Nuñes Pinheiro, un joven de 20 años de Eldorado, Misiones, llevó a cabo ataques conocidos como SIM swapping. La maniobra consistía en contactar a las empresas de telefonía celular haciéndose pasar por los titulares legítimos —entre ellos funcionarios públicos porteños— para pedir la reposición de un chip supuestamente extraviado o roto.*  
> *Para sortear las preguntas de seguridad de las operadoras, utilizaba datos personales que obtenía de diversas bases crediticias y públicas. Cuando la empresa habilitaba el nuevo chip en sus manos, la línea original de la víctima se quedaba inmediatamente sin señal.*  
> *Con la línea bajo su control, el atacante interceptaba los mensajes de texto con códigos de recuperación de WhatsApp y Telegram, tomando posesión de las cuentas por encargo de terceros anónimos que le pagaban en criptomonedas o billeteras virtuales. En la Ciudad de Buenos Aires, el caso concluyó con una condena firme de tres años de prisión en suspenso en juicio abreviado ante el Juzgado Penal N° 29. Ahora, Hugo continuará explicando las leyes que se aplicaron al caso."*

---

### BLOQUE 2: MARCO JURÍDICO APLICABLE
**Expositor:** Hugo Tcach  
**Tiempo:** 02:30 – 05:00 (2 minutos y 30 segundos)  
**Diapositiva:** 4

*(Diapositiva 4: Marco Jurídico Aplicable)*
> *"Gracias, Mateo. Al analizar jurídicamente lo ocurrido, encontramos un conjunto muy claro de normas del derecho penal argentino, principalmente a partir de la reforma de delitos informáticos de la Ley 26.388.*  
> *La figura central de la condena es el **Artículo 153 bis del Código Penal**, que sanciona el acceso ilegítimo a un sistema o dato informático de acceso restringido. Nuñes Pinheiro sabía que no tenía autorización para entrar a las cuentas de mensajería de las víctimas y utilizó ardides técnicos para sortear las barreras de autenticación.*  
> *A esto se suma el **Artículo 153**, que castiga la violación y el apoderamiento de comunicaciones electrónicas ajenas, y el **Artículo 197**, que reprime el entorpecimiento de los servicios de comunicación: al dar de baja la tarjeta SIM original, la víctima quedaba completamente incomunicada."*

*(Continúa en Diapositiva 4)*
> *"También analizamos si correspondía encuadrar el hecho como fraude informático bajo el artículo 173 inciso 16. Pero coincidimos con el criterio judicial: el fin de las maniobras no fue vaciar cuentas bancarias ni un desapoderamiento patrimonial directo, sino apoderarse de las comunicaciones privadas y documentos reservados.*  
> *En el plano constitucional, el **Artículo 18 de nuestra Constitución Nacional** es terminante: las comunicaciones y la correspondencia privada son inviolables. Interceptar mensajes de texto o chats sin una orden emitida por un juez competente constituye una violación gravísima a esta garantía.*  
> *Por último, la **Ley 25.326 de Protección de Datos Personales**, en su artículo 9, obliga a las empresas a adoptar medidas de seguridad técnicas y organizativas para que los datos no caigan en manos indebidas, un deber que las telefónicas incumplieron. Para conectar la investigación local con plataformas extranjeras como Telegram, resulta clave el **Convenio de Budapest**, aprobado por la Ley 27.411, que permite la conservación rápida de datos informáticos. Le doy paso a Farid para revisar los riesgos y nuestras medidas propuestas."*

---

### BLOQUE 3: MATRIZ DE RIESGOS Y MEDIDAS PROPUESTAS
**Expositor:** Farid Salomon  
**Tiempo:** 05:00 – 08:00 (3 minutos)  
**Diapositivas:** 5 y 6

*(Diapositiva 5: Matriz de Riesgos en tabla)*
> *"Gracias, Hugo. Como equipo de programación, construimos una matriz con siete riesgos principales, clasificándolos por probabilidad e impacto.*  
> *Los dos riesgos más críticos que detectamos son puramente técnicos:*  
> *El primero es la **reposición fraudulenta de tarjetas SIM** debido a validaciones débiles. Si una compañía entrega una línea solo respondiendo datos como el domicilio o la fecha de nacimiento —que son públicos o circulan en internet—, la probabilidad de fraude es altísima y el impacto es devastador.*  
> *El segundo riesgo crítico es **el uso del SMS como segundo factor de autenticación**. Los mensajes de texto no viajan cifrados y están atados al chip celular. Si clonan el chip, el atacante recibe el código en bandeja.*  
> *También priorizamos riesgos penales por el acceso a conversaciones, riesgos operativos por dejar incomunicada a la víctima, y el riesgo de que la prueba se anule en un juicio si no se cuida la cadena de custodia."*

*(Transición a Diapositiva 6: Medidas y Soluciones Propuestas)*
> *"Frente a estos riesgos, no planteamos soluciones complejas o inalcanzables, sino medidas realistas y básicas que cualquier sistema o empresa seria puede y debe implementar:*  
> *Primero, **verificación reforzada para reponer una SIM**. Las empresas deben terminar con los cuestionarios telefónicos fáciles: se debe exigir validación biométrica facial mediante la cámara del celular comparándola contra el DNI, o hacer el trámite presencial con documento físico.*  
> *Segundo, **aviso inmediato y ventana de espera**. Si alguien pide un chip nuevo, el sistema debe mandar de inmediato un correo al titular y una notificación en pantalla diciendo: 'Se pidió un chip nuevo; si no fuiste vos, hacé clic acá para frenarlo', dando un plazo de espera de un par de horas antes de cortar la línea.*  
> *Tercero, desde nuestro rol como desarrolladores de software, **debemos dejar de usar el SMS como único método de seguridad**. Es mucho más seguro implementar aplicaciones autenticadoras que generan códigos temporales en el propio teléfono y no dependen de la red celular.*  
> *Y cuarto, mantener **registros básicos e inalterables (logs)** que guarden quién autorizó el cambio, fecha, hora y desde qué dirección IP. Ahora Gonzalo explicará cómo se cuida la evidencia digital y las conclusiones del equipo."*

---

### BLOQUE 4: CADENA DE CUSTODIA, USO DE IA Y CONCLUSIONES
**Expositor:** Gonzalo Vega  
**Tiempo:** 08:00 – 10:30 (2 minutos y 30 segundos)  
**Diapositivas:** 7, 8, 9 y 10

*(Diapositiva 7: Uso Responsable y Trazable de IA)*
> *"Gracias, Farid. Para elaborar este trabajo utilizamos herramientas de Inteligencia Artificial generativa, pero con una regla estricta: ninguna afirmación legal ni dato del caso se dio por bueno sin verificarlo nosotros mismos contra las noticias reales y las leyes.*  
> *Por ejemplo, al inicio la IA sugería que el hacker había sido condenado por fraude informático y revelación de secretos; al contrastarlo con las notas de Infobae, Clarín y La Nación, descubrimos que eso no era exacto y lo corregimos de inmediato en nuestro informe y en la bitácora de trazabilidad."*

*(Transición a Diapositiva 8: Presentación de Evidencias y Cadena de Custodia)*
> *"En cuanto al manejo de la prueba digital, seguimos pautas muy claras: cuando se secuestra un celular encendido, no hay que ponerse a revisarlo ni abrir WhatsApp, porque se modifican archivos. Se debe colocar en modo avión o en una bolsa protectora para aislarlo de la red.*  
> *Nunca se trabaja sobre el archivo original: se hace una copia y se le calcula el código hash SHA-256. Ese código es una huella digital matemática: si alguien cambia una sola letra o espacio, el hash cambia por completo. Para demostrarlo en nuestros anexos, programamos un script simple en Python que calcula y guarda estos valores en un archivo de constancia. Todo esto se vuelca en un formulario de cadena de custodia donde consta quién entregó la prueba, quién la recibió y las firmas correspondientes."*

*(Transición a Diapositiva 9: Conclusiones y Rol Profesional)*
> *"Como conclusión de nuestro trabajo en equipo, este caso nos deja una enseñanza fundamental para nuestra carrera: la seguridad informática no es un agregado opcional, sino una obligación ética y profesional desde el primer día que diseñamos una base de datos o una pantalla de ingreso.*  
> *Los programadores tenemos acceso a información confidencial y a herramientas poderosas. Tenemos la responsabilidad de velar por la privacidad de las personas y de actuar siempre dentro del marco de la ley."*

*(Transición a Diapositiva 10: Recomendaciones Finales y Cierre)*
> *"Con esto cerramos nuestra exposición de la Comisión 5, esperando haber transmitido con claridad cómo la técnica informática y el derecho se complementan para prevenir incidentes y proteger la verdad en la justicia. Quedamos a disposición de los docentes para responder cualquier pregunta. Muchas gracias."*

---

## 3. Preguntas Probables del Docente y Respuestas Sugeridas

### Pregunta 1: *"¿Por qué afirman que el SMS no es un método seguro de segundo factor de autenticación?"*
* **Respuesta sugerida (a cargo de Farid o Mateo):**  
  *"El SMS viaja en texto plano a través de los protocolos de la red de telefonía celular y no está atado a la aplicación, sino a la tarjeta SIM física. Cuando un atacante realiza un SIM swapping y logra que la empresa active la línea en su propio chip, todos los mensajes de texto —incluyendo los códigos OTP de bancos, WhatsApp o correos— llegan a manos del atacante sin que la aplicación ni el usuario legítimo puedan impedirlo. Por eso es mucho más seguro usar aplicaciones autenticadoras de códigos temporales (TOTP) que funcionan localmente en el dispositivo."*

### Pregunta 2: *"Si el código hash cambia durante un procedimiento judicial, ¿la prueba queda automáticamente anulada?"*
* **Respuesta sugerida (a cargo de Gonzalo o Hugo):**  
  *"No necesariamente de forma automática, pero sí se abre una discusión procesal muy seria. El principio general es que la discrepancia en el hash hace presumir que el archivo fue modificado. Sin embargo, en la jurisprudencia argentina de la justicia porteña (como ocurrió en la Causa 41459/2019 de la Cámara PCyF), se determinó que si el cambio de hash se debió a un simple error involuntario de tipeo en el acta y la cadena de custodia física se mantuvo intacta y demostrable, la prueba no se anula. Pero la buena práctica pericial exige que el hash coincida bit a bit para no dejar dudas."*

### Pregunta 3: *"¿Qué diferencia existe entre la causa que resolvieron en la Ciudad de Buenos Aires y la causa federal que mencionaron?"*
* **Respuesta sugerida (a cargo de Mateo o Hugo):**  
  *"La jueza porteña María Araceli Martínez condenó a Nuñes Pinheiro en juicio abreviado únicamente por las maniobras concretas cometidas contra funcionarios de la Ciudad de Buenos Aires bajo la figura de acceso ilegítimo y entorpecimiento. Para no violar la garantía contra el doble juzgamiento (non bis in idem), la magistrada certificó que los hechos no se superpusieran con la causa que tramita en los tribunales federales de Comodoro Py, donde se investiga una presunta red mayor de espionaje que aún no tiene sentencia definitiva."*
