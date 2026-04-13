# 🚀 Full Stack Web Application (React + Flask)

## 📌 Project Overview

This project is a full-stack web application built using **React.js** for the frontend and **Python Flask** for the backend.

The application demonstrates **frontend–backend integration**, **REST API communication**, and **data structure implementation**.

It provides two main functionalities:

* 🧮 Calculator
* 🔗 Linked List Operations

---

## 🛠️ Technologies Used

### Frontend

* React.js
* Axios
* HTML, CSS (Styled UI)

### Backend

* Python
* Flask
* Flask-CORS

---

## ⚙️ Features

### 🧮 Calculator Module

* Addition
* Subtraction
* Multiplication
* Division
* Handles invalid inputs and division by zero
* Displays results dynamically

---

### 🔗 Linked List Module

* Insert node
* Delete node
* Search node
* Display current linked list
* Implemented using **Singly Linked List in Python**

---

## 🔗 API Endpoints

### Calculator API

**POST** `/calculate`

Request:

```json
{
  "num1": 10,
  "num2": 5,
  "operation": "add"
}
```

Response:

```json
{
  "result": 15
}
```

---

### Linked List API

**POST** `/linkedlist`

Request:

```json
{
  "operation": "insert",
  "value": 10
}
```

Response:

```json
{
  "list": [10]
}
```

---

## 🖥️ Project Structure

```
fullstack-react-flask-app/
│
├── backend/
│   ├── app.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── .gitignore
└── README.md
```

---

## ▶️ How to Run the Project

### 🔹 Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate   (Windows)
pip install -r requirements.txt
python app.py
```

Backend runs on:

```
http://localhost:5000
```

---

### 🔹 Frontend Setup

Open a new terminal:

```bash
cd frontend
npm install
npm start
```

Frontend runs on:

```
http://localhost:3000
```

---

## 🔄 How It Works

* The React frontend sends HTTP requests using Axios.
* Flask backend processes the request.
* Backend returns JSON response.
* UI updates dynamically based on response.

---

## ⚠️ Important Notes

* Backend must be running before frontend.
* If backend is stopped, frontend will show **Network Error / Server Error**.
* Ensure ports 3000 and 5000 are available.

---

## 🚀 Deployment (Optional)

* Frontend → Vercel / Netlify
* Backend → Render / Railway

Update API URL in frontend after deployment.

---

## 📸 Screenshots

(Add your screenshots here)

---

## 👨‍💻 Author

**Naveen Sudhagar**
📧 [naveensudhagar333@gmail.com](mailto:naveensudhagar333@gmail.com)

---

## 🎯 Conclusion

This project helped in understanding:

* Full-stack development
* REST API integration
* Data structures in backend
* Real-time UI updates

---
