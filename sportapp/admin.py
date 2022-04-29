from django.contrib import admin
from .models import Sport
from .models import Comment
from .models import Champions
from .models import Registration
# Register your models here.
admin.site.register(Sport)
admin.site.register(Comment)
admin.site.register(Champions)
admin.site.register(Registration)