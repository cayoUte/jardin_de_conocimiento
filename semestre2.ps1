# ============================================================
# setup-semestre2.ps1
# Uso: Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
#      .\semestre2.ps1
# ============================================================

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

Write-Host "`n========================================================" -ForegroundColor Cyan
Write-Host "  Creando estructura del repositorio - Semestre 2..." -ForegroundColor Cyan
Write-Host "========================================================`n" -ForegroundColor Cyan

# --- Directorio raiz ---
$ROOT = "semestre-2-tecnologia-desarrollo-software"
New-Item -ItemType Directory -Force -Path $ROOT | Out-Null
Set-Location $ROOT
[System.Environment]::CurrentDirectory = (Get-Location).Path    # <-- AGREGA ESTA
git init

# --- Carpetas base ---
New-Item -ItemType Directory -Force -Path "reviews" | Out-Null
New-Item -ItemType Directory -Force -Path "_templates" | Out-Null

# ============================================================
# MATERIAS Y SUS CARPETAS
# ============================================================
$estructura = @{
    "01-base-de-datos-I" = @(
        "notas-de-clase",
        "conceptos-clave",
        "ejercicios/en-clase",
        "ejercicios/independientes",
        "cheatsheets",
        "recursos",
        "proyectos",
        "scripts-sql/ddl",
        "scripts-sql/dml",
        "scripts-sql/consultas-utiles",
        "scripts-sql/procedimientos-funciones",
        "diagramas"
    )
    "02-estadistica-II-bi-bigdata" = @(
        "notas-de-clase",
        "conceptos-clave",
        "ejercicios/en-clase",
        "ejercicios/independientes",
        "cheatsheets",
        "recursos",
        "proyectos",
        "notebooks",
        "datasets",
        "scripts/python",
        "scripts/r",
        "scripts/excel"
    )
    "03-programacion-II" = @(
        "notas-de-clase",
        "conceptos-clave",
        "ejercicios/en-clase",
        "ejercicios/independientes",
        "ejercicios/retos-logica",
        "cheatsheets",
        "recursos",
        "proyectos",
        "codigo/snippets",
        "codigo/ejemplos-clase",
        "codigo/mini-proyectos"
    )
    "04-metodologia-desarrollo-software" = @(
        "notas-de-clase",
        "conceptos-clave",
        "ejercicios/en-clase",
        "ejercicios/independientes",
        "cheatsheets",
        "recursos",
        "proyectos",
        "diagramas/casos-de-uso",
        "diagramas/diagramas-clase",
        "diagramas/diagramas-secuencia",
        "diagramas/diagramas-actividad",
        "plantillas"
    )
    "05-redes-y-telecomunicaciones" = @(
        "notas-de-clase",
        "conceptos-clave",
        "ejercicios/en-clase",
        "ejercicios/independientes",
        "ejercicios/subnetting",
        "cheatsheets",
        "recursos",
        "proyectos",
        "laboratorios/packet-tracer",
        "laboratorios/wireshark",
        "laboratorios/comandos-red",
        "diagramas"
    )
    "06-arquitectura-de-computadores" = @(
        "notas-de-clase",
        "conceptos-clave",
        "ejercicios/en-clase",
        "ejercicios/independientes",
        "ejercicios/conversiones-numericas",
        "cheatsheets",
        "recursos",
        "proyectos",
        "simulaciones"
    )
}

# --- Crear directorios ---
$contador = 1
foreach ($materia in ($estructura.Keys | Sort-Object)) {
    Write-Host "[$contador/6] Creando: $materia/" -ForegroundColor Yellow
    foreach ($sub in $estructura[$materia]) {
        $path = Join-Path $materia $sub
        New-Item -ItemType Directory -Force -Path $path | Out-Null
        Set-Content -Path (Join-Path $path ".gitkeep") -Value "" -Encoding UTF8
    }
    $contador++
}

# ============================================================
# FUNCION HELPER PARA ESCRIBIR ARCHIVOS
# ============================================================
function Write-File {
    param(
        [string]$Path,
        [string[]]$Lines
    )
    $content = $Lines -join "`n"
    [System.IO.File]::WriteAllText($Path, $content, [System.Text.Encoding]::UTF8)
}

# ============================================================
# TEMPLATES
# ============================================================
Write-Host "`nCreando templates..." -ForegroundColor Yellow

