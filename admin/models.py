from mongoengine import Document, StringField, URLField, DictField, IntField, DateTimeField
import datetime
from random import randint

class Account(Document):
    
  name = StringField()
  username = StringField(default=None)
  email = StringField()
  password = StringField()
  profile_picture = URLField(default="https://cdn.dribbble.com/users/199982/screenshots/4044699/furkan-avatar-dribbble.png")
  created_at = DateTimeField()
  last_modified = DateTimeField(default=datetime.datetime.now)
  privileges = DictField(default={
    "admin": False, # Highest 
    "content_manager": False,
    "creator": False,
  })

  def save(self, *args, **kwargs):
    if not self.created_at:
      self.created_at = datetime.datetime.now()
    self.last_modified = datetime.datetime.now()
    return super(Account, self).save(*args, **kwargs)
  

  def set_picture(self, picture):
    self.profile_picture = picture
    self.save()
  

  def set_username(self, username):
    ## Check if not already exists
    ## Create
    ## Save
    pass
  

  def set_privileges(self, priviliges):
    for p in priviliges:
      if p in self.privileges.keys():
        self.privileges[p] = priviliges[p]
    print(self.privileges)
    self.save()