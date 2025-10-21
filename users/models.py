from django.contrib.auth.models import AbstractUser
from django.db import models
from BlogProject.models import SoftDeleteModel
from users.managers import UserManager


# Create your models here.

class User(SoftDeleteModel, AbstractUser):
    username = None

    # nullable 재정의
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)

    # unique 값 재정의
    email = models.EmailField(unique=True, null=False, max_length=100)

    # is_staff / is_active AbstractUser 상속
    # SoftDelModel-BaseModel의 created_at 사용
    date_joined = None

    nickname = models.CharField(unique=True, null=False, max_length=100)

    # USERNAME_FIELD 재정의
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nickname"]

    objects = UserManager()

    def __str__(self):
        return self.email



    # note | models.Model - id 자동 추가 로직
    # 명시적으로 primary_key를 정의하지 않을 경우, name=id의 AutoField 자동 추가
    # Model 내 캡슐화된 Options 클래스의 _prepare 로직 내
    """
        if self.pk is None:
            if self.parents:
                # Promote the first parent link in lieu of adding yet another
                # field.
                field = next(iter(self.parents.values()))
                # Look for a local field with the same name as the
                # first parent link. If a local field has already been
                # created, use it instead of promoting the parent
                already_created = [
                    fld for fld in self.local_fields if fld.name == field.name
                ]
                if already_created:
                    field = already_created[0]
                field.primary_key = True
                self.setup_pk(field)
            else:
                pk_class = self._get_default_pk_class()
                auto = pk_class(verbose_name="ID", primary_key=True, auto_created=True)
                model.add_to_class("id", auto)
    """

    # note | EmailField
    # -> Django Validation

    # note | def __str__(self)
    # 이 객체의 대표 값으로, print 하거나 admin 페이지에서 노출되는 str을 설정

    # note | blank option
    # null = DB 차원에서의 null 값 허용 여부
    # blank = Django 차원에서의

    # note | AbstractUser
    # Django Auth를 유지하면서 아예 새로운 User를 만들고 싶다면
    # -> AbstractBaseUser 상속 및 커스텀

    # EMAIL_FIELD = "email"
    # USERNAME_FIELD = "username" > "email"
    #       : 로그인 시 사용하는 주요 식별자로 unique=True여야 함
    # REQUIRED_FIELDS = ["email"] > ["nickname"]
    #       : 필수로 입력받아야 하는 데이터
    #

    """
        username_validator = UnicodeUsernameValidator()

        username = models.CharField(
            _("username"),
            max_length=150,
            unique=True,
            help_text=_(
                "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
            ),
            validators=[username_validator],
            error_messages={
                "unique": _("A user with that username already exists."),
            },
        )
        first_name = models.CharField(_("first name"), max_length=150, blank=True)
        last_name = models.CharField(_("last name"), max_length=150, blank=True)
        email = models.EmailField(_("email address"), blank=True)
        is_staff = models.BooleanField(
            _("staff status"),
            default=False,
            help_text=_("Designates whether the user can log into this admin site."),
        )
        is_active = models.BooleanField(
            _("active"),
            default=True,
            help_text=_(
                "Designates whether this user should be treated as active. "
                "Unselect this instead of deleting accounts."
            ),
        )
        date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    
        objects = UserManager()
    
        EMAIL_FIELD = "email"
        USERNAME_FIELD = "username"
        REQUIRED_FIELDS = ["email"]
    """