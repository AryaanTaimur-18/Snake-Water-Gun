# 🐍 Snake Water Gun

A modern implementation of the classic **Snake Water Gun** game built with **Python (Flask)** and a clean, responsive **HTML/CSS/JavaScript** frontend.

The game features a modern dark-themed interface, live score tracking, match history, and server-side game logic powered by Python.

---

## 🚀 Features

* 🎮 Play Snake, Water, or Gun against the computer
* 🐍 Snake drinks Water
* 💧 Water douses Gun
* 🔫 Gun shoots Snake
* 📊 Live score tracking
* 📝 Recent match history
* 🌙 Modern dark-themed UI
* ⚡ Flask-powered backend
* 🔒 Game logic handled entirely in Python

---

## 🛠️ Tech Stack

### Backend

* Python 3
* Flask

### Frontend

* HTML5
* CSS3
* JavaScript (Fetch API)

---

## 📂 Project Structure

```text
SnakeWaterGun/
│
├── app.py
│
├── templates/
│   └── index.html
│
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/snake-water-gun.git
cd snake-water-gun
```

### 2. Create a virtual environment (optional)

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\\Scripts\\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install flask
```

---

## ▶️ Running the Project

Start the Flask server:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## 🎲 Game Rules

| Player Choice | Beats    |
| ------------- | -------- |
| Snake 🐍      | Water 💧 |
| Water 💧      | Gun 🔫   |
| Gun 🔫        | Snake 🐍 |

Examples:

* 🐍 Snake vs 💧 Water → Player Wins
* 💧 Water vs 🔫 Gun → Player Wins
* 🔫 Gun vs 🐍 Snake → Player Wins

Matching choices result in a draw.

---

## 📸 Screenshots


markdown
<img width="100%" alt="Screenshot 2026-06-19 160816" src="https://github.com" />





---

## 🔮 Future Improvements

* Sound effects
* Leaderboard system
* Multiplayer support
* Difficulty levels
* Persistent score storage
* Enhanced animations

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

Aryaan

Built as a Flask learning project to combine Python backend development with modern frontend design.
