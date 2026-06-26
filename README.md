# Cognitive Twin for Astronaut Decision Prediction and Error Prevention

A proof-of-concept AI system that predicts potential astronaut decision errors in simulated microgravity environments and provides proactive haptic feedback before incorrect actions occur.

> Developed as a research prototype to explore personalized cognitive digital twins for space mission safety.

---

## Overview

Spatial disorientation is one of the biggest human-factor risks during space missions. In microgravity, astronauts can confidently make incorrect decisions because vestibular and visual cues become unreliable.

This project proposes a **Cognitive Twin**—a personalized AI model that learns an individual's decision-making patterns and predicts high-risk actions before they occur.

The system demonstrates how sequential sensor data can be analyzed using deep learning to enable proactive intervention through wearable haptic feedback.

---

## Features

- Personalized cognitive twin for each astronaut
- Sequential behavior modeling using LSTM networks
- Prediction of high-risk decision errors
- Real-time inference pipeline (proof of concept)
- Wearable haptic feedback trigger simulation
- Adaptive architecture for continuous personalization

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
        │Yes
        ▼
Haptic Feedback Trigger
```

---

## Tech Stack

- Python
- TensorFlow / Keras
- NumPy
- Pandas
- Scikit-learn
- LSTM Networks
- Edge AI (Concept)
- Wearable Haptic Feedback (Prototype)

---

## Methodology

### 1. Data Collection

Simulated astronaut task sequences are collected, including:

- Sequential sensor readings
- Motion data
- Task context
- Reaction time
- Intended vs actual movement

---

### 2. Model Training

An LSTM network learns temporal patterns that precede incorrect actions.

The model outputs a probability of an upcoming decision error.

---

### 3. Real-Time Prediction

Incoming sensor streams are processed continuously.

The trained model predicts whether the astronaut is likely to perform an incorrect action.

---

### 4. Intervention

If the predicted risk exceeds a threshold,

- A wearable device triggers haptic feedback
- The astronaut is prompted to verify the intended action before execution

---

## Repository Structure

```
.
├── README.md                              # Project documentation
├── astronaut_disorientation_dataset.csv   # Simulated astronaut sensor and task dataset used for model training
├── cognitive_twin_engine.py               # Core Cognitive Twin prediction engine and inference pipeline
├── SheNav_AI_code.ipynb                   # Jupyter notebook for model training, evaluation, and experimentation
├── SheNav_VR.ipynb                        # VR simulation workflow and data generation notebook
├── server.js                              # Backend server for real-time prediction API
└── index.html                             # Frontend interface for demonstrating the Cognitive Twin system
```

### File Descriptions

* **README.md** – Overview of the project, methodology, architecture, and usage instructions.

* **astronaut_disorientation_dataset.csv** – Synthetic dataset containing simulated astronaut sensor readings, task context, and labels used to train the Cognitive Twin model.

* **cognitive_twin_engine.py** – Implements the prediction pipeline, processes sequential inputs, loads the trained model, and generates decision-risk predictions.

* **SheNav_AI_code.ipynb** – Contains data preprocessing, feature engineering, model training, evaluation metrics, and experimental analysis.

* **SheNav_VR.ipynb** – Demonstrates the virtual reality simulation used to generate astronaut task scenarios and collect synthetic behavioral data.

* **server.js** – Node.js backend that serves prediction requests and connects the frontend with the AI inference engine.

* **index.html** – Web-based interface for interacting with the Cognitive Twin prototype and visualizing prediction results.


---

## Future Improvements

- Integration with VR-based astronaut simulators
- Transformer-based sequence models
- Federated learning across astronaut crews
- Personalized online learning
- Real wearable device integration
- Deployment on edge hardware

---

## Applications

- Space mission safety
- Human-AI collaboration
- Cognitive digital twins
- Human reliability prediction
- Aerospace decision support systems

---

## Status

**Proof of Concept (POC)**

This project demonstrates the feasibility of using personalized AI models to predict astronaut decision errors before execution. It is intended for research and educational purposes.

---

## Authors

**P. Libini**

B.Tech Computer Science Engineering (Artificial Intelligence)

Amrita Vishwa Vidyapeetham

---

## License

This project is intended for academic and research purposes.
