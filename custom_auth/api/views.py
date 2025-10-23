from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        token['is_superuser'] = user.is_superuser
        token['is_staff'] = user.is_staff
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



    # note | simplejwt/views.py
    """
    class TokenObtainPairView(TokenViewBase):
        \"""
        Takes a set of user credentials and returns an access and refresh JSON web
        token pair to prove the authentication of those credentials.
        \"""

        _serializer_class = api_settings.TOKEN_OBTAIN_SERIALIZER

    token_obtain_pair = TokenObtainPairView.as_view()
    """


    # note | @classmethod
    # 클래스 자체를 인자로 받아서 실행시키도록 하기 위함

    """
    class Dog:
        def bark(self):
            print("멍멍!")
    Dog.bark()
    
    # TypeError
    """

    """
    class Dog:
        def bark(self):
            print("멍멍!")
        
    dog = Dog()
    dog.bark()
    
    # 멍멍!
    """

    """
    class Dog:
        @classmethod
            def bark(cls):
                print(f"{cls.__name__}!!!")

    Dog.bark()
    
    # Dog!!!
    """


    # note | factory method
    # 인스턴스 객체를 생성하지 않고, 무엇을 만들지 '자식 클래스'가 정하도록 함
    # token_class: Optional[type[Token]] = None
    # 하위 클래스(TokenObtainPairSerializer)에서 token_class가 RefreshToken으로 정의됨
    # 하위 클래스의 메서드 validate()에서 get_token()의 cls가 self.user로 인자를 받음
    # -> return cls.token_class.for_user(user)
    # => return RefreshToken.for_user(user)
    # => cls = TokenObtainPairSerializer(호출된 하위 클래스 의미)
    # 따라서 하위 클래스를 객체를 제작(인스턴스)하지 않고, 직접 호출하기 위해 @classmethod 사용

    """
    simplejwt/serializers.py
    
    # 상위 클래스
    class TokenObtainSerializer(serializers.Serializer):
        username_field = get_user_model().USERNAME_FIELD
        token_class: Optional[type[Token]] = None
    
        ...

        @classmethod
        def get_token(cls, user: AuthUser) -> Token:
            return cls.token_class.for_user(user)  # type: ignore
            
    # 하위 클래스 > RefreshToken으로 정의
    class TokenObtainPairSerializer(TokenObtainSerializer):
        token_class = RefreshToken

        def validate(self, attrs: dict[str, Any]) -> dict[str, str]:
            ...
            refresh = self.get_token(self.user)
            ...
    """