# Foodhub

This repository contains a small food/blog site migrated to a minimal Django app using TailwindCSS (CDN) and MongoDB (via `djongo`).

Setup
-----
1. Create a virtual environment and activate it (Windows):

```powershell
python -m venv venv
venv\Scripts\activate
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Create a `.env` file based on `.env.example` and set `MONGO_URI` and `DJANGO_SECRET_KEY`.

4. Run migrations (djongo):

```powershell
python manage.py makemigrations
python manage.py migrate
```

5. Create admin user:

```powershell
python manage.py create_admin
```

6. Run the dev server:

```powershell
python manage.py runserver
```

Notes
-----
- Tailwind is loaded via CDN in `templates/base.html`. For production, compile Tailwind for optimal performance.
- MongoDB connection is read from `MONGO_URI`. If you're using MongoDB Atlas, set the full connection string in `.env`.
- The app uses Django server-rendered templates. Static files and media are served from `static/` and `media/` during development.

Notes about database choice
--------------------------
- This project uses `mongoengine` to store `Post` documents in MongoDB. `mongoengine` is maintained and works with modern Django versions.
- Django's built-in auth and admin continue to use a local SQLite database (`db.sqlite3`) so the `create_admin` command and Django admin work as expected. The Django admin will not manage `Post` documents in MongoDB.


What changed
------------
- Added minimal Django project at `foodhub_site/` and a `blog` app.
- Added CRUD views and templates for `Post` objects.
- Added `requirements.txt`, `.env.example`, and `create_admin` management command.
