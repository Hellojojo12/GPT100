from openai import OpenAI
from secure import *

# client = OpenAI(
#     base_url="https://api.gpts.vin/v1",
#     api_key='sk-Nqn4bgVjHfbJZgxx02Bc232fB9Cf4904B419D8D4B3999aA7'
# )


client = OpenAI(
    base_url=GPT_3_API,
    api_key=OPENAI_API_KEY
)

def get_response():
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "你是一个语文老师"},
            {"role": "user", "content": "怎么写日记"}
        ]
    )
    message = completion.choices[0].message.content
    return message


print(get_response())
