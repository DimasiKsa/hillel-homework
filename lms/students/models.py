import uuid
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.core.validators import MinLengthValidator
from django.db import models
import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from faker import Faker
from students.validators import no_elon_validator
from courses.models import Course, UserType
from django.contrib.auth.models import User, PermissionsMixin, AbstractBaseUser
from django.utils.translation import ugettext as _
from students.managers import CustomUserManager, PeopleManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=150, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)

    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    photo = models.ImageField(upload_to='user_photos/', null=True, blank=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)


class ExtendedUser(CustomUser):
    people = PeopleManager()

    class Meta:
        proxy = True
        ordering = ('first_name',)

    def some_action(self):
        print(self.username)


class Person(models.Model):

    first_name = models.CharField(
        max_length=60, null=False, validators=[MinLengthValidator(2)]
    )
    last_name = models.CharField(
        max_length=80, null=False, validators=[MinLengthValidator(2)]
    )
    email = models.EmailField(
        max_length=120, null=True, validators=[no_elon_validator], unique=True
    )
    birthdate = models.DateField(null=True, default=datetime.date.today)

    avatar_image = models.ImageField(upload_to='static/', null=True, blank=True)

    summary = models.FileField(upload_to='static/', null=True, blank=True)

    class Meta:
        abstract = True


class Student(Person):

    course = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.full_name()}, {self.age()}, {self.email} id({self.id})"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def age(self):
        return datetime.datetime.now().year - self.birthdate.year

    @classmethod
    def generate_instances(cls, count):
        faker = Faker()
        for _ in range(count):
            st = cls(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                email=faker.email(),
                birthdate=faker.date_time_between(start_date="-30y", end_date="-18y"),
            )
            st.save()


class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    birthdate = models.DateField(blank=True, null=True)
    avatar_image = models.ImageField(upload_to='static/', null=True, blank=True)
    summary = models.FileField(upload_to='static/', null=True, blank=True)
    type = models.ForeignKey(UserType, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)