# --- Template: Notas de clase ---
Write-File -Path "_templates/template-notas-clase.md" -Lines @(
    "# Materia - Semana XX: Titulo del Tema",
    "",
    "**Fecha:** DD/MM/AAAA",
    "**Profesor:** [Nombre]",
    "**Tema:** [Tema principal]",
    "",
    "---",
    "",
    "## Objetivos de la clase",
    "- Objetivo 1",
    "- Objetivo 2",
    "",
    "## Notas",
    "",
    "### Subtema 1",
    "",
    "",
    "### Subtema 2",
    "",
    "",
    "## Codigo / Ejemplos vistos en clase",
    "",
    "``````",
    "// Codigo aqui",
    "``````",
    "",
    "## Dudas pendientes",
    "- Duda 1",
    "- Duda 2",
    "",
    "## Relacion con otras materias",
    "- **[Materia]:** [Como se conecta]",
    "",
    "## Tarea / Actividades pendientes",
    "- [ ] Actividad 1 - Fecha limite: DD/MM/AAAA",
    "",
    "## Resumen en mis propias palabras",
    "> Escribe aqui un resumen breve."
)

# --- Template: Concepto clave ---
Write-File -Path "_templates/template-concepto-clave.md" -Lines @(
    "# Nombre del Concepto",
    "",
    "**Materia:** [Materia]",
    "**Tema relacionado:** [Tema]",
    "**Nivel:** Basico / Intermedio / Dominado",
    "",
    "---",
    "",
    "## Definicion",
    "",
    "",
    "## Por que es importante?",
    "",
    "",
    "## Explicacion detallada",
    "",
    "",
    "## Ejemplo practico",
    "",
    "``````",
    "// codigo o ejemplo",
    "``````",
    "",
    "## Conceptos relacionados",
    "- Concepto 1",
    "- Concepto 2",
    "",
    "## Fuentes",
    "- "
)

# --- Template: Ejercicio ---
Write-File -Path "_templates/template-ejercicio.md" -Lines @(
    "# Ejercicio: [Titulo]",
    "",
    "**Materia:** [Materia]",
    "**Tema:** [Tema]",
    "**Dificultad:** Facil / Media / Dificil",
    "**Estado:** Pendiente / En progreso / Resuelto",
    "",
    "---",
    "",
    "## Enunciado",
    "",
    "",
    "## Analisis del problema",
    "- **Datos de entrada:**",
    "- **Datos de salida:**",
    "- **Restricciones:**",
    "",
    "## Estrategia de solucion",
    "",
    "",
    "## Solucion",
    "",
    "``````",
    "// codigo de la solucion",
    "``````",
    "",
    "## Pruebas",
    "| Entrada | Salida esperada | Salida obtenida | OK |",
    "|---------|----------------|-----------------|-----|",
    "| | | | |",
    "",
    "## Lecciones aprendidas",
    "- "
)

# --- Template: Review semanal ---
Write-File -Path "_templates/template-semana-review.md" -Lines @(
    "# Review Semanal - Semana XX (DD/MM - DD/MM)",
    "",
    "---",
    "",
    "## Lo que aprendi esta semana",
    "",
    "| Materia | Tema principal | Comprension (1-5) |",
    "|---------|---------------|:------------------:|",
    "| BD I | | /5 |",
    "| Estadistica II | | /5 |",
    "| Programacion II | | /5 |",
    "| Metodologia DS | | /5 |",
    "| Redes | | /5 |",
    "| Arquitectura | | /5 |",
    "",
    "## Temas que necesito reforzar",
    "1. ",
    "2. ",
    "3. ",
    "",
    "## Conexiones entre materias",
    "- ",
    "",
    "## Tareas pendientes",
    "- [ ] ",
    "- [ ] ",
    "",
    "## Horas de estudio independiente",
    "",
    "| Materia | Lun | Mar | Mie | Jue | Vie | Sab | Total | Meta |",
    "|---------|:---:|:---:|:---:|:---:|:---:|:---:|:-----:|:----:|",
    "| BD I | | | | | | | 0h | 5h |",
    "| Estadistica | | | | | | | 0h | 4h |",
    "| Programacion | | | | | | | 0h | 8h |",
    "| Metodologia | | | | | | | 0h | 3h |",
    "| Redes | | | | | | | 0h | 4h |",
    "| Arquitectura | | | | | | | 0h | 4h |",
    "",
    "## Logros de la semana",
    "- ",
    "",
    "## Metas para la proxima semana",
    "- [ ] ",
    "- [ ] ",
    "",
    "## Reflexion personal",
    "> "
)

