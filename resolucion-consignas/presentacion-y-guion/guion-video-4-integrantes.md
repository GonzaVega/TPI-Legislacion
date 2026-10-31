# GUION ESTRUCTURADO PARA PRESENTACIÓN EN VIDEO (4 INTEGRANTES)

> **Materia:** Legislación – Tecnicatura Universitaria en Programación (UTN)  
> **Eje Temático:** Eje 1 – Cibercrimen, evidencia digital y cadena de custodia  
> **Caso:** Elías Ezequiel Nuñes Pinheiro (SIM Swapping, Acceso Ilegítimo y Preservación de Evidencia Digital)  
> **Comisión:** Comisión 5  
> **Duración Total Estimada:** 10 minutos (~1.300 palabras habladas a un ritmo de ~130 palabras por minuto; dentro del rango de 8 a 12 minutos)  
> **Apoyo Visual:** Diapositivas del archivo `Presentacion_TPI_Eje1.pptx` (10 diapositivas alineadas bloque por bloque)

---

## 1. Tabla General de Tiempos, Diapositivas y Extensión

| Bloque | Integrante | Temas Asignados | Diapositivas | Palabras Aprox. | Tiempo Estimado |
|:---|:---|:---|:---|:---|:---|
| **Bloque 1** | **Mateo Serafini** | Apertura, presentación del equipo, resumen ejecutivo y hechos verificados del caso Nuñes Pinheiro (Etapa 1). | Diapositivas 1, 2 y 3 | ~325 palabras | **00:00 a 02:30 (2:30 min)** |
| **Bloque 2** | **Gonzalo Vega** | Marco jurídico aplicable: Ley 26.388 (arts. 153 bis, 153, 197 y 255 CP; figuras conexas arts. 157 bis y 173 inc. 16), Art. 18 CN, Ley 25.326 y Convenio de Budapest (Etapa 2). | Diapositiva 4 | ~325 palabras | **02:30 a 05:00 (2:30 min)** |
| **Bloque 3** | **Farid Salomon** | Matriz cualitativa de siete riesgos y medidas simples de prevención para sistemas y operadoras (Etapas 3 y 4). | Diapositivas 5 y 6 | ~325 palabras | **05:00 a 07:30 (2:30 min)** |
| **Bloque 4** | **Hugo Tcach** | Uso crítico y trazable de IA, protocolo de 5 pasos, modelos con datos ficticios y hash SHA-256, conclusiones profesionales y cierre (Etapas 4, 5 y 6). | Diapositivas 7, 8, 9 y 10 | ~330 palabras | **07:30 a 10:00 (2:30 min)** |

---

## 2. Guion Literal por Integrante

### BLOQUE 1: APERTURA Y PRESENTACIÓN DEL CASO
**Expositor:** Mateo Serafini  
**Tiempo:** 00:00 – 02:30 (2 minutos y 30 segundos)  
**Diapositivas:** 1, 2 y 3

*(Diapositiva 1: Portada)*
> *"Buenas tardes, profesores y compañeros. Somos el equipo de la Comisión 5, integrado por Hugo Tcach, Farid Salomon, Gonzalo Vega y quien les habla, Mateo Serafini. En este trabajo analizamos el caso real de Elías Ezequiel Nuñes Pinheiro, vinculado a maniobras de cambio no autorizado de tarjetas SIM, acceso ilegítimo a cuentas de mensajería y preservación de evidencia digital."*

*(Diapositiva 2: Contexto y Estructura del Análisis)*
> *"Como estudiantes de programación, elegimos este caso porque muestra que la seguridad informática no depende solo del código de una aplicación, sino también de cómo se valida la identidad de las personas y cómo se protegen sus datos. Organizamos el recorrido en seis etapas: hechos y alcance del caso, marco legal aplicable, matriz de riesgos, medidas y protocolos propuestos, uso crítico de inteligencia artificial y conclusiones profesionales."*

