from openai import OpenAI
import time

client = OpenAI()

def wait_on_run(run, thread):
    while run.status == 'queued' or run.status == 'in_progress':
        run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
        time.sleep(1)
        print(run.status)
    return run


def display_thread_messages(messages):
    for thread_message in messages.data:
        print(thread_message.content[0].text.value)
        print("\n")


# STEP 1 - Create the assistant
assistant = client.beta.assistants.create(name="Mortgage Bot",
                                          instructions='You use Python code to help answer questions about mortgage and interest payments.',
                                          tools= [{'type': 'code_interpreter'}],
                                          model='gpt-3.5-turbo'
                                          )

# STEP 2 - Create the Thread - contains the messages objects. The thread is the memory.
thread = client.beta.threads.create()

# STEP 3 - Add a message to the thread
message = client.beta.threads.messages.create(thread_id=thread.id,
                                              role='user',
                                              content='I want to buy a house that costs $155000 on a 30 year fixed loan at 7.8% interest. What will my monthly payments be?'
                                              )
# Step 4 - Run the thread with assistant - run can invoke the tools like code interpreter

run = client.beta.threads.runs.create(thread_id=thread.id,
                                      assistant_id=assistant.id,
                                      instructions='Give a detailed analysis and considerations regarding the mortgage payment.')

wait_on_run(run, thread)

# STEP 5 - Display the message
messages = client.beta.threads.messages.list(thread_id=thread.id,
                                             order='asc',
                                             after=message.id,)


display_thread_messages(messages)

message = client.beta.threads.messages.create(thread_id=thread.id,
                                              role='user',
                                              content='What if I put a down payment of $50k on the house? How would that affect my monthly payment?')

run = client.beta.threads.runs.create(thread_id=thread.id,assistant_id=assistant.id)

wait_on_run(run, thread)

messages = client.beta.threads.messages.list(thread_id=thread.id,
                                             order='asc',
                                             after=message.id,)
display_thread_messages(messages)