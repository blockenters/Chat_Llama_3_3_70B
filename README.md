# Llama 3.3 70B 챗봇

Together AI의 Llama 3.3 70B Instruct Turbo 모델을 사용한 한국어 챗봇 데모입니다.

## 기능
- Meta의 최신 Llama 3.3 70B Instruct Turbo 모델 사용 : 무료 API 호출
- 스트림릿 기반의 직관적인 웹 UI
- 대화 맥락을 고려한 응답 생성
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
   - Together AI 웹사이트(https://www.together.ai)에서 API 키를 발급받으세요
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

## 주요 특징
- Llama 3.3 70B Instruct Turbo 모델의 강력한 한국어 성능
- 대화 맥락을 이해하고 자연스러운 응답 생성
- 웹 인터페이스를 통한 손쉬운 사용

## 주의사항
- API 키는 절대 공개 저장소에 커밋하지 마세요.
- `.gitignore`에 `.streamlit/secrets.toml`이 포함되어 있는지 확인하세요.