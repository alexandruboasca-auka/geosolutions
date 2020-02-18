### Installation

Install the dependencies 

Assuming Python3 and PIP installed, and a virtual env created for this project.
I'm using virtualenvwrapper, https://virtualenvwrapper.readthedocs.io/en/latest/

Create virtual env, install dependencies.

```sh
$ mkvirtualenv geosolutions
$ pip install -r requirements.py
```

cd into the geosolutions dir, migrate to the create the database.

```sh
$ cd geosolutions
$ python manage.py migrate
```

Use the "fill_points" command to populate the database with fill_points
Usage: "python manage.py fill_points <number_of_points:int>"

```sh
$ python manage.py fill_points 100
```

Run the dev server, no static file management required
```sh
$ python manage.py runserver
```