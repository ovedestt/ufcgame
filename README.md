# UFCGAME
Programador junior: Oved Estrada

# FASE 1: ANÁLISIS
Documento donde se analizaron los requerimientos funcionales y no funcionales del videojuego UFC GAME.
## Objetivos del proyecto
Desarrollar un videojuego inspirado en las artes marciales mixtas (MMA) que permita a los jugadores participar en combates dinámicos, seleccionar diferentes luchadores y competir en distintos modos de juego.
## Requerimientos funcionales
- Registro e inicio de sesión de usuarios.
- Selección de luchadores con estadísticas únicas.
- Sistema de combate en tiempo real.
- Barra de vida y energía.
- Menú principal con opciones de juego.
- Sistema de puntuación y resultados de combate.
- Guardado automático de progreso.
## Requerimientos no funcionales
- Interfaz amigable e intuitiva.
- Tiempo de respuesta menor a 2 segundos.
- Compatibilidad con sistemas Windows y Linux.
- Código modular y fácil de mantener.
- Seguridad en el almacenamiento de datos.
## Análisis de riesgos
- Posibles errores en la detección de colisiones.
- Problemas de rendimiento en equipos de bajos recursos.
- Desbalance entre personajes jugables.
- Pérdida de información durante el guardado de partidas.

# FASE 2: DISEÑO
Diseño de la arquitectura y estructura general del videojuego UFC GAME.
## Diseño de la interfaz
- Pantalla de inicio.
- Menú principal.
- Pantalla de selección de luchadores.
- Arena de combate.
- Pantalla de resultados y estadísticas.
## Diagramas elaborados
- Diagrama de flujo de navegación del juego.
- Diagrama de casos de uso.
- Diagrama de clases para la lógica de combate.
- Diagrama de la base de datos para almacenar usuarios y estadísticas.
## Diseño de la infraestructura
- Módulo de autenticación.
- Módulo de gestión de usuarios.
- Motor de combate.
- Sistema de puntuación.
- Sistema de almacenamiento de datos.
## Herramientas utilizadas
- Draw.io para diagramas.
- UML para modelado del sistema.
- Python como lenguaje principal de desarrollo.

# FASE 3: DESARROLLO
Implementación del videojuego utilizando Python.
## Tecnologías utilizadas
- Python 3.12
- Pygame para gráficos y animaciones.
- SQLite para almacenamiento de datos.
- Git para control de versiones.
## Módulos desarrollados
### Sistema de usuarios
- Registro de nuevos jugadores.
- Inicio de sesión.
- Gestión de perfiles.
### Sistema de combate
- Ataques básicos y avanzados.
- Sistema de defensa.
- Detección de impactos.
- Gestión de vida y energía.
### Sistema de interfaz
- Botones interactivos.
- Menús dinámicos.
- Pantallas de transición.
### Base de datos
- Almacenamiento de usuarios.
- Historial de combates.
- Estadísticas de victorias y derrotas.
## Pruebas realizadas
- Pruebas unitarias de funciones.
- Pruebas de integración entre módulos.
- Pruebas de rendimiento.
- Corrección de errores detectados.
## Resultados obtenidos
Se logró desarrollar una versión funcional del videojuego UFC GAME, permitiendo la interacción de usuarios, selección de personajes, realización de combates y almacenamiento de estadísticas de manera eficiente.
