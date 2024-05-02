from openai import OpenAI
import time

client = OpenAI()

#STEP 1 - Create the assistant
assistant = client.beta.assistants.create(name="Mortgage Bot",
                                          instructions='You use Python code to help answer questions about mortgage and interest payments.',
                                          tools= [{'type': 'code_interpreter'}],
                                          model='gpt-3.5-turbo'
                                          )

#STEP 2 - Create the Thread
thread = client.beta.threads.create()

#STEP 3 - Add a message to the thread
message = client.beta.threads.messages.create(thread_id=thread.id,
                                              role='user',
                                              content='I want to buy a house that costs $155000 on a 30 year fixed loan at 7.8% interest. What will my monthly payments be?'
                                              )
# Step 4 - Run the thread with assistant

run = client.beta.threads.runs.create(thread_id=thread.id,
                                      assistant_id=assistant.id,
                                      instructions='Give a detailed analysis and considerations regarding the mortgage payment.')

while run.status != 'completed':
    run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
    print(run.status)
    time.sleep(5)

print(run.status)

