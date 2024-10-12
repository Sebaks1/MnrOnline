from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3  # Define the number of empty choices displayed when adding a new question

class QuestionAdmin(admin.ModelAdmin):
    # This controls what fields to display in the list of questions
    list_display = ('question_text', 'pub_date')
    
    # This adds a filter sidebar by date published
    list_filter = ['pub_date']
    
    # This adds a search box for the questions
    search_fields = ['question_text']

    # Adding inline choices to the question form
    inlines = [ChoiceInline]

# Register the Question model with custom admin settings
admin.site.register(Question, QuestionAdmin)

# Register the Choice model separately, but if handled by QuestionAdmin, no need to register it separately.
# admin.site.register(Choice)
