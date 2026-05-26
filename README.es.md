# Mini Presentacion: Introduccion a crewAI

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![crewAI](https://img.shields.io/badge/crewAI-Framework-FF6B35)
![Ollama](https://img.shields.io/badge/Ollama-LLM_Local-000000?logo=ollama&logoColor=white)
![Llama](https://img.shields.io/badge/Llama_3.2-1b/3b-0467DF?logo=meta&logoColor=white)
![uv](https://img.shields.io/badge/uv-Gestor_de_Paquetes-DE5FE9)
![HTML](https://img.shields.io/badge/HTML-Diapositivas-E34F26?logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS-Estilos-1572B6?logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-Navegacion-F7DF1E?logo=javascript&logoColor=black)

Un repositorio educativo para aprender **crewAI** — un framework de Python para orquestar agentes de IA autonomos. Incluye una presentacion con diapositivas que explica los conceptos clave y un proyecto demo que puedes ejecutar en tu maquina.

## Contenido

```
.
├── docs/                  # Presentacion (HTML/CSS/JS)
│   ├── index.html        # Diapositivas
│   ├── style.css         # Estilos
│   └── script.js         # Logica de navegacion
│
├── mbti-gift-lab/        # Proyecto demo
│   ├── main.py           # Punto de entrada
│   ├── crew_logic.py     # Configuracion del crew y LLM
│   ├── agents.yaml       # Definicion de agentes
│   ├── tasks.yaml        # Definicion de tareas
│   └── README.md         # Guia completa de instalacion
│
└── README.md             # Estas aqui
```

## Arquitectura

Este repositorio tiene dos partes que funcionan juntas:

### 1. Presentacion (`docs/`)

Una presentacion en el navegador que cubre:

- Que son los agentes de IA y en que se diferencian de un solo LLM
- Sistemas de un solo agente vs. multi-agente
- Conceptos clave de crewAI: **Agent**, **Task**, **Tool** y **Crew**
- Como colaboran los agentes en un flujo secuencial
- Comparacion con herramientas similares (AutoGen, ChatDev)

Abre `docs/index.html` en cualquier navegador para verla.

### 2. Proyecto Demo (`mbti-gift-lab/`)

Un proyecto crewAI minimo y funcional que demuestra los conceptos de las diapositivas. Dos agentes de IA colaboran para generar recomendaciones de regalos personalizadas segun un tipo de personalidad MBTI:

```
Entrada del Usuario (MBTI)
      │
      ▼
┌──────────────┐     ┌───────────────┐     ┌───────────────┐
│  Lluvia de   │ ──▶ │   Critica     │ ──▶ │   Refinar     │
│    Ideas     │     │  (Selector)   │     │  (Listador)   │
│ (Listador)   │     │               │     │               │
└──────────────┘     └───────────────┘     └───────────────┘
                                                │
                                                ▼
                                         final_gifts.md
```

El demo se ejecuta completamente en tu maquina usando **Ollama** con un LLM local (Llama 3.2). No necesitas claves de API.

Consulta [`mbti-gift-lab/README.es.md`](mbti-gift-lab/README.es.md) para la guia completa paso a paso.

## Para Quien Es Esto?

- Cualquier persona curiosa sobre **sistemas de IA multi-agente**
- Desarrolladores que quieran probar crewAI sin leer toda la documentacion
- Estudiantes o presentadores que necesiten una introduccion lista sobre orquestacion de agentes

## Stack Tecnologico

| Componente | Tecnologia |
|------------|------------|
| Framework | [crewAI](https://github.com/crewAIInc/crewAI) |
| LLM | [Ollama](https://ollama.com) + Llama 3.2 (se ejecuta localmente) |
| Gestor de Paquetes | [uv](https://docs.astral.sh/uv/) |
| Presentacion | HTML/CSS/JS puro |

## Autora

**Mirae Kang** — [github.com/KangMirae](https://github.com/KangMirae)

## Licencia

Este proyecto es de codigo abierto y esta disponible para cualquier uso — personal, educativo o comercial. Sin restricciones.
