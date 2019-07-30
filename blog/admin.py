from django.contrib import admin
from .models import Blog
from .models import Sell_list
from .models import Buy_list

admin.site.register(Blog)
admin.site.register(Sell_list)
admin.site.register(Buy_list)
# Register your models here.
