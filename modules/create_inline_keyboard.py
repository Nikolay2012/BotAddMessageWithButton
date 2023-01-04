'''
    Модуль який створює лінійну клавіатуру для нашого зоображення чи тексту
'''
import telebot
import modules.create_inline_button as m_inline_button

inline_keyboard = telebot.types.InlineKeyboardMarkup()

inline_keyboard.add(m_inline_button.inline_button)