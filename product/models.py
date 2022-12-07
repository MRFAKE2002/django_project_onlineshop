from django.db import models
from django.contrib.auth import get_user_model
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


class Comment(models.Model):
    PRODUCT_STARS = [
        ('1' , _('bad')),
        ('1' , _('normal')),
        ('1' , _('good')),
    ]
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments', verbose_name=_('Product'),)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments', verbose_name=_('Author'),)
    body = models.TextField(verbose_name=_('Body'))
    star = models.CharField(choices=PRODUCT_STARS , max_length=5, verbose_name=_('Star'),)
    
    datetime_created = models.DateTimeField(verbose_name = _('datetime created'), default=timezone.now)
    datetime_modified = models.DateTimeField(verbose_name = _('datetime modified'), auto_now=True)
    
    active = models.BooleanField(verbose_name = _('active'), default=True)

