'''
    Модуль який відсилає фото
'''
import modules.create_bot as m_bot
import modules.create_path_to_file as m_create_path
import modules.create_inline_keyboard as m_inline_keyboard

def send_picture(message):
    if message.text.lower() == "get picture":
        #
        path_file = m_create_path.path_file("images/1.jpeg")
        m_bot.bot.send_photo(
            message.chat.id, 
            open(path_file, 'rb'), #
            "Гарне зображення!", #
            reply_markup= m_inline_keyboard.inline_keyboard #
        )
    m_bot.bot.register_next_step_handler(message, send_picture)