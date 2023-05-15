from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm,  PasswordChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth import get_user_model
import datetime
from nested_formset import nestedformset_factory


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label="아이디",
        widget=forms.TextInput(
            attrs={
                'class': 'form--control',
                'placeholder': '아이디를 입력하세요',
            }
        ),
    )
    first_name = forms.CharField(
        label="이름",
        widget=forms.TextInput(
            attrs={
                'class': 'form--control',
                'placeholder': '이름을 입력하세요',
            }

        ),
    )
    birthday = forms.DateField(
        initial=datetime.date(2000, 1, 1),
        label="생일",
        widget=forms.DateInput(
            attrs={
                'type':'date',
                'class': 'form--control',
            }
        ),
    )
    email = forms.EmailField(
        label="이메일",
        widget=forms.TextInput(
            attrs={
                'class': 'form--control',

            }
        ),
    )
    image = forms.ImageField(
        label='프로필 이미지',
        required=False,
        widget=forms.ClearableFileInput(
        attrs={
            'class': 'form--control',
            }
        )
    )
    
#  """    BIG_CHOICES = [
#         ('컨셉 & 아이디어', '컨셉 & 아이디어'),
#         ('작품성', '작품성'),
#         ('캐릭터', '캐릭터'),
#         ('감상평', '감상평'),
#         ('감독 & 연출', '감독 & 연출'),
#         ('스토리 & 구성', '스토리 & 구성'),
#         ('편집 & 각본', '편집 & 각본'),
#         ('시각 & 음향', '시각 & 음향'),
#         ('클라이맥스 & 결말', '클라이맥스 & 결말'),
#     ]
    
#     TAG_CHOICES = [
#         ('컨셉 & 아이디어', ( 
#             ('무슨 생각인지 알 수 없는', '무슨 생각인지 알 수 없는'), 
#             ('해석이 새로운', '해석이 새로운'), 
#             ('누구나 이해할 수 있는', '누구나 이해할 수 있는'), 
#             ('개성있는”, “개성있는'), 
#             ('유쾌함을 잃지 않는', '유쾌함을 잃지 않는'), 
#             ('상상력이 무한한', '상상력이 무한한'),
#          )),
#          ('작품성', (
#             ('러블리한', '러블리한'), 
#             ('영양가 없는', '영양가 없는'), 
#             ('모던한', '모던한'), 
#             ('취향을 저격하는', '취향을 저격하는'), 
#             ('옛날 감성인', '옛날 감성인'), 
#             ('B급감성인', 'B급감성인'), 
#             ('친구들끼리 보는', '친구들끼리 보는'), 
#             ('애인이랑 보는', '애인이랑 보는'), 
#             ('완성도가 높은', '완성도가 높은'), 
#             ('언제 봐도 좋은', '언제 봐도 좋은'), 
#             ('내 눈을 의심하는', '내 눈을 의심하는'), 
#             ('전혀 유쾌하지 않은', '전혀 유쾌하지 않은'),

#          )),
#          ('캐릭터', (
#             ('캐릭터가 사랑스러운', '캐릭터가 사랑스러운'), 
#             ('개 잘생긴', '개 잘생긴'), 
#             ('개 예쁜', '개 예쁜'), 
#             ('띨띨한', '띨띨한'), 
#             ('끼부리는', '끼부리는'), 
#             ('쥐어박고 싶은', '쥐어박고 싶은'), 
#             ('호구인', '호구인'), 
#             ('개새끼인', '개새끼인'), 
#             ('암걸리는', '암걸리는'), 
#             ('천재인', '천재인'), 
#             ('동물이 주인공인', '동물이 주인공인'),  
#         )),
        
        
#         ('감상평',  (
#             ('읭스러운', '읭스러운'), 
#             ('감탄사를 연발하는', '감탄사를 연발하는'), 
#             ('보는 내내 설레는', '보는 내내 설레는'), 
#             ('웃음이 떠나지 않는', '웃음이 떠나지 않는'), 
#             ('깜놀하는', '깜놀하는'), 
#             ('거부감 드는', '거부감 드는'), 
#             ('경악하는', '경악하는'), 
#             ('추억을 자극하는', '추억을 자극하는'), 
#             ('박장대소 하는', '박장대소 하는'), 
#             ('리뷰를 찾아보는', '리뷰를 찾아보는'), 
#             ('엄청난 충격을 받는', '엄청난 충격을 받는'), 
#             ('지루 할 수 있는', '지루 할 수 있는'),
            
