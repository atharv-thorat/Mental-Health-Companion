 Hand Gesture Recognition Game Simulator

## Overview

The **Hand Gesture Recognition Game Simulator** is a real-time computer vision system that uses a webcam to detect hand movements and translate predefined gestures into game control commands. The project demonstrates how **human–computer interaction (HCI)** can be enhanced using **gesture-based input** instead of traditional controllers like keyboards or mice.

The system is built using **MediaPipe Hand Tracking** and **OpenCV**, enabling accurate hand landmark detection and gesture recognition in real time.

---

## Project Objectives

* Capture real-time video input using a webcam
* Detect and track hand landmarks accurately
* Recognize static and dynamic hand gestures
* Map gestures to game control actions
* Simulate touchless game interaction

---

## Key Features

* Real-time webcam-based hand tracking
* Landmark-level hand detection using MediaPipe
* Rule-based gesture recognition logic
* Gesture-to-game-action mapping
* Modular pipeline for easy extension
* Lightweight and CPU-efficient implementation

---

## Workflow & File Description

```
01_webcam_test.py
        ↓
02_hand_landmarks.py
        ↓
03_hand_gesture_recognition.py
        ↓
04_gesture_game_control.py
```

### File Responsibilities

#### `01_webcam_test.py`

* Verifies webcam connectivity
* Displays live video feed
* Used for camera debugging and calibration

#### `02_hand_landmarks.py`

* Detects hand landmarks using MediaPipe
* Extracts 21 key points per hand
* Visualizes landmarks on the video stream

#### `03_hand_gesture_recognition.py`

* Analyzes landmark positions
* Classifies gestures based on finger states and angles
* Acts as the gesture recognition engine

#### `04_gesture_game_control.py`

* Maps recognized gestures to game actions
* Simulates control commands (e.g., move, jump, shoot)
* Represents the final interaction layer

---

## Technology Stack

* **Programming Language:** Python
* **Computer Vision:** OpenCV
* **Hand Tracking:** MediaPipe
* **Real-Time Processing:** Webcam feed
* **Game Control Logic:** Python event mapping

---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/hand-gesture-game-simulator.git
cd hand-gesture-game-simulator
```

### 2. Create Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies

```bash
pip install opencv-python mediapipe numpy
```

---

## How to Run

### Step 1: Test Webcam

```bash
python 01_webcam_test.py
```

### Step 2: Verify Hand Landmark Detection

```bash
python 02_hand_landmarks.py
```

### Step 3: Run Gesture Recognition

```bash
python 03_hand_gesture_recognition.py
```

### Step 4: Start Gesture-Based Game Control

```bash
python 04_gesture_game_control.py
```

---

## Supported Gestures (Example)

* Open Palm → Start / Move Forward
* Closed Fist → Stop
* Index Finger Up → Jump
* Two Fingers → Action / Shoot

*(Gestures can be extended or modified easily.)*

---

## Use Cases

* Gesture-controlled games
* Touchless user interfaces
* Virtual reality (VR) interaction systems
* Accessibility tools
* HCI research and experimentation

---

## Why This Project Is Important

Traditional input devices limit natural interaction. This project:

* Demonstrates **vision-based control systems**
* Enables **contactless interaction**
* Showcases real-time AI + CV integration
* Serves as a foundation for AR/VR and smart interfaces

It strongly aligns with **AI, Computer Vision, and Human–Computer Interaction** domains.

---

## Future Enhancements

* Dynamic gesture recognition (temporal modeling)
* Deep learning–based gesture classification
* Multi-hand and multi-user support
* Integration with Unity or Unreal Engine
* Custom gesture training module


