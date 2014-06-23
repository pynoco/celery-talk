Asynchronous Processing with Celery and Django
==============================================

This repo includes a working demo of how to use Celery with 
Django to queue up tasks.  It includes a Vagrantfile to assist
in setting up the development environment.

Following Along
---------------

You can follow along and play the demo app pretty easily using
Vagrant and Virtualbox.  Go ahead and download and install those
tools for your OS.  To get started just install the following packages once
you have successfully booted your machine.

```
git checkout git@github.com:pynoco/celery-talk.git
```

```
cd celery-talk
vagrant up
```

```
vagrant ssh
sudo apt-get update
sudo apt-get install python-pip python2.7-dev python-virtualenv python-setuptools git rabbitmq-server supervisor
cd /home/vagrant/celery-talk
virtualenv celery-talk-venv
source celery-talk-venv/bin/activate
pip install -r requirements.txt
```

Running the Worker

```
celery -A celery_demo worker -l info
```

Resources
---------

- [The Celery Project](http://www.celeryproject.org)
- [First Steps with Celery/Django](http://celery.readthedocs.org/en/latest/django/first-steps-with-django.html)
