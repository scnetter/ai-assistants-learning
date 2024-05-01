from openai import OpenAI

client = OpenAI()

# create the assistant - equivalent to 'system' role in prior chat completion exercise
assistant = client.beta.assistants.create(name='Math Tutor',
                                          instructions='You convert math problems into python code and then run the code to show the answer.',
                                          tools = [{'type': 'code_interpreter'}],
                                          model='gpt-3.5-turbo'
                                          )

# Create the thread
thread = client.beta.threads.create()

# messages.create() will also be used to add new messages to an existing thread
message = client.beta.threads.messages.create(thread_id=thread.id,
                                              role='user',
                                              content='What is 123456 * 46789')

# Take messages from user and choose an assistant to run the thread - can use specialized asst
run = client.beta.threads.runs.create(thread_id=thread.id,assistant_id=assistant.id)
# check the status of a run
print(run.status)
# retrieve the run to get the updated status until 'complete'
run = client.beta.threads.runs.retrieve(run_id=run.id, thread_id=thread.id)
print(run.status)
# thread -> Assistant RUN -> add new message to thread
# get messages from thread after complete
messages = client.beta.threads.messages.list(thread_id=thread.id)
# to get the most recent message
print(messages.data[0].content[0].text.value)
# to iterate through the messages
for message_thread in messages:
    print(message_thread.content[0].text.value)
    print("\n")

# to see the run steps:
run_steps = client.beta.threads.runs.steps.list(thread_id=thread.id, run_id=run.id)

for step in run_steps:
    print(step.step_details)
    print("\n")

# to see your assistants
assistants = client.beta.assistants.list(limit='20', order='desc')

for assistant in assistants:
    print(assistant.name)
    print("\n")

# to delete an assistant
response = client.beta.assistants.delete(assistant_id=assistant.id)
# errors usually mean assistant was already deleted or id is incorrect