import telebot
import time

bot = telebot.TeleBot('6777587419:AAH1Y7EE9i61PJeoNAQEhAvGRoHUdmJ0yvE')


@bot.message_handler(commands=['start', 'help'])
def start_help(message):
    bot.send_message(message.chat.id,
                     "Добро пожаловать в чат NeuroGPT.\nЯ постараюсь помочь, если это не нарушает никаких законов и "
                     "связано с саморазвитием и наукой.\nОднако, данный контент носит чисто информативный характер, и "
                     "перед применением предложенных мной практических советов следует проконсультироваться со своим "
                     "врачом.")


answer = """Я ведаю одним научно обоснованным методом прекращения икоты, который включает в себя перевозбуждение 
диафрагмального нерва три раза подряд с помощью специальной дыхательной техники. Вот как вы можете это сделать:
\n1. Глубоко вдохните через нос в течение примерно 3-4 секунд.\n2. Прежде чем выдохнуть воздух, сделайте еще один быстрый 
вдох через нос в течение примерно 1-2 секунд.\n3. Сделайте третий вдох через нос, даже если это всего на 
микросекунду.\n4. Задержите дыхание примерно на 15-20 секунд.\n5. Медленно выдохните через нос или рот.\n\nЭтот метод 
использует преимущества нейронных механизмов, вызывающих икоту, путем чрезмерного возбуждения диафрагмального нерва 
три раза подряд, а затем гиперполяризации его в течение некоторого времени после этого, что снижает вероятность его 
повторной активации. Важно вернуться к нормальному ритму дыхания после выполнения этой техники, чтобы полностью 
устранить икоту. Если вам нужно выполнить ее снова, не стесняйтесь. Это наиболее эффективный и научно обоснованный 
способ остановить икоту."""


@bot.message_handler(func=lambda message: True)
def answer_questions(message):
    time.sleep(600)
    bot.send_messag e(message.chat.id, answer)


bot.polling()
"""There is a scientifically supported method for stopping hiccups, which involves hyperexciting the phrenic nerve 
three times in a row through a specific breathing technique. Here's how you can do it: 1. Inhale deeply through your 
nose for about 3-4 seconds. 2. Before exhaling any air, take another quick inhale through your nose for about 1-2 
seconds. 3. Take a third inhale through your nose, even if it's just for a microsecond. 4. Hold your breath for about 
15-20 seconds. 5. Slowly exhale through your nose or mouth. This technique takes advantage of the neural mechanisms 
that cause hiccups by hyperexciting the phrenic nerve three times in a row, and then hyperpolarizing it for some time 
afterwards, making it less likely to get activated again. It's important to return to your normal breathing cadence 
after doing this technique to eliminate hiccups completely. If you need to perform it again, feel free to do so. This 
is the most efficient and science-supported way to stop hiccups based on the provided context."""
