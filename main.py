'''
    Основний модуль який запускає проект 
'''
# Імпортуємо модуль створити бота 
import modules.create_bot as m_bot
# Імпортуємо модуль який запускає бота 
import modules.command_start as m_start
# Бот прослуховує усі чати
m_bot.bot.polling(none_stop=True)