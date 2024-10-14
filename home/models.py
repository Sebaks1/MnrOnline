from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    """
    Model representing a news article.

    Attributes:
        title (str): The title of the news article.
        content (str): The content of the news article.
        date_posted (datetime): The date and time when the article was posted.
    """
    # Title of the news article, with a maximum length of 200 characters.
    title = models.CharField(max_length=200)
    
    # Content of the news article.
    content = models.TextField()
    
    # Date and time when the article was posted, set automatically to the current date/time when the article is created.
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # String representation of the News object, which is the title of the article.
        return self.title


class ContactMessage(models.Model):
    """
    Model representing a contact message sent by a user.

    Attributes:
        user (User): The user who sent the message.
        message (str): The content of the message.
        created_at (datetime): The date and time when the message was created.
    """
    # ForeignKey relationship to the User model. When a user is deleted, all their messages are also deleted.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Content of the contact message.
    message = models.TextField()
    
    # Date and time when the message was created, set automatically to the current date/time when the message is created.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # String representation of the ContactMessage object, truncated to the first 50 characters of the message.
        return self.message[:50]
