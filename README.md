<<<<<<< HEAD
# ArSa – Romantic Date Invitation Website

**Ar** = Arshia · **Sa** = Samina

A private, multi-step romantic invitation web application built with Django.

## Features

- Custom user model with roles (Admin / User)
- Multi-step "Date Mission" flow:
  1. Yes / No question (No is disabled with a playful modal)
  2. Date picker
  3. Time picker
  4. Interactive map (Leaflet + OpenStreetMap)
  5. Review & submit
  6. Celebration page (confetti, fireworks, balloons, hearts)
- User dashboard, profile, request history
- Admin dashboard with statistics, IP tracking, request management
- Soft romantic UI with glassmorphism, Samina's favorite color palette
- Fully responsive (mobile + desktop)
- CSRF protection, Django messages, session-based mission flow

## Color Palette

| Name      | Hex       |
|-----------|-----------|
| Primary   | `#8E1EA2` |
| Secondary | `#C654C3` |
| Accent    | `#ED96D7` |
| Light     | `#FFC0DE` |

## Tech Stack

- **Backend:** Django 5+/6, custom User model
- **Database:** SQLite (dev) / PostgreSQL (production)
- **Frontend:** Bootstrap 5, custom CSS, Leaflet.js, canvas-confetti
- **Auth:** Django Authentication

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Migrate
python manage.py migrate

# Create superuser (or use the seeded ones)
python manage.py createsuperuser

# Run
python manage.py runserver
```

### Seeded Accounts

| Username | Password   | Role  |
|----------|------------|-------|
| samina   | samina123  | User  |
| arshia   | arsa2026   | Admin |

## Production PostgreSQL

Uncomment the PostgreSQL block in `arsa_project/settings.py` and set:

```
POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_PORT
```

Also set `DJANGO_SECRET_KEY`, `DJANGO_DEBUG=False`, `DJANGO_ALLOWED_HOSTS`.

## Project Structure

```
arsa_project/     # Project settings & root URLs
accounts/         # Custom User, login/logout
dates/            # DateRequest model, mission flow, dashboards
templates/        # Base + all page templates
static/css/       # arsa.css (theme)
static/js/        # arsa.js (hearts, confetti helpers)
```

## Notes

- The "No" button on the first mission step never creates a request; it only shows a modal.
- IP addresses are captured on submission and visible only to admins.
- Location is stored as lat/lng + optional name.
- Mission progress is kept in the session until final submit.

Made with ❤️ for Samina.
=======
# ArSa
>>>>>>> 4bc433a1506116a187034e61af605b4ebd4bb8ad
