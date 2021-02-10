from django.contrib import admin

from .models import Panel, Timestamp, Date

# Register your models here.
admin.site.register(Date)
admin.site.register(Panel)
admin.site.register(Timestamp)