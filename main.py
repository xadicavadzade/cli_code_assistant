from openai import OpenAI
from api_config import APIConfig
from prompt import PromptBuilder


configs = APIConfig()
prompt = PromptBuilder()

client = OpenAI(
    api_key=configs.api_key,
    base_url=configs.base_url
)




print('If you want quit enter Q')
print("-" * 50)

messages = [{'role':'system','content':prompt.system_prompt}]




while True:
    user_prompt = input('Please enter your question: ')
    print("-" * 50)
    if user_prompt.upper() == 'Q':
        break
    messages.append({'role':'user','content':user_prompt})
    try:
        response = client.chat.completions.create(
            model=configs.model,
            messages=messages,
            temperature=configs.temperature,  
            max_tokens=configs.max_tokens
            )
        response = response.choices[0].message.content
        messages.append({'role': 'assistant', 'content': response})
        print(f"HERE IS YOUR ANSWER :\n {response}")
        print("-" * 50)
    except Exception as e:
        print(f"Try again, error: {e}")
        messages.pop() 


