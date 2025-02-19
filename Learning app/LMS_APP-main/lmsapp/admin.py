from django.contrib import admin
from . models import *
# Register your models here.

class what_you_learn_TubalarInline(admin.TabularInline):
    model = What_you_learn

class requirements_TubalarInline(admin.TabularInline):
    model = Requirements

class video_TubalarInline(admin.TabularInline):
    model = Video

class course_admin(admin.ModelAdmin):
    inlines = (what_you_learn_TubalarInline, requirements_TubalarInline, video_TubalarInline)

admin.site.register(Categories)
admin.site.register(Course, course_admin)
admin.site.register(Author)
admin.site.register(Level)
admin.site.register(What_you_learn)
admin.site.register(Requirements)
admin.site.register(Lesson)
admin.site.register(Language)

admin.site.register(UserCourse)
admin.site.register(Payment)
