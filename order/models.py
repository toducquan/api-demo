from django.db import models, transaction
from django.db.models import F
import datetime
# Create your models here.

def gen_new_id():
    current_date = datetime.datetime.today().strftime(r'%Y%m%d')
    with transaction.atomic():
        order = OrderCounter.objects.select_for_update().get_or_create(date=current_date)[0]
        new_number = order.counter + 1
        OrderCounter.objects.filter(pk=order.pk).update(counter=F('counter') + 1)
    return f"{current_date}-{new_number:05d}"

class OrderCounter(models.Model):
    date = models.CharField(primary_key=True, max_length=255)
    counter = models.IntegerField(default=0)

class Order(models.Model):
    id = models.CharField(primary_key=True, max_length=255, default=gen_new_id, editable=False)
    def __str__(self):
        return self.id
