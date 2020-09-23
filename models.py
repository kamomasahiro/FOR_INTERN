from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return '<Member:id=' + str(self.id) + ', ' + \
            self.name + '>'

class Message(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=300)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '<Message:id=' + str(self.id) + ', ' + \
            self.title + '(' + str(self.pub_date) + ')>'

    class Meta:
        ordering = ('pub_date',)
