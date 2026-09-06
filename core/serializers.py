from djoser.serializers import UserCreateSerializer

class My_user_create_serializers(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):

        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'username']