*(Diapositiva 3: Presentación del Caso Nuñes Pinheiro)*
> *"Los hechos ocurrieron en octubre de 2022 desde la ciudad de Eldorado, en la provincia de Misiones. Nuñes Pinheiro ejecutó ataques de SIM swapping contra el exministro de Seguridad porteño Marcelo D'Alessandro y, según informó el diario La Nación, también contra el entonces diputado Diego Santilli. Para lograrlo, primero obtenía datos personales de las víctimas —como el número de trámite del DNI— mediante consultas al RENAPER, a Nosis y al sitio Dark PFA. Con esos datos gestionaba de forma remota ante Movistar el cambio de chip, ya que la plataforma pedía únicamente número de línea, DNI y número de trámite, e insertaba una tarjeta SIM blanca comprada a la empresa Comtel. Al activarse el chip en Misiones, el titular quedaba sin señal y el atacante recibía los códigos de verificación para abrir WhatsApp y Telegram. Declaró ante la fiscal Daniela Dupuy que actuaba por encargo del usuario de Telegram 'ElJuanxd', cobrando entre doce mil y quince mil pesos por objetivo, y que luego quemó el celular y lo tiró al río Paraná. En la justicia porteña, la jueza María Araceli Martínez, del Juzgado Penal 29, homologó un acuerdo de juicio abreviado imponiéndole tres años de prisión en suspenso y ciento cincuenta horas de tareas comunitarias, mientras continúa en trámite una causa federal paralela en Comodoro Py. Le doy la palabra a Gonzalo para ver el marco legal."*

---

### BLOQUE 2: MARCO JURÍDICO APLICABLE
**Expositor:** Gonzalo Vega  
**Tiempo:** 02:30 – 05:00 (2 minutos y 30 segundos)  
**Diapositiva:** 4

*(Diapositiva 4: Marco Jurídico Aplicable)*
> *"Gracias, Mateo. Según informó Infobae, la condena en la justicia porteña fue por acceso ilegítimo a datos informáticos restringidos, sustracción de documento público y entorpecimiento de las comunicaciones, y según La Nación la destrucción del teléfono sumó una imputación por destrucción de medios de prueba. Como las notas periodísticas no citan números de artículo, desde el equipo realizamos la interpretación jurídica contrastando esos hechos con el Código Penal y la Ley 26.388.*  
> *En primer lugar, el **artículo 153 bis** reprime a quien, a sabiendas y sin autorización, acceda por cualquier medio a un sistema o dato informático de acceso restringido, con pena agravada cuando afecta a organismos o servicios públicos. Esto encuadra el ingreso no autorizado a las cuentas de mensajería y a los sistemas de consulta de datos.*  
> *En segundo lugar, el **artículo 153** sanciona abrir, desviar o interceptar comunicaciones electrónicas o telecomunicaciones ajenas, que es el efecto directo de desviar la línea celular para capturar mensajes.*  
> *En tercer lugar, el **artículo 197** castiga a quien interrumpiere o entorpeciere las comunicaciones telefónicas o de otra naturaleza, lo que ocurrió al dejar sin conectividad la tarjeta SIM original de la víctima.*  
> *Y en cuarto lugar, vinculamos el **artículo 255** tanto con la sustracción de documentos confiados a la custodia de un funcionario público como con la destrucción de objetos destinados a servir de prueba al haber quemado el teléfono.*  
> *Como análisis académico propio, distinguimos el **artículo 157 bis**, sobre acceso ilegítimo a bancos de datos personales, y explicamos por qué no se aplicó la defraudación informática del **artículo 173 inciso 16**: el ataque a las víctimas buscó controlar sus comunicaciones y no vaciar sus cuentas bancarias.*  
> *Todo esto se completa con el **artículo 18 de la Constitución Nacional** —que protege las comunicaciones privadas y la garantía contra el doble juzgamiento—, los **artículos 9 y 10 de la Ley 25.326** sobre seguridad y confidencialidad de datos personales, y el **Convenio de Budapest (Ley 27.411)** para preservar datos en plataformas extranjeras como Telegram. Ahora continúa Farid con los riesgos y las medidas propuestas."*

---

### BLOQUE 3: MATRIZ DE RIESGOS Y MEDIDAS DE PREVENCIÓN
**Expositor:** Farid Salomon  
**Tiempo:** 05:00 – 07:30 (2 minutos y 30 segundos)  
**Diapositivas:** 5 y 6

*(Diapositiva 5: Matriz de Riesgos)*
> *"Gracias, Gonzalo. A partir del caso armamos una matriz con siete riesgos evaluados de forma cualitativa por su probabilidad, impacto y criticidad.*  
> *Identificamos dos riesgos de nivel crítico. El primero es que se apruebe un cambio de tarjeta SIM pidiendo solo datos personales fáciles de conseguir, como el número de línea, el DNI y el número de trámite, lo que incumple el deber de seguridad del artículo 9 de la Ley 25.326.*  
> *El segundo riesgo crítico es usar mensajes de texto SMS como código de verificación: como el SMS llega al chip activo, quien logra duplicar la SIM recibe el código en su propio teléfono.*  
> *Luego ubicamos con criticidad alta el acceso indebido a cuentas de WhatsApp y Telegram —penado por los artículos 153 bis y 153 del Código Penal— y el riesgo procesal de que la evidencia digital pierda valor probatorio si falla la cadena de custodia.*  
> *Por último, con criticidad media analizamos la pérdida de señal del titular (artículo 197), la responsabilidad civil y administrativa de las empresas que no cuidan los datos de sus clientes, y el riesgo ético y penal para los programadores que participen en accesos no autorizados."*

