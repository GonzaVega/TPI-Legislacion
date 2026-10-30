# FORMULARIO DE REGISTRO Y CADENA DE CUSTODIA DE EVIDENCIA DIGITAL

> **Materia:** Legislación – Tecnicatura Universitaria en Programación (UTN)  
> **Modelo Estándar:** Documento de acompañamiento físico y lógico de evidencias digitales.

---

## 1. Datos Generales de la Causa o Incidente
* **Número de Expediente / Causa:** Causa N° 29/2023 - Juzgado PCyF N° 29 CABA
* **Carátula:** Averiguación de ilícito s/ Acceso ilegítimo y SIM Swapping
* **Fecha y Hora del Procedimiento Inicial:** 15 de marzo de 2023 – 10:15 hs.
* **Lugar del Secuestro:** Domicilio en calle Los Cedros N° 450, Eldorado, Provincia de Misiones.
* **Autoridad Judicial Interviniente:** Juzgado de 1ª Instancia en lo PCyF N° 29 de CABA.

---

## 2. Descripción e Individualización del Elemento Secuestrado
* **Ítem N°:** 01
* **Tipo de Elemento:** Teléfono Celular Inteligente (Smartphone) con tarjeta SIM.
* **Marca y Modelo:** Samsung Galaxy A52 (SM-A525M).
* **Número de Serie / IMEI:** IMEI 1: 358912093847120 / IMEI 2: 358912093847121.
* **Color y Estado Físico:** Color negro, pantalla sana sin astilladuras visibles, con funda plástica transparente.
* **Tarjeta SIM incorporada:** Empresa Personal / Telecom, N° de serie de chip impreso: `895432019283746501`.
* **Estado al Secuestro:** Encendido. Se procedió de inmediato a activar "Modo Avión" en presencia de testigos y se colocó en sobre antiestático con faja de seguridad N° 00812.

---

## 3. Verificación de Integridad Lógica (Cálculo de Hash)
* **Archivo / Imagen Generada:** `evidencia_item01_extraccion_logica.raw`
* **Tamaño del Archivo:** 4.294.967.296 bytes (4,00 GB).
* **Algoritmo Utilizado:** SHA-256 (Secure Hash Algorithm 256 bits).
* **Valor Hash Calculado:**  
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
* **Herramienta Empleada:** Script oficial en Python `05_calcular_hashes.py` ejecutado en consola pericial.

---

## 4. Registro Cronológico de Movimientos y Custodia

| Fecha y Hora | Responsable que Entrega | Responsable que Recibe | Motivo del Traslado / Operación | Firma Entrega | Firma Recepción |
|:---|:---|:---|:---|:---|:---|
| 15/03/2023 - 11:30 hs | Of. Ayte. Lucas Gómez (Policía actuante) | Sargento 1° Carlos Benítez (Traslado de Efectos) | Traslado desde lugar de allanamiento hacia sede policial central. | [Firma] | [Firma] |
| 15/03/2023 - 16:00 hs | Sargento 1° Carlos Benítez (Traslado de Efectos) | Lic. María Ramos (Laboratorio Forense Oficial) | Ingreso a depósito judicial para peritaje de volcado lógico de memoria. | [Firma] | [Firma] |
| 18/03/2023 - 09:15 hs | Lic. María Ramos (Laboratorio Forense) | TUP Gonzalo Vega (Consultor Técnico / Perito de Parte) | Examen conjunto y verificación de coincidencia del código hash SHA-256. | [Firma] | [Firma] |
| 18/03/2023 - 13:00 hs | TUP Gonzalo Vega (Consultor Técnico) | Lic. María Ramos (Laboratorio Forense) | Devolución de la pieza íntegra al depósito judicial cerrado. | [Firma] | [Firma] |

---

## 5. Observaciones Finales
La faja de seguridad N° 00812 se mantuvo intacta durante todo el procedimiento. El código hash calculado al inicio coincidió bit a bit con el calculado al finalizar la revisión técnica, acreditando que la evidencia no sufrió ninguna alteración.
