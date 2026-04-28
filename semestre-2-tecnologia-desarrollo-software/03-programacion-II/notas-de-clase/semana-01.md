# Materia - Semana XX: Titulo del Tema

**Fecha:** 07/04/2026
**Profesor:** Ceider Zambrano
**Tema:** Odoo historia, conceptos y arquitectura

---

## Objetivos de la clase
- Objetivo Describir historia y evolucion
analizzaarla arquitectura y sus capaps principales
Relacionar conceptos fundamentales de poo


## Notas
Base Tecnica
Clases y objetos
Herencia y polimorfismo 
Estructuras de datos

odo es un erp enterprise resource planning
modulos prestablecidos
tiene core open source
usuario administrador o SU

TinyERP
Creado en 2005 por un estudiante fabien pinckaers. Crea un script para comptri contra sap

OpenERP
Madurez del software en 2009. Adopcion masia por la comun opensource

Odoo
A partir del 2014
Forma un ecosistema moderno mas alla de ERP clasico(eCommerce, CMS) y cosolidacion como framework.

Arquitectura
3 Capas (Tier Architecture)

Cpa de datos PostgreSQL
Capa de presentacion (Cliente web)
Renderizado HTML/JS/CSS en el navegador del usuario final.

Capa Logica(Servidor odoo / python)
El motor donde viven sus clases lagoritmos y reglas de negocios

Capa de Datos

Patron MVC adaptado en Odoo


ORM object-Relational Mapping
es una tecnica y herramienta de sofweare q permite interactuar on bases de datos relacionales

Anatomia interna de un modulo
manifest - models- views - security

_manifest_.py
es un json con nombre, version summary, depends y otros campos como metadatos.

Vistas
archivos .xml
define la arquitectura visual
Conexion directa: los campls xml solo funcionan si ya han sido definidos  logicamente en los modulos

Reglas de acceso en security
Mediante archivos .xml o .csv
implementacion CRUD

Ciclo de vida del desarrollo
Paso 1: declarar en _manifest_.py definir la identidad
Paso 2: COnstruir Lgica en models( Programar clases en Python)
Paso3 Asignar permisos en /security(definir acceso CRUD en CSV)
Paso 4: Dise;ar Interfaz en /views (estructurar el UI en XML).
Paso 5 Ejectuar (Reiniciar servidor actualizar modulo, vizualizar en navegador)

owl odomate
### Subtema 1


### Subtema 2


## Codigo / Ejemplos vistos en clase

```
// Codigo aqui
```

## Dudas pendientes
- Duda 1
- Duda 2

## Relacion con otras materias
- **[Materia]:** [Como se conecta]

## Tarea / Actividades pendientes
- [ ] Actividad 1 - Fecha limite: DD/MM/AAAA

## Resumen en mis propias palabras
> Escribe aqui un resumen breve.


