# Cartoon Rendering Homework 2

## 설명
OpenCV를 사용해 이미지를 만화 스타일로 변환:
1. 이미지 크기 조정 (너비 800px).
2. 그레이스케일로 변환.
3. 미디언 블러로 노이즈 감소.
4. 적응형 임계값으로 가장자리 감지.
5. 양방향 필터로 색상 부드럽게.
6. 색상과 가장자리 결합.

6단계를 창으로 표시.

## 데모
- 원본 이미지: `1.jpg`
- 결과 이미지: `cartoon_output.jpg`

## 한계
- 작은 디테일 손실.
- 대비 낮으면 가장자리 거칠음.
- 양방향 필터로 색상 흐려짐.

## 실행 방법
1. OpenCV 설치: `pip install opencv-python`
2. `1.jpg`를 코드와 같은 폴더에 배치.
3. 실행: `python cartoon.py`
4. 결과는 `cartoon_output.jpg`로 저장.