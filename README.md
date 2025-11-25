# Ultron 🧑‍⚕️🤖

## 📌 Mindmap
<img width="5178" height="9537" alt="NotebookLM Mind Map (1)" src="https://github.com/user-attachments/assets/9782dfb2-99a7-4699-b84d-d98efd80148c" />



## 📌 Summary
Ultron is a unified health‑care AI system designed to simplify wellness management. Instead of searching for separate solutions for hair, skin, diet, and fitness, Ultron aggregates specialized agents into one orchestrated framework. The **Health Aggregator Agent** ensures all domains work together seamlessly, giving users a clear, reproducible, and holistic experience.

---

## 📌 Problem Statement
Healthcare often feels fragmented — users must search for separate AI solutions for hair care, skin care, diet, gym, and more. This makes holistic wellness management confusing and inefficient.  

**Ultron** solves this by aggregating specialized agents into one unified system. The **Health Aggregator Agent** orchestrates all domains, giving users a clear, one‑shot solution for body care.

---

## 🧩 Agents
Ultron is composed of modular agents, each responsible for a specific domain of health:

- 💇 **Hair Care Agent** – Personalized recommendations for hair health.  
- 🌿 **Skin Care Agent** – Routines, products, and preventive measures for skin wellness.  
- 🥗 **Diet Care Agent** – Nutritional guidance and diet planning.  
- 🏋️ **Gym Care Agent** – Workout routines, fitness tracking, and exercise optimization.  
- 🩺 **Health Aggregator Agent** – Central orchestrator integrating all agents seamlessly.  

---

## ⚙️ Tech Stack
- **Python** – Core language for agent development.  
- **Gemini CLI (Vibe Coding)** – Used to vibe code and orchestrate agent workflows.  
- **Google ADK** – For agent execution and web interface.  
- **Demo Images** – Included to visualize workflows and agent interactions.  

---

## 🚀 Getting Started

### Prerequisites
- Python (>= 3.10 recommended)  
- Gemini CLI installed (`pip install gemini-cli`)  
- Google ADK installed (`pip install google-adk`)  
- Git  

### Installation
```bash
# Clone the repository
git clone https://github.com/aneeshk888/Ultron.git

# Navigate into the project directory
cd Ultron

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

# Install dependencies
pip install -r requirements.txt

# Start the vibe coding session with Gemini CLI
gemini vibe run

# Run directly with Python
python main.py

# Run a specific agent with ADK
adk run myagent

# Launch the web interface on port 2000
adk web --port 2000
```

### Architecture 
    User([User]) --> Aggregator[Health Aggregator Agent]

    Aggregator --> Hair[Hair Care Agent]
    Aggregator --> Skin[Skin Care Agent]
    Aggregator --> Diet[Diet Care Agent]
    Aggregator --> Gym[Gym Care Agent]

    Hair -->|Recommendations| Aggregator
    Skin -->|Routines| Aggregator
    Diet -->|Nutrition Plans| Aggregator
    Gym -->|Workout Plans| Aggregator

    Aggregator --> User







### Demo






# Contributing to Ultron

First off, thank you for considering contributing to **Ultron** 🙌.  
This project thrives on collaboration, and we welcome improvements, bug fixes, new agents, and documentation enhancements.

---

## 🧩 How to Contribute


```bash
### 1. Fork the Repository
Create your own fork of the project to work independently.

### 2. Clone Your Fork

git clone https://github.com/<your-username>/Ultron.git
cd Ultron

### 3. Create a Branch
git checkout -b feature/add-sleep-care-agent

```


MIT License

```bash
Copyright (c) 2025 Aneesh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
copies of the Software, and to permit persons to whom the Software is  
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in  
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN  
THE SOFTWARE.

```
