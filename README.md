# Random Joke App

This is a full-stack app that shows a random joke every time you refresh or click a button — built with **React (frontend)** and **Flask (backend)**.

---

## 📁 Project Structure

laugh-api-app/
├── backend/ # Flask backend API
│ ├── src/app.py
│ └── requirements.txt
├── frontend/ # React frontend
│ ├── public/index.html
│ ├── src/App.js
│ ├── src/index.js
│ └── package.json
└── azure-pipelines.yml # Azure DevOps CI/CD

## Local Setup Instructions

### Backend (Flask)

1. Open terminal and run:

```bash
cd backend
python -m venv venv
venv\Scripts\activate     # On Windows
pip install -r requirements.txt
python src\app.py
```


2. Visit: http://localhost:5000/joke


### Frontend (React)

1. Open a new terminal:

bash
Copy
Edit
cd frontend
npm install
npm start

2. Visit: http://localhost:3000


## Troubleshooting
1. Failed to fetch in frontend → Make sure Flask backend is running
2. flask_cors not found → Run: pip install flask-cors
3. PowerShell won't activate venv → Use: Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned

### Azure CI/CD:

This project includes azure-pipelines.yml for Azure DevOps pipeline. It builds and deploys both frontend and backend.
