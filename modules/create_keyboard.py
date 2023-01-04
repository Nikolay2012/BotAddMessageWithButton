'''
    Модуль який створює клавіатуру
'''
# Імпортуємо telebot
import telebot
# Імпортуємо модуль створеної кнопки 
import modules.create_button as m_button
# Створюємо клавіатуру
keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard= True)
# Додаємо кнопку до клавіатури 
keyboard.add(m_button.button) 
