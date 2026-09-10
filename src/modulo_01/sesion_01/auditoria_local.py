"""
==============================================================================
COURSE: Python for Defensive Security: Fundamentals and Local Lab Tooling
REPOSITORY: python-defensive-security | Session 01 (PyDefSec)
FILE: auditoria_local.py
PURPOSE: Plantilla de inicio para el Reto Autónomo de Auditoría Local.
SCOPE: Entorno de pruebas autorizado en localhost (127.0.0.1) únicamente.
==============================================================================

INSTRUCCIONES PARA EL ESTUDIANTE:
    En este reto construirá su primera herramienta autónoma de auditoría defensiva.
    Este script se ejecuta de manera secuencial (de arriba hacia abajo).
    No requiere definir funciones complejas; todo el flujo se procesa paso a paso.

    Complete cada una de las secciones marcadas con '# TODO:' modificando los
    valores de prueba con sus datos reales o verificando la telemetría obtenida.

    Para ejecutar este script dentro de su entorno virtual activo (.venv):
        python auditoria_local.py
    o desde la raíz del repositorio:
        python src/modulo_01/sesion_01/auditoria_local.py

    Verifique que en la consola se imprima el reporte tabular con la identidad
    del analista, telemetría de la máquina, validación de Python 3.13 y el
    compromiso de confinamiento ético en localhost.
"""

# ==============================================================================
# IMPORTACIÓN DE MÓDULOS DE LA BIBLIOTECA ESTÁNDAR
# ==============================================================================
# En Python, los módulos son archivos con código predefinido que podemos reutilizar.
#
# 'import sys' e 'import platform':
# Importan el módulo completo. Para usar sus herramientas escribimos el nombre
# del módulo seguido de un punto (ejemplo: sys.version_info o platform.system()).
#
# 'from datetime import datetime':
# Importa únicamente la clase 'datetime' desde el módulo 'datetime'. Esto nos
# permite escribir directamente datetime.now() en lugar de datetime.datetime.now().

import sys
import platform
from datetime import datetime


# ==============================================================================
# --- PASO 1: Identidad del Analista Responsable ---
# ==============================================================================
# Asignamos cadenas de texto (tipo str) a variables para documentar quién es el
# operador autorizado responsable de ejecutar esta auditoría defensiva.
#
# TODO 1.1: Reemplace el texto entre comillas con su nombre completo.
# TODO 1.2: Ingrese su identificador institucional o matrícula académica.
# TODO 1.3: Personalice su rol operativo de seguridad defensiva si lo desea.

estudiante = "ANALISTA EN ENTRENAMIENTO"          # TODO: Reemplace con su nombre
matricula_id = "DEF-2026-09"                     # TODO: Reemplace con su matrícula o ID
rol_defensivo = "Auditor Defensivo Nivel 1"      # TODO: Ajuste su rol asignado


# ==============================================================================
# --- PASO 2: Telemetría de la Máquina ---
# ==============================================================================
# En ciberseguridad defensiva, la telemetría es la recolección automática de datos
# sobre el estado y características del sistema anfitrión (host).
#
# TODO 2.1: platform.system() retorna el nombre del SO (Linux, Darwin para macOS, Windows).
# TODO 2.2: platform.release() retorna la versión específica del núcleo (kernel).
# TODO 2.3: platform.machine() retorna la arquitectura del procesador (x86_64, arm64, etc.).
# TODO 2.4: datetime.now().strftime(...) obtiene la fecha y hora actual formateada.

os_sistema = platform.system()
os_release = platform.release()
os_arquitectura = platform.machine()
timestamp_auditoria = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Combinamos el nombre del sistema operativo y la arquitectura en un solo texto
info_sistema = f"{os_sistema} ({os_arquitectura})"


# ==============================================================================
# --- PASO 3: Validación de Python 3.13 y Aislamiento ---
# ==============================================================================
# Todo entorno defensivo profesional debe certificar la versión del lenguaje y el
# aislamiento de dependencias para garantizar reproducibilidad y evitar daños
# al sistema operativo principal.
#
# sys.version_info contiene información detallada sobre la versión del intérprete:
# - sys.version_info.major: Versión principal (debe ser 3)
# - sys.version_info.minor: Versión secundaria (debe ser 13)
# - sys.version_info.micro: Versión de parche (ejemplo: 0)

version_actual = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
ruta_interprete = sys.executable

# TODO 3.1: Comprobar mediante una expresión booleana si la versión es exactamente 3.13.
#           El operador 'and' exige que ambas condiciones sean verdaderas simultáneamente.
es_version_valida = sys.version_info.major == 3 and sys.version_info.minor == 13

# TODO 3.2: Evaluar la conformidad con una estructura condicional if / else.
if es_version_valida:
    estado_conformidad = "[APROBADO: Estándar Python 3.13 activo]"
else:
    estado_conformidad = f"[FALLO: Versión no autorizada ({version_actual})]"

# TODO 3.3: Verificar el aislamiento del entorno.
#           Comprobamos si la subcadena '.venv' está presente en la ruta del ejecutable.
if ".venv" in ruta_interprete:
    estado_aislamiento = "Aislado (.venv activo)"
else:
    estado_aislamiento = "ADVERTENCIA: Fuera de .venv"


# ==============================================================================
# --- PASO 4: Reporte en Consola con f-strings ---
# ==============================================================================
# Mostramos los resultados en la terminal dentro de un recuadro estructurado en ASCII.
# Las f-strings (f"...") nos permiten insertar variables directamente dentro del texto.
# La sintaxis {:<49} alinea el contenido a la izquierda ocupando un espacio fijo de
# 49 caracteres, garantizando que el borde derecho de la tabla quede recto.
#
# TODO 4.1: Examine cada print() y ejecute el archivo para verificar que el recuadro
#           tabular se imprima de forma clara con la declaración ética de localhost.

borde = "+-----------------------------------------------------------------------------+"

print(borde)
print("| REPORTE DE TELEMETRÍA Y AUDITORÍA DE ENTORNO LOCAL DEFENSIVO                |")
print(borde)
print(f"| Analista Responsable    : {estudiante:<49} |")
print(f"| Credencial / ID         : {matricula_id:<49} |")
print(f"| Rol Técnico             : {rol_defensivo:<49} |")
print(f"| Timestamp de Auditoría  : {timestamp_auditoria:<49} |")
print(f"| Sistema Operativo       : {info_sistema:<49} |")
print(f"| Versión Kernel          : {os_release:<49} |")
print(f"| Versión de Python       : {version_actual:<49} |")
print(f"| Estado de Conformidad   : {estado_conformidad:<49} |")
print(f"| Estado de Aislamiento   : {estado_aislamiento:<49} |")
print(f"| Ruta del Ejecutable     : {ruta_interprete:<49} |")
print(borde)
print("| DECLARACIÓN: Operación confinada a localhost (127.0.0.1). Sin red externa.  |")
print(borde)
