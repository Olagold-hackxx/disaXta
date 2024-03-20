from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group
from unfold.admin import ModelAdmin

from app.models import User, CustomToken


@admin.register(User)
class UserAdmin(ModelAdmin):
    search_fields = ("username", "first_name", "last_name", "email")
    ordering = ("email", "username")


@admin.register(CustomToken)
class CustomTokenAdmin(ModelAdmin):
    list_filter = ("user",)


admin.site.unregister(Group)
