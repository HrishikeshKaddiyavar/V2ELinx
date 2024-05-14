# admin.py
from django.contrib import admin
from .models import *

admin.site.register(StudentDetail)
admin.site.register(Class8Ranks)
admin.site.register(Class9Ranks)
admin.site.register(Class10Ranks)
admin.site.register(SchoolRanks)