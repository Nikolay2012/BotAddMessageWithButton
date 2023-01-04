'''
    Модуль який перевіряє команду старт 
'''
import modules.create_bot as m_bot
import modules.create_keyboard as m_keyboard
import modules.send_picture as m_send_pic

@m_bot.bot.message_handler(commands=["start"])

def bot_start(message):
    m_bot.bot.send_message(
        message.chat.id,
        "Hello user!",
        reply_markup= m_keyboard.keyboard
    )
    m_bot.bot.register_next_step_handler(message, m_send_pic.send_picture)