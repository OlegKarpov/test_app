# README #

### Creating a new project from this template

```
django-admin.py startproject <projectname> --template=https://github.com/igorgai/django-project-template/archive/master.zip --name=.gitignore,README.md,.bowerrc --extension=json,py,md,txt,less
```

### Basic setup ###
#### Python dependencies and database setup

1. Install pipenv (in case you don't have it installed yet). 
    In the terminal:
    ```
    pip install pipenv
    ```
    (https://docs.pipenv.org/#install-pipenv-today)
    
2. Navigate to the project directory:
    ```
    cd test_app_1/
    ```

3. Initialize virtual environment:
    ```
    pipenv install --three
    ```
4. Copy the file at *test_app_1/settings/local.example.py* and save it in the same directory under the name of *"local.py"*:

    ```
    cp test_app_1/settings/local.example.py test_app_1/settings/local.py
    ```

5. Install dependencies and initial data: 
    ```
    pipenv run fab initial_data
    ```

#### Create superuser

```
pipenv run python manage.py createsuperuser
```

#### Html/css/js dependencies

```
npm -g install bower (Node should be installed)
bower install
```

