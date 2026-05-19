# Django Portfolio

A modern personal portfolio built with Django 6, Bootstrap 5, database-backed portfolio content, contact message storage, responsive templates, SEO metadata, theme switching, typing animation, scroll reveal, and a customized Django Admin.

## Features

- Django 6.0.5 with split development and production settings
- Portfolio models for projects, skills, experience, and contact messages
- Login, signup, and logout pages using Django's built-in authentication
- Admin-managed projects, skill progress, timeline items, and inbox
- Homepage sections for hero, about, skills, projects, timeline, contact, and footer
- Separate timeline, projects, and contact pages using the same reusable components
- Bootstrap 5 templates with project-local CSS and JavaScript
- Dark/light theme toggle, typing animation, sticky navbar, scroll reveal, and animated skill bars
- SQLite development database and `.env` support without extra packages

## Project Structure

```text
.
├── config/
│   ├── settings/
│   │   ├── base.py
│   │   ├── development.py
│   │   └── production.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── core/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── contacts/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── accounts/
│   ├── forms.py
│   ├── views.py
│   └── urls.py
├── templates/
│   ├── base.html
│   ├── pages/
│   ├── partials/
│   └── admin/
├── static/
│   ├── css/
│   ├── js/
│   ├── docs/
│   └── img/
├── media/
├── manage.py
└── requirements.txt
```

## Setup

```powershell
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
copy .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open `http://127.0.0.1:8000/` for the portfolio and `http://127.0.0.1:8000/admin/` for the admin dashboard.

## Login and Signup

The auth pages are available at:

```text
/accounts/login/
/accounts/signup/
```

Users are stored in Django's standard `auth_user` table, so they will use the same database as the rest of the site.

## WAMP / MySQL Setup

1. Start WAMP and make sure the MySQL/MariaDB service is running.
2. Open phpMyAdmin and create a database named `portfolio_db`.
3. In `.env`, switch the database engine from SQLite to MySQL:

```env
DATABASE_ENGINE=mysql
MYSQL_DATABASE=portfolio_db
MYSQL_USER=root
MYSQL_PASSWORD=
MYSQL_HOST=127.0.0.1
MYSQL_PORT=3306
```

4. Install the MySQL driver and run migrations:

```powershell
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

If your WAMP root user has a password, put it in `MYSQL_PASSWORD`.

## Personalization

Edit `.env` to update your name, title, intro, email, phone, location, and social links. Then edit projects, skills, and timeline items in Django Admin.

## Useful Commands

```powershell
python manage.py makemigrations
python manage.py migrate
python manage.py test
python manage.py collectstatic --noinput
python manage.py check --deploy --settings=config.settings.production
```
