from django.contrib import admin

# Register your models here.
from authentication.models import CustomUser

admin.site.register(CustomUser)
