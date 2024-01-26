from interpreter import interpreter

interpreter.offline = True # Disables online features like Open Procedures
interpreter.vision = True
interpreter.llm.model = "openai/x" # Tells OI to send messages in OpenAI's format
interpreter.llm.api_key = "fake_key" # LiteLLM, which we use to talk to LM Studio, requires this
interpreter.llm.api_base = "http://localhost:1234/v1" # Point this at any OpenAI compatible server
interpreter.auto_run = True
interpreter.llm.max_tokens = 200
interpreter.llm.max_output = 1000
interpreter.llm.llm_supports_vision = True
interpreter.force_task_completion = True
interpreter.safe_mode = 'off'
interpreter.computer.emit_images = True

interpreter.chat()


#interpreter --os

'''from interpreter import interpreter

interpreter.offline = True # Disables online features like Open Procedures
interpreter.llm.model = "ollama_chat/mistral"
interpreter.llm.api_base = "http://localhost:11434"

interpreter.chat()'''



'''#interpreter.messages = [] use this to clrear meesgae history
#In your terminal, Open Interpreter will save previous conversations to <your application directory>/Open Interpreter/conversations/.
#interpreter --conversations (used to sleect chat)

"""%verbose [true/false]: Toggle verbose mode
%reset: Reset the current session
%undo: Remove the last message and its response
%save_message [path]: Save messages to a JSON file
%load_message [path]: Load messages from a JSON file"""


"""
To create multiple instances, use the base class, OpenInterpreter:
from interpreter import OpenInterpreter

agent_1 = OpenInterpreter()
agent_1.system_message = "This is a seperate instance."

agent_2 = OpenInterpreter()
agent_2.system_message = "This is yet another instance."
"""

"""For fun, you could make these instances talk to eachother:


def swap_roles(messages):
    for message in messages:
        if message['role'] == 'user':
            message['role'] = 'assistant'
        elif message['role'] == 'assistant':
            message['role'] = 'user'
    return messages

agents = [agent_1, agent_2]

# Kick off the conversation
messages = [{"role": "user", "message": "Hello!"}]

while True:
    for agent in agents:
        messages = agent.chat(messages)
        messages = swap_roles(messages)"""

"""OS Mode
OS mode is a highly experimental mode that allows Open Interpreter to control the operating system visually through the mouse and keyboard. It provides a multimodal LLM like GPT-4V with the necessary tools to capture screenshots of the display and interact with on-screen elements such as text and icons. It will try to use the most direct method to achieve the goal, like using spotlight on Mac to open applications, and using query parameters in the URL to open websites with additional information.

OS mode is a work in progress, if you have any suggestions or experience issues, please reach out on our Discord.

To enable OS Mode, run the interpreter with the --os flag:


interpreter --os"""

"""Offline
Running the computer in offline mode will disable some online features, like the hosted Computer API. Inherits from interpreter.offline.


Python

Profile

interpreter.computer.offline = True
​
Verbose
This is primarily used for debugging interpreter.computer. Inherits from interpreter.verbose.


Python

Profile

interpreter.computer.verbose = True
​
Emit Images
The emit_images attribute in interpreter.computer controls whether the computer should emit images or not. This is inherited from interpreter.llm.supports_vision.

This is used for multimodel vs. text only models. Running computer.display.view() will return an actual screenshot for multimodal models if emit_images is True. If it’s False, computer.display.view() will return all the text on the screen.

Many other functions of the computer can produce image/text outputs, and this parameter controls that.


Python

Profile

interpreter.computer.emit_images = True
'''