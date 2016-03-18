from __future__ import with_statement
from fabric.api import *
from fabric.utils import fastprint

env.user = 'ec2-user'
env.hosts = ['vingtcinq.io']


project_name = '{{ project_name }}'


def collect():
    with cd('/mnt/websites/%s' % project_name):
        run("git pull")
        # run("source venv/bin/activate && pip install -r requirements.txt")
        run("source venv/bin/activate && ./manage.py collectstatic --noinput")


def deploy():
    with cd('/mnt/websites/%s' % project_name):
        run("git pull")
        run("source venv/bin/activate && pip install -r requirements.txt")
        run("source venv/bin/activate && ./manage.py collectstatic --noinput")
        # run("source venv/bin/activate && ./manage.py migrate --settings main.settingsprod")
        run("venv/bin/uwsgi --reload %s.pid" % project_name)


def launch():
    with cd('/mnt/websites'):
        run("git clone https://charlesthk@bitbucket.org/e-reflex/%s.git" % project_name)
    with cd('/mnt/websites/%s' % project_name):
        run("virtualenv venv")
        run("source venv/bin/activate && pip install -r requirements.txt")
        run("source venv/bin/activate && pip install uwsgi")
        run("source venv/bin/activate && ./manage.py collectstatic --noinput")
        run("source venv/bin/activate && ./manage.py migrate --settings main.settingsprod")
        run("venv/bin/uwsgi %s.ini" % project_name)


def start():
    with cd('/mnt/websites/%s' % project_name):
        run("venv/bin/uwsgi %s.ini" % project_name)


def pull():
    with cd('/mnt/websites/%s' % project_name):
        run("git pull")


def reload():
    with cd('/mnt/websites/%s' % project_name):
        run("git pull")
        run("venv/bin/uwsgi --reload %s.pid" % project_name)


def commit(message):
    local("git add --all")
    local("git commit -m \"%s\"" % message)
    local("git push")


def creload(message):
    commit(message)
    with cd('/mnt/websites/%s' % project_name):
        run("git pull")
        run("source venv/bin/activate && ./manage.py collectstatic --noinput")
        run("venv/bin/uwsgi --reload %s.pid" % project_name)


def install():
    with cd('/mnt/websites/%s' % project_name):
        run("source venv/bin/activate && pip install -r requirements.txt")


def nginx():
    with cd('/mnt/websites/%s' % project_name):
        run("sudo cp %s.conf /etc/nginx/conf.d" % project_name)
        run("sudo service nginx restart")


def port():
    with hide('output'):
        ports = run('./ports')
        ports = ports.split('\r\n')
        for a in range(8000, 8100):
            if str(a) not in ports:
                fastprint(a)
                break
