from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton,\
    ReplyKeyboardRemove

btn_main_menu = KeyboardButton("Главное меню")

TOKEN = "6206247538:AAHrVH9AdGJVALrQBPW6htbTpCoUqdN54kk"
dic = ['course', 'help', 'call', 'prog', 'graphic', 'marketing', 'business', 'lang', 'python', 'js', 'trans', 'check']

HELP_MENU = """
<b>С помощью данного бота ты можешь ознакомиться и приобрести интересующие тебя курсы!</b>
"""


# --Main Menu--
btn_main = KeyboardButton('Курсы')  # +
btn_main1 = KeyboardButton('Помощь')  # +
btn_main2 = KeyboardButton('Связь с менеджером')  # +
main_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_main, btn_main1, btn_main2)
message = "С помощью данного бота ты сможешь ознакомиться и приобрести интересующие тебя курсы!😁" \

# --Course Menu--
btn_course = InlineKeyboardButton('Программирование', callback_data='prog')
btn_course1 = InlineKeyboardButton('Графика', callback_data='graphic')
btn_course2 = InlineKeyboardButton('Маркетинг', callback_data='marketing')
btn_course3 = InlineKeyboardButton('Ведение бизнеса', callback_data='business')
btn_course4 = InlineKeyboardButton('Иностранные языки', callback_data='lang')
course_menu = InlineKeyboardMarkup(row_width=2).add(btn_course, btn_course1, btn_course2, btn_course3,
                                                    btn_course4)

# --Prog Menu--
btn_prg = InlineKeyboardButton('Python-разработчик🐍', callback_data='python')
btn_prg1 = InlineKeyboardButton('C++ разработчик✨', callback_data='c++')
btn_prg2 = InlineKeyboardButton('JavaScript-разработчик💥', callback_data='js')
btn_prg3 = InlineKeyboardButton('Android-разработчик📱', callback_data='android')
btn_prg4 = InlineKeyboardButton('Назад⬅️', callback_data='back_course')
prog_menu = InlineKeyboardMarkup(row_width=2).add(btn_prg, btn_prg1, btn_prg2, btn_prg3, btn_prg4)

# --Graphic Menu--
btn_gr = InlineKeyboardButton('Photoshop🖼', callback_data='photoshop')
btn_gr1 = InlineKeyboardButton('Illustrator🫧', callback_data='illustrator')
btn_gr2 = InlineKeyboardButton('Blender⭐️', callback_data='blender')
btn_gr3 = InlineKeyboardButton('Назад⬅', callback_data='back_course')
graphic_menu = InlineKeyboardMarkup(row_width=3).add(btn_gr, btn_gr1, btn_gr2, btn_gr3)

# --Marketing Menu--
btn_mark = InlineKeyboardButton('Менеджер маркетплейсов✨', callback_data='marketplace')
btn_mark1 = InlineKeyboardButton('Интернет-маркетолог💴', callback_data='web-market')
btn_mark2 = InlineKeyboardButton('SEO-специалист с нуля🤑', callback_data='seo')
btn_mark3 = InlineKeyboardButton('Бренд-менеджер💳', callback_data='brand')
btn_mark4 = InlineKeyboardButton('Назад⬅', callback_data='back_course')
marketing_menu = InlineKeyboardMarkup(row_width=2).add(btn_mark, btn_mark1, btn_mark2, btn_mark3, btn_mark4)

# --Business Menu--
btn_bsn = InlineKeyboardButton('Бизнес-аналитики💰', callback_data='analytics')
btn_bsn1 = InlineKeyboardButton('Техники ведения бизнеса💴', callback_data='technology_bsn')
btn_bsn2 = InlineKeyboardButton('Назад⬅', callback_data='back_course')
business_menu = InlineKeyboardMarkup(row_width=2).add(btn_bsn, btn_bsn1, btn_bsn2)

# --Lang Menu--
btn_lang = InlineKeyboardButton('Английский язык🇬🇧', callback_data='english')
btn_lang1 = InlineKeyboardButton('Немецкий язык🇩🇪', callback_data='germ')
btn_lang2 = InlineKeyboardButton('Японский язык🥢', callback_data='jap')
btn_lang3 = InlineKeyboardButton('Польский язык🇵🇱', callback_data='poland')
btn_lang4 = InlineKeyboardButton('Назад⬅', callback_data='back_course')
lang_menu = InlineKeyboardMarkup(row_width=2).add(btn_lang, btn_lang1, btn_lang2, btn_lang3, btn_lang4)

# --Help Menu--
btn = InlineKeyboardButton('Как происходит оплата?', callback_data='trans')
btn1 = InlineKeyboardButton('Проверка оплаты💰', callback_data='check')
help_menu = InlineKeyboardMarkup(row_width=1).add(btn)
check_purch = InlineKeyboardMarkup(row_width=1).add(btn1)
help_text = "<b>Оплата работает по такому принципу, что вы выбираете заинтересовавший вас курс, нажимаете кнопку " \
       "подписаться, и после этого по высланным вам реквизитам производится оплата.</b>"
# Prog===============================================================================
# --Python Menu--
btn_python = InlineKeyboardButton('Записаться на курс🤙', callback_data='addcourse')
btn_python1 = InlineKeyboardButton('Назад⬅', callback_data='back_prog')
python_menu = InlineKeyboardMarkup(row_width=1).add(btn_python, btn_python1)

# --C++ Menu--
btn_cc = InlineKeyboardButton('Записаться на курс🤙', callback_data='addcourse')
btn_cc1 = InlineKeyboardButton('Назад⬅', callback_data='back_prog')
cc_menu = InlineKeyboardMarkup(row_width=1).add(btn_cc, btn_cc1)

