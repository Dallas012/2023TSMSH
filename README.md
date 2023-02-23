# Data_extraction_OCR
> 건물에너지 성능 평가를 위한 AI 기반 입력 데이터 자동화 솔루션입니다. ECO-Things 벤치마킹용 건물 에너지 성능평가 프로그램인 ECO2의 입력 데이터를 자동화를 위해 우선적으로 필요한 장비일람표 내 다양한 데이터를 자동으로 추출해줍니다.     업로드된 장비일람표 PDF 파일의 데이터를 OCR을 통해 추출하고 추출한 데이터를 JSON 형태로 가공된 결과물을 보여주는 웹 어플리케이션입니다.    

## Getting Started
### Clone Repository
```
$ git clone https://github.com/dev-dsmtech/ECO-Things.git
$ cd ECO-Things
```
### How to Run
#### 1. Installation:
python 버전:  3.9.13
```
$ pip install -r requirements.txt
```
#### 2. PDF 폴더 만들기
media 폴더 내 업로드된 PDF 파일 저장을 위한 PDF 폴더를 만든다

#### 3. Run server
```
python manage.py runserver
```

## 파일 구조
```
.
├── config/
|   ├── asgi.py
|   ├── settings.py
|   ├── urls.py
|   └── wsgi.py
├── Core/
|   ├── migrations
|   |   └── ...
|   ├── admin.py
|   ├── apps.py
|   ├── convert.py
|   ├── models.py
|   ├── tests.py
|   └── views.py
├── media/
|   ├── JSON
|   ├── PDF
|   └── Result
├── templates/Core/
|   ├── main.html
|   └── upload-file.html
├── .gitignore
├── manage.py
├── README.md
└── requirements.txt
```
- convert.py : Nanonets OCR 모델로 데이터 추출 -> 추출된 데이터 가공 후 저장
- media/JSON/ : OCR 모델로 추출된 결과물 저장
- media/PDF/ : 업로된 원본 장비일람표 저장
- media/Result/ : OCR 모델로 추출된 데이터 가공한 결과물 저장
- upload-file.html : 파일 업로드 및 업로드 후 결과물을 보여주기 위한 파일
----------------------------------------------------------
# API 설명
- **Nanonets API** : 장비일람표 내 테이블 구조와 텍스트 감지 및 인식
    
## Nanonets API 정리
- 용도 : 장비일람표에서 정보추출을 진행할때 Nanonets의 OCR 모델을 통해 추출된 정보를 가져온다
- 구조 : 감지된 테이블의 좌표 값이 먼저 나오고 해당 테이블 내의 텍스트 데이터와 그 좌표값이 하나씩 나온다
```
*Request 데이터 예시*

{
"message": "Success",
"result":[
	{
	  "message":"Success",
	  "input":"수정장비일람표1.pdf",
	  "prediction": [
		  {
			  "id": "9ee97d25-5203-4f8d-8073-f51d4df53308",
			  "label": "table",
			  "xmin":  196,
			  "ymin":  426,
			  "xmax":  3920,
			  "ymax":  692,
			  "score":  1,
			  "ocr_text":  "table",
			  "type":  "table",
			  "cells": [
				  {
					  "id":  "eab896df-1834-4c09-992c-1aa4bba61de6",
					  "row":  1,
					  "col":  1,
					  "row_span":  1,
					  "col_span":  1,
					  "label":  "",
					  "xmin":  196,
					  "ymin":  427,
					  "xmax":  378,
					  "ymax":  483,
					  "score":  0.8991148,
					  "text":  "기호",
					  "row_label":  "",
					  "verification_status":  "correctly_predicted",
					  "status":  "",
					  "failed_validation":  "",
					  "label_id":  ""
				   }
			 ]
		}
	]
}]}
```
---
# API Call 
url = http:// # 배포한 IP주소를 적으면 됨

#### Response 예시
```
{
    "page: 0": [
	    {
		    "table: 0": [
			    {
				    "PhxVxHz":  "1x220x60",
				    "kcal / hr":  "15,996",
				    "kg / hr":  "1.50",
				    "mm":  "435",
				    "가스 ( A )":  "15",
				    "기호":  "B 2",
				    "깊이 ( mm )":  "305",
				    "난방 환수 및 출구 ( A )":  "20",
				    "명칭":  "기숙사 난방 및 급탕 보일러",
				    "비고":  "",
				    "사용 ( kg / ) ( 난방 )":  "1.0",
				    "설치 장소":  "각 기숙사 보일러 실",
				    "소비 ( 난방 )":  "130",
				    "소비량 ( 온수 ) ( kcal / hr )":  "17,974",
				    "수량 ( 대 )":  "89",
				    "압력 ( cm2 ) ( 온수 )":  "0.8 ~ 3.5",
				    "외형 치수 ( mm )":  "660",
				    "용량 ( 선정 용량 ) ( kcal / hr )":  "15,000",
				    "전력 ( 밥 ) ( 온수 )":  "130",
				    "접속 구경 ( 급수 및 온수 ) ( A )":  "15",
				    "최대 가스 ( 난방 ) ( kg / hr )":  "1.33",
				    "형 식":  "콘덴싱"
				 }
			]
	]}
}
```

