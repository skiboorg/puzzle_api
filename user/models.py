from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save


class UserManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self, email, password, **extra_fields):
        user = self.model( email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)



class User(AbstractUser):
    username = None
    first_name = None
    last_name = None
    avatar = models.ImageField('Фото', upload_to='user/avatars',blank=True,null=True)
    email = models.EmailField('email', blank=True, null=True, unique=True)
    nickname = models.CharField('Ник', max_length=50, blank=False, null=True)
    balance = models.IntegerField('Баланс', default=1000)
    add_balance = models.IntegerField('Баланс снимаемый', default=0)

    rating = models.IntegerField('Рейтинг', default=0)
    age = models.IntegerField('Возраст', blank=True, null=True)
    sex = models.CharField('Пол', max_length=50, blank=True, null=True)
    study = models.TextField('Образование',  blank=True, null=True)
    work = models.TextField('Работа',  blank=True, null=True)
    profession = models.TextField('Профессия', blank=True, null=True)

    games_count = models.IntegerField(default=3)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return '{id}: {user}'.format(id=self.id, user=self.email)

    def get_avatar(self):
        if self.avatar:
            return self.avatar.url
        else:
            return '/media/no-avatar.svg'


