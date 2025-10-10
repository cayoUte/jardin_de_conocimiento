# 🌳 Mi Jardín del Conocimiento: Desarrollo de Software
Este no es un simple repositorio de apuntes. Es un Jardín Digital, una bitácora viva de mi viaje a través de la carrera de Desarrollo de Software en la UTE. Aquí, las ideas se siembran, se conectan y crecen con el tiempo.

## ¿Qué es un Jardín Digital en este Contexto?
A diferencia de un archivador tradicional donde las notas se guardan en carpetas rígidas y se olvidan, un Jardín Digital funciona más como una red neuronal o un cerebro. Es un espacio de aprendizaje imperfecto y en constante crecimiento.

Los principios clave de este jardín son:

  🌱 Conexión sobre Colección: El valor no está en cuántas notas tengo, sino en cómo se conectan. Un concepto de Programación I puede (y debe) enlazarse con uno de Bases de Datos II.
  🧠 Notas Atómicas: Cada concepto fundamental vive en su propio archivo. Esto permite enlazarlo desde múltiples contextos, creando una red de conocimiento robusta y reutilizable.
  ✍️ Aprendizaje Activo: Las notas se escriben con mis propias palabras. Es un espacio para procesar, cuestionar y entender, no solo para transcribir.
  🔄 Evolución Constante: Las notas no son estáticas. Puedo volver a una idea del primer semestre con el conocimiento del cuarto y refinarla. Es un sistema que evoluciona conmigo.
## 🗺️ ¿Cómo está Organizado este Jardín?
La estructura está diseñada para facilitar la navegación cronológica (por semestre) y la conexión conceptual (a través de enlaces).

La jerarquía principal es:

```
/SEMESTRE-XX/
└── 01-nombre-de-la-materia/
    ├── _assets/
    ├── AAAA-MM-DD-Tema-de-clase.md
    ├── Concepto-NombreDelConcepto.md
    └── Apendice-Glosario.md
```
Convención de Nombres
FORMATO / PREFIJO	PROPÓSITO	EJEMPLO
AAAA-MM-DD-Tema.md	Notas de Clase: Mi bitácora cronológica. Lo que pasó y se vio en cada clase.	2024-09-06-Variables-y-Tipos-de-Datos.md
Concepto-Nombre.md	Notas Atómicas: El corazón del jardín. Una idea, explicada a fondo.	Concepto-Variable.md
Apendice-Nombre.md	Recursos: Glosarios, bibliografías, y enlaces útiles para una materia.	Apendice-Recursos-Utiles.md
_assets/	Archivos: Carpeta para todas las imágenes, PDFs y otros archivos de la materia.	_assets/diagrama-flujo-login.png
## 🛠️ Guía de Estilo y Herramientas
Para que el jardín florezca, sigo un conjunto de reglas de formato que enriquecen la experiencia visual y cognitiva.

### 1. Jerarquía y Énfasis
Uso los encabezados (#, ##, ###) para estructurar cada nota. Las negritas son para conceptos clave y las cursivas para énfasis o términos nuevos.

### 2. Enlaces Internos (Wiki-Links)
La herramienta más importante. Conecto ideas usando la sintaxis [[Nombre-del-Archivo]].

Por ejemplo, en una nota de clase puedo escribir: “Hoy aprendimos sobre el [[Concepto-Bucle-For]], que es una estructura de control fundamental.”

### 3. Bloques de Código
El código siempre se formatea con resaltado de sintaxis para facilitar la lectura.


```
# Ejemplo de un bloque de código en Python
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)
```
### 4. Citas y Alertas
Uso las citas (>) para resaltar ideas importantes del profesor, “insights” personales o advertencias.

¡Ojo! No olvides el caso base en una función recursiva para evitar un stack overflow.

### 5. Etiquetas (Tags)
Uso etiquetas # al final de las notas para crear conexiones transversales. #programacion #algoritmia #estructuras-de-control

## 🚀 Roadmap del Proyecto

- [x] Estructurar el primer semestre usando los scripts.
- [x] Definir la guía de estilo en este README.
- [ ] Empezar a conectar conceptos entre Programación I y Matemáticas.
- [ ] Crear el primer mapa mental visual usando las imágenes en _assets.

### Herramientas Recomendadas
- Editor: Obsidian para una experiencia visual con gráficos de conocimiento.
- Alternativa: VS Code con la extensión Markdown All in One.
- Control de Versiones: Git y GitHub.
--- 

Este jardín es mi herramienta principal de estudio. Está diseñado para ser explorado, no solo archivado. ¡A sembrar conocimiento