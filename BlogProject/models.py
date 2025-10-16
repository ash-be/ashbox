from django.db import models
from django.utils import timezone

class BaseModel(models.Model):
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now=True)

    class Meta:
        abstract = True


class SoftDeleteModel(BaseModel):
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def delete(self, *args, **kwargs):
        """
        Perform softDel by df.
        Pass 'hard=True' to execute Django's origin Del.
        """
        if kwargs.pop("hard", False):
            super().delete(*args, **kwargs)
        else :
            self.is_deleted = True
            self.deleted_at = timezone.now()
            self.save()

    class Meta:
        abstract = True



    # note | Meta class
    # model의 meta data를 담는 클래스 > jpa에서의 각종 어노테이션들
    # Options
    #     abstract bool : DB 테이블로 생성하지 않고, 상속 용도로만 사용
    #     -> base model에 사용

    # note | *args, **kwargs
    # softDel만 정의할 경우
    # def delete(self):
    #     self.is_deleted = True
    #     self.deleted_at = timezone.now()
    #     self.save()

    # hardDel을 함께 정의할 경우
    # => hard=True일 때, 상속받는 super(Models.delete)의 del을 활용
    # => 인자 값 및 옵션 등을 super에게 전달하기 위해 사용
    # *: tuple 형태로 여러 개의 위치 인자를 전달
    # ** : dict 형태로 여러 개의 키워드 인자를 전달

    """
        def test(*nums, **fruit):
            print(nums)
            print(fruit)
    
        test(1, 2, 3, apple=red, banana=yellow)
        # (1, 2, 3)
        # {'apple': "red", 'banana': "yellow"}
    """

    # kwargs.pop("hard", False)
    # kwargs에서 hard를 찾고, 있으면 그 값을 반환
    # 없으면, k 값(False) 반환

    """    
        def pop(self, k, d=None):  # real signature unknown; restored from __doc__
            \"""
            D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
        
            **If the key is not found, return the default if given;
            otherwise, raise a KeyError.**
            \"""
            pass
    """

    # models.delete()
    """
        def delete(self, using=None, keep_parents=False):
            if not self._is_pk_set():
                raise ValueError(
                    "%s object can't be deleted because its %s attribute is set "
                    "to None." % (self._meta.object_name, self._meta.pk.attname)
                )
            using = using or router.db_for_write(self.__class__, instance=self)
            collector = Collector(using=using, origin=self)
            collector.collect([self], keep_parents=keep_parents)
            return collector.delete()
    """