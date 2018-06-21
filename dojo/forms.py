#dojo/forms.py

from django import forms
from .models import Post


def min_length_3_validator(value):
    if(len(value) < 3):
        raise forms.ValidationError('3글자 이상입력 해줘용')




#모델을 만들고 바로 여기와서 이렇게 작성을 하게 되면 장고가 알아서 필드 값을 만들어서 제공해준다. 그리고 벨리데이션을 이용해서 필드에
#서 발생하는 오류와 처리를 담당 해준다 여기까지는 지금 -> 폼형식을 만든 것이고 아직은!! 화면에 보여주는 작업을 하지 않았습니다.
class PostForm(forms.Form):
    title = forms.CharField(validators=[min_length_3_validator])
    content = forms.CharField(widget=forms.Textarea) #문자열은 다 문자열 일뿐 길이제한이 없기 때문에

    def save(self, commit=True):
        post = Post(**self.cleaned_data)
        # post = Post(**{'title':120938,'content':120938}) 이런 식으로 들어가느끼 내가 마음대로 낚아도 된다는 것을 보여주네
        if commit:
            post.save()
        return post
