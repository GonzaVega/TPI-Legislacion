# MATRIZ DE RIESGOS LEGALES, TÉCNICOS Y DE CUMPLIMIENTO

> **Caso:** Elías Ezequiel Nuñes Pinheiro – SIM swapping y acceso ilegítimo  
> **Autores:** Mateo Serafini, Hugo Tcach, Farid Salomon, Gonzalo Vega (Comisión 5)  
> **Materia:** Legislación – Tecnicatura Universitaria en Programación (UTN)  
> **Formato:** este documento y la planilla `04_Matriz_Riesgos.xlsx`.  
> **Nota sobre los niveles:** probabilidad, impacto y criticidad son una valoración cualitativa hecha por el equipo; no se calculan con ninguna fórmula. Las marcas [F#] remiten a las notas listadas en `08_Fuentes_Caso.md`.

---

| ID | Riesgo detectado | Tipo | Norma o principio vinculado | Probabilidad | Impacto | Criticidad | Medida propuesta |
|:---|:---|:---|:---|:---|:---|:---|:---|
| **R1** | Cambio de SIM aprobado con datos personales fáciles de conseguir. En el caso, la plataforma pedía número de línea, DNI y número de trámite [F4, F7]. | Técnico / Operativo | Ley 25.326 (art. 9) | Alta | Muy alto | **Crítica** | Pedir un paso más de verificación: trámite presencial con DNI o confirmación por otro canal ya registrado del titular. |
| **R2** | Códigos de verificación por SMS: los recibe quien tenga la SIM, aunque no sea el titular. | Técnico / Seguridad | Ley 25.326 (art. 9) y buenas prácticas de seguridad | Alta | Muy alto | **Crítica** | Ofrecer una app autenticadora de códigos (TOTP) u otro método que no dependa del SMS. |
| **R3** | Acceso indebido a cuentas de mensajería (WhatsApp, Telegram) y a conversaciones privadas [F1]. | Penal | Código Penal, arts. 153 bis y 153 | Alta | Alto | **Alta** | Activar la verificación en dos pasos con PIN propio de la aplicación, independiente de la línea. |
| **R4** | Pérdida de señal del titular al darse de baja su SIM [F1]. | Operativo / Penal | Código Penal, art. 197 | Alta | Medio | **Media** | Avisar por correo o notificación y dar un tiempo para frenar el trámite antes de dar de baja la SIM. |
| **R5** | Pérdida de valor de la prueba digital por fallas en la cadena de custodia. | Procesal / Legal | Art. 18 CN, ISO/IEC 27037 y jurisprudencia de la Cámara PCyF CABA (Sala III, 05/10/2021) | Media | Muy alto | **Alta** | Aplicar el protocolo de 5 pasos: aislar, copiar, calcular hash SHA-256 y registrar la custodia. |
| **R6** | Responsabilidad de la empresa por no cuidar los datos personales de sus clientes. | Administrativo / Civil | Ley 25.326 (arts. 9 y 31) | Alta | Medio | **Media** | Registrar quién autorizó cada cambio de SIM, con fecha, hora y dirección IP. |
| **R7** | Riesgo ético y penal para programadores que participen en accesos no autorizados. | Ético / Penal | Código Penal, art. 153 bis | Media | Alto | **Media** | Formarse en ética y legislación, no vender credenciales ni acceder sin autorización y rechazar pedidos dudosos. |
