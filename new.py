import openai
openai.api_key = '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'

response = openai.Completion.create(
  model='text-davinci-003',
  prompt='主题: 早餐 风\n两句话的恐怖故事:',
  temperature=0.8,
  max_tokens=120,
  top_p=1.0,
  frequency_penalty=0.5,
  presence_penalty=0.0,
)

print(response.choices[0].text)

