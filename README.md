# python-crawling-program

### 파이썬 asyncio / requests / selenium 라이브러리 이용하여 사이트 크롤링 프로그램을 구현
#### 업무 중 날짜값을 매개변수의 값으로 받는 사이트 크롤링이 필요하여 설계한 로직입니다.

* 사이트 url 입력하면 사이트의 body 태그의 텍스트와 status 를 크롤링하여 csv 파일로 저장 가능

\
**1. 파일 다운로드**

\
**2. 파일 경로**

2-1. 실행 프로그램  
![image](https://user-images.githubusercontent.com/82769484/223893153-774d3057-53ce-4ece-9a7b-dfaaff697aef.png)  

압축 풀고 dist 폴더 들어가면 실행프로그램 있으니, 원하시는 경로에 놓고 자유롭게 사용 가능합니다.  
다만, 크롤링 결과 csv는 실행프로그램과 동일한 디렉터리에 저장되니 참고 바랍니다.

\
**3. 프로그램 실행**  
![image](https://user-images.githubusercontent.com/82769484/223894191-5db417ca-1947-4c49-bd72-42adebdb281f.png)  

실행프로그램의 초기 화면입니다.
여기서 크롤링할 라이브러리를 선택할 수 있습니다.

\
3-1. asyncio  
![image](https://user-images.githubusercontent.com/82769484/223894342-0b4e5303-69cb-4b2d-9e29-87f2b267e788.png)  

순서대로 input 합니다.
- url은 파라미터 값 이전 = 까지 모두 입력해야 합니다.
- 날짜 형식은 인풋 후 자동으로 'YYYY-MM-DD' 형식으로 변환되니, '20230101' 형식으로 입력합니다.

\
![image](https://user-images.githubusercontent.com/82769484/223894485-ab3b3a52-d2c3-4b4e-97b7-6a51f550bb34.png)  
![image](https://user-images.githubusercontent.com/82769484/223894500-2c6d2c04-7d70-44ee-bd84-dfbf7d1ee1dc.png)  

인풋값은 필터링을 거칩니다. 올바른 값을 입력할 때까지 계속 while문이 돌아갑니다.  

\
> 2023-01-01 ~ 2023-12-31 실행결과  
![image](https://user-images.githubusercontent.com/82769484/223894629-d37abe43-dd82-48af-82db-b9044a41aeba.png)  
![image](https://user-images.githubusercontent.com/82769484/223894658-4ad79875-f17e-4792-80a8-9ece169c3065.png)  

csv 파일의 이름도 자유롭게 입력할 수 있습니다.  

실행프로그램이 있는 디렉터리 안에 ver1.csv 파일이 생성되었습니다.  
elapsed time 값으로 크롤링하는 데 소요된 시간을 확인할 수 있습니다.  

asyncio 라이브러리로 비동기 처리해서 다른 크롤링 버전들보다 1/100 이상 소요시간이 확 줄어들었습니다.  

\
3-2. requests  
![image](https://user-images.githubusercontent.com/82769484/223894784-865c8f52-54a0-488c-9bb2-547880089d6c.png)  

로직은 동일합니다.  
ver2.csv 파일이 생성됩니다.  

\
3-3. selenium  
![image](https://user-images.githubusercontent.com/82769484/223894903-ddeb6967-402a-4347-a1f8-c694fac9fe27.png)  

로직은 동일합니다.  
ver3.csv 파일이 생성됩니다.  

\
4. 프로그램 종료  
![image](https://user-images.githubusercontent.com/82769484/223895017-aaf121d8-77e6-422f-beb8-f1997ad8570e.png)  

프로그램을 종료하고 싶을 땐 3을 입력하고, 아무 키나 누르면 실행프로그램이 종료됩니다.  
