
# import os
# import dotenv

# from openai import OpenAI

# client = OpenAI(api_key="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", base_url="https://api.deepseek.com")

# deepseek = "sk-bea9babbadd043cbbad7a32139a3cfbc"
# openAi = "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"

# completion = client.chat.completions.create(

#     model="gpt-3.5-turbo",
#      messages=[
#         {"role": "system", "content": "You are a helpful assistant"},
#         {"role": "user", "content": "Hello"},
#     ],
#     stream=False
# )

# response = completion.choices[0].message.content

# print(response)

