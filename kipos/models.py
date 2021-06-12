import uuid

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


# Create your models here.

class KiposUserManager(BaseUserManager):
    def create_user(self, username, email, password):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
                email = self.normalize_email(email),
                username = username,
        )

        user.set_password(password)
        user.uuid = uuid.uuid4()
        user.save(using = self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
                email = email,
                password = password,
                username = username,
        )
        user.is_admin = True
        user.save(using = self._db)
        return user


class KiposUser(AbstractBaseUser):
    username = models.CharField(max_length = 40, unique = True)
    email = models.EmailField(max_length = 40, unique = True)
    uuid = models.CharField(max_length = 40, unique = True)
    is_active = models.BooleanField(default = True)
    is_admin = models.BooleanField(default = False)
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'password']
    objects = KiposUserManager()

    def __str__(self):
        return self.username + " " + self.email + " " + self.uuid

    def has_perm(self, perm, obj = None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Module(models.Model):
    user = models.ForeignKey(KiposUser, on_delete = models.CASCADE)
    name = models.CharField(max_length = 40,default = 'module')
    uuid=models.IntegerField(unique = True)
    forced_local_mode=models.BooleanField(default = False)
    telemetry =models.JSONField()
    settings = models.JSONField()

    def __str__(self):
        return self.user.uuid+" "+self.user.username+" "+str(self.id)
