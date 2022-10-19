from django.contrib import admin
from .models import * # W
# Register your models here.
# alexwilson Password

admin.site.register(Room) # Register model with admin panel
admin.site.register(Topic)
admin.site.register(Message)