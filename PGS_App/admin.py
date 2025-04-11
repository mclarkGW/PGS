from django.contrib import admin
from .models import Roles
from .models import PersonalGoldSource
from .models import JobLevel
from .models import Role_Skill


class RolesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'roletype')

class PersonalGoldSourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')

class JoblevelAdmin(admin.ModelAdmin):
    list_display = ('id','title')

class Role_SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

admin.site.register(Roles, RolesAdmin)
admin.site.register(PersonalGoldSource, PersonalGoldSourceAdmin)
admin.site.register(JobLevel, JoblevelAdmin)
admin.site.register(Role_Skill, Role_SkillAdmin)


