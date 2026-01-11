
Resetting your Database
-----------------------

If you have a problem running `migrate` or `makemigrations` in this project, you might want
to start with a fresh MySQL database.  Since we are using a MySQL server, we can't
just delete the SQLite file and start over - so we have written a script to automate the process.

Take your time and follow these instructions carefully.  These assume you have (1) properly set up 
your virtual envronment and (2) checked out `~/dj4e-samples` correctly as described in
the very first assignment.

(1) Start a terminal and make sure your virtual environment is activated. Check the Django version.

    python -m django --version

It should be '5.2'.

(2) Next, make sure you have the latest up-to-date version of `~/dj4e-samples`.

    cd ~/dj4e-samples
    git checkout .           # Discards any changes you mistakenly made to dj4e-samples
    git checkout django52    # Make sure you have the correct version of the samples 
    git pull

(3) Next empty out your database and reset all the migrations so they can be reconstructed.

    cd ~/django_projects/market
    python ~/dj4e-samples/tools/resetdb.py

(4) Then go back to the setup instructions and pick up with the `makemigrations` and `migrate` steps, as well as
`createsuperuser` if needed.

Here is an example execution of this process:

    (.ve52) 14:06 ~/django_projects/market (main)$ cd ~/dj4e-samples/
    (.ve52) 14:07 ~/dj4e-samples (django52)$ git checkout .
    Updated 0 paths from the index
    (.ve52) 14:07 ~/dj4e-samples (django52)$ git checkout django52
    Already on 'django52'
    Your branch is up to date with 'origin/django52'.
    (.ve52) 14:07 ~/dj4e-samples (django52)$ git pull
    Already up to date.
    (.ve52) 14:07 ~/dj4e-samples (django52)$ cd ~/django_projects/market
    (.ve52) 14:06 ~/django_projects/market (main)$ python ~/dj4e-samples/tools/resetdb.py 
    Found Django project at: /home/csev/django_projects/market
    Using settings module: config.settings
    When you want to use social login, please see dj4e-samples/github_settings-dist.py
    ============================================================
    Database and Migration Reset Script
    ============================================================
    This will DELETE ALL TABLES and ALL MIGRATION FILES!
    Are you sure you want to continue? (yes/no): yes
    Dropping all tables...
      Dropping table: auth_group
      Dropping table: auth_group_permissions
      Dropping table: auth_permission
      Dropping table: auth_user
      Dropping table: auth_user_groups
      Dropping table: auth_user_user_permissions
      Dropping table: django_admin_log
      Dropping table: django_content_type
      Dropping table: django_migrations
      Dropping table: django_session
      Dropping table: social_auth_association
      Dropping table: social_auth_code
      Dropping table: social_auth_nonce
      Dropping table: social_auth_partial
      Dropping table: social_auth_usersocialauth
      Dropping table: taggit_tag
      Dropping table: taggit_taggeditem
    All tables dropped successfully.
    Deleting migration files...
      Processing: /home/csev/django_projects/market/home/migrations
      Deleting: /home/csev/django_projects/market/home/migrations/__pycache__/__init__.cpython-313.pyc
    Deleted 1 migration files.
    ============================================================
    Reset completed successfully!
    ============================================================
    Next steps:
    1. Run: python manage.py makemigrations
    2. Run: python manage.py migrate
    3. Run: python manage.py createsuperuser (if needed)
    (.ve52) 14:06 ~/django_projects/market (main)$ 

Depending on how far along in the Marketplace application you are, there may
be more tables dropped and migrations deleted.

