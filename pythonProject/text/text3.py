from openai import OpenAI
from secure import *

client = OpenAI(
    base_url=GPT_3_API,
    api_key=OPENAI_API_KEY
)

COMPLETION_MODEL = "gpt-3.5-turbo"

prompt = """
Consideration proudct : 工厂现货PVC充气青蛙夜市地摊热卖充气玩具发光蛙儿童水上玩具

1. Compose human readable product title used on Amazon in English within 20 words.
2. Write 5 selling points for the products in Amazon.
3. Evaluate a price range for this product in U.S.

Output the result in JSON format with three properties called title, selling_points and price_range.
"""

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

print(get_response(prompt))
