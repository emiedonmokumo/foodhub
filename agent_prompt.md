# Agent Task: Migrate foodhub → Django + Tailwind (CDN) + MongoDB

Overview
-------
You are an autonomous VS Code agent. Your job is to convert the existing static `foodhub` site (Bootstrap + plain HTML) into a minimal Django app using TailwindCSS via CDN and MongoDB as the data store. The site is a small food/blog project with `index.html`, `style.css`, and an `images/` folder. Preserve assets where possible and convert templates to Django template rendering.

High-level goals
----------------
- Replace Bootstrap styles with TailwindCSS (use CDN) and remove/replace `style.css` rules that conflict.
- Create a Django project and a `blog` app that implements CRUD for `Post` objects (title, slug, body/content, featured_image reference, published_date, tags (optional)).
- Use MongoDB as the primary DB. Configure Django to use MongoDB (use a maintained adapter such as `djongo` or `mongoengine`; prefer `djongo` for minimal ORM changes). Document whichever you choose in `README.md`.
- Keep server-side rendering with Django templates (no SPA). Convert existing HTML files into Django templates with a `base.html` layout.
- Add a management command to create a single admin user automatically (credentials read from `.env` or default to `admin` / `ChangeMe123!` — instruct user to change it).
- Update `README.md` with setup/run instructions, dependencies, and how to create/run the admin user command.

Constraints & decisions
---------------------
- Tailwind must be loaded via CDN: include `<script src="https://cdn.tailwindcss.com"></script>` in `base.html` and use Tailwind utility classes in templates.
- Templates must use Django template rendering (i.e., put templates under `templates/` and use `{% %}` and `{{ }}`).
- Keep `images/` as static media. Configure `MEDIA_URL`/`MEDIA_ROOT` in Django settings to serve in development.
- Keep changes minimal and preserve the existing look where reasonable by mapping Bootstrap classes to Tailwind equivalents.
- Create `requirements.txt` and list pinned dependencies used.

Deliverables
------------
- Django project in repository root (minimal name: `foodhub_site`) and a `blog` app.
- `requirements.txt` with `Django`, `djongo` (or `mongoengine`), `pymongo`, and any small helper libs like `python-dotenv`.
- Templates: `templates/base.html`, `templates/index.html` (converted), and templates for posts: `post_list.html`, `post_detail.html`, `post_form.html`, `post_confirm_delete.html`.
- CRUD views (class-based views preferred) and URL routes under `blog/urls.py` and included in project `urls.py`.
- `models.py` for `Post` compatible with chosen MongoDB adapter; migrations or instructions if migrations are not supported.
- Management command `python manage.py create_admin` which creates a single admin user (reads from `.env` or defaults). Add a sample `.env.example`.
- Update `README.md` with setup and commands.

Acceptance criteria
------------------
- Running the steps in `README.md` leads to a working Django dev server with rendered pages and basic CRUD for posts.
- Tailwind utilities are used in templates (no remaining Bootstrap CDN or dependencies in templates).
- MongoDB is the configured DB and the app can create/read/update/delete `Post` entries.
- A single admin user can be created via the management command.

Step-by-step instructions for the agent (do these actions)
------------------------------------------------------
1. Inventory & backup
   - Inspect repository files: list `index.html`, `style.css`, `images/` and any other files.
   - Create a branch/backup: `git checkout -b migrate/django-tailwind-mongo` (if repo is git-initialized).

2. Scaffold Django project & app
   - Create Django project: `django-admin startproject foodhub_site .` (project at repo root).
   - Create app: `python manage.py startapp blog`.
   - Add `blog` to `INSTALLED_APPS`.

3. Requirements & environment
   - Create `requirements.txt` (example pins):
     - Django>=4.2
     - djongo>=1.3.6
     - pymongo
     - python-dotenv
   - Add `.env.example` with keys: `DJANGO_SECRET_KEY`, `MONGO_URI`, `ADMIN_USERNAME`, `ADMIN_PASSWORD`.

