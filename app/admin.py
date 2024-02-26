from django.contrib import admin 
from app.models import *

# Register your models 
admin.site.register(Topic)

admin.site.register(WebPage)

admin.site.register(AccessRecord)