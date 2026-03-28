# 📚 BookHaven — Online Book Store (Django)

A full-stack Django web application for browsing and purchasing books.

## 🚀 Quick Start

### 1. Install dependencies
```bash
pip install django Pillow requests
```

### 2. Apply migrations
```bash
python manage.py migrate
```

### 3. Create superuser (admin)
```bash
python manage.py createsuperuser
```

### 4. Seed sample data (optional)
```bash
python manage.py shell
# Then paste the seed script from seed_data.py
```

### 5. Run the server
```bash
python manage.py runserver
```

Visit: http://127.0.0.1:8000

## 🔑 Admin Panel
- URL: http://127.0.0.1:8000/admin/
- Default credentials: **admin / admin123** (change in production!)

## 🤖 AI Book Summaries (Google Gemini)
1. Get a free API key from https://makersuite.google.com/app/apikey
2. Open `bookstore/settings.py`
3. Replace `YOUR_GEMINI_API_KEY_HERE` with your actual key

## 📁 Project Structure
```
bookstore/
├── bookstore/          # Main project config
│   ├── settings.py
│   └── urls.py
├── books/              # Books app (models, views, admin)
├── cart/               # Cart & Orders app
├── subscribers/        # Newsletter subscribers
├── templates/          # HTML templates
│   ├── base.html
│   ├── books/
│   └── cart/
├── static/css/         # Custom CSS
├── media/              # Uploaded book covers
└── db.sqlite3          # SQLite database
```

## ✨ Features
- 🏠 Home page with hero section, best sellers, new arrivals, audiobooks
- 📚 Book listings with category filters
- 🔍 Full-text search across title, author, description
- 📖 Detailed book pages with AI-powered summaries
- 🛒 Session-based cart with quantity management
- 💳 Dummy checkout with order confirmation
- 📧 Newsletter subscription
- 🛠️ Full Django admin panel for managing everything
- 📱 Responsive design (mobile-friendly)
