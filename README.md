# UFCGAME
2
Programador junior: Oved Estrada
3
 
4
# FASE 1: ANÁLISIS
5
 
6
Documento donde se analizaron los requerimientos funcionales y no funcionales del videojuego UFC GAME.
7
 
8
## Objetivos del proyecto
9
Desarrollar un videojuego inspirado en las artes marciales mixtas (MMA) que permita a los jugadores participar en combates dinámicos, seleccionar diferentes luchadores y competir en distintos modos de juego.
10
 
11
## Requerimientos funcionales
12
- Registro e inicio de sesión de usuarios.
13
- Selección de luchadores con estadísticas únicas.
14
- Sistema de combate en tiempo real.
15
- Barra de vida y energía.
16
- Menú principal con opciones de juego.
17
- Sistema de puntuación y resultados de combate.
18
- Guardado automático de progreso.
19
 
20
## Requerimientos no funcionales
21
- Interfaz amigable e intuitiva.
22
- Tiempo de respuesta menor a 2 segundos.
23
- Compatibilidad con sistemas Windows y Linux.
24
- Código modular y fácil de mantener.
25
- Seguridad en el almacenamiento de datos.
26
 
27
## Análisis de riesgos
28
- Posibles errores en la detección de colisiones.
29
- Problemas de rendimiento en equipos de bajos recursos.
30
- Desbalance entre personajes jugables.
31
- Pérdida de información durante el guardado de partidas.
32
 
33
---
34
 
35
# FASE 2: DISEÑO
36
 
37
Diseño de la arquitectura y estructura general del videojuego UFC GAME.
38
 
39
## Diseño de la interfaz
40
- Pantalla de inicio.
41
- Menú principal.
42
- Pantalla de selección de luchadores.
43
- Arena de combate.
44
- Pantalla de resultados y estadísticas.
45
 
46
## Diagramas elaborados
47
- Diagrama de flujo de navegación del juego.
48
- Diagrama de casos de uso.
49
- Diagrama de clases para la lógica de combate.
50
- Diagrama de la base de datos para almacenar usuarios y estadísticas.
51
 
52
## Diseño de la infraestructura
53
- Módulo de autenticación.
54
- Módulo de gestión de usuarios.
55
- Motor de combate.
56
- Sistema de puntuación.
57
- Sistema de almacenamiento de datos.
58
 
59
## Herramientas utilizadas
60
- Draw.io para diagramas.
61
- UML para modelado del sistema.
62
- Python como lenguaje principal de desarrollo.
63
 
64
---
65
 
66
# FASE 3: DESARROLLO
67
 
68
Implementación del videojuego utilizando Python.
69
 
70
## Tecnologías utilizadas
71
- Python 3.12
72
- Pygame para gráficos y animaciones.
73
- SQLite para almacenamiento de datos.
74
- Git para control de versiones.
75
 
76
## Módulos desarrollados
77
### Sistema de usuarios
78
- Registro de nuevos jugadores.
79
- Inicio de sesión.
80
- Gestión de perfiles.
81
 
82
### Sistema de combate
83
- Ataques básicos y avanzados.
84
- Sistema de defensa.
85
- Detección de impactos.
86
- Gestión de vida y energía.
87
 
88
### Sistema de interfaz
89
- Botones interactivos.
90
- Menús dinámicos.
91
- Pantallas de transición.
92
 
93
### Base de datos
94
- Almacenamiento de usuarios.
95
- Historial de combates.
96
- Estadísticas de victorias y derrotas.
97
 
98
## Pruebas realizadas
99
- Pruebas unitarias de funciones.
100
- Pruebas de integración entre módulos.
101
- Pruebas de rendimiento.
102
- Corrección de errores detectados.
103
 
104
## Resultados obtenidos
105
Se logró desarrollar una versión funcional del videojuego UFC GAME, permitiendo la interacción de usuarios, selección de personajes, realización de combates y almacenamiento de estadísticas de manera eficiente.
