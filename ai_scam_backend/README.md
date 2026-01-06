🛡️ AI Scam Detector

AI Scam Detector — это веб-приложение для анализа текстовых сообщений и определения уровня риска мошенничества.
Проект реализует гибридный AI-подход, объединяющий семантическое машинное обучение и детерминированные правила для критических сценариев.

✨ Основные возможности

🌍 Многоязычная поддержка
English · Русский · Español · Português · Қазақша

🧠 Семантический AI-анализ
На основе sentence embeddings и cosine similarity

⚠️ Трёхуровневая классификация сообщений

🟢 Safe — безопасное сообщение

🟡 Dangerous — потенциально опасное сообщение

🔴 Scam — мошенничество

📊 Визуализация риска
Цветовая индикация + шкала confidence

🔗 REST API
Для интеграции с другими системами

## 🧩 System Architecture

The system follows a layered architecture with a clear separation
between presentation, API, and AI logic.

```text
┌──────────────────────┐
│      User (Web)      │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│   Flutter Web UI     │
│  (Risk Visualization)│
└──────────┬───────────┘
           │ HTTP (JSON)
           ▼
┌──────────────────────┐
│   FastAPI Backend    │
│      REST API        │
└──────────┬───────────┘
           │
           ▼
┌────────────────────────────────────┐
│        Hybrid Analysis Engine       │
│                                    │
│  ┌─────────────┐   ┌─────────────┐ │
│  │ Rule-based  │   │ Semantic AI │ │
│  │  Detection  │   │ (Embeddings)│ │
│  └──────┬──────┘   └──────┬──────┘ │
│         │                 │        │
│         └───────┬─────────┘        │
│                 ▼                  │
│        Risk Aggregation Logic       │
│      (Safe / Dangerous / Scam)      │
└────────────────────┬───────────────┘
                     │
                     ▼
              JSON Response
##

🧠 AI-подход

В проекте используется гибридная модель анализа, аналогичная реальным антифрод-системам.

🔹 Rule-based анализ (Safety Net)

Детерминированные правила применяются для критических сценариев, где ошибка недопустима:

банковский фишинг

запрос подтверждения личных данных

имитация уведомлений служб безопасности

Такие сообщения немедленно классифицируются как мошенничество.

🔹 Semantic AI (основной AI-компонент)

Для оценки риска используется семантическое сравнение текста с эталонными мошенническими сценариями:

многоязычная модель Sentence Transformers

вычисление cosine similarity между эмбеддингами

устойчивость к языку и формулировкам

Результат интерпретируется как уровень риска (0.0 – 1.0).

🚀 Установка и запуск
🔧 Backend (FastAPI)
cd ai_scam_backend
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
Backend будет доступен по адресу:
👉 http://127.0.0.1:8000
🎨 Frontend (Flutter Web)
cd ai_scam_web
flutter pub get
flutter run -d chrome
🔌 REST API
POST /analyze
{
  "text": "Your bank account has been suspended. Verify your identity."
}
Ответ:
{
  "language": "en",
  "verdict": "scam",
  "confidence": 0.95,
  "signals": ["phishing"],
  "method": "semantic AI + rules"
}
🧪 Примеры тестирования
| Сообщение                          | Результат    |
| ---------------------------------- | ------------ |
| `Привет, ты завтра свободен?`      | 🟢 Safe      |
| `Можешь перевести деньги сегодня?` | 🟡 Dangerous |
| `Guaranteed profit with no risk`   | 🟡 Dangerous |
| `Подтвердите данные банка`         | 🔴 Scam      |

🎓 Назначение проекта

Проект разработан в рамках дипломной работы и демонстрирует:

практическое применение AI в задачах кибербезопасности

использование многоязычных семантических моделей

гибридный подход к обнаружению мошенничества

🛠 Используемые технологии

Backend: FastAPI, Python

AI: Sentence Transformers, PyTorch

Frontend: Flutter Web

ML-подход: Semantic similarity + rule-based filtering
