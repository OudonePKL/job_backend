from .models import UserModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm  # user프로필 수정
from django.forms import ModelForm, TextInput, PasswordInput, EmailInput, Textarea, DateInput, ClearableFileInput


# from django.contrib.auth import get_user_model


class UserForm(ModelForm):
    class Meta:
        model = UserModel
        fields = ['name', 'email', 'password',]

        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",  # 부트스트랩 적용에 필요!
                'placeholder': 'name'
            }),
            'email': EmailInput(attrs={
                'class': "form-control",
                'placeholder': 'Email'
            }),
            'code': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Code'
            }),
            'password': PasswordInput(attrs={
                'class': "form-control",
                'style': "font-family: sans-serif",
                'placeholder': 'Password'
            }),
        }


# class CustomUserChangeForm(UserChangeForm):
#     password = None
#
#     class Meta:
#         model = UserModel
#         fields = ['email', 'birth', 'comment', 'imgUrl', 'blog']
#
#         widgets = {
#             'email': EmailInput(attrs={
#                 'class': "form-control",
#                 'placeholder': 'Email'
#             }),
#             # 생일자 모양 맞춰주기 DateInput
#             'birth': DateInput(attrs={
#                 'class': "form-control",
#                 'placeholder': 'Birth',
#                 'type': 'date'
#             }),
#             'comment': Textarea(attrs={
#                 'class': "form-control",
#                 'placeholder': 'comment'
#             }),
#             # FileInput -> 프로필 수정할때 업로드한 사진이 안 불러와짐
#             'imgUrl': ClearableFileInput(attrs={
#                 'class': "form-control",
#                 'placeholder': 'imgUrl'
#             }),
#             'blog': TextInput(attrs={
#                 'class': "form-control",
#                 'placeholder': 'blog'
#             })
#         }