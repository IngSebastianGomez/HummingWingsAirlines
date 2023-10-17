from django.contrib import admin
from api.models.email_template import EmailTemplate
from api.models.email_tracking import EmailTracking
from api.models.environment_variables import EnvironmentVariables
from api.models.root import Root
from api.models.user import User

# Register your models here.
admin.site.register(Root)
admin.site.register(User)
admin.site.register(EmailTemplate)
admin.site.register(EmailTracking)
admin.site.register(EnvironmentVariables)
