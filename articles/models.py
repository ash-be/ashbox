from django.db import models
from BlogProject.models import SoftDeleteModel

from users.models import User
# Create your models here.

class Category(SoftDeleteModel):
    category_name = models.CharField(max_length=100, null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles', null=False, blank=False)

    def __str__(self):
        return self.category_name


class Article(SoftDeleteModel):
    title = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='articles')
    # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    state = models.CharField(max_length=100, default="DRAFT", null=False, blank=False)
    published_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title


    # note | Relation
    # models.ForeignKey()
    # 필수 설정 옵션: to(참조 대상 모델), on_delete()
    """
        def __init__(
            self,
            to,
            on_delete,
            related_name=None,
            related_query_name=None,
            limit_choices_to=None,
            parent_link=False,
            to_field=None,
            db_constraint=True,
            **kwargs,
        ):
    """

    # on_delete options(models.)
    # deletion에서 import하면
    #     on_delete=CASCADE -> 이렇게 작성 가능 ㅋ

    # from django.db.models.deletion import (
    #     CASCADE,
    #     DO_NOTHING,
    #     PROTECT,
    #     RESTRICT,
    #     SET,
    #     SET_DEFAULT,
    #     SET_NULL,
    #     ProtectedError,
    #     RestrictedError,
    # )