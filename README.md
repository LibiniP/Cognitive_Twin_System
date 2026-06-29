# Cognitive Twin for Astronaut Decision Prediction and Error Prevention

A proof-of-concept AI system that predicts potential astronaut decision errors in simulated microgravity environments and provides proactive haptic feedback before incorrect actions occur.

> Developed as a research prototype to explore personalized Cognitive Digital Twins for improving astronaut decision support and space mission safety.

---

## Overview

Spatial disorientation is one of the most significant human-factor risks during space missions. In microgravity, astronauts can confidently perform incorrect actions because vestibular and visual cues become unreliable.

This project proposes a **Cognitive Twin**—a personalized AI model that continuously learns an astronaut's decision-making patterns and predicts high-risk actions before they occur.

The system demonstrates how sequential behavioral data can be analyzed using deep learning to enable proactive intervention through wearable haptic feedback, helping astronauts verify their actions before errors occur.

---

## Features

* Personalized Cognitive Twin for each astronaut
* Sequential behavior modeling using LSTM neural networks
* Prediction of high-risk decision errors
* Real-time inference pipeline (proof of concept)
* Wearable haptic feedback trigger simulation
* Adaptive architecture for continuous personalization
* WebSocket-based communication between AI and VR simulator

---

## System Architecture

```
Sensor Data
     │
     ▼
Preprocessing
     │
     ▼
LSTM Prediction Model
     │
Risk Score Generation
     │
     ▼
Decision Threshold
     │
 ┌───────────────┐
 │ High Risk?    │
 └──────┬────────┘
        │ Yes
        ▼
Haptic Feedback Trigger
```

---

## Tech Stack

* Python
* PyTorch
* NumPy
* Pandas
* Scikit-learn
* Streamlit
* Node.js
* Express.js
* WebSockets
* LSTM Neural Networks
* Wearable Haptic Feedback (Prototype)

---

## Methodology

### 1. Data Collection

Simulated astronaut task sequences are generated, including:

* Sequential sensor readings
* Motion data
* Head orientation
* Task context
* Reaction time
* Intended versus actual movement

---

### 2. Model Training

An LSTM-based Cognitive Twin learns temporal behavioral patterns that precede incorrect astronaut actions.

The trained model outputs the probability that an upcoming decision will be incorrect.

---

### 3. Real-Time Prediction

Incoming sensor streams are processed continuously.

The Cognitive Twin predicts whether the astronaut is likely to perform an incorrect action before execution.

---

### 4. Intervention

If the predicted risk exceeds a predefined threshold:

* A wearable device triggers haptic feedback.
* The astronaut receives a warning before executing the action.
* The system encourages action verification without interrupting mission workflow.

---

## Repository Structure

```
.
├── README.md
├── astronaut_disorientation_dataset.csv
├── cognitive_twin_engine.py
├── SheNav_AI_code.ipynb
├── SheNav_VR.ipynb
├── server.js
├── index.html
├── requirements.txt
└── package.json
```

---

## File Descriptions

* **README.md** – Project overview, methodology, architecture, and usage instructions.
* **astronaut_disorientation_dataset.csv** – Synthetic astronaut behavioral dataset used for training and evaluation.
* **cognitive_twin_engine.py** – Core Cognitive Twin inference engine.
* **SheNav_AI_code.ipynb** – Data preprocessing, feature engineering, model training, and experimentation.
* **SheNav_VR.ipynb** – VR simulation workflow used for synthetic data generation.
* **server.js** – WebSocket server connecting the VR simulator and Cognitive Twin AI engine.
* **index.html** – Browser-based interface for interacting with the prototype.
* **requirements.txt** – Python dependencies.
* **package.json** – Node.js dependencies.

---

## Demonstration Workflow

The prototype consists of three interconnected components:

1. **VR Simulator**
2. **Cognitive Twin AI Engine**
3. **Real-Time WebSocket Communication Server**

Workflow:

```
VR Simulator
      │
      ▼
Sensor Streams
      │
      ▼
Cognitive Twin
      │
Risk Prediction
      │
      ▼
Haptic Alert
      │
      ▼
Astronaut Action Correction
```

The Cognitive Twin continuously analyzes incoming behavioral sequences and predicts high-risk decisions before execution, triggering simulated haptic warnings when necessary.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/LibiniP/Cognitive_Twin_System.git
cd Cognitive_Twin_System
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

Install Node.js dependencies:

```bash
npm install
```

---

## Running the Project

Start the WebSocket server:

```bash
node server.js
```

Run the AI engine:

```bash
python cognitive_twin_engine.py
```

Or open the Jupyter notebook:

```bash
jupyter notebook SheNav_AI_code.ipynb
```

---

## Future Improvements

* Integration with VR-based astronaut simulators
* Transformer-based sequence models
* Federated learning across astronaut crews
* Personalized online learning
* Real wearable haptic device integration
* Edge AI deployment for onboard spacecraft systems

---

## Applications

* Space mission safety
* Human-AI collaboration
* Cognitive Digital Twins
* Human reliability prediction
* Aerospace decision support
* Adaptive astronaut assistance systems

---

## Status

**Proof of Concept (POC)**

This project demonstrates the feasibility of using personalized AI models to predict astronaut decision errors before execution. It is intended for research, educational, and prototype demonstration purposes.

---

## Disclaimer

This project uses simulated astronaut behavioral data and demonstrates the concept of Cognitive Digital Twins. It is not intended for operational deployment in real space missions.

---

## Authors

**P. Libini**

B.Tech Computer Science Engineering (Artificial Intelligence)

Amrita Vishwa Vidyapeetham

---

## License

This project is intended for academic, educational, and research purposes.
