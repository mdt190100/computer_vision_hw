OpenCV를 사용한 비디오 레코더

1 )소개
이 프로그램은 **OpenCV**를 사용하여 웹캠에서 비디오를 녹화하는 Python 프로그램입니다. 사용자는 다음 기능을 이용할 수 있습니다:
- **미리보기 모드 (Preview Mode)**
- **녹화 모드 (Record Mode)**
- **블러 효과 On/Off (Blur Effect)**
- **비디오를 `output.avi` 파일로 저장**

2 )설치
(1)필요 소프트웨어
- Python 3
- OpenCV (`cv2`)

(2)필수 라이브러리 설치
터미널 또는 명령 프롬프트에서 다음 명령어 실행:
```bash
pip install opencv-python numpy
```

(3)사용법
다음 명령어로 프로그램 실행:
```bash
python video_recorder.py
```
(4)키보드 단축키:
| 키 | 기능 |
|------|----------|
| `ESC` | 프로그램 종료 |
| `SPACE` | 녹화 시작/정지 |
| `B` | 블러 효과 On/Off |

3 )비디오 저장
- 녹화 중일 때 비디오는 `output.avi` 파일로 저장됩니다.
- `XVID` 코덱을 사용하며 해상도 **640x480**, **FPS = 30**입니다.
