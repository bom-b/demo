from django.db import models

# Create your models here.
class Survey(models.Model) :
    survey_idx = models.AutoField(primary_key=True)
    question = models.CharField(max_length=120,blank=True,null=True)
    ans1 = models.TextField(null=True)
    ans2 = models.TextField(null=True)
    ans3 = models.TextField(null=True)
    ans4 = models.TextField(null=True)
    #설문 진행상태 (y = 진행중 n = 종료)
    status = models.CharField(max_length=1, default='y')

class Answer(models.Model):
    answer_idx = models.AutoField(primary_key=True)
    survey_idx = models.ForeignKey("Survey", related_name="survey", on_delete=models.CASCADE, db_column="survey_idx")
    num = models.IntegerField()