import requests
import json
from transformers import AutoTokenizer

TOKEN_PATH = "./token_file/models--CohereForAI--aya-expanse-32b/snapshots/c1df2547e1f5fe22e1f4897f980f231dc74cfc27"

tokenizer = AutoTokenizer.from_pretrained(TOKEN_PATH, local_files_only=True)

def inference_llm_steam(prompt, stream_onoff):
"""
This is a simple LLM API call here, using various models like the token file above.
Later in FRAG, phi-4 is used instead of the token file above.
"""
    return response


def chatml_addition(user_msg):
    chatml = tokenizer.apply_chat_template(user_msg, tokenize=False, add_generation_prompt=True)
    return chatml


def context_limit_count(chatml, inst_msg):
    if chatml: 
        text = chatml_addition(chatml)
        tokens = tokenizer.encode(text, add_special_tokens=True)
        token_count = len(tokens)

        if token_count >= 14000 

            summary_template = """
이제까지의 내용은 당신과 나의 대화 내용입니다. 
이것을 간략하게 요약하세요.

## 이전 대화 기록:
{log}

## 요약:
"""
            sys_msg = summary_template.format(log = chatml)
            chat_add = [
                {"role": "user", "content": sys_msg}
            ]
            chatml_add = tokenizer.apply_chat_template(chat_add, tokenize=False, add_generation_prompt=True)

            pre_summary = inference_stream_off(chatml_add)
            print(chatml[-1]['content'])
            last_answer = chatml[-1]['content']
            ladst_add_msg = "# 이제까지의 대화 기록 : \n"+  pre_summary +" \n내 질문으로 마지막에 한 답변 :" + last_answer
            print()
            print(ladst_add_msg)
            chat_pre_summary = [
                {"role":"user", "content": inst_msg },
                {"role": "assistant", "content": ladst_add_msg }
            ]
            chatml = chat_pre_summary  

        print("토큰 수:", token_count)
    else:

        print("chatml이 비어 있습니다.")  

    return chatml