# ============================================================
# README POR MATERIA
# ============================================================
Write-Host "Creando README de cada materia..." -ForegroundColor Yellow

$materiasInfo = @{
    "01-base-de-datos-I" = @("Base de Datos I", "48", "128")
    "02-estadistica-II-bi-bigdata" = @("Estadistica II (BI y Big Data)", "48", "112")
    "03-programacion-II" = @("Programacion II", "64", "192")
    "04-metodologia-desarrollo-software" = @("Metodologia de Desarrollo de Software", "32", "80")
    "05-redes-y-telecomunicaciones" = @("Redes y Telecomunicaciones", "48", "112")
    "06-arquitectura-de-computadores" = @("Arquitectura de Computadores", "32", "96")
}

foreach ($materia in ($materiasInfo.Keys | Sort-Object)) {
    $nombre = $materiasInfo[$materia][0]
    $hcc = $materiasInfo[$materia][1]
    $hth = $materiasInfo[$materia][2]

    Write-File -Path "$materia/README.md" -Lines @(
        "# $nombre",
        "",
        "**Profesor:** [Nombre]",
        "**Horario:** [Dias y horas]",
        "**Horas contacto:** $hcc | **Horas totales:** $hth",
        "",
        "---",
        "",
        "## Objetivos de la Materia",
        "1. ",
        "2. ",
        "3. ",
        "",
        "## Sistema de Evaluacion",
        "| Evaluacion | Porcentaje | Fecha |",
        "|------------|:----------:|-------|",
        "| Parcial 1 | % | DD/MM |",
        "| Parcial 2 | % | DD/MM |",
        "| Proyecto Final | % | DD/MM |",
        "| Talleres/Quices | % | Continuo |",
        "",
        "## Cronograma de Temas",
        "| Semana | Tema | Estado |",
        "|:------:|------|:------:|",
        "| 01 | | Pendiente |",
        "| 02 | | Pendiente |",
        "| 03 | | Pendiente |",
        "| 04 | | Pendiente |",
        "| 05 | | Pendiente |",
        "| 06 | | Pendiente |",
        "| 07 | | Pendiente |",
        "| 08 | | Pendiente |",
        "| 09 | | Pendiente |",
        "| 10 | | Pendiente |",
        "| 11 | | Pendiente |",
        "| 12 | | Pendiente |",
        "| 13 | | Pendiente |",
        "| 14 | | Pendiente |",
        "| 15 | | Pendiente |",
        "| 16 | | Pendiente |",
        "",
        "## Notas Rapidas",
        "- "
    )

    # Glosario
    Write-File -Path "$materia/conceptos-clave/glosario.md" -Lines @(
        "# Glosario - $nombre",
        "",
        "| Termino | Definicion | Ejemplo |",
        "|---------|-----------|---------|",
        "| | | |"
    )

    # Recursos
    Write-File -Path "$materia/recursos/enlaces-y-bibliografia.md" -Lines @(
        "# Recursos y Bibliografia - $nombre",
        "",
        "## Libros",
        "- ",
        "",
        "## Videos / Cursos",
        "- ",
        "",
        "## Enlaces utiles",
        "- ",
        "",
        "## Herramientas",
        "- "
    )
}

# ============================================================
# PLANTILLAS DE METODOLOGIA
# ============================================================
Write-Host "Creando plantillas de metodologia..." -ForegroundColor Yellow

Write-File -Path "04-metodologia-desarrollo-software/plantillas/template-historia-usuario.md" -Lines @(
    "# Historia de Usuario",
    "",
    "**ID:** HU-XXX",
    "**Titulo:** ",
    "**Sprint/Iteracion:** ",
    "",
    "---",
    "",
    "## Descripcion",
    "**Como** [tipo de usuario]",
    "**Quiero** [accion/funcionalidad]",
    "**Para** [beneficio/valor]",
    "",
    "## Criterios de Aceptacion",
    "- [ ] Criterio 1",
    "- [ ] Criterio 2",
    "- [ ] Criterio 3",
    "",
    "## Estimacion",
    "- **Puntos de historia:** ",
    "- **Prioridad:** Alta / Media / Baja"
)