4. Configure MongoDB
   - In `foodhub_site/settings.py` replace default DATABASES with configuration for `djongo` using `MONGO_URI` read from environment (use `python-dotenv` to load `.env`).
   - Provide a fallback local URI if not provided but warn in `README.md`.

5. Models & migrations
   - Implement `Post` model in `blog/models.py` with fields: `title`, `slug`, `content`, `featured_image` (CharField or ImageField with `MEDIA` set), `published_date`, `created_at`, `updated_at`.
   - Run `python manage.py makemigrations` and `python manage.py migrate`. If `djongo` is used and migrations are supported, keep them; otherwise document alternate steps.

6. Views, URLs, Templates
   - Implement class-based CRUD views: `PostListView`, `PostDetailView`, `PostCreateView`, `PostUpdateView`, `PostDeleteView`.
   - Add `blog/urls.py` with named routes and include in project `urls.py`.
   - Move `index.html` content into `templates/index.html` and create `templates/base.html` with Tailwind CDN script in `<head>`.
   - Replace Bootstrap grid/classes with Tailwind equivalents. Where conversion is ambiguous, prioritize semantic layout and clean Tailwind utilities.

7. Static & media
   - Configure `STATIC_URL`, `STATICFILES_DIRS` (include existing static if any), `MEDIA_URL`, `MEDIA_ROOT` in `settings.py`.
   - Ensure `images/` is served in development via `MEDIA_URL` mapping in `urls.py`.

8. Admin & create_admin command
   - Register `Post` in `admin.py`.
   - Add `blog/management/commands/create_admin.py` which reads `ADMIN_USERNAME` and `ADMIN_PASSWORD` from environment or uses defaults, then creates a superuser if none exists. Make the password strongly worded by default and add a clear comment to change it.

9. Remove Bootstrap and update CSS
   - Remove Bootstrap CDN inclusions from templates.
   - Replace `style.css` contents selectively: convert custom rules into Tailwind utility classes. If some complex rules remain, move them to a smaller `custom.css` and include it after the Tailwind CDN; prefer using utility classes instead.

10. Update `README.md`
   - Add setup steps (virtualenv, install `requirements.txt`).
   - MongoDB instructions (local URI example and cloud example), how to run migrations (if applicable), how to run `create_admin`, and how to run the dev server.
   - Note Tailwind is loaded via CDN and that production should use a compiled Tailwind for optimization.

11. Verification steps
   - `python -m venv venv`
   - `venv\\Scripts\\activate` (Windows)
   - `pip install -r requirements.txt`
   - `python manage.py migrate`
   - `python manage.py create_admin` (or `createsuperuser` fallback)
   - `python manage.py runserver`
   - Visit `http://127.0.0.1:8000/` and test creating, editing, deleting posts.

Extras & notes for the implementer
---------------------------------
- If you choose `mongoengine` instead of `djongo`, implement model layer accordingly and use forms/views to work directly with `mongoengine` documents. Document this choice and instructions in `README.md`.
- Keep templates semantic and accessible; prefer responsive layouts using Tailwind's utility classes.
- Commit frequently and keep commits scoped (e.g., `scaffold: django project`, `feat: post model and migrations`, `style: replace bootstrap with tailwind base`).

What to output back to me (final agent report)
--------------------------------------------
- List of files created/modified (paths).
- `requirements.txt` contents.
- The `DJANGO` settings lines that configure `DATABASES` (masked secrets OK) and `MEDIA`/`STATIC` settings.
- The management command path and default credentials used (if any).
- Any manual steps left for the user (e.g., how to set `MONGO_URI`).

If anything blocking appears (ambiguous Bootstrap features, missing images, or adapter limitations), ask a single concise question and propose a recommended default.

----
This prompt should be used by a VS Code agent to perform the migration and produce a working Django app with Tailwind (CDN) and MongoDB-backed CRUD for posts. Keep changes minimal and document deviations in `README.md`.
