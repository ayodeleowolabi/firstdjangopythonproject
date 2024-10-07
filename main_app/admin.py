from django.contrib import admin
from .models import Character, GameSession, Location


admin.site.register(Character)
admin.site.register(GameSession)
admin.site.register(Location)

# Register your models here.
