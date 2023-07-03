```python
from models.outline import Outline
from utils.openai_api import call_openai

class OutlineCreator:
    def __init__(self, user_input):
        self.user_input = user_input
        self.outline = Outline()

    def create_outline(self):
        self.outline.subject = self.user_input.subject
        self.outline.keywords = self.user_input.keywords
        self.outline.target_content_type = self.user_input.target_content_type
        self.outline.word_count = self.user_input.word_count

        # Generate outline using OpenAI API
        self.outline.content = call_openai(self.outline.subject, self.outline.keywords)

        return self.outline

    def save_outline(self):
        # Save the outline instance to the database
        self.outline.save()

    def load_outline(self, outline_id):
        # Load the outline instance from the database
        self.outline = Outline.load(outline_id)
```