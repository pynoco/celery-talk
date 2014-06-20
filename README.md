Asynchronous Processing with Celery and Django
==============================================



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
sudo apt-get install python-pip python2.7-dev python-virtualenv python-setuptools git rabbitmq-server
cd /home/vagrant/celery-talk
virtualenv celery-talk-venv
source celery-talk-venv/bin/activate
pip install -r requirements.txt

```

