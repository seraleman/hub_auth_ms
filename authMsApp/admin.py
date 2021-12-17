from django.contrib import admin
from .models.user import User
from .models.role import Role

# Register your models here.

admin.site.register(User)
admin.site.register(Role)
