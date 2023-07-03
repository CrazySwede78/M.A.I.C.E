```python
import os
from models.step import Step
from utils.openai_api import call_openai
from utils.google_search import search_google
from utils.webscraper import scrape_web
from utils.pinecone_vector_db import use_pinecone

class StepGenerator:
    def __init__(self, step_id, part_id, outline_id, project_id, user_input_id):
        self.step_id = step_id
        self.part_id = part_id
        self.outline_id = outline_id
        self.project_id = project_id
        self.user_input_id = user_input_id
        self.step = None

    def generate_step(self):
        # Load necessary data
        step = Step.load(self.step_id)
        part = Part.load(self.part_id)
        outline = Outline.load(self.outline_id)
        project = Project.load(self.project_id)
        user_input = UserInput.load(self.user_input_id)

        # Use OpenAI API to generate step content
        step_content = call_openai(user_input.subject, user_input.keywords, user_input.target_content_type, user_input.word_count)

        # If non-fiction, search Google for additional content
        if user_input.target_content_type == 'non-fiction':
            google_results = search_google(user_input.subject + ' ' + user_input.keywords)
            step_content += scrape_web(google_results)

        # Save step content
        step.content = step_content
        step.save()

        # Update Pinecone vector database
        use_pinecone(step_content, self.step_id)

        self.step = step

    def get_step(self):
        return self.step
```