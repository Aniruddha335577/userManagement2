from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display="firstname","lastname","country","profession","membership"

admin.site.register(Member,MemberAdmin)