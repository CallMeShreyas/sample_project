from django.db import models
from student.models import Student
# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length = 20)
    date_created = models.DateField()

    def __str__(self):
        return self.name

class Test(models.Model):
    name = models.CharField(max_length = 20)
    start_time = models.DateTimeField(blank = False)
    end_time = models.DateTimeField(blank = False)
    course_related = models.ForeignKey(Course, on_delete = models.CASCADE)
    given_by = models.ForeignKey(Student, on_delete = models.CASCADE)

    def __str__(self):
        return self.name


class Question(models.Model):
    test_related = models.ForeignKey(Test, on_delete = models.CASCADE)
    question = models.CharField(max_length = 100)

    option_1 = models.CharField(max_length = 50, default = "")
    option_2 = models.CharField(max_length = 50, default = "")
    option_3 = models.CharField(max_length = 50, default = "")
    option_4 = models.CharField(max_length = 50, default = "")

    correct_answer = models.CharField(max_length = 50, default = "")

    def __str__(self):
        return self.question

class Answer(models.Model):
    given_by = models.ForeignKey(Student, on_delete = models.CASCADE)
    question_related = models.ForeignKey(Question, on_delete = models.CASCADE   )
    answer = models.CharField(max_length = 50, default = "")
 
    def __str__(self):
        return self.answer



# class Option(models.Model):
#     question_related = models.ForeignKey(Question, on_delete = models.CASCADE)
#     option_1 = models.CharField(max_length = 50)
#     option_2 = models.CharField(max_length = 50)
#     option_3 = models.CharField(max_length = 50)
#     option_4 = models.CharField(max_length = 50)
#     question_str = str(question_related)

#     def __str__(self):
#         return self.question_str

# class CorrectOption(models.Model):
#     question_related = models.ForeignKey(Question, on_delete = models.CASCADE)
#     correct_answer = models.ForeignKey(Option, on_delete = models.CASCADE)

#     def __str__(self):
#         return self.question_related


# class Answer(models.Model):
#     question_related = models.ForeignKey(Question, on_delete = models.CASCADE)
#     answer_given = models.ForeignKey(Option, on_delete = models.CASCADE)
#     given_by = models.ForeignKey(Student, on_delete = models.CASCADE)

#     def __str__(self):
#         return self.question_related

