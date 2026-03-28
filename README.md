# 📚 BookHaven — Online Book Store (Django)

A full-stack Django web application for browsing and purchasing books, ready for production deployment.

---

## 🚀 Deploy to Render (Free Hosting)

### Step 1 — Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

### Step 2 — Create a Render account
Go to https://render.com and sign up (free).

### Step 3 — New Web Service
1. Click **New → Web Service**
2. Connect your GitHub account
3. Select your repository
4. Render will auto-detect `render.yaml` and fill in settings

### Step 4 — Set Environment Variables
In the Render dashboard → Environment tab, add:
| Key | Value |
|-----|-------|
| `SECRET_KEY` | (click "Generate" for a random value) |
| `DEBUG` | `False` |
| `GEMINI_API_KEY` | your Google Gemini key (optional) |

### Step 5 — Deploy!
Click **Deploy**. Render will:
- Install all packages from `requirements.txt`
- Run `python manage.py collectstatic`
- Run `python manage.py migrate`
- Start the server with `gunicorn`

Your site will be live at `https://bookhaven.onrender.com` (or similar).

---

## 🛠️ Create Admin User (after deploy)
In Render dashboard → your service → **Shell** tab:
```bash
python manage.py createsuperuser
```

---

## 💻 Run Locally
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Visit: http://127.0.0.1:8000
Admin: http://127.0.0.1:8000/admin/

---

## 📁 Project Structure
```
bookstore/
├── bookstore/         ← Config (settings.py, urls.py)
├── books/             ← Books app
├── cart/              ← Cart & Orders
├── subscribers/       ← Newsletter
├── templates/         ← HTML templates
├── static/            ← CSS, JS
├── requirements.txt   ← Python packages
├── build.sh           ← Render build script
├── render.yaml        ← Render config
└── .gitignore
```

## ✨ Features
- Home with hero, best sellers, new arrivals, audiobooks
- Category browsing & full-text search
- Book detail page with AI summary (Google Gemini)
- Session cart, checkout & order confirmation
- Newsletter subscription
- Full Django admin panel
