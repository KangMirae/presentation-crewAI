# Mini Presentation: Introduction to crewAI

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![crewAI](https://img.shields.io/badge/crewAI-Framework-FF6B35)
![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-000000?logo=ollama&logoColor=white)
![Llama](https://img.shields.io/badge/Llama_3.2-1b/3b-0467DF?logo=meta&logoColor=white)
![uv](https://img.shields.io/badge/uv-Package_Manager-DE5FE9)
![HTML](https://img.shields.io/badge/HTML-Slides-E34F26?logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS-Styling-1572B6?logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-Navigation-F7DF1E?logo=javascript&logoColor=black)

An educational repository for learning **crewAI** — a Python framework for orchestrating autonomous AI agents. It includes a slide-based presentation explaining the core concepts and a hands-on demo project you can run locally.

## What's Inside

```
.
├── docs/                  # Slide presentation (HTML/CSS/JS)
│   ├── index.html        # Presentation slides
│   ├── style.css         # Slide styling
│   └── script.js         # Navigation logic
│
├── mbti-gift-lab/        # Hands-on demo project
│   ├── main.py           # Entry point
│   ├── crew_logic.py     # Crew setup and LLM config
│   ├── agents.yaml       # Agent definitions
│   ├── tasks.yaml        # Task definitions
│   └── README.md         # Full setup guide
│
└── README.md             # You are here
```

## Architecture

This repo has two parts that work together:

### 1. Presentation (`docs/`)

A browser-based slide deck that covers:

- What AI agents are and how they differ from a single LLM
- Single-agent vs. multi-agent systems
- crewAI's core concepts: **Agent**, **Task**, **Tool**, and **Crew**
- How agents collaborate in a sequential workflow
- Comparison with similar tools (AutoGen, ChatDev)

Open `docs/index.html` in any browser to view.

### 2. Demo Project (`mbti-gift-lab/`)

A minimal, working crewAI project that demonstrates the concepts from the slides. Two AI agents collaborate to generate personalized gift recommendations based on an MBTI personality type:

```
User Input (MBTI)
      │
      ▼
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  Brainstorm  │ ──▶ │   Critique   │ ──▶ │   Refine     │
│ (List Maker) │     │   (Picker)   │     │ (List Maker) │
└──────────────┘     └──────────────┘     └──────────────┘
                                               │
                                               ▼
                                        final_gifts.md
```

The demo runs entirely on your machine using **Ollama** with a local LLM (Llama 3.2). No API keys needed.

See [`mbti-gift-lab/README.md`](mbti-gift-lab/README.md) for the full step-by-step setup guide.

## Who Is This For?

- Anyone curious about **multi-agent AI systems**
- Developers who want to try crewAI without reading the entire docs first
- Students or presenters who need a ready-made introduction to agent orchestration

## Tech Stack

| Component | Technology |
|-----------|------------|
| Framework | [crewAI](https://github.com/crewAIInc/crewAI) |
| LLM | [Ollama](https://ollama.com) + Llama 3.2 (runs locally) |
| Package Manager | [uv](https://docs.astral.sh/uv/) |
| Presentation | Vanilla HTML/CSS/JS |

## Author

**Mirae Kang** — [github.com/KangMirae](https://github.com/KangMirae)

## License

This project is open source and available for any use — personal, educational, or commercial. No restrictions.
