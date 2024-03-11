from django.contrib import admin
from . models import Movies,Language,Actors,Genre,Review
# Register your models here.
class ActorsAdmin(admin.ModelAdmin):
    list_display = ["name"]
    # prepopulated_fields = {'slug':('name',)}
admin.site.register(Actors,ActorsAdmin)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ["name"]
    # prepopulated_fields = {'slug':('name',)}
admin.site.register(Language,LanguageAdmin)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["id","name",'time','release_date']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Movies,MovieAdmin)
class GenreAdmin(admin.ModelAdmin):
    list_display = ["name"]
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Genre,GenreAdmin)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["movie","count"]
admin.site.register(Review,ReviewAdmin)