import telebot
import random
import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
device = torch.cuda.get_device_name()

model_name_or_path = r"C:\Users\crisc\Desktop\NeuroGPT\text-generation-webui-main\models\TheBloke_Llama-2-7B-Chat-GPTQ"
# To use a different branch, change revision
# For example: revision="gptq-4bit-64g-actorder_True"
model = AutoModelForCausalLM.from_pretrained(model_name_or_path,
                                             device_map="auto",
                                             trust_remote_code=False,
                                             revision="main")

tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, use_fast=True)




# Inference can also be done using transformers' pipeline

# print("*** Pipeline:")
# pipe = pipeline(
#     "text-generation",
#     model=model,
#     tokenizer=tokenizer,
#     max_new_tokens=512,
#     do_sample=True,
#     temperature=0.7,
#     top_p=0.95,
#     top_k=40,
#     repetition_penalty=1.1
# )
#
# print(pipe(prompt_template)[0]['generated_text'])





# Initialize the Telegram bot
bot = telebot.TeleBot('5538738432:AAEswTLFBcLHZU8V-2XxAE0xbk-hQKW20DU')



def generate_random_interesting_start(topic):
    starts = {
        'self-improvement': [
            'Neurobiologically, ',
            'From a psychological standpoint, ',
            'According to research, ',
            'Studies have shown that ',
            'In order to improve your self-improvement journey, ',
        ],
        'self-help': [
            'To overcome challenges and achieve your goals, ',
            'For personal growth and emotional well-being, ',
            'Seeking support and guidance from others can be beneficial, ',
            'Developing healthy habits and routines is essential for self-help, ',
            'Remember, self-help is a journey, not a destination, ',
        ],
        'science': [
            'Scientifically speaking, ',
            'According to the latest research, ',
            'Recent studies have revealed that ',
            'In the realm of science, ',
            'Researchers have discovered that ',
        ],
    }
    if topic in starts:
        return random.choice(starts[topic])
    else:
        return ''

# С точки зрения нейробиологии вшить в промпт :TODO
@bot.message_handler(commands=['start', 'help'])
def start_help(message):
    bot.send_message(message.chat.id,
                     "Welcome to the NeuroGPT. Feel free to ask me any questions related "
                     "to these topics. I'll try my best to answer them in a comprehensive and informative way." 
                     f"I use {device}")


@bot.message_handler(func=lambda message: True)
def answer_questions(message):
    question = message.text.lower()

    prompt = question
    prompt_template = f'''[INST] <<SYS>>
    You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe.  Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature. If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information.
    <</SYS>>
    {prompt}[/INST]

    '''
    # print("\n\n*** Generate:")

    input_ids = tokenizer(prompt_template, return_tensors='pt').input_ids.cuda()
    output = model.generate(inputs=input_ids, temperature=0.7, do_sample=True, top_p=0.95, top_k=40, max_new_tokens=512)
    answer = tokenizer.decode(output[0])
    bot.send_message(message.chat.id, answer)

bot.polling()