*(Diapositiva 6: Medidas Simples de Prevención Propuestas)*
> *"Para mitigar estos riesgos proponemos cuatro medidas simples, concretas y aplicables sin depender de tecnología costosa:*  
> *Primero, sumar un paso adicional para aprobar un cambio de SIM: exigir el trámite presencial con DNI o una confirmación por otro canal que el titular ya tenga registrado, en lugar de validar solo con datos estáticos.*  
> *Segundo, enviar un aviso previo por correo electrónico o notificación cuando alguien solicita un nuevo chip y dar un tiempo prudencial para que el titular pueda frenar el trámite antes de que se dé de baja su tarjeta SIM.*  
> *Tercero, al desarrollar aplicaciones, dejar de depender del SMS y ofrecer aplicaciones autenticadoras de códigos temporales, además de activar el PIN de verificación en dos pasos propio de WhatsApp y Telegram.*  
> *Y cuarto, guardar registros básicos de actividad con fecha, hora, dirección IP y quién autorizó cada cambio. Le paso la palabra a Hugo para explicar el protocolo de evidencia digital, el uso de IA y las conclusiones."*

---

### BLOQUE 4: USO DE IA, EVIDENCIA DIGITAL Y CONCLUSIONES
**Expositor:** Hugo Tcach  
**Tiempo:** 07:30 – 10:00 (2 minutos y 30 segundos)  
**Diapositivas:** 7, 8, 9 y 10

*(Diapositiva 7: Etapa 5 – Uso Responsable y Trazable de IA)*
> *"Gracias, Farid. En la etapa cinco documentamos el uso de inteligencia artificial. Utilizamos Gemini para borradores, código y maquetación, y Claude Sonnet para planificar y auditar la veracidad del trabajo. La revisión fue clave porque detectó que en los primeros borradores la IA había inventado enlaces, fechas de octubre de 2023 y datos de secuestro que no existían. Por eso abrimos y leímos las nueve notas periodísticas reales, guardamos sus textos completos en los anexos y separamos con claridad los datos confirmados, los reportados por un solo medio y las interpretaciones propias."*

*(Diapositiva 8: Etapa 4 – Protocolo de Evidencia Digital y Modelos de Práctica)*
> *"En cuanto al manejo de la prueba digital, tomando como base la norma ISO/IEC 27037 y el protocolo de la Resolución 232/2023, armamos una guía básica de cinco pasos:*  
> *Uno, identificar y anotar los dispositivos o archivos con su serie o IMEI. Dos, aislar: dejar apagado lo que esté apagado y, si hay un celular encendido, ponerlo en modo avión sin revisarlo. Tres, copiar: trabajar siempre sobre una copia y guardar el original sin tocar. Cuatro, calcular el código hash SHA-256 del original y de la copia para comprobar que no cambiaron ni una sola letra. Y cinco, registrar cada entrega con fecha, hora y firmas en la cadena de custodia, dejando constancia escrita si se corrige algún error material, tal como analizó la Sala Tercera de la Cámara Penal porteña en su fallo de octubre de 2021.*  
> *Como en el caso real el imputado destruyó su teléfono y no hay actas públicas del expediente, en nuestros anexos incluimos un archivo de registro ficticio de práctica, calculamos su hash real con nuestro script en Python y completamos sobre ese ejemplo los modelos de cadena de custodia e informe técnico."*

*(Diapositiva 9: Conclusiones y Rol Profesional del Programador)*
> *"Como conclusión, este caso nos enseña que los programadores debemos diseñar la autenticación pensando en la seguridad desde el inicio, generar registros confiables en los sistemas, cuidar la integridad de la prueba digital y actuar con responsabilidad ética y apego a la ley."*

*(Diapositiva 10: Cierre de la Presentación)*
> *"Con esto finalizamos la presentación del equipo de la Comisión 5. Muchas gracias por su atención."*
