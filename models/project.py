```python
from marshmallow import Schema, fields

class Project:
    def __init__(self, subject, keywords, target_content_type, word_count):
        self.subject = subject
        self.keywords = keywords
        self.target_content_type = target_content_type
        self.word_count = word_count
        self.outline = None
        self.parts = []
        self.steps = []
        self.merge_verify = None

    def set_outline(self, outline):
        self.outline = outline

    def add_part(self, part):
        self.parts.append(part)

    def add_step(self, step):
        self.steps.append(step)

    def set_merge_verify(self, merge_verify):
        self.merge_verify = merge_verify

class ProjectSchema(Schema):
    subject = fields.Str(required=True)
    keywords = fields.List(fields.Str(), required=True)
    target_content_type = fields.Str(required=True)
    word_count = fields.Int(required=True)
    outline = fields.Nested('OutlineSchema', many=False)
    parts = fields.Nested('PartSchema', many=True)
    steps = fields.Nested('StepSchema', many=True)
    merge_verify = fields.Nested('MergeVerifySchema', many=False)
```