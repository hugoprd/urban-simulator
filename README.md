[PT-BR](#-pt-br) | [EN-US](#-en-us)

---

# PT-BR

# 🏙️ Simulador Urbano Preditivo (Micro-MVP)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)

> ⚠️ **Aviso:** Este repositório contém apenas um Produto Mínimo Viável (MVP) / Prova de Conceito (PoC). Ele representa uma versão "Micro" de um projeto de pesquisa muito maior que servirá como base para o meu Trabalho de Conclusão de Curso (TCC) em Sistemas de Informação.

## Sobre este Repositório (O MVP)
O objetivo deste código é provar e validar rapidamente o conceito central da pesquisa: a viabilidade de simular visualmente a relação de causa e efeito entre indicadores socioeconômicos (como desemprego e evasão escolar) e índices de criminalidade urbana.

Para garantir agilidade nesta etapa de validação, a arquitetura atual foi simplificada intencionalmente:
* **Backend Analítico:** Utiliza um modelo *Random Forest Regressor* (via `scikit-learn`) treinado com dados tabulares para inferência rápida.
* **Frontend Visual:** Utiliza a biblioteca `matplotlib` com widgets nativos para gerar um mapa de calor 2D interativo, representando um grid urbano genérico.
* **Gerenciamento de Ambiente:** Estruturado de forma moderna e isolada utilizando o `uv`.

### Demonstração Interativa
*(Arraste e solte o vídeo/GIF da sua gravação de tela mexendo nos sliders aqui)*

---

## O Futuro do Projeto (Escopo do TCC)
O projeto final que sucederá este repositório terá uma complexidade arquitetural e matemática muito superior, aplicando o estado da arte em Gêmeos Digitais para a gestão pública orientada a dados. 

As evoluções mapeadas para o repositório principal do TCC incluem:

| Componente | Versão Atual (Este Repo) | Versão Final (TCC) |
| :--- | :--- | :--- |
| **Interface Visual** | Gráfico 2D estático com *Matplotlib* | Ambiente de simulação interativa utilizando a engine **Godot 4**. |
| **Modelo Preditivo** | Algoritmo *Random Forest* básico | **Rede Neural Customizada**, otimizada para identificar correlações espaço-temporais complexas. |
| **Arquitetura** | Script monolítico único | **Microsserviços**, com total desacoplamento via WebSockets para comunicação de baixíssima latência entre a IA (backend Python) e a renderização (frontend Godot). |
| **Dados** | Geração e mapeamento genérico | Dados e formato real do **Rio de Janeiro** (integrando bases abertas). |

---

## Como executar este MVP localmente

Este projeto utiliza o gerenciador de pacotes [UV](https://github.com/astral-sh/uv) para garantir velocidade e ambientes isolados.

**1. Clone o repositório:**
```bash
git clone https://github.com/hugoprd/urban-simulator
cd urban-simulator
```

**2. Instale o uv:**
*2.1 Linux:*
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

*(Se o seu sistema não tiver curl, use wget: `wget -qO- https://astral.sh/uv/install.sh | sh`)*

*2.2 Windows:*
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**3. Instale as dependências:**
```bash
uv add pandas scikit-learn matplotlib numpy
```

**4. Execute o main:**
```bash
uv run main.py
```

# EN-US

# Predictive Urban Simulator (Micro-MVP)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)

> ⚠️ **Notice:** This repository contains only a Minimum Viable Product (MVP) / Proof of Concept (PoC). It represents a "Micro" version of a much larger research project that will serve as the basis for my Bachelor's Thesis in Information Systems.

## About this Repository (The MVP)
The goal of this codebase is to quickly prove and validate the core concept of my research: the feasibility of visually simulating the cause-and-effect relationship between socioeconomic indicators (such as unemployment and school dropout rates) and urban crime rates.

To ensure agility during this validation stage, the current architecture was intentionally simplified:
* **Analytical Backend:** Uses a *Random Forest Regressor* model (via `scikit-learn`) trained with tabular data for rapid inference.
* **Visual Frontend:** Uses the `matplotlib` library with native widgets to generate an interactive 2D heatmap, representing a generic urban grid.
* **Environment Management:** Structured in a modern and isolated way using `uv`.

### Interactive Demonstration
*(Drag and drop the video/GIF of your screen recording adjusting the sliders here)*

---

## The Future of the Project (Thesis Scope)
The final project that will succeed this repository will feature much higher architectural and mathematical complexity, applying state-of-the-art Digital Twins for data-driven public management. 

The mapped evolutions for the main Thesis repository include:

| Component | Current Version (This Repo) | Final Version (Thesis) |
| :--- | :--- | :--- |
| **Visual Interface** | Interactive 2D chart with *Matplotlib* | Interactive simulation environment built on the **Godot 4** engine. |
| **Predictive Model** | Basic *Random Forest* algorithm | **Custom Neural Network**, optimized to identify complex spatio-temporal correlations. |
| **Architecture** | Isolated monolithic script | **Microservices**, with complete decoupling via WebSockets for ultra-low latency communication between the AI (Python backend) and rendering (Godot frontend). |
| **Data** | Generic generation and mapping | Real-world data and map format of **Rio de Janeiro** (integrating open government databases). |

---

## How to run this MVP locally

This project uses the [UV](https://github.com/astral-sh/uv) package manager to ensure speed and isolated environments.

**1. Clone the repository:**
```bash
git clone https://github.com/hugoprd/urban-simulator
cd urban-simulator
```

**2. Install UV:**
*2.1 Linux:*
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

*(If your system lacks curl, use wget: `wget -qO- https://astral.sh/uv/install.sh | sh`)*

*2.2 Windows:*
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**3. Instale dependencies:**
```bash
uv add pandas scikit-learn matplotlib numpy
```

**4. Run the main script:**
```bash
uv run main.py
```