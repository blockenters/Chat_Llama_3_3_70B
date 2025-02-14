# Llama 3.3 70B 챗봇

Together AI의 Llama 3.3 70B API를 사용한 한국어 챗봇 데모입니다.

## 기능
- Llama 3.3 70B 모델을 사용한 대화형 인터페이스
- 스트림릿 기반의 직관적인 웹 UI
- 대화 기록 유지
- 예시 질문 버튼 제공

## 설치 방법

1. 저장소 클론
   ```bash
   git clone https://github.com/yourusername/llama-chatbot.git
   cd llama-chatbot
   ```

2. 필요한 패키지 설치
   ```bash
   pip install -r requirements.txt
   ```

3. Together AI API 키 설정
   - Together AI 웹사이트에서 API 키를 발급받으세요
   - `.streamlit/secrets.toml` 파일을 생성하고 다음 내용을 추가하세요:
   ```toml
   TOGETHER_API_KEY = "your-api-key-here"
   ```

## 실행 방법
```bash
streamlit run app.py
```


## 환경 설정
- Python 3.10 이상
- 필요한 주요 패키지:
  - streamlit
  - together


## 주의사항
- API 사용량에 따라 Together AI 측의 과금이 발생할 수 있습니다.
- API 키는 절대 공개 저장소에 커밋하지 마세요.