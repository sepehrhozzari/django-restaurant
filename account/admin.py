from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

UserAdmin.fieldsets[2][1]['fields'] += ('profile_picture',)

admin.site.register(User, UserAdmin)
