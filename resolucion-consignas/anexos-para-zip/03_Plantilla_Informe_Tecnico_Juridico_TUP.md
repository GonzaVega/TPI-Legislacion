# MODELO DE INFORME TÉCNICO-JURÍDICO PARA EL PROGRAMADOR (TUP)

> **Materia:** Legislación – Tecnicatura Universitaria en Programación (UTN)  
> **Destinatario:** Autoridades judiciales, directores de tecnología o clientes corporativos.  
> **Estructura:** Diseñada según las buenas prácticas periciales para documentar hallazgos informáticos de manera ordenada, objetiva y verificable.

---

### INFORME TÉCNICO PERICIAL DE PARTE

**A la Autoridad Judicial Interviniente / A quien corresponda:**

#### 1. Identificación del Profesional Interviniente
* **Profesional:** Gonzalo Vega (en equipo con Mateo Serafini, Hugo Tcach y Farid Salomon).
* **Título / Rol:** Técnico Universitario en Programación (TUP) – Consultor Técnico de Parte.
* **Causa / Expediente de Referencia:** Causa N° 29/2023 ("Nuñes Pinheiro s/ Delitos Informáticos").
* **Fecha de Emisión del Informe:** 30 de octubre de 2026.

#### 2. Objeto del Examen Técnico
El presente informe tiene por objeto examinar la copia forense del archivo de registro de autenticaciones y conexiones (`auth_access_log.txt`) correspondiente al período 10 al 15 de marzo de 2023, con la finalidad de:
1. Constatar la existencia de accesos o solicitudes de cambio de SIM desde direcciones IP no habituales.
2. Verificar la integridad de los datos digitales analizados.
3. Determinar los factores técnicos que posibilitaron la interrupción del servicio legítimo.

#### 3. Origen y Resguardo de la Evidencia Analizada
* **Origen de los datos:** Servidor de aprovisionamiento de líneas de telecomunicaciones y registro de eventos de la plataforma de autogestión.
* **Forma de obtención:** Copia digital extraída mediante procedimiento forense bajo cadena de custodia (Faja N° 00812).
* **Medida de preservación:** Trabajo realizado sobre una copia lógica de trabajo, manteniéndose el soporte original bajo depósito judicial.

#### 4. Verificación de Integridad (Código Hash)
Antes de proceder al análisis y al finalizar el mismo, se verificó el código hash SHA-256 del archivo examinado:
* **Archivo Analizado:** `auth_access_log.txt` (Tamaño: 14.280.912 bytes).
* **Hash SHA-256 Obtenido:**  
  `a6c5b9e2810f3c5d88921a44e7892b1156ca0198273645bcae981245009123fe`
* **Resultado:** Coincidencia exacta con el valor consignado en el acta de recepción judicial, acreditando que el contenido se mantuvo íntegro y sin alteraciones.

#### 5. Metodología y Procedimiento Empleado
Se utilizó un entorno de análisis aislado sin conexión a redes externas. Se procesaron las líneas de texto mediante scripts de filtrado y búsqueda de patrones de direcciones IP, números de línea y marcas de tiempo (timestamps).

#### 6. Hallazgos Relevantes (Observación Objetiva)
1. **Línea objetivo:** 011-4589-XXXX.
2. **Evento crítico:** El día 12 de marzo de 2023 a las 14:18:22 UTC se registró una solicitud web de reposición de chip SIM ingresada desde la dirección IP `181.44.120.XX` (geolocalizada en el rango asignado a la provincia de Misiones).
3. **Mecanismo de validación:** El sistema aprobó la reposición tras recibir respuestas coincidentes sobre número de trámite de DNI y domicilio anterior, sin requerir validación biométrica ni confirmación previa por correo electrónico alternativo.
4. **Desconexión:** A las 14:19:05 UTC, el chip original de la víctima quedó registrado como "baja por reemplazo", perdiendo conexión a la red celular.
5. **Captura de código:** A las 14:21:40 UTC, el sistema despachó un mensaje SMS con código de verificación de 6 dígitos hacia el nuevo chip activado, confirmándose la conexión a una antena celular de la localidad de Eldorado.

#### 7. Conclusión Técnico-Jurídica
1. **Integridad probatoria:** La evidencia examinada cumple con los requisitos de origen conocido, trazabilidad documentada e integridad verificada mediante hash SHA-256.
2. **Causa técnica del incidente:** El acceso ilegítimo a la línea telefónica y posterior toma de control de las aplicaciones de mensajería fue posible debido a la debilidad del mecanismo de validación de identidad para el reemplazo de SIM y a la fragilidad intrínseca del SMS como método de autenticación.
3. **Recomendación pericial:** Se sugiere la preservación preventiva de los registros de tráfico de las direcciones IP involucradas conforme a los mecanismos de cooperación rápida previstos en la legislación vigente.

---

**Firma del Profesional:**  
Gonzalo Vega – Técnico Universitario en Programación (UTN)  
En representación del equipo de consultoría técnica (Comisión 5).
