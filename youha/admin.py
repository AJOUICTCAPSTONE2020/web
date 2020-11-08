from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):  # add this
  list_display = ('name', 'email', 'password') # add this
  

admin.site.register(User,UserAdmin)