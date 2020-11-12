# DjangoApt

* djangoapt/settings.py
  * SECRET_KEY 입력
* pages/settings.py
  * API_SERVICE_KEY : https://www.data.go.kr/ 에서 국토교통부_아파트매매 실거래자료와 국도교통부_아파트 전월세 자료 활용 신청해서 나온 Key 입력
  * MY_GU_CODE에 법정동 코드
  * MY_DONGS에 원하는 동 입력
* python manage.py migrate

![Alt text](doc/DjangoAptImport.png?raw=true "Import")
![Alt text](doc/DjangoAptList.png?raw=true "List")