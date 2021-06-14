from django.db import models
import hashlib
import Crypto.Random
import base64

# Model for Users
class User(models.Model):
    username= models.TextField(unique=True, null=False)
    email= models.EmailField(unique=True,null=False)
    photoURL= models.TextField()
    password= models.TextField(null=False)
    salt= models.TextField()

    def __init__(self, username, email, photoURL, password, salt=None):
        if len(password)<6:
            return
        password, salt= self.setSaltAndPassword(password)
        super().__init__(username, email, photoURL, password, salt)

    def correctPassword(self,password):
        return self.encryptPassword(password, self.salt()) == self.password()
    
    def createSalt(self):
        return base64.b64encode(Crypto.Random.get_random_bytes(16))

    def encryptPassword(self, plainPassword, salt):
        return hashlib.sha256(plainPassword).update(salt).hexdigest()

    def setSaltAndPassword(self, password):
        salt= self.createSalt()
        password= self.encryptPassword(password,salt)
        return password,salt