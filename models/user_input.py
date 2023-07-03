```python
from marshmallow import Schema, fields

class UserInput:
    def __init__(self, subject, keywords, target_content_type, word_count):
        self.subject = subject
        self.keywords = keywords
        self.target_content_type = target_content_type
        self.word_count = word_count

class UserInputSchema(Schema):
    subject = fields.Str(required=True)
    keywords = fields.List(fields.Str(), required=True)
    target_content_type = fields.Str(required=True)
    word_count = fields.Int(required=True)
```