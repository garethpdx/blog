from django.db import models
from django.contrib.auth.models import User as MeasurementUser
from django.forms import ModelForm
import datetime


class Measurement(models.Model):
    created_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(auto_now=True)
    type = models.ForeignKey('Category')
    value = models.IntegerField()
    notes = models.CharField(max_length=200, null=True)
    user = models.ForeignKey('User')

    def __unicode__(self):
        return u'{0} - {1}'.format(self.type.name,
                                   self.created_at)


class Category(models.Model):
    created_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50)
    min_value = models.IntegerField(default=1)
    min_value_desc = models.CharField(max_length=50,
                                      default='Minimally')
    max_value = models.IntegerField(default=4)
    max_value_desc = models.CharField(max_length=50,
                                      default='Maximally')
    hidden = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name


class User(MeasurementUser):
    pass


class MeasurementForm(ModelForm):
    class Meta:
       model = Measurement
       exclude = ['user','created_at','updated_at']
