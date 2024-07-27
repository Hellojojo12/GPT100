"""
无法运行！！！！！！
"""
from openai import OpenAI
from secure import *

client = OpenAI(
    base_url=GPT_3_API,
    api_key=OPENAI_API_KEY
)

COMPLETION_MODEL = "gpt-3.5-turbo"

# prompt = 'hello'


def get_response(prompt):
    completions = client.completions.create(
        model=COMPLETION_MODEL,
        prompt=prompt,
        max_tokens=512,
        n=1,
        stop=None,
        temperature=0.0,
    )
    message = completions.choices[0].text
    return message


print(get_response("prompt"))
