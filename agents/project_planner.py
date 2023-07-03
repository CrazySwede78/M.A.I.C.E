```python
from models.project import Project
from models.user_input import UserInput
from utils.openai_api import call_openai
from utils.google_search import search_google
from utils.webscraper import scrape_web
from utils.pinecone_vector_db import use_pinecone

class ProjectPlanner:
    def __init__(self):
        self.project = None
        self.user_input = None

    def create_project(self, user_input: UserInput):
        self.user_input = user_input
        self.project = Project(user_input.subject, user_input.keywords, user_input.target_content_type, user_input.word_count)

    def plan_project(self):
        # Use OpenAI API to generate a project plan
        project_plan = call_openai(self.user_input.subject, self.user_input.keywords, self.user_input.target_content_type, self.user_input.word_count)
        self.project.set_plan(project_plan)

    def gather_resources(self):
        # Use Google Search and Web Scraper for non-fiction writing
        if self.user_input.target_content_type == 'non-fiction':
            search_results = search_google(self.user_input.keywords)
            scraped_data = scrape_web(search_results)
            self.project.set_resources(scraped_data)

    def embed_data(self):
        # Use Pinecone Vector Database for embedded data
        embedded_data = use_pinecone(self.project.resources)
        self.project.set_embedded_data(embedded_data)

    def get_project(self):
        return self.project
```