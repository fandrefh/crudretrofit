from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField('Nome', max_length=100)

    def __str__(self):
        return self.name

class Expense(models.Model):
    description = models.CharField('Descrição', max_length=150)
    payed = models.DecimalField('Valor pago', max_digits=25, decimal_places=2)
    category = models.ForeignKey(Category, related_name='categories', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.description
    
    @property
    def category_name(self):
        # https://stackoverflow.com/questions/17280007/retrieving-a-foreign-key-value-with-django-rest-framework-serializers
        return self.category.name
