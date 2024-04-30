from openai import OpenAI
import os

if __name__ == '__main__':
    client = OpenAI()

    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages= [
            {'role': 'system',
             'content': """You are a nerdy and humorous but friendly and helpful assistant. 
             You are an expert python programmer."""
             },
            {'role': 'user',
             'content': 'What is the capital of France.'}
        ]
    )

    print(response.choices[0].message.content)