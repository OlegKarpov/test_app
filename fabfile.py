import os

from django.contrib.auth import get_user_model
from fabric.context_managers import cd
from fabric.contrib import django
from fabric.decorators import task
from fabric.operations import env, local, run
from fabric.utils import puts

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
django.settings_module('test_app_1.settings')

django.setup()


ADMIN_EMAIL_ADDRESS = 'admin@example.com'

env.project_name = 'test_app_1'
env.project_root_dir = os.path.dirname(os.path.abspath(__file__))

env.project_src_dir = '{project_root_dir}/{project_name}'.format(**env)

@task
def pipenv_requirements():
    """
    Update the requirements using global pipenv.
    """
    with cd(env.project_src_dir):
        run('pipenv install')


@task
def migrate():
    """
    Run DB migrations.
    """
    pipenv_run('python manage.py migrate')


@task
def npm_install():
    """
    Install NPM dependencies and build
    """
    with cd(env.node_modules_dir):
        run('npm install')


@task
def collectstatic():
    """
    Run DB migrations.
    """
    pipenv_run('python manage.py collectstatic --noinput')


def pipenv_run_local(command):
    """
    Run a "pipenv run" command locally.
    """
    local('pipenv run {pipenv_command}'.format(pipenv_command=command, **env))



def pipenv_run(command):
    """
    Run a "pipenv run" command on the server.
    """
    with cd(env.project_src_dir):
        run('pipenv run {pipenv_command}'.format(pipenv_command=command, **env))


def add_admin():
    user_model = get_user_model()
    admin = user_model(email=ADMIN_EMAIL_ADDRESS)
    admin.is_superuser = True
    admin.is_staff = True
    admin.set_password('admin')
    admin.save()


# def add_foo():
#     pass

@task
def initial_data():
    puts('==> Hi there! :)')
    puts('==> Installing the requirements...')
    local('pipenv install --dev')
    puts('==> Creating the db...')
    pipenv_run_local('python manage.py migrate')
    local('bower install')
    puts('==> Creating the superuser...')
    add_admin()
    # puts('==> Adding initial data...')
    # add_foo()
    puts('==> All done. Please do your thing and leave :)')
