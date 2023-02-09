import openai

class Chatbot:
    def __init__(self):
        openai.api_key="**-******"
        
    def get_response(self,user_input):
        responses = openai.Completion.create(
            # model="text_davinci-003",
            prompt=user_input,
            # max_tokens=3000,
            # temperature=0.5,
            model='text-davinci-003',
            # prompt='主题: 早餐 风\n两句话的恐怖故事:',
            temperature=0.8,
            max_tokens=3000,
            top_p=1.0,
            frequency_penalty=0.5,
            presence_penalty=0.0,
        ).choices[0].text
        return responses

if __name__ == "__main__":
    chatbot=Chatbot()
    response=chatbot.get_response("Write a joke about birds")
    print(response)
