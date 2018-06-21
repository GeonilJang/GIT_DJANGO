ep12
여러 템플릿 파일 별로 필연적으로 발생하는 중복을 "상속"을 통해 중복제거 상속은 여러번 이루어 질수 있다.

** 1)부모 템플릿은 전체 레이아웃을 정의하며,
** 2)자식 템플릿이 재정의할 block을 다수 정의 해야한다.

자식 템플릿은 부모 템플릿을 상속받은 후에 부모 템플릿의 block 영역에 대해 재정의만 가능하며 그외 코드는 무시

템플릿 상속 문법:: 항시 자식 템플릿 코드 내, "최상단"에 쓰여져야 합니다.

{% extends "부모 템플릿 경로" %}

* 자식템플릿은 부모가 정의한 부분 안에 block 안에만 사용이 가능합니다.


-- 프로젝트 전반적으로 사용할 수 있는 템플릿을 만들고 상속 상속 이런 식으로 만들어 사용하느 것이 좋다

보통 전반적으로 사용할 정보는 셋팅이 있는 폴더에 같이 모아두는 것이 좋다

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


ep13

ep14

url reverse




** HTML form ** ** HTML form ** ** HTML form ** ** HTML form ** ** HTML form ** ** HTML form **
ep18
Get 방식 ->  head
Post 방식 -> head + body (여기에 담아서 보낸다) 택배에 비유

enctype 데이터 인코딩 방법
기본 : application/x-www-from-urlencoded
파일 : multipart/form-data
실제로 쓰지는 않음 : test/plain

urlencoded란?
key=value 값의 쌍이 &문자로 이어진 형태를 말한다.
공백은 +로 인코딩하며, Specia(한글 같은거) 문자들은 ascii 16진수로 변경

from urllib.parse import urlencode
print(urlencode({'key1':'value1', 'key2':10:, 'name':'공유'}))-> key1=value&이런식으로 인코딩해준다
print('공유'.encode('utf8'))
print(''.join('%{:X}'.format(ch) for in '공유'.encode('utf8')))



<form action="" method ="POST" enctype="application/x-www-form-urlencoded">
  <input type="text">
  <textarea></textarea>

</form>




 ** cross site request forgery ** ** cross site request forgery ** ** cross site request forgery ** ** cross site request forgery **
 ep19

사이트 간 요청 위조 공격

공격자 사이트의 웹페이지에 접속하면, 그 즉시 site-victim.com에 새글쓰기 요청 사용자 모르게 전달됩니다.

<body>
  <form name="arrack_form" method="post" action="http://site-victim.com/blog/post/new">
    <input type="hidden" name="title" value="스팸 제목"/>
    <input type="hidden" name="content" value="스팸 내용"/>
  <form>
</body>



csrf를 막기 위해 post 요청에 한해, csrf token 발급 및 체크

post요청에 한해 CsrfViewMiddleware를 통해 csrf token을 체크
- 체크 오류 시에는 403 forbidden 응답

Get요청에서는 csrf token이 불필요



------>   |            get 단계에서 token을 발급시켜서 post 로 보낸다 그래서 token확인
          | 뷰
<------   |

<body>
  <form name="arrack_form" method="post" action="http://site-victim.com/blog/post/new">
    {% csrf_token %} 으로 써줌
    <input type="text">
    <textarea></textarea>
  <form>
</body>

이렇게 전달해준다.



 ** 뷰함수 호출시 이자와 리턴값 (HttpRequest, HttpResponse) **** 뷰함수 호출시 이자와 리턴값 (HttpRequest, HttpResponse) **
 ep20