#         )),
        
#         ('감독 & 연출', (
#             ('거장의 작품인', '거장의 작품인'), 
#             ('구닥다리인', '구닥다리인'), 
#             ('레트로한', '레트로한'), 
#             ('특유의 매력이 있는', '특유의 매력이 있는'), 
#             ('기술적인 성취를 보인', '기술적인 성취를 보인'), 
#             ('장인정신인', '장인정신인'), 
#             ('거침없는', '거침없는'), 
#             ('미친 연출력인', '미친 연출력인'), 
#             ('감독에게 찬사를 보내는', '감독에게 찬사를 보내는'), 
#             ('연출이 과감한', '연출이 과감한'),
            
#         )),
        
#         ('스토리 & 구성', (
#             ('인생이 담겨있는', '인생이 담겨있는'), 
#             ('내용 별거 없는', '내용 별거 없는'),
#             ('두서없는', '두서없는'),
#             ('급발진하는', '급발진하는'), 
#             ('막장 드라마인', '막장 드라마인'), 
#             ('완급 조절에 실패한', '완급 조절에 실패한'), 
#             ('내용이 뻔한', '내용이 뻔한'),
#             ('결말이 뻔히 보이는', '결말이 뻔히 보이는'),
#             ('내용이 알찬', '내용이 알찬'),
#             ('속도감 있는', '속도감 있는'),
#             ('권선징악인', '권선징악인'),
#             ('반전의 묘미가 있는', '반전의 묘미가 있는'),    
#             ('꼬이고 꼬인', '꼬이고 꼬인'),   
#             ('전개가 깔끔한', '전개가 깔끔한'),
#         )),
        
#         ('편집 & 각본', (
#              ('의식의 흐름', '의식의 흐름'),    
#              ('유행어를 낳은', '유행어를 낳은'),    
#              ('가벼운 농담을 던지는', '가벼운 농담을 던지는'),    
#              ('클리셰를 깨는', '클리셰를 깨는'),    
#              ('말장난을 하는', '말장난을 하는'),    
#              ('빌드업한', '빌드업한'),    
#              ('문학적인', '문학적인'),
#         )),
        
#         ('시각 & 음향', ( 
#             ('구경하는 재미가 있는', '구경하는 재미가 있는'),    
#             ('블링블링한', '블링블링한'),    
#             ('색감이 다채로운', '색감이 다채로운'),    
#             ('특유의 색감이 있는', '특유의 색감이 있는'),    
#             ('화려한', '화려한'),    
#             ('영상미가 세련된', '영상미가 세련된'),    
#             ('마법 같은', '마법 같은'),    
#             ('음악이 조화를 이루는', '음악이 조화를 이루는'),    
#             ('한 폭의 그림 같은', '한 폭의 그림 같은'),    
#             ('비주얼 쇼크인', '비주얼 쇼크인'),
#         )),
        
#         ('클라이맥스 & 결말', (
#             ("클라이맥스","클라이맥스"),
#             ("마무리가 훈훈한","마무리가 훈훈한"),
#             ("극적인 피날레","극적인 피날레"),
#             ("예상치 못한 결말","예상치 못한 결말"),
#             ("마무리가 훈훈한", "마무리가 훈훈한"),
#             ("주인공이 행복해지는", "주인공이 행복해지는"),
#             ("열린 결말인", "열린결말인"),
#             ('결말이 마음에 드는','결말이 마음에 드는'),
#             ('황급한','황급한'),
#         )),
#     ]
    
#     big_tags = forms.MultipleChoiceField(
#         label = '태그 대분류',
#         widget = forms.CheckboxSelectMultiple(
            
