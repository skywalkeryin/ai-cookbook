import os

from openai import OpenAI

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)


completion = client.chat.completions.create(
    model="deepseek/deepseek-v3-base:free",
    messages=[
        {"role": "system", "content": "You're a helpful assistant."},
        {
            "role": "user",
            "content": "Write a limerick about the Python programming language.",
        },
    ],
)

response = completion.choices[0].message.content
print(response)
