

import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def generate_answer(
        context,
        question
):

    prompt = f"""
    You are a helpful document assistant.

Answer ONLY from the provided context.

If the answer is not present in the context, say:

"I could not find that information in the document."

    Context:
    {context}

    Question:
    {question}
    """

    response = client.chat.completions.create(
        model="deepseek/deepseek-chat-v3-0324",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content