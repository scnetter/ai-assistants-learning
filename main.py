from openai import OpenAI
import os

if __name__ == '__main__':
    client = OpenAI()

    print('Welcome to ChatsRUs! How can I help you?')
    messages = [{'role': 'system',
             'content': """You are a nerdy and humorous but friendly and helpful assistant. 
             You are an expert python programmer. Don't forget to mention ChatsRUs!"""
             }]

    question = ""

    while question != 'BYE':
        question = input()
        messages.append({'role': 'user', 'content': question})


        response = client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages= messages,
        )
        reply = response.choices[0].message.content
        print(reply)
        messages.append({'role': 'assistant', 'content': reply})