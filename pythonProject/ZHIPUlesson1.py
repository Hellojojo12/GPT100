from secure import *

from zhipuai import ZhipuAI


client = ZhipuAI(api_key=ZHIPUAI_API_KEY)
MODEL = 'glm-4'
messages = [
        {"role": "user", "content": "你好！你叫什么名字"},
    ]

response = client.chat.completions.create(
  model=MODEL,
    messages=messages,
    stream=True,
    )
for chunk in response:
    print(chunk.choices[0].delta)