from django.contrib import admin
from . models import district
from . models import branch
from . models import person_info


# Register your models here.

admin.site.register(district)
admin.site.register(branch)
admin.site.register(person_info)