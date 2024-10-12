from django.db import models

class Question(models.Model):
    """
    Represents a question in a poll.

    Attributes:
        question_text (str): The text of the question being asked.
        pub_date (datetime): The date and time when the question was published.
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        """
        Returns the string representation of the Question instance, which is 
        the question text.
        """
        return self.question_text


class Choice(models.Model):
    """
    Represents a choice for a specific question in a poll.

    Attributes:
        question (ForeignKey): A foreign key relationship to the Question model.
        choice_text (str): The text of the choice.
        votes (int): The number of votes this choice has received.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """
        Returns the string representation of the Choice instance, which is 
        the choice text.
        """
        return self.choice_text
