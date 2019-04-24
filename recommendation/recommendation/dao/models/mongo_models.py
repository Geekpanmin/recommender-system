from mongoengine import Document, StringField, ListField


class Poem(Document):
    meta = {
        'db_alias': 'poem_db',
        'collection': 'poem',
        'strict': False,
        'indexes': [
            'author',
            'paragraphs',
            'title'
        ]
    }

    author = StringField(required=True)
    paragraphs = ListField(required=True)
    strains = ListField(required=True, unique_with="user_id")
    title = StringField(required=True)
    other = StringField(required=False)


class Ci(Document):
    meta = {
        'db_alias': 'poem_db',
        'collection': 'ci',
        'strict': False,
        'indexes': [
            'author',
            'paragraphs',
            'rhythmic'
        ]
    }

    author = StringField(required=True)
    paragraphs = ListField(required=True)
    rhythmic = ListField(required=False, unique_with="user_id")
    other = StringField(required=False)
