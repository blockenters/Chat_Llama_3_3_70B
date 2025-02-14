import streamlit as st
from together import Together

# Together AI 클라이언트 초기화
client = Together(api_key=st.secrets["TOGETHER_API_KEY"])

# 페이지 기본 설정
st.set_page_config(
    page_title="Llama 3.3 70B Chatbot",
    page_icon="🦙",
    layout="wide"
)

# 제목과 설명 추가
st.title("Llama 3.3 70B Chatbot")
st.markdown("Together AI의 Llama 3.3 70B 모델을 사용한 대화 테스트용 데모입니다.")

# 챗봇 응답 생성 함수
def generate_response(messages):
    try:
        response = client.chat.completions.create(
            model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
            messages=messages,
            temperature=0.7,
            top_p=0.7,
            top_k=50,
            repetition_penalty=1,
            stop=["<|eot_id|>", "<|eom_id|>"]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"죄송합니다, 응답 생성 중 문제가 발생했습니다: {str(e)}"

# 세션 상태 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []

# 예시 메시지 버튼들
example_messages = ["안녕하세요!", "너는 누구니?", "무엇을 할 수 있니?"]
cols = st.columns(len(example_messages))
for col, example in zip(cols, example_messages):
    if col.button(example):
        st.session_state.messages.append({"role": "user", "content": example})
        with st.spinner("생각 중..."):
            chat_messages = [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
            response = generate_response(chat_messages)
            st.session_state.messages.append({"role": "assistant", "content": response})

# 이전 대화 내용 표시
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 사용자 입력 처리
if prompt := st.chat_input("메시지를 입력하세요..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("생각 중..."):
            chat_messages = [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
            response = generate_response(chat_messages)
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response}) 