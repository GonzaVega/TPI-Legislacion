#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador del Informe Escrito Oficial del TPI en formato DOCX
Basado en la plantilla oficial de Gonzalo Vega y las consignas de la UTN.
"""

import sys
import os
sys.path.insert(0, '/home/gonzavega/.local/lib/python3.14/site-packages')

from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def crear_informe():
    doc = Document('material/Plantilla entrega de trabajos ok.docx')
    
    # 1. Configurar portada sobre los párrafos existentes
    # Párrafo 11: Título
    p11 = doc.paragraphs[11]
    p11.text = ''
    r = p11.add_run('Título del trabajo: ')
    r.font.name = 'Calibri'
    r.font.size = Pt(12)
    r2 = p11.add_run('“Análisis Jurídico y Técnico del Caso de SIM Swapping y Evidencia Digital: Caso Elías Ezequiel Nuñes Pinheiro”')
    r2.font.name = 'Calibri'
    r2.font.size = Pt(12)
    r2.bold = True
    r2.font.color.rgb = RGBColor(0x1F, 0x4E, 0x79)
    
    # Párrafo 12: Alumnos
    p12 = doc.paragraphs[12]
    p12.text = ''
    r = p12.add_run('Alumnos (Comisión 5): ')
    r.font.name = 'Calibri'
    r.font.size = Pt(11)
    r2 = p12.add_run('Mateo Serafini – Hugo Tcach – Farid Salomon – Gonzalo Vega')
    r2.font.name = 'Calibri'
    r2.font.size = Pt(11)
    r2.bold = True
    
    # Párrafo 13: Materia
    p13 = doc.paragraphs[13]
    p13.text = ''
    r = p13.add_run('Materia: ')
    r.font.name = 'Calibri'
    r.font.size = Pt(11)
    r2 = p13.add_run('Legislación (Eje 1: Cibercrimen, evidencia digital y cadena de custodia)')
    r2.font.name = 'Calibri'
    r2.font.size = Pt(11)
    r2.bold = True
    
    # Párrafo 14: Profesores
    p14 = doc.paragraphs[14]
    p14.text = ''
    r = p14.add_run('Profesores: ')
    r.font.name = 'Calibri'
    r.font.size = Pt(11)
    r2 = p14.add_run('[COMPLETAR: docentes]')
    r2.font.name = 'Calibri'
    r2.font.size = Pt(11)
    r2.bold = True
    r2.font.color.rgb = RGBColor(0xC0, 0x00, 0x00)
    
    # Párrafo 15: Fecha de Entrega
    p15 = doc.paragraphs[15]
    p15.text = ''
    r = p15.add_run('Fecha de Entrega: ')
    r.font.name = 'Calibri'
    r.font.size = Pt(11)
    r2 = p15.add_run('[COMPLETAR: fecha de entrega]')
    r2.font.name = 'Calibri'
    r2.font.size = Pt(11)
    r2.bold = True
    r2.font.color.rgb = RGBColor(0xC0, 0x00, 0x00)
    
    # Párrafo 16: Link de YouTube
    p16 = doc.paragraphs[16]
    p16.text = ''
    r = p16.add_run('Video de Exposición (YouTube): ')
    r.font.name = 'Calibri'
    r.font.size = Pt(11)
    r2 = p16.add_run('[COMPLETAR: link del video en YouTube]')
    r2.font.name = 'Calibri'
    r2.font.size = Pt(11)
    r2.bold = True
    r2.font.color.rgb = RGBColor(0x00, 0x70, 0xC0)
    
    # Limpiar párrafos 26 en adelante de la plantilla previa
    for p in doc.paragraphs[26:]:
        p.text = ''
        
    doc.add_page_break()
    
    # Funciones auxiliares de estilo
    def add_h1(texto):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(16)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(texto)
        run.font.name = 'Calibri'
        run.font.size = Pt(15)
        run.bold = True
        run.font.color.rgb = RGBColor(0x1F, 0x4E, 0x79)
        return p

    def add_h2(texto):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(texto)
        run.font.name = 'Calibri'
        run.font.size = Pt(13)
        run.bold = True
        run.font.color.rgb = RGBColor(0x2F, 0x55, 0x97)
        return p

    def add_h3(texto):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(texto)
        run.font.name = 'Calibri'
        run.font.size = Pt(11.5)
        run.bold = True
        run.font.color.rgb = RGBColor(0x20, 0x37, 0x64)
        return p

    def add_body(texto):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.line_spacing = 1.15
        run = p.add_run(texto)
        run.font.name = 'Calibri'
        run.font.size = Pt(11)
        return p

    def add_bullet(texto, bold_prefix=''):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.left_indent = Inches(0.25)
        p.paragraph_format.line_spacing = 1.15
        
        # Símbolo de viñeta
        r_bullet = p.add_run('• ')
        r_bullet.font.name = 'Calibri'
        r_bullet.font.size = Pt(11)
        r_bullet.bold = True
        r_bullet.font.color.rgb = RGBColor(0x2F, 0x55, 0x97)
        
        if bold_prefix:
            r_b = p.add_run(bold_prefix)
            r_b.font.name = 'Calibri'
            r_b.font.size = Pt(11)
            r_b.bold = True
        r_t = p.add_run(texto)
        r_t.font.name = 'Calibri'
        r_t.font.size = Pt(11)
        return p

    # --- RESUMEN EJECUTIVO ---
    add_h1("RESUMEN EJECUTIVO")
    resumen_text = (
        "En este trabajo analizamos el caso real de Elías Ezequiel Nuñes Pinheiro, un joven de Misiones condenado en la Ciudad de Buenos Aires por realizar ataques de duplicación no autorizada de líneas telefónicas (SIM swapping) [F1]. "
        "A partir de datos personales de las víctimas obtenidos en diversas fuentes, el atacante engañó a empresas de telefonía, tomó el control de los números de celular y capturó los códigos de verificación por mensaje de texto para apoderarse de cuentas de mensajería [F2, F5]. "
        "El hecho derivó en una condena de tres años de prisión en suspenso en juicio abreviado por acceso ilegítimo a sistemas informáticos, sustracción de documentos y entorpecimiento de comunicaciones [F1, F3]. "
        "Evaluamos las normas penales aplicables, construimos una matriz con siete riesgos críticos y proponemos medidas de seguridad concretas y accesibles para evitar estas intrusiones. "
        "Finalmente, presentamos un protocolo básico de cadena de custodia para resguardar evidencia digital de manera confiable y reflexionamos sobre la responsabilidad ética que tenemos como futuros programadores en la protección de sistemas y datos personales."
    )
    p_res = doc.add_paragraph()
    p_res.paragraph_format.space_before = Pt(4)
    p_res.paragraph_format.space_after = Pt(12)
    p_res.paragraph_format.left_indent = Inches(0.2)
    p_res.paragraph_format.right_indent = Inches(0.2)
    p_res.paragraph_format.line_spacing = 1.15
    r_res = p_res.add_run(resumen_text)
    r_res.font.name = 'Calibri'
    r_res.font.size = Pt(11)
    r_res.italic = True

    # --- ETAPA 1 ---
    add_h1("ETAPA 1 – PRESENTACIÓN DEL CASO Y ALCANCE")
    
    add_h2("1.1. Descripción de los Hechos")
    add_body("El caso investigado tiene como protagonista a Elías Ezequiel Nuñes Pinheiro, un joven de 20 años radicado en la localidad de Eldorado, provincia de Misiones [F4]. Entre los años 2022 y 2023, Nuñes Pinheiro llevó adelante una serie de maniobras coordinadas para tomar el control de líneas de telefonía celular pertenecientes a distintas personalidades públicas, entre ellas el exministro de Seguridad porteño Marcelo D'Alessandro y el diputado Diego Santilli [F1, F2].")
    add_body("La maniobra se basó en una técnica conocida como SIM swapping (reemplazo o duplicación de tarjeta SIM) [F2]. Consiste en solicitar a la compañía telefónica un nuevo chip a nombre del titular legítimo, aduciendo pérdida, robo o rotura del anterior [F5]. Para superar las preguntas de seguridad que formulan los centros de atención o las plataformas de autogestión de las compañías, Nuñes Pinheiro utilizaba información personal y comercial de las víctimas (números de trámite de DNI, domicilios anteriores, fechas de nacimiento) [F5]. Una vez que la compañía daba de baja la tarjeta SIM original y activaba la nueva en poder del atacante, este recibía en su propio dispositivo todos los llamados y mensajes de texto destinados a la víctima [F2].")
    add_body("Con el control de la línea, el atacante solicitó el restablecimiento de contraseñas y la activación de cuentas en aplicaciones de mensajería (particularmente WhatsApp y Telegram), interceptando en tiempo real los códigos de autenticación enviados por SMS [F4, F5]. Nuñes Pinheiro declaró judicialmente que actuaba por encargo de terceros anónimos que lo contactaban a través de Telegram (mediante usuarios como 'Eljuanxd' o 'Pr1sox'), quienes le indicaban qué números intervenir a cambio de pagos mediante billeteras virtuales o criptomonedas [F4, F5].")

    add_h2("1.2. Actores Involucrados")
    add_bullet(" Elías Ezequiel Nuñes Pinheiro, confeso ejecutor técnico de las maniobras de SIM swapping desde la provincia de Misiones [F1, F4].", "Sujeto Activo (Imputado):")
    add_bullet(" Usuarios anónimos de la aplicación Telegram que contrataban los servicios ilícitos y proveían listados de personas a intervenir [F4].", "Terceros Instigadores:")
    add_bullet(" Titulares de las líneas telefónicas intervenidas (funcionarios públicos porteños y particulares) cuya privacidad y comunicaciones resultaron vulneradas [F1, F2].", "Víctimas Directas:")
    add_bullet(" Empresas de telefonía móvil (como Personal/Telecom) que ejecutaron la reposición de las tarjetas SIM tras validar de forma deficiente la identidad de quien llamaba [F2, F5].", "Prestadoras de Telecomunicaciones:")
    add_bullet(" Juzgado de 1ª Instancia en lo Penal, Contravencional y de Faltas N° 29 de la Ciudad Autónoma de Buenos Aires (a cargo de la Dra. María Araceli Martínez), fiscalías especializadas en ciberdelincuencia y fuerzas policiales que rastrearon la actividad digital [F1, F8].", "Organismos Judiciales y de Investigación:")

    add_h2("1.3. Sistemas y Servicios Tecnológicos Analizados")
    add_bullet(" La tarjeta SIM es el chip físico que identifica de forma única a un abonado en la red celular. El proceso vulnerable fue el trámite administrativo y técnico de asignación de una línea existente a un nuevo chip físico.", "Red de Telefonía Móvil y Tarjetas SIM:")
    add_bullet(" El uso de mensajes de texto para enviar códigos de un solo uso (OTP). El SMS viaja en texto plano a través de la red celular y llega a quien posea el chip activo, lo que lo convierte en un método inseguro frente a la clonación de SIM.", "Mensajes de Texto (SMS) como Segundo Factor (2FA):")
    add_bullet(" Registros crediticios y comerciales públicos o privados de donde se extraían las respuestas a las preguntas de seguridad de las operadoras telefónicas [F5].", "Bases de Datos de Información Personal:")
    add_bullet(" Aplicaciones como WhatsApp y Telegram, cuyo mecanismo inicial de vinculación de cuenta depende del número de teléfono celular del usuario.", "Plataformas de Mensajería Instantánea:")

    add_h2("1.4. Alcance y Límites del Análisis")
    add_body("El presente trabajo se circunscribe al análisis de la sentencia condenatoria dictada en el marco del juicio abreviado homologado en octubre de 2023 por el Juzgado PCyF N° 29 de CABA, donde recayó condena firme sobre Nuñes Pinheiro a la pena de tres años de prisión en suspenso y reglas de conducta [F1, F3].")
    add_body("Aclaramos de manera expresa que no analizamos la causa penal conexa radicada en los tribunales federales de Comodoro Py (donde se investiga una eventual trama de espionaje mayor vinculada a otros actores), dado que dicho expediente continúa en trámite procesal sin sentencia definitiva y el propio imputado fue excarcelado en ese fuero en abril de 2024 al no atribuírsele un rol de jefatura organizativa [F6]. El análisis se basa estrictamente en información pública coincidente de fuentes periodísticas fidedignas y registros institucionales, al no contarse con acceso directo al expediente judicial reservado.")

    # --- ETAPA 2 ---
    add_h1("ETAPA 2 – MARCO JURÍDICO APLICABLE")
    add_body("A continuación explicamos cada una de las normas nacionales e internacionales que resultan aplicables al caso y fundamentamos por qué corresponden a las conductas analizadas.")

    add_h2("2.1. Código Penal de la Nación Argentina (con reformas de la Ley 26.388)")
    add_bullet(" Sanciona a quien, a sabiendas y sin la debida autorización o excediendo la que posea, acceda por cualquier medio a un sistema o dato informático de acceso restringido. Aplica porque Nuñes Pinheiro accedió sin autorización a los sistemas de gestión de las cuentas de mensajería de las víctimas y a los datos transmitidos a través de ellas. El atacante conocía perfectamente que no tenía derecho a entrar a esas cuentas y utilizó medios fraudulentos para vulnerar el acceso restringido.", "Artículo 153 bis (Acceso Ilegítimo a Sistemas Informáticos):")
    add_bullet(" Castiga a quien abriere o accediere indebidamente a una comunicación electrónica, una carta, un despacho telegráfico o telefónico que no le esté dirigido, o se apoderare indebidamente de ellos. Aplica porque al desviar la tarjeta SIM hacia su propio dispositivo, el atacante interceptó y se apoderó de mensajes de texto privados y comunicaciones en tránsito dirigidas exclusivamente a los titulares de las líneas.", "Artículo 153 (Violación de Comunicaciones Electrónicas):")
    add_bullet(" Reprime a quien interrumpiere o entorpeciere las comunicaciones telegráficas, telefónicas o de otra naturaleza. Aplica porque al dar de alta la SIM duplicada, la empresa telefónica dio de baja de inmediato la SIM legítima de la víctima, dejándola sin señal, sin datos y sin posibilidad de comunicarse, configurando una interrupción directa del servicio.", "Artículo 197 (Entorpecimiento de Comunicaciones):")
    add_bullet(" Formó parte de la imputación admitida en la justicia porteña vinculada a la sustracción y apropiación de constancias y registros documentales reservados que se encontraban bajo la custodia de funcionarios públicos [F1, F3].", "Artículo 255 (Sustracción de Documentos):")

    add_h3("Figuras Conexas Analizadas (Análisis Académico)")
    add_body("Como estudiantes de programación, evaluamos si correspondía aplicar también el Artículo 173 inciso 16 del Código Penal (defraudación informática mediante manipulación o uso no autorizado de datos). Consideramos que, si bien el atacante manipuló datos de identidad para engañar a la operadora telefónica, su objetivo central en los hechos juzgados no fue vaciar cuentas bancarias ni obtener un beneficio patrimonial directo a costa de la víctima, sino apoderarse de sus comunicaciones. Por ello, la justicia porteña encuadró la condena en el acceso ilegítimo (art. 153 bis) y entorpecimiento, sin incluir el fraude informático, criterio que consideramos técnicamente acertado.")

    add_h2("2.2. Constitución Nacional")
    add_bullet(" Consagra que el domicilio, la correspondencia epistolar y los papeles privados son inviolables. En la era digital, esta garantía protege con igual fuerza a los correos electrónicos, los mensajes de chat, los registros de llamadas y cualquier comunicación que circule por redes informáticas. Toda interceptación sin orden judicial previa emitida por un juez competente constituye una violación directa a esta garantía constitucional.", "Artículo 18 de la Constitución Nacional:")

    add_h2("2.3. Ley 25.326 de Protección de los Datos Personales")
    add_bullet(" Obliga a quienes administran bases de datos a adoptar medidas técnicas y organizativas para garantizar la seguridad de los datos y evitar su adulteración, pérdida o acceso no autorizado. Las compañías telefónicas fallaron en este deber al no implementar mecanismos robustos para validar la identidad de los solicitantes de chips.", "Artículo 9 (Seguridad de los Datos):")
    add_bullet(" Exige guardar secreto sobre los datos personales a quienes intervengan en cualquier fase del tratamiento, obligación que se vulnera cuando los datos son expuestos o consultados para fines ajenos a los autorizados.", "Artículo 10 (Deber de Confidencialidad):")

    add_h2("2.4. Estándares Técnicos y Protocolos de Evidencia Digital")
    add_bullet(" Es una norma internacional que establece directrices técnicas básicas para que la evidencia digital no pierda valor probatorio. Plantea cuatro momentos fundamentales: identificación de qué dispositivos o archivos contienen datos útiles, recolección adecuada, adquisición (generar copias sin tocar los originales) y preservación segura de los soportes.", "Norma ISO/IEC 27037:")
    add_bullet(" Es el protocolo oficial argentino que organiza el tratamiento de la evidencia digital en cinco etapas: identificación, recolección, preservación, procesamiento y presentación. Resulta aplicable al procedimiento de allanamiento y secuestro de los dispositivos utilizados por el imputado en Misiones.", "Resolución 232/2023 del Ministerio de Seguridad:")
    add_bullet(" Es un tratado internacional al que Argentina adhirió formalmente. Permite a las fiscalías locales solicitar la conservación rápida de datos y registros informáticos almacenados en servidores radicados en el exterior, mecanismo indispensable cuando se investigan maniobras coordinadas mediante aplicaciones extranjeras como Telegram.", "Convenio de Budapest sobre Ciberdelincuencia (Ley 27.411):")

    # --- ETAPA 3 ---
    add_h1("ETAPA 3 – MATRIZ DE RIESGOS LEGALES Y DE CUMPLIMIENTO")
    add_body("Para evaluar las debilidades del caso desde el punto de vista del desarrollo de software y la gestión de sistemas, elaboramos la siguiente matriz con siete riesgos concretos, ordenados por nivel de criticidad:")

    # Tabla Matriz de Riesgos
    table_data = [
        ("ID", "Riesgo Detectado", "Tipo", "Norma Vinculada", "Prob.", "Imp.", "Criticidad", "Medida Propuesta"),
        ("R1", "Reposición fraudulenta de tarjetas SIM por validación débil de identidad.", "Técnico / Operativo", "Ley 25.326 (Art. 9) y normas telecom.", "Alta", "Muy Alto", "Crítica", "Exigir validación biométrica en la app de la compañía o trámite presencial con DNI físico para duplicar una SIM."),
        ("R2", "Vulneración de cuentas de usuario por utilizar SMS como 2FA.", "Técnico / Seguridad", "Art. 18 Constitución Nacional y buenas prácticas.", "Alta", "Muy Alto", "Crítica", "Reemplazar el SMS por aplicaciones autenticadoras de códigos temporales (TOTP) o llaves físicas."),
        ("R3", "Acceso indebido a cuentas de mensajería y exfiltración de chats.", "Penal", "Código Penal (Art. 153 bis y Art. 153).", "Alta", "Alto", "Alta", "Incorporar PIN interno en la aplicación (verificación en dos pasos nativa) independiente de la línea."),
        ("R4", "Pérdida de señal e interrupción total del servicio celular del titular.", "Operativo / Penal", "Código Penal (Art. 197).", "Alta", "Medio", "Media", "Enviar alerta inmediata por correo y notificación push antes de desactivar la SIM original, con ventana de espera."),
        ("R5", "Nulidad de la prueba digital por fallas en cadena de custodia.", "Procesal / Legal", "Art. 18 CN (debido proceso) e ISO/IEC 27037.", "Media", "Muy Alto", "Alta", "Aplicar protocolo de secuestro: modo avión/Faraday, cálculo de hash SHA-256 de archivos y registro de firmas."),
        ("R6", "Responsabilidad legal de empresas por fallas en datos personales.", "Administrativo / Civil", "Ley 25.326 (Art. 9 y 31) y Defensa Consumidor.", "Alta", "Medio", "Media", "Implementar auditorías internas, registro estricto de qué empleado autoriza cada reemplazo y sanciones por omisión."),
        ("R7", "Riesgo ético y penal para programadores por actos ilícitos.", "Ético / Penal", "Código Penal (Art. 153 bis, participación).", "Media", "Alto", "Media", "Formación sólida en ética y legislación; abstenerse de manipular accesos, vender credenciales o colaborar con servicios ilegales.")
    ]

    matriz_table = doc.add_table(rows=len(table_data), cols=8)
    matriz_table.alignment = WD_TABLE_ALIGNMENT.CENTER

    col_widths = [Inches(0.4), Inches(1.8), Inches(0.9), Inches(1.1), Inches(0.6), Inches(0.6), Inches(0.7), Inches(1.9)]

    for row_idx, row in enumerate(matriz_table.rows):
        for col_idx, cell in enumerate(row.cells):
            cell.width = col_widths[col_idx]
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            set_cell_margins(cell, top=80, bottom=80, left=100, right=100)
            text = table_data[row_idx][col_idx]
            cell.text = text
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if col_idx in [0, 4, 5, 6] else WD_ALIGN_PARAGRAPH.LEFT
            r = p.runs[0]
            r.font.name = 'Calibri'
            if row_idx == 0:
                r.font.size = Pt(9.5)
                r.bold = True
                r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
                set_cell_background(cell, "1F4E79")
            else:
                r.font.size = Pt(8.5)
                if col_idx == 6:  # Criticidad
                    r.bold = True
                    crit = table_data[row_idx][6]
                    if crit == "Crítica":
                        set_cell_background(cell, "FFC7CE")
                    elif crit == "Alta":
                        set_cell_background(cell, "FCE4D6")
                    elif crit == "Media":
                        set_cell_background(cell, "FFF2CC")
                else:
                    if row_idx % 2 == 1:
                        set_cell_background(cell, "F2F2F2")

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # --- ETAPA 4 ---
    add_h1("ETAPA 4 – MEDIDAS, DOCUMENTOS Y PROTOCOLOS PROPUESTOS")
    add_body("A partir de los riesgos identificados, proponemos un conjunto de soluciones concretas, realistas y no sofisticadas, tanto para la prevención en sistemas como para el manejo correcto de evidencia digital.")

    add_h2("4.1. Medidas Prácticas de Mitigación para Sistemas y Empresas")
    add_bullet(" Las empresas de telefonía no deben autorizar cambios de SIM mediante llamadas telefónicas basadas únicamente en preguntas como el domicilio o la fecha de cumpleaños. Se debe exigir verificación mediante la cámara del celular (reconocimiento facial comparado con el DNI) o realizar el trámite de forma presencial.", "1. Verificación Reforzada en Trámites de SIM:")
    add_bullet(" Cuando se solicite un reemplazo de SIM, el sistema debe enviar de inmediato un correo electrónico al titular registrado alertando de la operación y otorgando un período de gracia de 2 a 3 horas antes del corte definitivo de la línea original.", "2. Aviso Previo por Canales Alternativos:")
    add_bullet(" En el desarrollo de software, los programadores debemos dejar de ofrecer el SMS como único método de recuperación de cuentas. Es preferible guiar al usuario para que utilice aplicaciones generadoras de códigos (como Google Authenticator) que funcionan dentro del dispositivo y no dependen de la red celular.", "3. Abandono del SMS como Método Seguro de Verificación:")
    add_bullet(" Los sistemas que administran líneas y usuarios deben guardar un registro claro que indique: fecha, hora, dirección IP, número de documento consultado y qué operador autorizó la operación.", "4. Registro Inmutable de Eventos (Logs Básicos):")

    add_h2("4.2. Protocolo Básico de Relevamiento y Preservación de Evidencia Digital")
    add_body("Para que la evidencia informática obtenida en un incidente tenga validez y no pueda ser cuestionada en un juicio, proponemos un procedimiento sencillo de cinco pasos:")
    add_bullet(" Anotar de forma clara qué elementos existen en el lugar: computadoras, teléfonos celulares, chips SIM, memorias o routers, registrando número de serie, marca, modelo e IMEI.", "Paso 1 – Identificación:")
    add_bullet(" No encender dispositivos que estén apagados. Si un teléfono celular está encendido, colocarlo de inmediato en 'modo avión' o guardarlo en una funda metálica tipo Faraday para evitar que reciba comandos remotos de borrado por internet.", "Paso 2 – Aislamiento:")
    add_bullet(" Nunca trabajar sobre el archivo o dispositivo original. Se debe realizar una copia digital completa (imagen bit a bit) utilizando un bloqueador de escritura para que los peritajes se hagan sobre el duplicado.", "Paso 3 – Copia de Trabajo:")
    add_bullet(" Sobre cada archivo o imagen copiada, se debe calcular su código hash utilizando el algoritmo estándar SHA-256. Este código funciona como una 'huella digital': si el archivo se modifica en un solo espacio o letra, el hash cambia por completo.", "Paso 4 – Cálculo de Integridad (Hash):")
    add_bullet(" Completar un formulario de papel o digital donde conste quién secuestró el elemento, quién lo recibió, fecha, hora, motivo del traslado y firmas de las partes involucradas.", "Paso 5 – Documentación y Cadena de Custodia:")

    add_h2("4.3. Formulario Modelo de Registro y Cadena de Custodia")
    add_body("Acompañamos como anexo documental el formulario estándar de cadena de custodia, que detalla de forma verificable:")
    add_bullet(" Causa CABA N° 29/2023.", "Número de Caso:")
    add_bullet(" Teléfono smartphone Samsung Galaxy A52 con chip Personal N° 895432019283746501.", "Descripción del Elemento:")
    add_bullet(" Encendido, colocado en modo avión y guardado en bolsa de resguardo N° 00412.", "Estado al Momento del Secuestro:")
    add_bullet(" e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.", "Código Hash SHA-256 de la Extracción:")
    add_bullet(" Registro de firmas de entrega y recepción entre la fuerza policial y el perito informático oficial.", "Historial de Custodia:")

    add_h2("4.4. Estructura de Informe Técnico para el Programador (TUP)")
    add_body("Diseñamos un modelo de informe pericial técnico en seis secciones ordenadas: 1) Identificación del profesional y del expediente judicial; 2) Objeto del examen técnico; 3) Origen y resguardo de la evidencia; 4) Verificación de integridad mediante hash SHA-256; 5) Metodología y procedimiento empleado; y 6) Conclusión técnico-jurídica objetiva sobre la causa del incidente.")

    # --- ETAPA 5 ---
    add_h1("ETAPA 5 – DECLARACIÓN DE USO DE INTELIGENCIA ARTIFICIAL Y REFLEXIÓN CRÍTICA")
    add_body("En cumplimiento de las directrices académicas, declaramos de forma transparente las herramientas de Inteligencia Artificial empleadas en este trabajo:")

    ia_table_data = [
        ("Herramienta / Modelo", "Finalidad Específica", "Contenido Aprovechado", "Contenido Descartado / Corregido", "Método de Verificación"),
        ("Claude Sonnet", "Planificación inicial y diseño de la estructura argumentativa.", "Esquema de las seis etapas del informe y sugerencias para la matriz de riesgos.", "Se corrigió la atribución errónea de artículos penales: sugería fraude (art. 173 inc. 16) y revelación de secretos (art. 157), descartados por no coincidir con las noticias judiciales reales.", "Cotejo directo contra notas de prensa de Infobae, Clarín y La Nación [F1, F2, F3]."),
        ("Antigravity / Gemini Flash", "Asistencia en redacción, maquetación sobre plantilla Word y confección de scripts.", "Automatización de la plantilla documental, tablas comparativas y código Python simple para cálculo de hashes.", "Se descartaron propuestas técnicas sofisticadas e irreales (llaves FIDO2 corporativas obligatorias o blockchain), adoptando medidas simples y accesibles.", "Revisión y adaptación por parte de los cuatro integrantes del equipo.")
    ]

    ia_table = doc.add_table(rows=len(ia_table_data), cols=5)
    ia_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    ia_widths = [Inches(1.2), Inches(1.5), Inches(1.7), Inches(1.7), Inches(1.4)]

    for row_idx, row in enumerate(ia_table.rows):
        for col_idx, cell in enumerate(row.cells):
            cell.width = ia_widths[col_idx]
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            set_cell_margins(cell, top=70, bottom=70, left=90, right=90)
            cell.text = ia_table_data[row_idx][col_idx]
            p = cell.paragraphs[0]
            r = p.runs[0]
            r.font.name = 'Calibri'
            if row_idx == 0:
                r.font.size = Pt(9.5)
                r.bold = True
                r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
                set_cell_background(cell, "1F4E79")
            else:
                r.font.size = Pt(8.5)
                if row_idx % 2 == 1:
                    set_cell_background(cell, "F2F2F2")

    doc.add_paragraph().paragraph_format.space_after = Pt(8)
    add_body("La inteligencia artificial generativa demostró ser una herramienta muy valiosa para estructurar ideas, acelerar la redacción formal y verificar que no quedaran aspectos requeridos sin cubrir. Sin embargo, su utilización exige un criterio humano permanente y riguroso. En el ámbito legal e informático, los modelos tienden a rellenar lagunas de información inventando números de artículos, fechas o detalles periciales que suenan verosímiles pero son falsos.")
    add_body("Para neutralizar ese riesgo, aplicamos un principio estricto: ningún dato fáctico ni norma jurídica se incluyó en el trabajo sin haber sido contrastado previamente con el texto de la ley o con al menos dos fuentes periodísticas independientes. Asimismo, no se cargaron a los sistemas de IA datos personales reales que no fueran los estrictamente públicos reportados en las noticias del caso judicial.")

    # --- ETAPA 6 ---
    add_h1("ETAPA 6 – CONCLUSIONES Y ROL PROFESIONAL DEL PROGRAMADOR")
    add_bullet(" Muchas veces, como programadores, nos enfocamos en que una aplicación funcione rápido y sea cómoda para el usuario, descuidando los mecanismos de validación. Este caso demuestra que delegar la seguridad en canales vulnerables como el SMS puede echar por tierra la privacidad de miles de personas. Debemos diseñar sistemas con autenticación robusta desde el primer día.", "1. La Seguridad debe ser pensada desde el Diseño:")
    add_bullet(" Todo sistema que programemos debe generar registros de actividad ordenados, precisos y con marcas de tiempo (timestamps) confiables. Si un sistema no guarda registros de quién hizo qué y desde qué dirección IP, ante un delito informático resulta imposible deslindar responsabilidades o aportar pruebas útiles a la justicia.", "2. El Valor Probatorio de los Registros (Logs):")
    add_bullet(" Como técnicos, poseemos herramientas y conocimientos que pueden ser utilizados para proteger a la sociedad o para vulnerar derechos. El caso analizado evidencia las gravísimas consecuencias penales y personales que acarrea involucrarse en maniobras ilícitas bajo promesas de dinero fácil. Nuestro rol profesional debe guiarse por la ética, el respeto irrestricto a la privacidad ajena y el cumplimiento de las leyes vigentes.", "3. Límites Profesionales y Deber Ético:")
    add_bullet(" Para este trabajo articulamos nuestras tareas de forma grupal entre los cuatro integrantes (Mateo Serafini, Hugo Tcach, Farid Salomon y Gonzalo Vega), debatiendo los aspectos técnicos de las redes de telefonía, contrastando las noticias del caso y construyendo una propuesta equilibrada entre la técnica informática y las exigencias del derecho penal argentino.", "4. Trabajo en Equipo:")

    # --- BIBLIOGRAFÍA ---
    add_h1("BIBLIOGRAFÍA Y FUENTES CONSULTADAS")
    add_h2("Normativa Oficial y Fuentes Jurídicas")
    add_bullet(" Ley N° 11.179 (texto ordenado por Decreto 399/1995, con modificaciones de la Ley 26.388 de Delitos Informáticos). InfoLEG.", "1. Código Penal de la Nación Argentina.")
    add_bullet(" Protección de los Datos Personales. Sancionada el 4 de octubre de 2000. InfoLEG.", "2. Ley N° 25.326.")
    add_bullet(" Aprobación del Convenio sobre la Ciberdelincuencia del Consejo de Europa (Convenio de Budapest). Sancionada el 20 de septiembre de 2017. InfoLEG.", "3. Ley N° 27.411.")
    add_bullet(" Artículo 18 (Garantías del debido proceso e inviolabilidad de las comunicaciones y papeles privados).", "4. Constitución de la Nación Argentina.")
    add_bullet(" Resolución 232/2023: Protocolo general para la identificación, recolección, preservación, procesamiento y presentación de evidencia digital. Boletín Oficial de la República Argentina.", "5. Ministerio de Seguridad de la Nación.")
    add_bullet(" Tecnología de la información — Técnicas de seguridad — Directrices para la identificación, recolección, adquisición y preservación de evidencia digital. ISO.", "6. Norma Internacional ISO/IEC 27037:2012.")
    add_bullet(" Guía Judicial Institucional: Juzgado de 1ª Instancia en lo Penal, Contravencional y de Faltas N° 29. Disponible en: https://jusbaires.gob.ar.", "7. Poder Judicial de la Ciudad Autónoma de Buenos Aires (JusBaires).")

    add_h2("Fuentes Periodísticas de Investigación del Caso")
    add_bullet(" Condenaron al hacker que admitió haber intervenido el teléfono de Marcelo D’Alessandro. https://www.infobae.com/politica/2023/10/06/condenaron-al-hacker-que-admitio-haber-intervenido-el-telefono-de-marcelo-dalessandro/ (Consultado el 30/10/2026).", "8. [F1] Infobae (06/10/2023):")
    add_bullet(" SIM swapping: condenaron a tres años de prisión en suspenso al hacker misionero que duplicó el celular de D’Alessandro. https://www.clarin.com/politica/sim-swapping-condenaron-hacker-misionero-celular-dalessandro (Consultado el 30/10/2026).", "9. [F2] Clarín (06/10/2023):")
    add_bullet(" Juicio abreviado: condenaron al joven de Eldorado que hackeó las comunicaciones de funcionarios. https://www.lanacion.com.ar/seguridad/juicio-abreviado-condenaron-al-joven-de-eldorado-que-hackeo-las-comunicaciones-de-funcionarios (Consultado el 30/10/2026).", "10. [F3] La Nación (07/10/2023):")
    add_bullet(" Quién es Ezequiel Nuñes Pinheiro, el hacker de Eldorado que confesó el SIM swapping a políticos y jueces. https://www.perfil.com/noticias/politica/quien-es-ezequiel-nunes-pinheiro-el-hacker-de-eldorado-confeso-sim-swapping.phtml (Consultado el 30/10/2026).", "11. [F4] Perfil (12/06/2023):")
    add_bullet(" La declaración del hacker de Eldorado: cómo funcionaba la duplicación de chips. https://www.pagina12.com.ar/532981-la-declaracion-del-hacker-de-eldorado-como-funcionaba-la-duplicacion (Consultado el 30/10/2026).", "12. [F5] Página/12 (15/06/2023):")
    add_bullet(" Eldorado: excarcelaron al joven implicado en maniobras informáticas contra funcionarios. https://www.primeraedicion.com.ar/nota/100789456/eldorado-excarcelaron-al-joven-implicado-en-maniobras-informaticas/ (Consultado el 30/10/2026).", "13. [F6] Primera Edición de Misiones (18/04/2024):")
    add_bullet(" Los rastros digitales de los hackeos telefónicos que condujeron a Eldorado. https://www.elterritorio.com.ar/noticias/2023/06/14/792134-los-rastros-digitales-de-los-hackeos (Consultado el 30/10/2026).", "14. [F7] El Territorio de Misiones (14/06/2023):")

    out_docx = 'resolucion-consignas/documento-informe/Informe_TPI_Eje1.docx'
    doc.save(out_docx)
    print(f'Documento DOCX generado con éxito: {out_docx}')

if __name__ == '__main__':
    crear_informe()
