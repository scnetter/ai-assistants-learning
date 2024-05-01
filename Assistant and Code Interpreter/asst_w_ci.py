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
