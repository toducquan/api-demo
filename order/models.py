from django.db import models, transaction
from django.db.models import F
import datetime
# Create your models here.

def gen_new_id():
    # Get the current date
    current_date = datetime.datetime.today().strftime(r'%Y%m%d')
    with transaction.atomic():
        # Lock the OrderCounter object for the current date
        order_counter = OrderCounter.objects.select_for_update().get_or_create(date=current_date)[0]
        # Increase the counter by 1
        new_counter = order_counter.counter + 1
        # Save and release resource
        OrderCounter.objects.filter(pk=order_counter.pk).update(counter=F('counter') + 1)
    return f"{current_date}-{new_counter:05d}"

def gen_new_id_v2():
    # Get the current date
    current_date = datetime.datetime.today().strftime(r'%Y%m%d')
    # Get the lastest id in current date
    latest_counter = OrderV2.objects.filter(id__startswith=current_date).order_by("-id").first()
    if latest_counter is not None:
        new_counter = int(latest_counter.id.split('-')[1]) + 1
    else:
        new_counter = 1
    return f"{current_date}-{new_counter:05d}"

class OrderCounter(models.Model):
    date = models.CharField(primary_key=True, max_length=255)
    counter = models.IntegerField(default=0)

class Order(models.Model):
    id = models.CharField(primary_key=True, max_length=255, default=gen_new_id, editable=False)
    def __str__(self):
        return self.id
    
class OrderV2(models.Model):
    id = models.CharField(primary_key=True, max_length=255, default=gen_new_id_v2, editable=False)
    def __str__(self):
        return self.id
