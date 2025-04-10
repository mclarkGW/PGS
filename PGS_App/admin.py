from django.contrib import admin
from .models import Roles
from .models import PersonalGoldSource


class RolesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'roletype')

class PersonalGoldSourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')

admin.site.register(Roles, RolesAdmin)
admin.site.register(PersonalGoldSource, PersonalGoldSourceAdmin)


