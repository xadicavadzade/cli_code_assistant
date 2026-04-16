from openai import OpenAI
from api_config import ApiConfig
from prompt import Prompt


configs = ApiConfig()
prompt = Prompt()

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
            temperature=configs.temprature,  
            max_tokens=configs.max_tokes
            )
        response = response.choices[0].message.content
        messages.append({'role': 'assistant', 'content': response})
        print(f"HERE IS YOUR ANSWER :\n {response}")
        print("-" * 50)
    except Exception as e:
        print(f"Try again, error: {e}")
        messages.pop() 