#         ),
#         choices = BIG_CHOICES,
#     )
#  """
    
    TAG_CHOICES = [
        ('스펙터클한', '스펙터클한'), ('빨리보고싶은', '빨리보고싶은'), ('인생이담겨있는', '인생이담겨있는'), 
        ('믿고 보는 배우인', '믿고 보는 배우인'), ('튀어나오는', '튀어나오는'),
        ('환상적인', '환상적인'), ('기승전결이 완벽한','기승전결이 완벽한'), ('외모가 잘생긴','외모가 잘생긴'), ('가슴 떨리는', '가슴 떨리는'),
        ('미장센이 좋은', '미장센이 좋은'), ('감독의 센스가 좋은', '감독의 센스가 좋은'), ('이해시켜 주는', '이해시켜 주는'), ('서정적인', '서정적인'), ('상상력이 무한한', '상상력이 무한한'),
        ('위대한 쇼인','위대한 쇼인'), ('구성이 알찬','구성이 알찬'), ('뒤끝 없는','뒤끝 없는'), ('화면 효과가 좋은','화면 효과가 좋은'), ('종결 낸','종결 낸'), ('배우들이 대거 출연한', '배우들이 대거 출연한'), ('인생의 진리를 느끼는','인생의 진리를 느끼는'), ('진심으로 응원하는','진심으로 응원하는'), ('깔쌈한', '깔쌈한'), 
        ('잘 다듬어진', '잘 다듬어진'), ('감독이 섬세한', '감독이 섬세한'), ('웃기고 재밌는', '웃기고 재밌는'), ('전개에 군더더기가 없는', '전개에 군더더기가 없는'), ('명대사를 남기는', '명대사를 남기는'), ('중간중간 놀라는', '중간중간 놀라는'), ('끝맺는', '끝맺는'), ('감독이 대단한', '감독이 대단한'), ('맨날 똑같은', '맨날 똑같은'), 
        ('노래와 춤이 있는', '노래와 춤이 있는'), ('카메오가 나오는','카메오가 나오는'), ('감독의 센스가 좋은', '감독의 센스가 좋은'), ('일확천금을 노리는', '일확천금을 노리는'), ('군더더기 없는', '군더더기 없는'), ('B급감성인', 'B급감성인'), ('아무말 대잔치인', '아무말 대잔치인'), ('갑툭튀 장면이 있는', '갑툭튀 장면이 있는'), 
        ('감독이 뚝심있는', '감독이 뚝심있는'), ('꿀 떨어지는', '꿀 떨어지는'), ('야심작인', '야심작인'), ('말 그대로 미친', '말 그대로 미친'), ('생각할 거리가 많은','생각할 거리가 많은'), ('적나라하게 보여 주는', '적나라하게 보여 주는'), ('폭력적인', '폭력적인'),
        ('상영시간이 긴', '상영시간이 긴'), ('내용이 산으로 가는', '내용이 산으로 가는'), ('난해한', '난해한'), ('지루한', '지루한'), ('무슨 소리인지 모르겠는', '무슨 소리인지 모르겠는'), ('시대착오적인', '시대착오적인'), ('결말이 부실한', '결말이 부실한'),
    ]
    tags = forms.MultipleChoiceField(
        label = '태그 중분류',
        widget = forms.CheckboxSelectMultiple(
            
        ),
        choices = TAG_CHOICES,
    )
    password1 = forms.CharField(
        label="비밀번호",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form--control',
                'placeholder': '비밀번호를 입력하세요',
            }
        ),
    )
    password2 = forms.CharField(
        label="비밀번호 확인",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form--control',
                'placeholder': '비밀번호를 다시 입력하세요',
            }
        ),
    )
    password=None
    
    
    
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('username', 'first_name', 'birthday', 'email', 'image','tags',)

