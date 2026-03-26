# Django For Everybody Projects

This repository contains two Django projects I built while working through the University of Michigan's Django for Everybody (DJ4E) specialization.

The codebase is split into:

- `mysite`: smaller practice apps used to learn core Django concepts
- `market`: a larger marketplace-style application that combines CRUD, authentication, comments, favorites, tagging, image uploads, and deployment-oriented configuration

The project was originally deployed on PythonAnywhere and later copied here for portfolio/documentation purposes.

## Repository Structure

```text
DjangoForEverybody/
├── mysite/
│   ├── autos/
│   ├── cats/
│   ├── hello/
│   ├── home/
│   ├── polls/
│   ├── solo1/
│   └── mysite/
├── market/
│   ├── config/
│   ├── home/
│   ├── mkt/
│   └── manage.py
└── readme.md
```

## What This Repository Covers

Across both projects, the work demonstrates:

- Django project and app structure
- URL routing and view composition
- Function-based views and class-based generic views
- Template rendering with Bootstrap
- Session and cookie handling
- Authentication with Django's built-in auth system
- Login-protected CRUD flows
- Model relationships using `ForeignKey` and `ManyToManyField`
- Form handling and validation
- File upload handling for images
- Search, comments, favorites, and tagging
- MySQL-based deployment configuration for PythonAnywhere
- Optional GitHub social login integration

## Project 1: `mysite`

`mysite` is the learning sandbox project. It contains multiple small apps, each focused on a specific Django concept from the specialization.

### Apps Inside `mysite`

#### `home`

The landing page links to the practice applications:

- Polls
- Hello/session test
- Autos CRUD
- Cats CRUD

#### `hello`

A minimal view used to practice:

- returning a raw `HttpResponse`
- storing values in the session
- resetting a counter after several visits
- setting a cookie

#### `solo1`

A very small app that returns a simple text response. This appears to be one of the early assignment apps for basic routing and responses.

#### `polls`

Based on the Django tutorial structure, this app includes:

- `Question` and `Choice` models
- list/detail/results views
- vote submission
- vote counting with `F()` expressions

This app demonstrates:

- model relationships
- generic class-based views
- forms submitted with POST
- URL reversing

#### `autos`

A login-protected CRUD app built around:

- `Make`
- `Auto`

Features:

- create, update, delete, and list autos
- manage car makes separately
- model forms
- validation with `MinLengthValidator`
- use of both manual `View` classes and generic editing views

This app shows the transition from basic forms to more structured CRUD patterns.

#### `cats`

Another login-protected CRUD app with:

- `Breed`
- `Cat`

Features:

- create, update, delete, and list cats
- separate breed management
- relational modeling with `ForeignKey`
- simple UX logic to prevent creating cats before breeds exist

This app reinforces the same CRUD ideas as `autos`, but with a cleaner class-based approach.

## Project 2: `market`

`market` is the larger and more complete DJ4E application in this repository. It functions as a small marketplace where authenticated users can create ads, upload images, comment on listings, favorite ads, and organize content with tags.

### Main Apps Inside `market`

#### `home`

Provides:

- a simple home page
- login templates
- optional social login template
- a context processor exposing Django settings to templates
- a custom template tag for Gravatar avatars

#### `mkt`

This is the main marketplace app.

### Marketplace Data Model

#### `Ad`

Represents a marketplace listing with:

- title
- price
- description text
- owner
- timestamps
- optional uploaded image stored in the database as binary data
- tags via `django-taggit`

#### `Comment`

Represents a user comment on an ad:

- linked to an ad
- linked to the user who created it
- timestamped

#### `Favorite`

Represents a user's favorite relationship with an ad:

- linked to a user
- linked to an ad
- constrained so the same user cannot favorite the same ad twice

### Marketplace Features

