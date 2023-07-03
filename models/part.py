```python
from marshmallow import Schema, fields

class Part:
    def __init__(self, part_id, subject, keywords, target_content_type, word_count, content=""):
        self.part_id = part_id
        self.subject = subject
        self.keywords = keywords
        self.target_content_type = target_content_type
        self.word_count = word_count
        self.content = content

class PartSchema(Schema):
    part_id = fields.Str(required=True)
    subject = fields.Str(required=True)
    keywords = fields.List(fields.Str(), required=True)
    target_content_type = fields.Str(required=True)
    word_count = fields.Int(required=True)
    content = fields.Str()
```