import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop_system.settings")

app = Celery("shop_system")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'change_price': {
        'task': 'order_processing.tasks.change_price_product',
        'schedule': crontab(minute='*/1')
    }
}
