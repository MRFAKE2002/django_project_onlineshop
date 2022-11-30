from django.db import models
from django.shortcuts import reverse
from django.utils.translation import gettext as _ # we use this function to translate 
from django.utils import timezone

class Product(models.Model):
    title = models.CharField(_('Title'), max_length=100)
    text = models.TextField()
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(_('Active'), default=True)
    
    datetime_created = models.DateTimeField(_('Create'), default=timezone.now)
    datetime_modified = models.DateTimeField(_('Modified'), auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])
   