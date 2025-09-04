프로젝트명: 서울시 사고유형 분석  
실행 파일: ProjectMain (응용 프로그램)  
실행 코드: Taap.py  

이 프로젝트는 Python의 tkinter GUI 라이브러리를 기반으로 하여, 서울시의 교통사고 데이터를 시각적으로 분석하고 이미지로 저장할 수 있는 응용 프로그램입니다.

주요 파일 설명  
- Taap.py: StartMenu를 호출하여 GUI 창을 구성하는 메인 실행 파일  
- allmenu.py: graph.py, image.py, saveimg.py를 불러와 모든 작업을 처리하는 핵심 파일  
- graph.py: 사고 데이터를 시각화하는 그래프 관련 클래스 및 함수 정의  
- image.py: 분석 결과를 이미지로 출력하는 기능을 담당  
- saveimg.py: 생성된 이미지를 저장하는 방식 정의

전체 흐름 요약  
- 사용자가 ProjectMain을 실행하면 Taap.py가 작동하여 GUI 창이 생성됩니다.  
- Taap.py는 allmenu.py의 StartMenu를 호출하여 초기 화면을 구성합니다.  
- allmenu.py는 사용자 입력에 따라 graph.py, image.py, saveimg.py의 기능을 호출하여 그래프를 생성하고 이미지를 출력 및 저장합니다.  
- 모든 작업은 GUI를 통해 직관적으로 이루어지며, 분석 결과를 시각적으로 확인할 수 있습니다.
