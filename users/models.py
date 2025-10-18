from django.db import models
from BlogProject.models import SoftDeleteModel

# Create your models here.

class User(SoftDeleteModel):
    # id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True, null=False, max_length=100)
    password = models.CharField(max_length=100)
    nickname = models.CharField(unique=True, null=False, max_length=100)
    role = models.CharField(null=False, default="USER", max_length=100)

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