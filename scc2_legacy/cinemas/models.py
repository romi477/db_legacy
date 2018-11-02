from django.db import models


class CustomerManager(models.Manager):
    def get_by_natural_key(self, iso, name):
        return self.get(iso=iso, name=name)



class Customer(models.Model):
    objects = CustomerManager()
    unique_together = ('iso', 'name')

    iso = models.CharField(max_length=2)
    name = models.CharField(max_length=20)

    class Meta:
        unique_together = ('iso', 'name')

    def __str__(self):
        return f'{self.iso}-{self.name}'

    def natural_key(self):
        return (self.iso, self.name)



class Cinema(models.Model):

    owner = models.ForeignKey(Customer, on_delete=models.CASCADE)
    title = models.CharField(max_length=25, unique=True)
    uniqueid = models.CharField(max_length=36, unique=True)
    ownervalue = models.IntegerField()
    creation = models.DateField()

    def __str__(self):
        return self.title