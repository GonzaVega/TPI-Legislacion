# PROTOCOLO BÁSICO DE RELEVAMIENTO, PRESERVACIÓN Y DOCUMENTACIÓN DE EVIDENCIA DIGITAL

> **Materia:** Legislación – Tecnicatura Universitaria en Programación (UTN)  
> **Equipo:** Mateo Serafini, Hugo Tcach, Farid Salomon, Gonzalo Vega (Comisión 5)  
> **Finalidad:** Establecer una guía práctica de pasos claros y secuenciales para el tratamiento de evidencia digital en incidentes informáticos, evitando nulidades procesales o pérdida de valor probatorio.

---

## 1. Principio Fundamental
En informática forense y evidencia digital existe una regla de oro: **nunca se trabaja ni se experimenta sobre la evidencia original**. Toda revisión, búsqueda de patrones o análisis técnico debe realizarse sobre una copia idéntica verificada mediante código hash.

---

## 2. Secuencia de Trabajo en Cinco Pasos

### Paso 1: Identificación y Registro Inicial
* Identificar visualmente todos los elementos con capacidad de almacenamiento o comunicación presentes en el lugar: computadoras, notebooks, teléfonos celulares, chips SIM, discos externos, pendrives y routers.
* Registrar de inmediato en la planilla de inventario: marca, modelo, número de serie, dirección MAC o código IMEI según corresponda.
* Tomar fotografías generales y en detalle del estado en que se encuentran los equipos antes de tocarlos.

### Paso 2: Aislamiento Físico y de Red
* **Dispositivos apagados:** Deben permanecer apagados. Nunca deben encenderse para "ver qué tienen adentro", ya que el propio sistema operativo altera miles de registros de fecha y hora al iniciar.
* **Teléfonos celulares encendidos:**
  1. No intentar desbloquearlos ingresando patrones al azar.
  2. Colocarlos de inmediato en "modo avión" para cortar la conexión a la red celular y Wi-Fi.
  3. Si no es posible activar el modo avión, apagar el equipo o introducirlo dentro de una bolsa o caja metálica de aislamiento (tipo Faraday).
  4. Esto impide que el dispositivo reciba mensajes nuevos o que un atacante envíe una orden remota de borrado de fábrica por internet.

### Paso 3: Generación de Copia de Trabajo (Adquisición)
* Conectar el medio de almacenamiento original a una computadora de peritaje utilizando un dispositivo bloqueador de escritura (*write blocker*) para asegurar que ningún bit del original pueda ser modificado.
* Generar una imagen digital bit a bit (duplicado exacto) del disco, memoria o archivo que se necesita analizar.
* El medio original se guarda bajo custodia segura y todo el trabajo de análisis pericial se realiza exclusivamente sobre la copia generada.

### Paso 4: Cálculo y Verificación de Integridad (Código Hash)
* Apenas finalizada la copia, se calcula su código hash utilizando el algoritmo estándar **SHA-256**.
* El código hash obtenido es una cadena alfanumérica única (una huella digital matemática).
* Se calcula también el hash sobre el soporte original. Si ambos códigos coinciden exactamente, queda demostrado que la copia es idéntica al original y no sufrió ninguna alteración.
* Este valor se deja asentado de inmediato en el acta con fecha, hora y firma.

### Paso 5: Registro de Cadena de Custodia y Resguardo
* Todo elemento físico se coloca en una bolsa de seguridad numerada, cerrada con faja y firmada por los intervinientes.
* Cada vez que la evidencia se traslada de un lugar a otro o cambia de responsable (por ejemplo, del oficial policial al perito informático), se completa el formulario de cadena de custodia indicando fecha, hora, motivo y firmas.
