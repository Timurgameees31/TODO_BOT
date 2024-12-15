from telebot import TeleBot
from constant import TOKEN
from controllers import Controller

# Создаем экземпляр бота
bot = TeleBot(TOKEN)
controller = Controller(bot)

# Подключаем обработчики
controller.register_handlers()

print("Bot is running...")
bot.polling()

