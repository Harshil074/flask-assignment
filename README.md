# Flask Git Workflow Assignment

This repository demonstrates advanced Git operations using a Flask-based project as part of an academic assignment.

---

## 🚀 Objective
To understand and implement real-world Git workflows including branching, merging, conflict resolution, reset, and rebasing.

---

## 🛠️ Technologies Used
- Git & Git Bash
- GitHub (SSH authentication)
- Python (Flask)
- HTML
- Nano Editor
- Windows OS

---

## 📂 Branch Strategy
- **main** – Stable production-ready branch
- **Harshil** – Initial Flask project setup
- **Harshil_new** – JSON API update branch
- **master_1** – Frontend (To-Do page)
- **master_2** – Backend (API route)

---

## ✨ Features Implemented
- SSH-based secure GitHub authentication
- Flask backend with REST API
- HTML-based To-Do frontend
- JSON-based API data handling
- Clean and traceable Git commit history

---

## 🔀 Git Operations Covered
- Branch creation and deletion
- Merging branches into main
- Merge conflict resolution
- `git reset --soft`
- Interactive rebasing without squashing commits
- Force pushing after history rewrite

---

## 🔌 Backend API
### POST `/submittodoitem`
Accepts JSON data:
```json
{
  "itemName": "Sample Task",
  "itemDescription": "Task description"
}
