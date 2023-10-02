from django.contrib import admin
from first_app.models import Topic,AccessRecord,Webpage,User,FormUser
class userAdmin(admin.ModelAdmin):
    list_display= ('name', 'email', 'text')
    search_fields = ('name', 'email')
    list_editable = ['email']
    fields = ['text', 'email']
# Register your models here.
admin.site.register(Topic)
admin.site.register(AccessRecord)
admin.site.register(Webpage)
admin.site.register(User)
admin.site.register(FormUser,userAdmin)


