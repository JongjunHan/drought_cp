# drought-cp
<p align="justify">
</p>

배포 주소 : https://drought-info.herokuapp.com <br/>
모델링 과정 : https://github.com/JongjunHan/drought_ds

## 프로젝트 목표
<p align="justify">
</p>

- 현재 이상기후 및 여타 자연재해들로 우리나라 역시 가뭄에 대해 안전한 지역이 아니게 됨

- 그에 따라 가장 가뭄의 여파가 심할 것이라 예상이 되는 곡창지대의 중심지이자 강원도 지역에 비해 비교적 최근부터 가뭄피해를 호소하기 시작한 호남지역을 대상으로 예측 여부 모델과 서비스를 개발하게 됨

- ASOS(종관기상관측)자료와 SPI(표준강수지수)를 통한 가뭄 예측을 하기위한 모델을 제작

- 그에 따라 미래 시점의 가뭄에 대한 예측을 진행하고 그에 대한 피해를 최소화하기 위해 예방 및 치료 방안에 대한 제시, 관련 뉴스를 소개하며 경각심을 올리기 위함

## 디렉토리 구조
<p align="justify">
</p>

<img width="340" alt="image" src="https://user-images.githubusercontent.com/102279444/190044879-ad35c650-88ec-4fc0-908e-39fb99516dbd.png">

## 웹페이지
<p align="justify">
</p>

1. main

<img width="1512" alt="스크린샷 2022-09-14 오전 10 16 09" src="https://user-images.githubusercontent.com/102279444/190045963-0d9be092-74b1-4a29-b52f-3bfbb5031bf9.png">

- 프로젝트 진행 과정에 있어서 팀 소개와 6하원칙 기반의 소개 화면

2. model

<img width="1512" alt="스크린샷 2022-09-14 오전 10 00 39" src="https://user-images.githubusercontent.com/102279444/190045991-748ef108-8b40-4065-9cab-de25f38d2038.png">

- 구현한 모델을 통한 가뭄 여부 예측 서비스를 구현함

- 추가적으로 선택을 하면 가뭄 여부와 그에 따라 가뭄을 예방하거나 치료하기 위한 부가 서비스를 소개함

3. dashboard

<img width="1512" alt="스크린샷 2022-09-14 오전 10 16 16" src="https://user-images.githubusercontent.com/102279444/190046005-3c5e339e-8d13-4d90-aad3-e95c2ad7d129.png">

- 가뭄과 관련된 내용에 대한 정보를 알려주기 위한 대시보드

- 이를 통해 가뭄과 관련된 과거 정보를 알 수 있으며, 가뭄에 대한 지수인 SPI에 대한 소개와 정보를 얻을 수 있음

4. news

<img width="1512" alt="스크린샷 2022-09-14 오전 10 16 20" src="https://user-images.githubusercontent.com/102279444/190045997-b61b56ff-945c-482e-a570-313d45b3dfa1.png">

- 가뭄과 관련된 뉴스를 소개하는 채널

## 모델 과정
<p align="justify">
</p>

- input Data > 종관관측(ASOS) API > Modeling > Output 의 순으로 진행이 됨