# --JS Menu--
btn_js = InlineKeyboardButton('Записаться на курс🤙', callback_data='addcourse')
btn_js1 = InlineKeyboardButton('Назад⬅', callback_data='back_prog')
js_menu = InlineKeyboardMarkup(row_width=1).add(btn_js, btn_js1)

# --Android Menu--
btn_android = InlineKeyboardButton('Записаться на курс🤙', callback_data='addcourse')
btn_android1 = InlineKeyboardButton('Назад⬅', callback_data='back_prog')
android_menu = InlineKeyboardMarkup(row_width=1).add(btn_android, btn_android1)
# ===============================================================================!

# Graphic===============================================================================
# --Photoshop Menu--
btn_photoshop = InlineKeyboardButton('Записаться на курс🤙', callback_data='addcourse')
btn_photoshop1 = InlineKeyboardButton('Назад⬅', callback_data='back_graphic')
photoshop_menu = InlineKeyboardMarkup(row_width=1).add(btn_photoshop, btn_photoshop1)

# --Illustrator Menu--
btn_illustrator = InlineKeyboardButton('Записаться на курс🤙', callback_data='addcourse')
btn_illustrator1 = InlineKeyboardButton('Назад⬅', callback_data='back_graphic')
illustrator_menu = InlineKeyboardMarkup(row_width=1).add(btn_illustrator, btn_illustrator1)

# --Blender Menu--
btn_blender = InlineKeyboardButton('Записаться на курс🤙', callback_data='addcourse')
btn_blender1 = InlineKeyboardButton('Назад⬅', callback_data='back_graphic')
blender_menu = InlineKeyboardMarkup(row_width=1).add(btn_blender, btn_blender1)
# Graphic===============================================================================!

# Marketing Menu===============================================================================

# --Менеджер маркетплейсов--
btn_marketplace = InlineKeyboardButton('Записаться на курс🤙', callback_data='addcourse')
btn_marketplace1 = InlineKeyboardButton('Назад⬅', callback_data='back_marketing')
marketplace_menu = InlineKeyboardMarkup(row_width=1).add(btn_marketplace, btn_marketplace1)

# --Интернет-маркетолог--
btn_marketolog = InlineKeyboardButton('Записаться на курс🤙', callback_data='addcourse')
btn_marketolog1 = InlineKeyboardButton('Назад⬅', callback_data='back_marketing')
marketolog_menu = InlineKeyboardMarkup(row_width=1).add(btn_marketolog, btn_marketolog1)

# --SEO-специалист с нуля--
btn_seo = InlineKeyboardButton('Записаться на курс🤙', callback_data='addcourse')
btn_seo1 = InlineKeyboardButton('Назад⬅', callback_data='back_marketing')
seo_menu = InlineKeyboardMarkup(row_width=1).add(btn_seo, btn_seo1)

# --Бренд-менеджер--
btn_brand = InlineKeyboardButton('Записаться на курс🤙', callback_data='addcourse')
btn_brand1 = InlineKeyboardButton('Назад⬅', callback_data='back_marketing')
brand_menu = InlineKeyboardMarkup(row_width=1).add(btn_brand, btn_brand1)

# Marketing Menu===============================================================================!

# Business Menu===============================================================================
# --Бизнес-аналитики--
btn_analytics = InlineKeyboardButton('Записаться на курс🤙', callback_data='addcourse')
btn_analytics1 = InlineKeyboardButton('Назад⬅', callback_data='back_business')
analytics_menu = InlineKeyboardMarkup(row_width=1).add(btn_analytics, btn_analytics1)

# --Техники ведения бизнеса--
btn_doing_bsns = InlineKeyboardButton('Записаться на курс🤙', callback_data='addcourse')
btn_doing_bsns1 = InlineKeyboardButton('Назад⬅', callback_data='back_business')
doing_bsns_menu = InlineKeyboardMarkup(row_width=1).add(btn_doing_bsns, btn_doing_bsns1)

# Business Menu===============================================================================

# Lang Menu===============================================================================

# --Английский--
btn_eng = InlineKeyboardButton('Записаться на курс🤙', callback_data='addcourse')
btn_eng1 = InlineKeyboardButton('Назад⬅', callback_data='back_lang')
eng_menu = InlineKeyboardMarkup(row_width=1).add(btn_eng, btn_eng1)

# --Немецкий--
btn_germ = InlineKeyboardButton('Записаться на курс🤙', callback_data='addcourse')
btn_germ1 = InlineKeyboardButton('Назад⬅', callback_data='back_lang')
germany_menu = InlineKeyboardMarkup(row_width=1).add(btn_germ, btn_germ1)

# --Японский--
btn_jap = InlineKeyboardButton('Записаться на курс🤙', callback_data='addcourse')
btn_jap1 = InlineKeyboardButton('Назад⬅', callback_data='back_lang')
japanese_menu = InlineKeyboardMarkup(row_width=1).add(btn_jap, btn_jap1)

# --Польский--
btn_pol = InlineKeyboardButton('Записаться на курс🤙', callback_data='addcourse')
btn_pol1 = InlineKeyboardButton('Назад⬅', callback_data='back_lang')
poland_menu = InlineKeyboardMarkup(row_width=1).add(btn_pol, btn_pol1)

# Lang Menu===============================================================================!

# Back_to_main_menu

btn_back_menu = InlineKeyboardButton('Вернуться в Главное меню⬅', callback_data='back_to_main_menu')
back_to_main_menu = InlineKeyboardMarkup(resize_keyboard=True).add(btn_back_menu)
