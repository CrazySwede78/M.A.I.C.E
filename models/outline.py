```python
from marshmallow import Schema, fields

class Outline:
    def __init__(self, id, project_id, subject, keywords, target_content_type, word_count):
        self.id = id
        self.project_id = project_id
        self.subject = subject
        self.keywords = keywords
        self.target_content_type = target_content_type
        self.word_count = word_count

class OutlineSchema(Schema):
    id = fields.Int(required=True)
    project_id = fields.Int(required=True)
    subject = fields.Str(required=True)
    keywords = fields.List(fields.Str(), required=True)
    target_content_type = fields.Str(required=True)
    word_count = fields.Int(required=True)
```