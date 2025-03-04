"""
问答机器人，不能使用
"""

from openai import OpenAI
from secure import *

client = OpenAI(
    base_url="https://api.gpts.vin/v1",
    api_key=OPENAI_API_KEY
)


def ask_gpt3(prompt):
    response = client.completions.create(
        # model="text-davinci-003",
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=512,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].text.strip()
    return message


print("你好，我是一个聊天机器人，请你提出你的问题吧?")

questions = []
answers = []


def generate_prompt(prompt, questions, answers):
    num = len(answers)
    for i in range(num):
        prompt += "\n Q : " + questions[i]
        prompt += "\n A : " + answers[i]
    prompt += "\n Q : " + questions[num] + "\n A : "
    return prompt


while True:
    user_input = input("> ")
    questions.append(user_input)
    if user_input.lower() in ["bye", "goodbye", "exit"]:
        print("Goodbye!")
        break
    prompt = generate_prompt("", questions, answers)
    answer = ask_gpt3(prompt)
    print(answer)
    answers.append(answer)
