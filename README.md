# 📝 Todo_Folio

A simple and elegant portfolio + todo web app built with **Flask**, designed to showcase personal info and manage tasks using a clean Bootstrap interface.


## 🔗 Live Demo

🚀 Deployed at: [[https://your-live-link-here.com](https://todo-render-2-yelb.onrender.com)]

---

## 📌 Features

- 🔐 Flask-powered backend
- 🎨 Bootstrap 5 UI design
- 🧠 "About Me" section to showcase personal profile
- ✅ Create, Update, Delete tasks
- 📅 Tasks saved with timestamps
- 🗂 SQLite for persistent local storage
- 🌐 Responsive design, mobile-ready

---

## 📂 Project Structure

Todo_Folio/

├── app.py # Main Flask application

├── templates/ # HTML templates (Jinja2)

│ ├── base.html

│ ├── home.html

│ ├── update.html

│ └── ...

├── static/ # CSS, JS, images (if any)

├── requirements.txt # Python dependencies

└── README.md # Project overview



---

## ⚙️ Setup Instructions

### 1. Clone the repository

git clone https://github.com/sanjayzorojuro/Todo_Folio.git
cd Todo_Folio

2. Create virtual environment and activate it
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # For Linux/macOS
# OR
venv\Scripts\activate     # For Windows

3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt

5. Run the app locally
bash
Copy
Edit
python app.py
Visit http://127.0.0.1:5000 in your browser.



🚀 Deployment
This app can be deployed to platforms like:

Render

Railway

Fly.io

Heroku (paid plans only)



Example start command for deployment:
bash

Copy

Edit

gunicorn app:app




🛠 Built With

Flask

Bootstrap 5

Jinja2

SQLite

sqlalchemy

python3

Html

Render




📜 License
This project is open source and available under the MIT License.





