# ICO 변환기

이 프로그램은 일반적인 이미지 파일(.png, .jpg, .jpeg)을 ICO 파일로 변환하는 간단한 GUI 애플리케이션입니다.

## 주요 기능

- 다중 파일 선택 및 변환 지원
- 사용자 친화적인 인터페이스

## 최근 업데이트 (2024-09-08)

1. 사용자 인터페이스 개선
   - 버튼 디자인 및 색상 변경
   - 윈도우 크기 조정
   - 폰트 통일 및 크기 조정

2. 기능 개선
   - 파일 선택 전 '변환' 버튼 비활성화
   - 변환 완료 후 결과 메시지 표시

3. 코드 최적화
   - `enumerate()` 사용으로 파일 처리 개선
   - 파일 이름 생성 로직 개선

4. 오류 처리 강화
   - 파일 미선택 시 오류 메시지 표시

5. 코드 구조 개선
   - tkinter 애플리케이션을 클래스 기반으로 리팩토링
   - main 함수 추가로 프로그램 실행 구조 개선
   - 객체 지향 프로그래밍 원칙 적용으로 유지보수성 향상

## 사용 방법

1. "파일 선택" 버튼을 클릭하여 변환할 이미지 파일을 선택합니다.
2. "변환" 버튼을 클릭하여 선택한 파일을 ICO 형식으로 변환합니다.
3. 변환된 파일은 프로그램과 같은 디렉토리에 저장됩니다.

## 요구 사항

- Python 3.x
- Pillow 라이브러리
- tkinter (대부분의 Python 설치에 기본 포함)

## 설치 및 실행

1. 저장소를 클론합니다:
   ```
   git clone https://github.com/your-username/ico-converter.git
   ```
2. 필요한 라이브러리를 설치합니다:
   ```
   pip install Pillow
   ```
3. 프로그램을 실행합니다:
   ```
   python icoConverter.py
   ```

## 기여

버그 리포트, 기능 제안 또는 풀 리퀘스트는 언제나 환영합니다!