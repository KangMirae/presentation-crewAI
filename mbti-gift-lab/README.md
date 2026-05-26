# MBTI Gift Lab

A beginner-friendly project that demonstrates how to use **CrewAI** with a local **Ollama** LLM. Given an MBTI personality type, a crew of AI agents collaborates to brainstorm, critique, and refine gift recommendations — all running entirely on your machine.

## What Does It Do?

You enter an MBTI type (e.g. `INFP`, `ESTJ`), and two AI agents work together through three sequential tasks:

1. **Brainstorm** — The *Gift List Maker* agent creates 5 gift ideas tailored to the MBTI type.
2. **Critique** — The *Gift Picker* agent reviews the list and picks 2 gifts that are too generic, explaining why.
3. **Refine** — The *Gift List Maker* takes the feedback and replaces the 2 weak gifts with better, more personal ones.

The result is saved to `final_gifts.md`.

## How CrewAI Works Here

CrewAI orchestrates multiple AI **Agents**, each with a defined role, goal, and backstory. These agents are assigned **Tasks** that run sequentially — the output of one task feeds into the next. Together, they form a **Crew**.

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

## Project Structure

```
mbti-gift-lab/
├── main.py          # Entry point — takes user input and kicks off the crew
├── crew_logic.py    # Core logic — defines the LLM, agents, tasks, and crew
├── agents.yaml      # Agent definitions (roles, goals, backstories)
├── tasks.yaml       # Task definitions (descriptions, expected outputs)
└── README.md
```

### `main.py`

The entry point of the application. It prompts the user for an MBTI type, creates an instance of `MbtiLoopCrew`, and runs the crew. The final result is printed to the console.

### `crew_logic.py`

Contains the `MbtiLoopCrew` class, which:

- Loads agent and task configurations from the YAML files.
- Initializes the LLM (Ollama running Llama 3.2 locally).
- Creates two `Agent` instances and three `Task` instances.
- Assembles them into a `Crew` and kicks it off with the user's MBTI type as input.

### `agents.yaml`

Defines the two agents used by the crew:

- **gift_lister** — A "Gift List Maker" who comes up with gift ideas based on personality.
- **gift_picker** — A "Gift Picker" who reviews the list and flags generic choices.

Each agent has a `role`, `goal`, and `backstory` that guide how the LLM behaves.

### `tasks.yaml`

Defines the three tasks that the crew executes in order:

- **brainstorm_task** — Generate 5 gift ideas for the given MBTI type.
- **critique_task** — Identify 2 generic gifts and explain why they should be replaced.
- **refinement_task** — Replace the weak gifts with better, more personal alternatives.

Each task has a `description`, `expected_output`, and an assigned `agent`.

---

## Step-by-Step Setup Guide

### Step 1 — Install uv

[uv](https://docs.astral.sh/uv/) is a fast Python package and project manager.

**macOS / Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

For other options, see the [uv installation docs](https://docs.astral.sh/uv/getting-started/installation/).

### Step 2 — Install Ollama

Download and install Ollama from the official site: **https://ollama.com/download**

- **macOS** — Download the app and drag it to Applications.
- **Linux** — Run `curl -fsSL https://ollama.com/install.sh | sh`
- **Windows** — Download and run the installer.

### Step 3 — Pull the LLM model

```bash
ollama pull llama3.2:1b
```

> **Tip:** For much better results, use the 3b model instead:
> ```bash
> ollama pull llama3.2:3b
> ```
> Then update the model name in `crew_logic.py` from `"ollama/llama3.2:1b"` to `"ollama/llama3.2:3b"`.

### Step 4 — Create the project and install dependencies

```bash
mkdir mbti-gift-lab
cd mbti-gift-lab
uv init
uv add crewai pyyaml --prerelease allow
```

This initializes a new Python project and installs the two required packages:
- **crewai** — The multi-agent orchestration framework.
- **pyyaml** — For loading the YAML configuration files.

### Step 5 — Start Ollama

```bash
ollama serve
```

> **Note:** On macOS, if you opened the Ollama app, it is already serving in the background. You can skip this step.

### Step 6 — Write the code

Create the following 4 files inside your `mbti-gift-lab/` directory. You can find the source code for each file in this repository:

| File | Purpose |
|------|---------|
| `agents.yaml` | Defines the two AI agents (List Maker and Picker) |
| `tasks.yaml` | Defines the three tasks (Brainstorm, Critique, Refine) |
| `crew_logic.py` | Loads configs, sets up the LLM, agents, tasks, and crew |
| `main.py` | Entry point that takes user input and runs the crew |

### Step 7 — Run it

```bash
uv run main.py
```

You will be prompted to enter an MBTI type. Type one in (e.g. `INFP`) and watch the agents collaborate in real time. The final list of 5 gift recommendations will be printed to the console and saved to `final_gifts.md`.
