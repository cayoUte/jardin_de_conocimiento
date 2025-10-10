@echo off
setlocal

:: --- Configuración ---
set "CARPETA_RAIZ=UNIVERSIDAD-DESARROLLO-SOFTWARE"
set "CARPETA_SEMESTRE=SEMESTRE-01"

:: --- Inicio del Script ---
echo.
echo =========================================================
echo  Iniciando la creacion de la estructura del conocimiento
echo =========================================================
echo.

:: Crear carpetas principales y navegar a la del semestre
if not exist "%CARPETA_RAIZ%\%CARPETA_SEMESTRE%" (
    mkdir "%CARPETA_RAIZ%\%CARPETA_SEMESTRE%"
)
cd "%CARPETA_RAIZ%\%CARPETA_SEMESTRE%"

echo Ubicacion: %cd%
echo.

:: Definir y crear la estructura para cada materia
call :crear_materia "01" "Matematicas" "matematicas"
call :crear_materia "02" "Estadistica I (Descriptiva)" "estadistica-i-descriptiva"
call :crear_materia "03" "Programacion I" "programacion-i"
call :crear_materia "04" "Sistemas Operativos" "sistemas-operativos"
call :crear_materia "05" "Tecnologias de la Informacion y la Comunicacion" "tecnologias-de-la-informacion"
call :crear_materia "06" "Introduccion a la Contabilidad" "introduccion-a-la-contabilidad"

echo.
echo =========================================================
echo  Exito! La estructura del primer semestre fue creada.
echo =========================================================
echo.
goto :eof


:: --- Subrutina para crear la estructura de una materia ---
:crear_materia
set "num=%~1"
set "nombre_completo=%~2"
set "slug=%~3"
set "dir_name=%num%-%slug%"

echo Creando estructura para: %nombre_completo%
if not exist "%dir_name%" mkdir "%dir_name%"
if not exist "%dir_name%\_assets" mkdir "%dir_name%\_assets"

(
    echo # %nombre_completo%
    echo.
    echo Este es el espacio principal para la asignatura de **%nombre_completo%**.
) > "%dir_name%\README.md"

(
    echo # Glosario de %nombre_completo%
) > "%dir_name%\Apendice-Glosario.md"

(
    echo # Recursos Utiles de %nombre_completo%
) > "%dir_name%\Apendice-Recursos-Utiles.md"

echo    -> Directorio creado: %dir_name%
echo.
goto :eof

