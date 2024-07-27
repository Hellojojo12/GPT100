import openai
from secure import OPENAI_API_KEY

# 设置API密钥
openai.api_key = OPENAI_API_KEY

COMPLETION_MODEL = "gpt-3.5-turbo"

prompt = 'hello'

def get_response(prompt):
    completions = openai.Completion.create(
        model=COMPLETION_MODEL,
        prompt=prompt,
        max_tokens=512,
        n=1,
        stop=None,
        temperature=0.0,
    )
    message = completions.choices[0].text.strip()
    return message

print(get_response(prompt))
