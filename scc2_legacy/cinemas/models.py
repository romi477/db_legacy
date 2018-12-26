from django.db import models
from django.shortcuts import reverse


class CustomerManager(models.Manager):
    def get_by_natural_key(self, iso, name):
        return self.get(iso=iso, name=name)


class Customer(models.Model):
    objects = CustomerManager()

    iso = models.CharField(max_length=2)
    name = models.CharField(max_length=20)

    class Meta:
        unique_together = ('iso', 'name')

    def __str__(self):
        return f'{self.name}  [{self.iso}]'

    def natural_key(self):
        return (self.iso, self.name)

    def get_absolute_url(self):
        return reverse('customer_info', kwargs={'iso': self.iso, 'name': self.name})


class Cinema(models.Model):
    owner = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL)
    wide_tag = models.CharField(max_length=25, null=True, blank=True)
    narrow_tag = models.CharField(max_length=25, null=True, blank=True)
    title = models.CharField(max_length=25, unique=True)
    slug = models.SlugField(max_length=30, unique=True, db_index=True, editable=True)
    uniqueid = models.CharField(max_length=36, verbose_name='UID')
    ownervalue = models.IntegerField()
    creation = models.DateField()
    notation = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-creation']
        verbose_name = 'Product'

    def __str__(self):
        return f'{self.title}  [{self.creation}]'

    def get_absolute_url(self):
        return reverse('product_info', kwargs={'iso': self.owner.iso, 'name': self.owner.name, 'slug': self.slug})
