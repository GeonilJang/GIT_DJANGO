#dojo/forms.py

from django import forms
from .models import Post


#<-------------------------------------------------------------------------------------------->

#아래 Meta를 이용하고 싶으면 아래 인증함수를 models.py에 넣어주세요
# def min_length_3_validator(value):
#     if(len(value) < 3):
#         raise forms.ValidationError('3글자 이상입력 해줘용')




#모델을 만들고 바로 여기와서 이렇게 작성을 하게 되면 장고가 알아서 필드 값을 만들어서 제공해준다. 그리고 벨리데이션을 이용해서 필드에
#서 발생하는 오류와 처리를 담당 해준다 여기까지는 지금 -> 폼형식을 만든 것이고 아직은!! 화면에 보여주는 작업을 하지 않았습니다.
# class PostForm(forms.Form):
#     title = forms.CharField(validators=[min_length_3_validator])
#     content = forms.CharField(widget=forms.Textarea) #문자열은 다 문자열 일뿐 길이제한이 없기 때문에
#
#     def save(self, commit=True):
#         post = Post(**self.cleaned_data)
#         # post = Post(**{'title':120938,'content':120938}) 이런 식으로 들어가느끼 내가 마음대로 낚아도 된다는 것을 보여주네
#         if commit:
#             post.save()
#         return post

#<-------------------------------------------------------------------------------------------->

"""
아래 코드는 위의 코드와 동일하게 동작 한다
ModelForm

+ django Form Base
+ 지정된 Model로 부터 필드 정보를 읽어 들여, form fields를 셋팅
class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = '__all__'  #전체 필드 지정. 혹은 list로 읽어올 필드면 지정

+내부적으로 model instance를 유지
+유효성 검증에 통과한 값들로 (cleaned_data), 지정 model instance 로의 저장 (save)을 지원 (Create or Update)
"""
#데이터 베이스를 만들때 사용한 그 모델 틀을 가지고 폼도 똑같이 만들겠다 그런데
#완전 똑같이는 안만들고 내가 필요하다고 생각한 입력 값만을 아래와 같은 방법으로 커스텀 할 수 있다
# 그런데 상속받는게 다르네!!
# 여기에 자동적으로 save() 함수가 포함 되어있다 그래서 view에서 save()를 사용할 수 있는 것임.
"""
위와 동일한 사용으로 아래 처럼 구현을 하는데

저기에는 값을 model에 넣어 주는 코드가 이미 존재 하기때문에 저것을 사용하고 있는view.py에서는 데이터를 잘 받고 있다
모델에서 값을 가져와서 화면에 보여줄 형식만 만들었을 뿐이다
"""
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        #fields = '__all__'
        fields = ['title','content','user_agent']
        widgets = {
            'user_agent':forms.HiddenInput,
        }