- User authentication with Django auth
- Optional GitHub OAuth login via `social-auth-app-django`
- Create, update, and delete ads
- Ownership checks so users can only edit/delete their own content
- Upload listing images with size validation
- Image streaming through a dedicated view
- Add and delete comments on ads
- Toggle favorites asynchronously
- Search ads by title, description, or tag
- Human-readable timestamps with Django humanize
- Bootstrap-based UI with a reusable navigation template
- Gravatar avatar display in the navbar

### Marketplace Views and Patterns

The `market` project demonstrates several good intermediate Django patterns:

- custom owner-aware base views in `mkt/owner.py`
- explicit handling of `request.FILES` for uploads
- many-to-many relationships through intermediate models
- `Q` objects for multi-field search
- AJAX-style favorite toggling with JavaScript
- conditional login templates depending on whether GitHub OAuth settings are present

## Technology Stack

Core stack used in this repository:

- Python
- Django 5.2
- Bootstrap 5
- SQLite for `mysite`
- MySQL for deployed `market`

Notable packages used in `market`:

- `django-crispy-forms`
- `crispy-bootstrap5`
- `django-extensions`
- `djangorestframework`
- `django-taggit`
- `social-auth-app-django`
- `mysqlclient`

## Running the Projects Locally

These are two separate Django projects. Run them independently.

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd DjangoForEverybody
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

### 3. Install Dependencies

For `mysite`, Django is the main dependency:

```bash
pip install "Django>=5.2,<5.3"
```

For `market`, use the provided requirements file:

```bash
cd market
pip install -r requirements52.txt
cd ..
```

## Running `mysite`

`mysite` uses SQLite and is the easier project to run locally.

```bash
cd mysite
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Available sections include:

- `/`
- `/hello/`
- `/polls/`
- `/autos/`
- `/cats/`
- `/solo1/`

## Running `market`

`market` is configured for PythonAnywhere/MySQL in `config/settings.py`, so it will likely need adjustment before it runs locally on another machine.

At minimum, review:

- database settings
- GitHub OAuth settings
- any deployment-specific credentials

### Recommended Local Approach

If you want to run `market` locally without reproducing the deployed MySQL setup, switch the database configuration to SQLite or your own MySQL instance.

Typical steps:

```bash
cd market
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Main routes:

- `/` for the ads list
- `/ad/<id>` for ad detail
- `/ad/create` for creating a listing
- `/accounts/login/` for authentication
- `/oauth/` for GitHub social auth when configured

## Notes About Deployment

The `market` project was configured for PythonAnywhere and includes:

- MySQL database settings
- optional GitHub OAuth settings file
- references to PythonAnywhere deployment workflow

Because this repository is now being used as a local/portfolio copy, deployment-specific values should be treated as environment-specific and not as portable defaults.

For a cleaner public version of this project, the next step would be:

- move secrets and credentials into environment variables
- create separate `local` and `production` settings
- document deployment steps explicitly

## Learning Progression Reflected in the Code

One useful thing about this repository is that it shows a clear learning path:

1. basic responses and routing in `hello` and `solo1`
2. models and tutorial-style views in `polls`
3. authenticated CRUD in `autos`
4. relational CRUD and better UX in `cats`
5. a fuller user-facing product in `market`

That progression makes the repository useful not just as a finished app collection, but also as a record of how Django concepts were learned and applied incrementally.

## What I Would Improve Next

If this repository were being taken from coursework to production quality, the next improvements would be:

- split settings into `base`, `local`, and `production`
- remove hardcoded deployment secrets from tracked files
- add automated tests for forms, permissions, and favorite toggling
- add image/media storage using Django's file storage system instead of binary DB storage
- standardize template styling and navigation across both projects
- add API endpoints or a DRF layer for the marketplace

## Summary

This repository captures my hands-on work through the DJ4E specialization, starting from small focused exercises and ending with a more complete marketplace application. It shows practical Django experience with:

- models
- templates
- authentication
- CRUD
- forms
- file uploads
- relational data modeling
- deployment-oriented configuration

It is best understood as a learning portfolio that documents both the coursework exercises and the larger final-style application built during that process.
