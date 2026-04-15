
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain how AI works in a few words",
        }
    ],
   model="openai/gpt-oss-120b",
)

print(chat_completion.choices[0].message.content)