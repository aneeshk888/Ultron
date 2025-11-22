# Ultron 🧑‍⚕️🤖

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

<img width="674" height="890" alt="Screenshot 2025-10-18 191919" src="https://github.com/user-attachments/assets/190a88e4-4799-4360-a7fa-0d1a93772811" />
<img width="675" height="912" alt="Screenshot 2025-10-18 191102" src="https://github.com/user-attachments/assets/b0ed6c1e-ddfd-4646-9c1b-fb79d82857e5" />
<img width="925" height="464" alt="Screenshot 2025-10-15 134540" src="https://github.com/user-attachments/assets/838952c5-d2b6-4cc4-8699-653cfd0a6bbf" />
<img width="659" height="352" alt="Screenshot 2025-10-15 132048" src="https://github.com/user-attachments/assets/d95f8c3c-e95c-419e-b487-14d1be5675c1" />
<img width="511" height="724" alt="Screenshot 2025-10-11 134222" src="https://github.com/user-attachments/assets/b33665ec-fcfc-482d-b612-34595a84b0c2" />
<img width="896" height="452" alt="Screenshot 2025-10-09 203421" src="https://github.com/user-attachments/assets/602b4dcd-4c3b-4296-a3b4-2c5cd3b75971" />
<img width="1052" height="765" alt="Screenshot 2025-10-09 203029" src="https://github.com/user-attachments/assets/92207461-78d3-4049-b666-c610347c0175" />
<img width="682" height="312" alt="Screenshot 2025-09-30 015102" src="https://github.com/user-attachments/assets/48fad353-3a5a-4127-99e6-ed28dfbbe64a" />
<img width="1209" height="745" alt="Screenshot 2025-09-19 192652" src="https://github.com/user-attachments/assets/f92dc490-963f-475e-b545-fad34f18d4d5" />
<img width="288" height="587" alt="Screenshot 2025-09-19 032520" src="https://github.com/user-attachments/assets/b12903b3-18ed-4261-b04a-d5f211e63e56" />
<img width="1167" height="655" alt="Screenshot 2025-09-16 201050" src="https://github.com/user-attachments/assets/7f2f41a4-6cf6-4f79-944c-a8a6b79bc598" />
<img width="936" height="529" alt="Screenshot 2025-09-16 194724" src="https://github.com/user-attachments/assets/03529413-fb6a-4d13-aa9b-a15f5e6346df" />
<img width="1411" height="329" alt="Screenshot 2025-09-13 051706" src="https://github.com/user-attachments/assets/595cbb9d-8760-40da-9f02-561c78fc03c6" />
<img width="1354" height="288" alt="Screenshot 2025-09-13 051639" src="https://github.com/user-attachments/assets/e2a95641-7a26-4874-afba-6241551644f1" />
<img width="1350" height="371" alt="Screenshot 2025-09-13 051421" src="https://github.com/user-attachments/assets/d7b851be-3011-4b51-b24e-7cd28ae16700" />
<img width="1421" height="292" alt="Screenshot 2025-09-13 051355" src="https://github.com/user-attachments/assets/102ed2bd-ab16-421b-b138-a5889cc40a8d" />
<img width="1368" height="280" alt="Screenshot 2025-09-13 051329" src="https://github.com/user-attachments/assets/36e60430-4132-4d42-b891-d12a9ee25a95" />
<img width="1371" height="294" alt="Screenshot 2025-09-13 051301" src="https://github.com/user-attachments/assets/7eee326d-d97c-4027-a997-25d2efe70338" />
<img width="1360" height="326" alt="Screenshot 2025-09-13 020330" src="https://github.com/user-attachments/assets/872d8ac5-d2f7-41bd-8a72-36de7a72968a" />
<img width="1390" height="385" alt="Screenshot 2025-09-13 015951" src="https://github.com/user-attachments/assets/7185e44e-b677-4614-bd8c-c781bfd49546" />
<img width="1355" height="304" alt="Screenshot 2025-09-10 182535" src="https://github.com/user-attachments/assets/fc623665-4ef1-439f-8e7b-2fa32edf56d5" />
<img width="1376" height="358" alt="Screenshot 2025-09-10 182438" src="https://github.com/user-attachments/assets/6e04aee4-3111-4656-bfb8-043651e64519" />
<img width="1377" height="314" alt="Screenshot 2025-09-10 174330" src="https://github.com/user-attachments/assets/85ee4b41-15de-48d8-a663-5e2d7436ae32" />
<img width="1357" height="272" alt="Screenshot 2025-09-10 174151" src="https://github.com/user-attachments/assets/8948865e-ce3a-467e-ac5b-660d01bf8acb" />
<img width="1077" height="377" alt="Screenshot 2025-09-08 165603" src="https://github.com/user-attachments/assets/b49482b1-c668-41e0-afcf-6938bcf8dda9" />
<img width="688" height="254" alt="Screenshot 2025-09-08 165538" src="https://github.com/user-attachments/assets/128a5aa2-28b3-4dcd-aca1-7c6816472065" />
<img width="452" height="92" alt="Screenshot 2025-09-08 160919" src="https://github.com/user-attachments/assets/ca337d71-e5ec-4e59-8d7f-0a5b279de03f" />
<img width="1886" height="854" alt="Screenshot 2025-11-08 133539" src="https://github.com/user-attachments/assets/66356ecf-6ad0-447f-a7fd-bcd87d6a52e0" /><img width="1579" height="750" alt="Screenshot 2025-11-22 144837" src="https://github.com/user-attachments/assets/355e1b2b-b3b0-4ab0-a015-1a6c6a105d1e" />
<img width="995" height="817" alt="Screenshot 2025-11-08 140023" src="https://github.com/user-attachments/assets/67e49d63-8aa7-4627-bd3e-be4f15e485fd" /><img width="1568" height="746" alt="Screenshot 2025-11-22 144852" src="https://github.com/user-attachments/assets/e422a122-43cc-4b18-bb0a-d94798fc34fb" />
<img width="1897" height="834" alt="Screenshot 2025-11-08 133354" src="https://github.com/user-attachments/assets/381db725-cc81-4713-9f20-527297f5fe94" /><img width="1579" height="747" alt="Screenshot 2025-11-22 144922" src="https://github.com/user-attachments/assets/397bac86-333e-4610-85f3-d1686adb5ee1" />
<img width="577" height="110" alt="Screenshot 2025-09-08 160852" src="https://github.com/user-attachments/assets/62b080a5-96a3-4e5f-8d79-8cea8eeda381" />
<img width="796" height="798" alt="Screenshot 2025-05-13 171555" src="https://github.com/user-attachments/assets/3f625ef8-4a2c-479a-8ca9-9f37a7731d96" />
<img width="1585" height="203" alt="Screenshot 2025-11-22 145635" src="https://github.com/user-attachments/assets/a6194757-c13c-4f6d-a52e-1972627d43b6" />
<img width="1918" height="897" alt="Screenshot 2025-11-22 145553" src="https://github.com/user-attachments/assets/abfdc78f-a9c1-480f-9850-77b3777c56c4" />
<img width="1903" height="884" alt="Screenshot 2025-11-22 145546" src="https://github.com/user-attachments/assets/1df1c3d0-c6b8-41c7-9baf-2f40f683dde5" />
<img width="1919" height="877" alt="Screenshot 2025-11-22 145538" src="https://github.com/user-attachments/assets/595dd9a9-29e5-42f0-835e-28dc97818c08" />
<img width="1889" height="893" alt="Screenshot 2025-11-22 145455" src="https://github.com/user-attachments/assets/fbb85716-bfec-4212-b501-c70b74848631" />
<img width="1904" height="826" alt="Screenshot 2025-11-22 145408" src="https://github.com/user-attachments/assets/68292ba7-c00e-45c9-ba35-07ba3d1cb479" />
<img width="1919" height="870" alt="Screenshot 2025-11-22 145343" src="https://github.com/user-attachments/assets/381e3e37-4a1d-46ac-a462-820ac1719c24" />
<img width="1919" height="877" alt="Screenshot 2025-11-22 145329" src="https://github.com/user-attachments/assets/68cddf7a-6b1d-42e5-89e9-8f117941fb23" />
<img width="1918" height="866" alt="Screenshot 2025-11-22 145253" src="https://github.com/user-attachments/assets/fc12be82-35bb-4a03-ac19-e4cf23518615" />
<img width="1557" height="755" alt="Screenshot 2025-11-22 145020" src="https://github.com/user-attachments/assets/eab0766a-edb4-4303-b018-d3fc6e8eb316" />
<img width="1579" height="749" alt="Screenshot 2025-11-22 145001" src="https://github.com/user-attachments/assets/9ab3de72-604e-4319-974b-9157753d83ce" />
<img width="1571" height="740" alt="Screenshot 2025-11-22 144949" src="https://github.com/user-attachments/assets/6a1fe5db-2502-4e35-9a5c-53c968589b9b" />
<img width="1566" height="745" alt="Screenshot 2025-11-22 144937" src="https://github.com/user-attachments/assets/04864fbc-799e-4e56-92d5-a28b94f91ab0" />


# Contributing to Ultron

First off, thank you for considering contributing to **Ultron** 🙌.  
This project thrives on collaboration, and we welcome improvements, bug fixes, new agents, and documentation enhancements.

---

## 🧩 How to Contribute

### 1. Fork the Repository
Create your own fork of the project to work independently.

### 2. Clone Your Fork
```bash
git clone https://github.com/<your-username>/Ultron.git
cd Ultron

### 3. Create a Branch
git checkout -b feature/add-sleep-care-agent<img width="1914" height="831" alt="Screenshot 2025-11-08 133410" src="https://github.com/user-attachments/assets/fc53e93b-c46f-459c-b79c-2b836b22e9d0" />




MIT License

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