class CustomUserChangeForm(UserChangeForm):
    email = forms.EmailField(
        label= False,
        widget=forms.TextInput(
            attrs={
                'class': 'form--control',
                'placeholder': '이메일을 입력하세요',
               
            }
        )
    )
    first_name = forms.CharField(
        label= False,
        widget=forms.TextInput(
            attrs={
                'class': 'form--control',
                'placeholder': '이름을 입력하세요',
               
            }
        )
    )
    birthday = forms.DateField(
        initial=datetime.date(2000, 1, 1),
        label=False,
        widget=forms.DateInput(
            attrs={
                'type':'date',
                'class': 'form--control',
            }
        ),
    )
    image = forms.ImageField(
        label=False,
        required=False,
        widget=forms.ClearableFileInput(
        attrs={
            'class': 'form--control',
            }
        )
    )
    
    TAG_CHOICES = [
        ('스펙터클한', '스펙터클한'), ('빨리보고싶은', '빨리보고싶은'), ('인생이담겨있는', '인생이담겨있는'), 
        ('믿고 보는 배우인', '믿고 보는 배우인'), ('튀어나오는', '튀어나오는'),
        ('환상적인', '환상적인'), ('기승전결이 완벽한','기승전결이 완벽한'), ('외모가 잘생긴','외모가 잘생긴'), ('가슴 떨리는', '가슴 떨리는'),
        ('미장센이 좋은', '미장센이 좋은'), ('감독의 센스가 좋은', '감독의 센스가 좋은'), ('이해시켜 주는', '이해시켜 주는'), ('서정적인', '서정적인'), ('상상력이 무한한', '상상력이 무한한'),
        ('위대한 쇼인','위대한 쇼인'), ('구성이 알찬','구성이 알찬'), ('뒤끝 없는','뒤끝 없는'), ('화면 효과가 좋은','화면 효과가 좋은'), ('종결 낸','종결 낸'), ('배우들이 대거 출연한', '배우들이 대거 출연한'), ('인생의 진리를 느끼는','인생의 진리를 느끼는'), ('진심으로 응원하는','진심으로 응원하는'), ('깔쌈한', '깔쌈한'), 
        ('잘 다듬어진', '잘 다듬어진'), ('감독이 섬세한', '감독이 섬세한'), ('웃기고 재밌는', '웃기고 재밌는'), ('전개에 군더더기가 없는', '전개에 군더더기가 없는'), ('명대사를 남기는', '명대사를 남기는'), ('중간중간 놀라는', '중간중간 놀라는'), ('끝맺는', '끝맺는'), ('감독이 대단한', '감독이 대단한'), ('맨날 똑같은', '맨날 똑같은'), 
        ('노래와 춤이 있는', '노래와 춤이 있는'), ('카메오가 나오는','카메오가 나오는'), ('감독의 센스가 좋은', '감독의 센스가 좋은'), ('일확천금을 노리는', '일확천금을 노리는'), ('군더더기 없는', '군더더기 없는'), ('B급감성인', 'B급감성인'), ('아무말 대잔치인', '아무말 대잔치인'), ('갑툭튀 장면이 있는', '갑툭튀 장면이 있는'), 
        ('감독이 뚝심있는', '감독이 뚝심있는'), ('꿀 떨어지는', '꿀 떨어지는'), ('야심작인', '야심작인'), ('말 그대로 미친', '말 그대로 미친'), ('생각할 거리가 많은','생각할 거리가 많은'), ('적나라하게 보여 주는', '적나라하게 보여 주는'), ('폭력적인', '폭력적인'),
        ('상영시간이 긴', '상영시간이 긴'), ('내용이 산으로 가는', '내용이 산으로 가는'), ('난해한', '난해한'), ('지루한', '지루한'), ('무슨 소리인지 모르겠는', '무슨 소리인지 모르겠는'), ('시대착오적인', '시대착오적인'), ('결말이 부실한', '결말이 부실한'),
    ]

    tags = forms.MultipleChoiceField(
        label = '태그',
        widget = forms.CheckboxSelectMultiple(
            
        ),
        choices = TAG_CHOICES,
    )
    password=None
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('first_name', 'birthday', 'email', 'image')

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label=False,
        widget=forms.TextInput(
            attrs = {
                'class': 'login--form--control',
                'placeholder' : '아이디',
              
            }
        )
    )
    password = forms.CharField(
        label=False,
        widget=forms.PasswordInput(
            attrs = {
                'class': 'login--form--control',
                'placeholder' : '비밀번호',
               
            }
        )
    )

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=False,
        widget=forms.PasswordInput(
            attrs = {
                'class': 'form--control',
                'placeholder' : '기존 비밀번호',
            }
        )
    )
    new_password1 = forms.CharField(
        label=False,
        widget= forms.PasswordInput(
        attrs = {
                'class': 'form--control',
                'placeholder' : '새 비밀번호',

            }
        ),
        help_text='',
    )
    new_password2 = forms.CharField(
        label=False,
        widget= forms.PasswordInput(
        attrs = {
                'class': 'form--control',
                'placeholder' : '새 비밀번호(확인)',

            }
        ),
        help_text='',
    )