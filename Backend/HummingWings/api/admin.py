from django.contrib import admin
from api.models.root import Root
from api.models.user import User

# Register your models here.
admin.site.register(Root)
admin.site.register(User)
