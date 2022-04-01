from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save


class UserManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self, wallet, password, **extra_fields):
        user = self.model( wallet=wallet, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, wallet, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(wallet, password, **extra_fields)

    def create_superuser(self, wallet, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(wallet, password, **extra_fields)



class User(AbstractUser):
    username = None
    first_name = None
    last_name = None
    avatar = models.ImageField('Фото', upload_to='user/avatars',blank=True,null=True)
    email = models.EmailField('email', blank=True, null=True, unique=True)
    nickname = models.CharField('Ник', max_length=50, blank=False, null=True)
    balance = models.DecimalField('Баланс', default=0, max_digits=10, decimal_places=3)

    total_add = models.IntegerField('Баланс пополнен всего', default=0)
    total_remove = models.IntegerField('Баланс снят всего', default=0)

    wallet = models.CharField('Адрес кошелька', max_length=255, blank=True, null=True, unique=True)


    rating = models.IntegerField('Рейтинг', default=0)


    games_count = models.IntegerField(default=5)

    USERNAME_FIELD = 'wallet'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return '{id}: {user}'.format(id=self.id, user=self.wallet)

    def get_avatar(self):
        if self.avatar:
            return self.avatar.url
        else:
            return '/media/no-avatar.svg'