Write-File -Path "04-metodologia-desarrollo-software/plantillas/template-caso-uso.md" -Lines @(
    "# Caso de Uso",
    "",
    "**ID:** CU-XXX",
    "**Nombre:** ",
    "**Actor principal:** ",
    "",
    "---",
    "",
    "## Descripcion breve",
    "",
    "",
    "## Precondiciones",
    "1. ",
    "",
    "## Flujo principal",
    "1. El usuario...",
    "2. El sistema...",
    "",
    "## Flujos alternativos",
    "1. ",
    "",
    "## Postcondiciones",
    "1. "
)

Write-File -Path "04-metodologia-desarrollo-software/plantillas/template-requerimientos.md" -Lines @(
    "# Especificacion de Requerimientos",
    "",
    "**Proyecto:** ",
    "**Version:** 1.0",
    "**Fecha:** ",
    "",
    "---",
    "",
    "## 1. Introduccion",
    "### 1.1 Proposito",
    "### 1.2 Alcance",
    "",
    "## 2. Descripcion General",
    "### 2.1 Perspectiva del producto",
    "### 2.2 Funcionalidades principales",
    "",
    "## 3. Requerimientos Funcionales",
    "| ID | Descripcion | Prioridad | Estado |",
    "|----|-------------|:---------:|:------:|",
    "| RF-001 | | Alta | Pendiente |",
    "| RF-002 | | Media | Pendiente |",
    "",
    "## 4. Requerimientos No Funcionales",
    "| ID | Descripcion | Categoria | Prioridad |",
    "|----|-------------|-----------|:---------:|",
    "| RNF-001 | | Rendimiento | |",
    "| RNF-002 | | Seguridad | |"
)

# ============================================================
# REVIEWS SEMANALES
# ============================================================
Write-Host "Creando reviews semanales..." -ForegroundColor Yellow

for ($i = 1; $i -le 16; $i++) {
    $num = $i.ToString("00")
    $templateContent = Get-Content "_templates/template-semana-review.md" -Raw -Encoding UTF8
    $weekContent = $templateContent -replace "Semana XX", "Semana $num"
    [System.IO.File]::WriteAllText("reviews/semana-$num.md", $weekContent, [System.Text.Encoding]::UTF8)
}

# ============================================================
# .gitignore
# ============================================================
Write-Host "Creando .gitignore..." -ForegroundColor Yellow

Write-File -Path ".gitignore" -Lines @(
    "# OS",
    ".DS_Store",
    "Thumbs.db",
    "Desktop.ini",
    "",
    "# IDEs",
    ".vscode/",
    ".idea/",
    "*.swp",
    "",
    "# Compilados",
    "*.class",
    "*.exe",
    "*.o",
    "__pycache__/",
    "*.pyc",
    "",
    "# Datasets grandes",
    "*.csv",
    "*.xlsx",
    "",
    "# Temporales",
    "*.tmp",
    "*.log",
    "*.bak",
    "",
    "# Dependencias",
    "node_modules/",
    "venv/",
    ".env",
    "",
    "# Jupyter",
    ".ipynb_checkpoints/"
)

# ============================================================
# PLAN DE ESTUDIO
# ============================================================
Write-Host "Creando plan de estudio..." -ForegroundColor Yellow

Write-File -Path "PLAN-DE-ESTUDIO.md" -Lines @(
    "# Plan de Estudio - Semestre 2",
    "",
    "## Objetivos del Semestre",
    "1. Dominar fundamentos de bases de datos relacionales y SQL",
    "2. Aplicar estadistica al analisis de datos con herramientas de BI",
    "3. Consolidar la programacion orientada a objetos",
    "4. Conocer y aplicar metodologias de desarrollo de software",
    "5. Comprender fundamentos de redes y telecomunicaciones",
    "6. Entender la arquitectura interna de los computadores",
    "",
    "## Distribucion Semanal de Estudio (28h independientes)",
    "",
    "| Materia | Horas/semana | Dias sugeridos |",
    "|---------|:------------:|----------------|",
    "| BD I | 5h | Lun, Mie |",
    "| Estadistica II | 4h | Mar, Jue |",
    "| Programacion II | 8h | Lun, Mie, Vie, Sab |",
    "| Metodologia DS | 3h | Mar |",
    "| Redes | 4h | Jue, Sab |",
    "| Arquitectura | 4h | Vie, Sab |",
    "",
    "## Rutina Diaria",
    "1. Antes de clase (30 min): Revisar notas anteriores",
    "2. Durante clase: Tomar notas, marcar dudas",
    "3. Despues de clase (1-2h): Pasar notas al repo, commit",
    "4. Noche (1-2h): Practica y ejercicios",
    "5. Sabado (4-5h): Review semanal + completar pendientes",
    "6. Domingo: Descanso",
    "",
    "## Fechas Importantes",
    "| Fecha | Evento | Materia |",
    "|-------|--------|---------|",
    "| | | |"
)

