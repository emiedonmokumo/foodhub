from datetime import datetime
from mongoengine import Document, StringField, DateTimeField, URLField


class Post(Document):
    title = StringField(max_length=255, required=True)
    slug = StringField(max_length=255)
    content = StringField()
    featured_image = StringField(max_length=512)
    published_date = DateTimeField()
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

    meta = {
        'collection': 'posts',
        'ordering': ['-published_date', '-created_at']
    }

    def __str__(self):
        return self.title

    def to_dict(self):
        return {
            'id': str(self.id),
            'title': self.title,
            'slug': self.slug,
            'content': self.content,
            'featured_image': self.featured_image,
            'published_date': self.published_date,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
