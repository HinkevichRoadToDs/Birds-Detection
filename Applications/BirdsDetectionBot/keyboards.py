from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

# Клавиатура главного меню
kbrd_menu = ReplyKeyboardMarkup(resize_keyboard=True)
info_btn = KeyboardButton('О проекте')
kbrd_menu.add(info_btn)


# Кнопка под фото голубя
inline_dove = InlineKeyboardMarkup(row_width=3)
wiki_dove = InlineKeyboardButton(text='Узнать о голубе', url='https://ru.wikipedia.org/wiki/Голуби')
inline_dove.add(wiki_dove)


# Кнопка под фото синицы
inline_bluetit = InlineKeyboardMarkup(row_width=3)
wiki_bluetit = InlineKeyboardButton(text='Узнать о синице', url='https://ru.wikipedia.org/wiki/Большая_синица')
inline_bluetit.add(wiki_bluetit)


# Кнопка под фото дрозда
inline_thrush = InlineKeyboardMarkup(row_width=3)
wiki_thrush = InlineKeyboardButton(text='Узнать о дрозде', url='https://en.wikipedia.org/wiki/Thrush_(bird)')
inline_thrush.add(wiki_thrush)


# Кнопка под фото воробья
inline_sparrow = InlineKeyboardMarkup(row_width=3)
wiki_sparrow = InlineKeyboardButton(text='Узнать о воробье', url='https://en.wikipedia.org/wiki/House_sparrow')
inline_sparrow.add(wiki_sparrow)

# Кнопка под фото дятла
inline_woodpecker = InlineKeyboardMarkup(row_width=3)
wiki_woodpecker = InlineKeyboardButton(text='Узнать о дятле', url='https://en.wikipedia.org/wiki/Woodpecker')
inline_woodpecker.add(wiki_woodpecker)

# Кнопка под фото кардинала
inline_cardinal = InlineKeyboardMarkup(row_width=10)
wiki_cardinal = InlineKeyboardButton(text='Узнать о красном кардинале', url='https://ru.wikipedia.org/wiki/Красный_кардинал')
inline_cardinal.add(wiki_cardinal)