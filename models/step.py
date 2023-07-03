```python
from marshmallow import Schema, fields

class Step:
    def __init__(self, step_id, step_message, content_type, word_count, keywords, subject):
        self.step_id = step_id
        self.step_message = step_message
        self.content_type = content_type
        self.word_count = word_count
        self.keywords = keywords
        self.subject = subject

class StepSchema(Schema):
    step_id = fields.Str()
    step_message = fields.Str()
    step_content_type = fields.Str()
    step_word_count = fields.Int()
    step_keywords = fields.List(fields.Str())
    step_subject = fields.Str()
```