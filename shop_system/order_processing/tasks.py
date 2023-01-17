from shop_system.celery import app
from celery import shared_task
from django.core.management import call_command

@app.task
def sample_task():
    print('hello from AZOV')


@shared_task
def change_price_product():
    call_command('check_discount', )
