from django.contrib import admin
from unesco.models import Site, Category, Region, State, Iso
# Register your models here.
admin.site.register(Site)
admin.site.register(State)
admin.site.register(Region)
admin.site.register(Category)
admin.site.register(Iso)
