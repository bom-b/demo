from django.contrib import admin

from survey2.models import PracticeSurvey, PracticeAnswer


# Register your models here.
class SurveyAdmin(admin.ModelAdmin):
    list_display = ("question", "ans1", "ans2", "ans3", "ans4", "status")

admin.site.register(PracticeSurvey,SurveyAdmin)
admin.site.register(PracticeAnswer)