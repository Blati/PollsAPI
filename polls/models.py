from django.db import models


class PollMain(models.Model):
    poll_main_name = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    ends_at = models.DateTimeField()
    poll_main_text = models.CharField(max_length=255)

    def __str__(self):
        return str(self.poll_main_name)


class Poll(models.Model):
    poll = models.ForeignKey(PollMain, on_delete=models.CASCADE, related_name='polls')
    poll_name = models.CharField(max_length=255)
    poll_text = models.CharField(max_length=255)

    def __str__(self):
        return str(self.poll_name)


class Choice(models.Model):
    poll = models.ForeignKey(Poll, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255, blank=True)
    choice_text = models.TextField(blank=True)

    def __str__(self):
        return str(self.choice_text)


class Vote(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name='votes')
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    voted_by = models.CharField(max_length=255, primary_key=True)

    class Meta:
        unique_together = ("poll", "voted_by")
