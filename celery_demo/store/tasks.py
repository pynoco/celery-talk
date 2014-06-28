from __future__ import absolute_import
import time
from celery import shared_task


@shared_task
def add(x, y):
    print(x + y)
    return x + y


@shared_task
def process_payment():
	# this takes a long time to process
	time.sleep(10)
	print("processed")