from django.contrib import admin
from App_Blog.models import Blog,Comment,Likes

# Register your models here.

admin.site.site_header = 'Blog Administration'
admin.site.site_title = 'Blog Administration'
admin.site.index_title = 'Exclusive Admin Site'

admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Likes)
