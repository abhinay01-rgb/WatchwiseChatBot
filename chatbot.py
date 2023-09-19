
from dotenv import dotenv_values
secrets = dotenv_values('hf.env')

hf_email = secrets['EMAIL']
hf_pass = secrets['PASS']

from hugchat import hugchat
from hugchat.login import Login


# Function for generating LLM response
def generate_response(prompt_input, email, passwd):
    # Hugging Face Login
    sign = Login(email, passwd)
    cookies = sign.login()
    # Create ChatBot
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    return chatbot.chat(prompt_input)

prompt = "which is the costlier watch in the world?"
response = generate_response(prompt, hf_email, hf_pass)
print(response)