from django.contrib import admin
from .models import Course, Week, Page

# define the courses panel for the admin
class CourseAdmin( admin.ModelAdmin ) : 

    exclude = ( "slug", )

# define the courses panel for the admin
class WeekAdmin( admin.ModelAdmin ) : 

    exclude = ( "slug", )


# define the courses panel for the admin
class PageAdmin( admin.ModelAdmin ) : 

    exclude = ( "slug", )

# register the models
admin.site.register( Course, CourseAdmin )
admin.site.register( Week, WeekAdmin )
admin.site.register( Page, PageAdmin )