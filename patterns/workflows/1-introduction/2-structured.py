import os

from openai import OpenAI
from pydantic import BaseModel

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)


# --------------------------------------------------------------
# Step 1: Define the response format in a Pydantic model
# --------------------------------------------------------------


class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]


# --------------------------------------------------------------
# Step 2: Call the model
# --------------------------------------------------------------

# completion = client.chat.completions.create(
#     model="deepseek/deepseek-v3-base:free",
#     messages=[
#         {"role": "system", "content": "Extract the event information."},
#         {
#             "role": "user",
#             "content": "Alice and Bob are going to a science fair on Friday.",
#         },
#     ],
#     # response_format=CalendarEvent,
# )

completion = client.chat.completions.create(
    model="deepseek/deepseek-v3-base:free",
    messages=[
        {"role": "system", "content": "Extract the event information."},
        {
            "role": "user",
            "content": "Alice and Bob are going to a science fair on Friday.",
        },
    ],
)


# --------------------------------------------------------------
# Step 3: Parse the response
# --------------------------------------------------------------
print(completion.choices[0].message.content)
# event = completion.choices[0].message.parsed
# event.name
# event.date
# event.participants