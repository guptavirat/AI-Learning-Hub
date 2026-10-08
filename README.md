# 🤖 AI Learning Hub

An interactive learning platform built using **Streamlit** to help users learn Artificial Intelligence concepts, track progress, and validate knowledge through quizzes.

## 🚀 Features

### 📚 Learn AI Topics

Explore AI concepts through structured learning modules:

- Artificial Intelligence
- Generative AI
- Agentic AI
- Prompt Engineering
- Machine Learning
- Deep Learning
- AI Applications

### 🔑 Concept Explorer

- Topic-wise concept navigation
- Support for subtopics
- Concept definitions loaded from JSON files
- Easy content management without code changes

### ✅ Progress Tracking

- Concept completion tracking
- Topic completion tracking
- Overall learning progress bar
- Visual completion indicators (✅)

### 📝 Knowledge Check

- Topic-wise quizzes
- Random question selection
- Score calculation
- Correct / Wrong / Unanswered statistics
- Optional answer review

---

## 🏗️ Project Structure

```text
AI-Learning-Hub/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── ai.json
│   ├── generative_ai.json
│   ├── agentic_ai.json
│   ├── prompt_engineering.json
│   ├── machine_learning.json
│   ├── deep_learning.json
│   └── ai apps.json
│
└── quizzes/
    ├── machine_learning_quiz.json
    ├── deep_learning_quiz.json
    └── generative_ai_quiz.json
```

---

## 📖 Topic JSON Format

```json
{
  "description": "Machine Learning enables systems to learn from data.",
  "concepts": {
    "Supervised Learning": "Learning from labeled data.",
    "Unsupervised Learning": "Learning from unlabeled data.",
    "Reinforcement Learning": "Learning through rewards and penalties."
  }
}
```

---

## 📖 Topic with Subtopics

```json
{
  "description": "Prompt Engineering is the art of designing effective prompts.",
  "subtopics": {
    "Prompt Basics": {
      "concepts": {
        "Zero-Shot Prompting": "Prompting without examples.",
        "Few-Shot Prompting": "Prompting with examples."
      }
    }
  }
}
```

---

## 📝 Quiz JSON Format

```json
{
  "quiz": [
    {
      "question": "What is supervised learning?",
      "options": [
        "Learning from labeled data",
        "Learning from unlabeled data",
        "Learning from images",
        "Learning from hardware"
      ],
      "answer": "Learning from labeled data"
    }
  ]
}
```

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## ☁️ Deployment

This application is deployed using:

- GitHub
- Streamlit Community Cloud

Any changes pushed to the main branch are automatically deployed.

---

## 🎯 Future Enhancements

- User authentication
- Learning paths
- Certificates
- AI Tutor / Copilot Integration
- Quiz history
- Progress persistence
- Leaderboards
- Admin content management

---

## 👨‍💻 Author

**Virat Gupta**

Manager | Learning & Development | AI Enthusiast

---

## ⭐ Support

If you found this project helpful, please consider starring the repository.