# ============================================================
# RECURSOS GENERALES
# ============================================================
Write-File -Path "RECURSOS-GENERALES.md" -Lines @(
    "# Recursos Generales - Semestre 2",
    "",
    "## Beneficios Estudiantiles",
    "- GitHub Student Developer Pack: https://education.github.com/pack",
    "- JetBrains Education: https://www.jetbrains.com/community/education/",
    "",
    "## Herramientas Esenciales",
    "- VS Code: https://code.visualstudio.com/",
    "- Obsidian: https://obsidian.md/",
    "- Draw.io: https://app.diagrams.net/",
    "- Anki: https://apps.ankiweb.net/",
    "",
    "## Aprender a Aprender",
    "- Learning How to Learn: https://www.coursera.org/learn/learning-how-to-learn",
    "- Learn Git Branching: https://learngitbranching.js.org/"
)

# ============================================================
# README PRINCIPAL
# ============================================================
Write-Host "Creando README principal..." -ForegroundColor Yellow

Write-File -Path "README.md" -Lines @(
    "# Segundo Semestre - Tecnologia en Desarrollo de Software",
    "",
    "Repositorio de aprendizaje organizado para el segundo semestre.",
    "",
    "## Materias",
    "",
    "| # | Materia | Horas CC | Horas TH | Estado |",
    "|---|---------|:--------:|:--------:|:------:|",
    "| 01 | [Base de Datos I](./01-base-de-datos-I/) | 48 | 128 | En curso |",
    "| 02 | [Estadistica II (BI y Big Data)](./02-estadistica-II-bi-bigdata/) | 48 | 112 | En curso |",
    "| 03 | [Programacion II](./03-programacion-II/) | 64 | 192 | En curso |",
    "| 04 | [Metodologia de Desarrollo de Software](./04-metodologia-desarrollo-software/) | 32 | 80 | En curso |",
    "| 05 | [Redes y Telecomunicaciones](./05-redes-y-telecomunicaciones/) | 48 | 112 | En curso |",
    "| 06 | [Arquitectura de Computadores](./06-arquitectura-de-computadores/) | 32 | 96 | En curso |",
    "",
    "**Total: 272 horas CC / 720 horas TH**",
    "",
    "## Estructura",
    "",
    "Cada materia contiene:",
    "- ``notas-de-clase/`` - Apuntes semanales",
    "- ``conceptos-clave/`` - Glosarios y teoria",
    "- ``ejercicios/`` - Practicas en clase e independientes",
    "- ``cheatsheets/`` - Guias rapidas de referencia",
    "- ``recursos/`` - Enlaces y bibliografia",
    "",
    "## Progreso Semanal",
    "Los reviews semanales estan en la carpeta [reviews/](./reviews/)",
    "",
    "## Convenciones de Commits",
    "``````",
    "tipo(materia): descripcion breve",
    "",
    "Tipos: notas | docs | ejercicio | codigo | cheatsheet | recurso | fix | review",
    "``````"
)

# ============================================================
# FINALIZADO
# ============================================================
Write-Host ""
Write-Host "========================================================" -ForegroundColor Green
Write-Host "  ESTRUCTURA CREADA EXITOSAMENTE!" -ForegroundColor Green
Write-Host "========================================================" -ForegroundColor Green
Write-Host ""
Write-Host "  Proximos pasos:" -ForegroundColor Cyan
Write-Host "    git add ." -ForegroundColor White
Write-Host '    git commit -m "init: estructura inicial del semestre 2"' -ForegroundColor White
Write-Host "    git remote add origin TU-URL-DE-GITHUB" -ForegroundColor White
Write-Host "    git push -u origin main" -ForegroundColor White
Write-Host ""
Write-Host "  A darle duro al semestre!" -ForegroundColor Green
Write-Host "========================================================`n" -ForegroundColor Green