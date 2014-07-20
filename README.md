Asynchronous Processing with Celery and Django
==============================================

[Presentation](http://celery.presentations.stegelman.com)

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
cd /home/vagrant
virtualenv celery-talk-venv
source celery-talk-venv/bin/activate
cd /home/vagrant/celery-demo
pip install -r requirements.txt
```

Enable Rabbitmq Management Plugin (Required for flower)

```
cd /usr/lib/rabbitmq/lib/rabbitmq_server-2.7.1/sbin
sudo ./rabbitmq-plugins enable rabbitmq_management
sudo service rabbitmq-server restart
```

Running the Worker

```
cd /home/vagrant/celery-demo/celery_demo
celery -A celery_demo worker -l info
```

Start Flower

```
cd /home/vagrant/celery-demo/celery_demo
celery flower -A celery_demo --address=0.0.0.0 --port=5555 --broker_api=http://guest:guest@localhost:55672/api/
```

Resources
---------

- [The Celery Project](http://www.celeryproject.org)
- [First Steps with Celery/Django](http://celery.readthedocs.org/en/latest/django/first-steps-with-django.html)
- [Celery Flower](https://github.com/mher/flower)
- [Django Celery and Reids](https://godjango.com/63-deferred-tasks-and-scheduled-jobs-with-celery-31-django-17-and-redis/)
