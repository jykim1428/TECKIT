사용자가 브라우저에 입력을 하면 서버에 요청이 가게 되고 서버에서 다시 브라우저에 응답을 보내게 된다
클라이언트와 서버는 역할이며
요청을 보내면 클라이언트
요청을 "응답"하면 서버의 역할을 한다고 말함

프레임 워크: 소프트웨어 개발을 위한 기능, 구조의 틀을 제공
             시스템 흐름을 프레임워크가 제어

라이브러리:  소프트 웨어 개발을 위한 기능을 제공  
             시스템 흐름을 개발자가 제어

orm, templates, admin

#first-django라는 파일 만들기
mkdir first-django

#first-django라는 파일 현재 위치로 이동
cd first-django

#현재 패키지들이 설치된 버전 확인
pip list


python -v


pip install --upgrade pip

#가상환경 생성
python -m venv venv

#현재 디렉토리 확인
dir

#가상 환경 진입
.\venv\Scripts\activate

#장고 설치
pip install django 

#장고 프로젝트와 앱을 생성하는 명형어
django-admin startproject config .

#서버 실행
python manage.py runserver

#서버 종료
ctrl+c

#demos라는 앱을 생성
django-admin startapp demos
->이후 settings.py에서 istalled_app부분에 'demos', 추가(콤마 빼먹지 말기!)
->views.py에서 기능 구현


