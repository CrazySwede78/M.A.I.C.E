```python
import openai
from models.user_input import UserInput

class OpenAI_API:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def call_openai(self, user_input: UserInput):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=user_input.prompt,
            temperature=user_input.temperature,
            max_tokens=user_input.max_tokens
        )
        return response.choices[0].text.strip()

    def generate_creative_text(self, subject, keywords, target_content_type, word_count):
        user_input = UserInput(
            prompt=f"Write a {target_content_type} about {subject} with the following keywords: {', '.join(keywords)}",
            temperature=0.5,
            max_tokens=word_count
        )
        return self.call_openai(user_input)
```