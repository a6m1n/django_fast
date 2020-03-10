"""Classic admin registry"""
from django.contrib import admin
from app_users import models


admin.site.register(models.Languages)
admin.site.register(models.CustomUser)
admin.site.register(models.LeadLanguages)
