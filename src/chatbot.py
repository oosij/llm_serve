import streamlit as st
import requests
import json
from transformers import AutoTokenizer
from clean_func import emoji_clean
from llm_func import chatml_addition, context_limit_count

API_URL = "LLM_API_URL"

class ChatApp:
    def __init__(self):
        self.setup_streamlit()
        self.initialize_session_state()

    def setup_streamlit(self):
        """Setup Streamlit UI components"""
        st.markdown(
            """
            <style>
            .title-style {
                font-size: 40px;
                color: #FF5733;
                font-weight: bold;
                text-align: center;
                margin-bottom: 20px;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        st.markdown('<h1 class="title-style">Hello, ThinkAI!</h1>', unsafe_allow_html=True)

    def initialize_session_state(self):
        """Initialize session state variables"""
        if 'chat_history' not in st.session_state:
            st.session_state.chat_history = []

    @property
    def system_message(self):
        """Define system message with instructions"""

        sys_msg = """<SYS>당신은 금융 투자 증권 지식에 해박한 친절한 AI, ThinkAI입니다. instruction을 기반으로 질문에 성실히 답변하세요."""
        inst_msg = """
        \n### instruction
        - 마지막 답변이 끝날때 공백이 있으면 안됩니다.
        - 한자(chinese character)를 절대로 쓰지마세요.
        - 임의의 표시가 아닌 구체적인 표시를 해야만 합니다.
        - 대화를 유도하도록 답변 끝에 연관된 질문을 하세요. 자연스럽게 하셔야 합니다. 
        - "이제까지의 대화 기록: "으로 요약한 내용이 존재한다면, 해당 대화 기록을 참고해서 이어지듯이 자연스럽게 답변하세요. 

        \n
        ## 질문: """

        return sys_msg + inst_msg

    def handle_api_response(self, response, message_placeholder):
        """Handle streaming API response"""
        full_response = ""
        try:
            for chunk in response.iter_content(chunk_size=None, decode_unicode=True):
                if chunk:
                    chunk_text = chunk.decode('utf-8') if isinstance(chunk, bytes) else chunk
                    full_response += chunk_text

                    try:
                        if full_response.strip().startswith('{'):
                            parsed_response = json.loads(full_response)
                            if isinstance(parsed_response, dict) and 'content' in parsed_response:
                                cleaned_message = parsed_response['content']
                            else:
                                cleaned_message = full_response
                        else:
                            cleaned_message = full_response

                        if cleaned_message.startswith("{'role':") and cleaned_message.endswith("}"):
                            cleaned_message = cleaned_message.split("'content': '")[1].rsplit("'}", 1)[0]

                        cleaned_message = emoji_clean(cleaned_message)
                        message_placeholder.markdown(cleaned_message)

                    except (json.JSONDecodeError, IndexError, KeyError):
                        cleaned_message = emoji_clean(full_response)
                        message_placeholder.markdown(cleaned_message)

            final_message = cleaned_message
            if final_message.startswith("{'role':") and final_message.endswith("}"):
                try:
                    final_message = final_message.split("'content': '")[1].rsplit("'}", 1)[0]
                except (IndexError, KeyError):
                    pass

            st.session_state.chat_history.append({
                "role": "assistant",
                "content": final_message
            })

        except Exception as e:
            st.error(f"Error processing response: {str(e)}")

    def display_message(self, message, is_first_message=False):
        display_content = message['content']
        if is_first_message and display_content.startswith(self.system_message):
            display_content = display_content[len(self.system_message):].strip()

        with st.chat_message(message['role']):
            st.write(display_content)

    def process_user_input(self, user_input):
        if user_input == '0':
            st.write(f'[Chat End : Your chat turn is {len(st.session_state.chat_history) // 2}]')
            return None

        if not st.session_state.chat_history:
            user_message = f"{self.system_message} {user_input}"
        else:
            user_message = user_input

        
        st.session_state.chat_history = context_limit_count(st.session_state.chat_history, self.system_message)
     

        st.session_state.chat_history.append({
            "role": "user",
            "content": user_message
        })

        messages = st.session_state.chat_history.copy()
        headers = {"Content-Type": "application/json"}
        data = {"prompt": chatml_addition(messages)}

        try:
            return requests.post(API_URL, headers=headers, json=data, stream=True)
        except requests.RequestException as e:
            st.error(f"API 요청 중 오류가 발생했습니다: {str(e)}")
            return None

    def display_chat_history(self, empty_space):
        """Display all messages in chat history"""
        with empty_space.container():
            for i, message in enumerate(st.session_state.chat_history):
                self.display_message(message, i == 0)

    def run(self):
        """Run the chat application"""
        empty_space = st.empty()
        user_input = st.chat_input("질문을 입력하세요.")

        if user_input:
            with empty_space.container():
                for i, message in enumerate(st.session_state.chat_history):
                    self.display_message(message, i == 0)

                with st.chat_message("user"):
                    st.write(user_input)

                response = self.process_user_input(user_input)
                if response:
                    with st.chat_message("assistant"):
                        message_placeholder = st.empty()
                        self.handle_api_response(response, message_placeholder)
        else:
            self.display_chat_history(empty_space)


if __name__ == "__main__":
    chat_app = ChatApp()
    chat_app.run()
