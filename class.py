import openai
from pydantic import BaseModel

openai.organization = 'org-IgV1huByEyX3v19MeqJLgEM1'
openai.api_key = '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'


class Document(BaseModell):
prompt: str = ''

def inference(prompt: str) -> list:
completion = openai.ChatCompletion.create(
model="gpt-3.5-turbo",
messages=[
{"role": "system",
"content": "estudiante de la carrera de desarrollo de software"},
{"role": "user", "content": prompt}
]
)
content = completion.choices[0].message.content
total_tokens = completion.usage.total_tokens
return [content, total_tokens]