from django.db import models

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # Answer모델은 Question질문의 답변이므로 Question의 속성을 가져야 하는데 다른 모델 속성을 가지려면
    # ForeignKey를 이용한다. on_delete=models.CASCADE는 답변에 연결된 질문이 삭제되면 답변도 함께 삭제하라는 의미
    content = models.TextField()
    create_date = models.DateTimeField()
