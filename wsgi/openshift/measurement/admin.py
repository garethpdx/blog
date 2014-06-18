from django.contrib import admin
from measurement.models import Measurement, Category, User

admin.site.register(Measurement)
admin.site.register(Category)
admin.site.register(User)
