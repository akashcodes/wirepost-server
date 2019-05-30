
import datetime
from mongoengine import Document, StringField, URLField, IntField, DateTimeField
from random import randint


class Post(Document):

    title = StringField()
    content_markup = StringField()
    content_html = StringField()
    banner = URLField()
    views = IntField(min_value=0)
    creation_date = DateTimeField()
    modified_date = DateTimeField(default=datetime.datetime.now)
    category = StringField()
    color= StringField()
    url = StringField()

    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = datetime.datetime.now()
        self.modified_date = datetime.datetime.now()
        return super(Post, self).save(*args, **kwargs)


    """def generate_url(self):
        try:
            oid = self.id
            title = self.title
            url = str(title).lower().strip().replace(" ", "-")
            while Post.objects(url=url).count() != 0:
                rand = randint(0, 1000000)
                url = url + "-" + str(rand)
            self.url = url
            self.save()
        except:
            print("Some error occured while generating post URL ...")
    """

    def view(self):
        self.views += 1
        self.save()