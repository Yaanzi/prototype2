from openai import OpenAI

client = OpenAI(
    api_key= "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"
)

prompt = "how to read lab test result?"

chat_completion = client.chat.completions.create(
    messages = [
        {
            "role":"user",
         "content":prompt
         },    
    ],
    model="gpt-3.5-turbo"
)

print(chat_completion.choices[0].message.content)