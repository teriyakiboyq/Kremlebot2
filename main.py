from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
import markups
import time

bot = Bot(token=markups.TOKEN)
dp = Dispatcher(bot)


# --Main menu--
@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'Приветствую, <b>{message.from_user.first_name}</b>👋\n{markups.message}',
                           parse_mode='html', reply_markup=markups.main_menu)
    await message.delete()


@dp.message_handler(Text(equals="Курсы"))
async def course_menu(message: types.Message):
    await bot.send_message(message.from_user.id, "<b>Выберите интересующий вас курс</b>",
                           reply_markup=markups.course_menu, parse_mode='html')
    await message.delete()


@dp.message_handler(Text(equals="Помощь"))
async def course_menu(message: types.Message):
    await bot.send_message(message.from_user.id, "<b><u>❓</u>Часто задаваемые вопросы<u>❓</u></b>",
                           reply_markup=markups.help_menu, parse_mode='html')
    await message.delete()


@dp.message_handler(Text(equals="Связь с менеджером"))
async def course_menu(message: types.Message):
    msg = "Пользователь {} запросил поддержку \"{}\".".format(message.from_user.username, message.text)
    # ms = f"Пользователь {bot.send_contact(message.from_user.id, '-', message.from_user.username)} запросил помощь"
    await bot.send_message(message.from_user.id, "<b>В ближайшее время с вами свяжется менеджер.</b>",
                           parse_mode='html')
    await bot.send_message('1320178646', msg)


# --Help menu--
@dp.callback_query_handler(Text('trans'))
async def course_prog(callback: types.CallbackQuery):
    await callback.message.answer(markups.help_text, parse_mode='html')
    await callback.message.delete()


@dp.callback_query_handler(Text('check'))
async def course_prog(callback: types.CallbackQuery):
    await callback.answer('Оплата произведена успешно!✅')
    time.sleep(3)
    await callback.message.answer('<b>Спасибо за покупку!😃</b>', parse_mode='html')


# --Course menu--
@dp.callback_query_handler(Text('prog'))
async def course_prog(callback: types.CallbackQuery):
    await callback.message.answer('Отличный выбор‼️ \nТеперь самое время выбрать направление!',
                                  reply_markup=markups.prog_menu)
    await callback.message.delete()


@dp.callback_query_handler(Text('graphic'))
async def course_graphic(callback: types.CallbackQuery):
    await callback.message.answer('Отличный выбор‼️ \nТеперь самое время выбрать направление!',
                                  reply_markup=markups.graphic_menu)
    await callback.message.delete()


@dp.callback_query_handler(Text('marketing'))
async def course_marketing(callback: types.CallbackQuery):
    await callback.message.answer('Отличный выбор‼️ \nТеперь самое время выбрать направление!',
                                  reply_markup=markups.marketing_menu)
    await callback.message.delete()


@dp.callback_query_handler(Text('business'))
async def course_business(callback: types.CallbackQuery):
    await callback.message.answer('Отличный выбор‼️ \nТеперь самое время выбрать направление!',
                                  reply_markup=markups.business_menu)
    await callback.message.delete()


@dp.callback_query_handler(Text('lang'))
async def course_lang(callback: types.CallbackQuery):
    await callback.message.answer('Отличный выбор‼️ \nТеперь самое время выбрать направление!',
                                  reply_markup=markups.lang_menu)
    await callback.message.delete()


# --Programming menu--
@dp.callback_query_handler(Text('python'))
async def prog_python(callback: types.CallbackQuery):
    await callback.bot.send_photo(chat_id=callback.message.chat.id, photo='https://cdn-icons-png.flaticon.com/512'
                                                                          '/5968/5968286.png',
                                  caption=f'<b>Язык программирования Python является одним из самых популярный языков'
                                          f'программирования, благодаря своей простоте и в то же время наличием'
                                          f'мощных инструментов, благодаря которым вы сможете с удовольствием кодить,'
                                          f'и именно для правильного синтаксиса нужна база знаний, которую как раз в'
                                          f' полной мере получаешь в данном курсе.</b>',
                                  reply_markup=markups.python_menu, parse_mode='html')
    await callback.message.delete()


@dp.callback_query_handler(Text('c++'))
async def prog_python(callback: types.CallbackQuery):
    await callback.bot.send_photo(chat_id=callback.message.chat.id, photo='https://avatars.dzeninfra.ru/get-zen_doc'
                                                                          '/5231889/pub_62c56c22bafc740dd37d5c73_62'
                                                                          'c56d262d1a144289408b2d/scale_1200',
                                  caption=f'<b>Программисты на C++ создают сложные программы и сервисы. '
                                          f'Они разрабатывают высоконагруженные сетевые приложения, игры, графические '
                                          f'движки, компоненты для операционных систем и железа. На этом языке написаны'
                                          f' Windows, Linux и macOS, Android, Chrome, Counter-Strike, StarCraft и '
                                          f'Diablo. '
                                          f' Вы освоите легендарный язык программирования с нуля: напишете поисковый '
                                          f'движок, собственный Booking.com и получите навыки работы в команде.</b>',
                                  reply_markup=markups.cc_menu, parse_mode='html')
    await callback.message.delete()


@dp.callback_query_handler(Text('js'))
async def prog_python(callback: types.CallbackQuery):
    await callback.bot.send_photo(chat_id=callback.message.chat.id, photo='https://www.cischool.ru/wp-content/uploads/'
                                                                          '2021/04/Depositphotos_41138921_l-2015.jpg',
                                  caption=f'<b>Вы с нуля научитесь программировать на языке Java и создавать'
                                          f' веб-приложения на фреймворке Spring. За полгода получите фундаментальные '
                                          f'навыки и соберёте портфолио, а мы поможем найти работу.</b>',
                                  reply_markup=markups.js_menu, parse_mode='html')
    await callback.message.delete()


@dp.callback_query_handler(Text('android'))
async def prog_python(callback: types.CallbackQuery):
    await callback.bot.send_photo(chat_id=callback.message.chat.id, photo='https://f.vividscreen.info/soft/0343e0e7f2f'
                                                                          '37aeb23ac5e55e2615c28/Android-Tech-Back'
                                                                          'ground-2048x2048.jpg',
                                  caption=f'<b>По данным Google, 3 млрд устройств работает на Android. '
                                          f'Телевизоры, смартфоны и умные часы напичканы полезными приложениями, '
                                          f'с помощью которых мы смотрим сериалы, платим за покупки, общаемся и '
                                          f'заказываем еду. Теперь и вы сможете создавать такие сервисы.</b>',
                                  reply_markup=markups.android_menu, parse_mode='html')
    await callback.message.delete()


# -- Handler Back --

# -- Back Lang.Prog - Prog --
@dp.callback_query_handler(Text('back_prog'))
async def course_lang(callback: types.CallbackQuery):
    await callback.message.answer('Назад⬅', reply_markup=markups.prog_menu)
    await callback.message.delete()


# -- Back Prog - Course --
@dp.callback_query_handler(Text('back_course'))
async def course_lang(callback: types.CallbackQuery):
    await callback.message.answer('Назад⬅', reply_markup=markups.course_menu)
    await callback.message.delete()


# -- Back AplyGraphic - Graphic --
@dp.callback_query_handler(Text('back_graphic'))
async def course_lang(callback: types.CallbackQuery):
    await callback.message.answer('Назад⬅', reply_markup=markups.graphic_menu)
    await callback.message.delete()


# -- Back LastPage - MainMenu --
@dp.callback_query_handler(Text('back_to_main_menu'))
async def course_lang(callback: types.CallbackQuery):
    await callback.message.answer('Главное меню', reply_markup=markups.main_menu)
    await callback.message.delete()

# -- Back OtherMarketing - Marketing --
@dp.callback_query_handler(Text('back_marketing'))
async def course_lang(callback: types.CallbackQuery):
    await callback.message.answer('Назад⬅', reply_markup=markups.marketing_menu)
    await callback.message.delete()


# -- Back OtherBusiness - Business --
@dp.callback_query_handler(Text('back_business'))
async def course_lang(callback: types.CallbackQuery):
    await callback.message.answer('Назад⬅', reply_markup=markups.business_menu)
    await callback.message.delete()


# -- Back OtherLang - Lang --
@dp.callback_query_handler(Text('back_lang'))
async def course_lang(callback: types.CallbackQuery):
    await callback.message.answer('Назад⬅', reply_markup=markups.lang_menu)
    await callback.message.delete()


# --Graphic menu--

@dp.callback_query_handler(Text('photoshop'))
async def prog_python(callback: types.CallbackQuery):
    await callback.bot.send_photo(chat_id=callback.message.chat.id, photo='https://sun6-23.userapi.com/s/v1/ig2/3f'
                                                                          'o0bY2GyOkOxhrCzAVCSl-68Jj75RwHm6K_i6Nq4'
                                                                          'F6TMAvuenZ608fqmcuKv_cW_Qn7yWH67vbdHy26'
                                                                          'q91jbbO4.jpg?size=900x900&quality=96&cr'
                                                                          'op=0,0,900,900&ava=1',
                                  caption=f'<b>Научитесь создавать удобные сайты и приложения, работать с анимацией и '
                                          f'презентовать проекты клиентам. Сможете начать карьеру в дизайне и брать '
                                          f'первые заказы уже после 8 месяцев интенсивных занятий.</b>',
                                  reply_markup=markups.photoshop_menu, parse_mode='html')
    await callback.message.delete()


@dp.callback_query_handler(Text('illustrator'))
async def prog_python(callback: types.CallbackQuery):
    await callback.bot.send_photo(chat_id=callback.message.chat.id, photo='https://community.adobe.com/t5/image/server'
                                                                          'page/image-id/44547i823334290E0EECC2?v=v2',
                                  caption=f'<b>Научитесь создавать удобные сайты и приложения, работать с анимацией и '
                                          f'презентовать проекты клиентам. Сможете начать карьеру в дизайне и брать '
                                          f'первые заказы уже после 8 месяцев интенсивных занятий.</b>',
                                  reply_markup=markups.illustrator_menu, parse_mode='html')
    await callback.message.delete()


@dp.callback_query_handler(Text('blender'))
async def prog_python(callback: types.CallbackQuery):
    await callback.bot.send_photo(chat_id=callback.message.chat.id, photo='https://satellasoft.com/img/thumb/categoria/'
                                                                          '1427222621.jpg',
                                  caption=f'<b>Научитесь создавать удобные сайты и приложения, работать с анимацией и '
                                          f'презентовать проекты клиентам. Сможете начать карьеру в дизайне и брать '
                                          f'первые заказы уже после 8 месяцев интенсивных занятий.</b>',
                                  reply_markup=markups.blender_menu, parse_mode='html')
    await callback.message.delete()


# --Marketing menu--

@dp.callback_query_handler(Text('marketplace'))
async def prog_python(callback: types.CallbackQuery):
    await callback.bot.send_photo(chat_id=callback.message.chat.id, photo='https://pic.rutubelist.ru/video/93/03/9303fe'
                                                                          'fb391fd68ed854699019fd781c.jpg',
                                  caption=f'<b>Вы с нуля освоите востребованную и перспективную профессию. Узнаете, '
                                          f'как сотрудничать с начинающими селлерами и крупными компаниями. '
                                          f'Получите реальный бюджет на продвижение и сможете на старте зарабатывать '
                                          f'от 60000 рублей, не выходя из дома.</b>',
                                  reply_markup=markups.marketplace_menu, parse_mode='html')
    await callback.message.delete()


@dp.callback_query_handler(Text('web-market'))
async def prog_python(callback: types.CallbackQuery):
    await callback.bot.send_photo(chat_id=callback.message.chat.id, photo='https://avatars.mds.yandex.net/get-altay/57'
                                                                          '51673/2a0000017dc75f1ec84fd4b33a99a1'
                                                                          'f7f7db/XXL',
                                  caption=f'<b>Вы с нуля освоите востребованную и перспективную профессию. Узнаете, '
                                          f'как сотрудничать с начинающими селлерами и крупными компаниями. '
                                          f'Получите реальный бюджет на продвижение и сможете на старте зарабатывать '
                                          f'от 60000 рублей, не выходя из дома.</b>',
                                  reply_markup=markups.marketolog_menu, parse_mode='html')
    await callback.message.delete()


@dp.callback_query_handler(Text('seo'))
async def prog_python(callback: types.CallbackQuery):
    await callback.bot.send_photo(chat_id=callback.message.chat.id, photo='https://sun9-87.userapi.com/impf/W-zJN_4s'
                                                                          'dJcQEO7FEWbuYk9mEa44xehtc6lqdg/r-yEaMZ50R'
                                                                          'Y.jpg?size=604x502&quality=96&sign='
                                                                          '8751aadf76828d21f5d24972e84035f7&type=album',
                                  caption=f'<b>Вы с нуля освоите востребованную и перспективную профессию. Узнаете, '
                                          f'как сотрудничать с начинающими селлерами и крупными компаниями. '
                                          f'Получите реальный бюджет на продвижение и сможете на старте зарабатывать '
                                          f'от 60000 рублей, не выходя из дома.</b>',
                                  reply_markup=markups.seo_menu, parse_mode='html')
    await callback.message.delete()


@dp.callback_query_handler(Text('brand'))
async def prog_python(callback: types.CallbackQuery):
    await callback.bot.send_photo(chat_id=callback.message.chat.id, photo='https://synergy.ru/assets/upload/news/'
                                                                          'bspic/61.2.jpg',
                                  caption=f'<b>Вы с нуля освоите востребованную и перспективную профессию. Узнаете, '
                                          f'как сотрудничать с начинающими селлерами и крупными компаниями. '
                                          f'Получите реальный бюджет на продвижение и сможете на старте зарабатывать '
                                          f'от 60000 рублей, не выходя из дома.</b>',
                                  reply_markup=markups.brand_menu, parse_mode='html')
    await callback.message.delete()


# --Business menu--

@dp.callback_query_handler(Text('analytics'))
async def prog_python(callback: types.CallbackQuery):
    await callback.bot.send_photo(chat_id=callback.message.chat.id, photo='https://selsup.ru/wp-content/uploads/2022/07'
                                                                          '/why-use-google-analytics.jpeg',
                                  caption=f'<b>Систематизируете управленческий опыт, чтобы внедрять изменения и '
                                          f'принимать сложные вызовы. Начнёте чувствовать себя уверенным руководителем '
                                          f'даже в условиях неопределённости.</b>',
                                  reply_markup=markups.analytics_menu, parse_mode='html')
    await callback.message.delete()


@dp.callback_query_handler(Text('technology_bsn'))
async def prog_python(callback: types.CallbackQuery):
    await callback.bot.send_photo(chat_id=callback.message.chat.id, photo='https://kartinkin.net/uploads/posts/2022-03'
                                                                          '/1647983955_65-kartinkin-net-p-kartinki'
                                                                          '-dlya-delovoi-prezentatsii-76.jpg',
                                  caption=f'<b>Систематизируете управленческий опыт, чтобы внедрять изменения и '
                                          f'принимать сложные вызовы. Начнёте чувствовать себя уверенным руководителем '
                                          f'даже в условиях неопределённости.</b>',
                                  reply_markup=markups.doing_bsns_menu, parse_mode='html')
    await callback.message.delete()


# --Language menu--

@dp.callback_query_handler(Text('english'))
async def prog_python(callback: types.CallbackQuery):
    await callback.bot.send_photo(chat_id=callback.message.chat.id, photo='https://sun6-20.userapi.com/s/v1/ig2/Ks'
                                                                          'ScvRBaRi9-f7CB50-hzUcovdYlp6CIpXB3_DNVqa'
                                                                          'Iaw0kQCI5RxrUPJUMGKZy_ANOj5wDmamzrok3gD77'
                                                                          'iKrsq.jpg?size=726x726&quality=95&crop=19,'
                                                                          '0,726,726&ava=1',
                                  caption=f'<b>Курс по данному языку позволяет в полной мере изучить английский язык'
                                          f'для дальнейшего его применения в рабочей сфере, переезде в другую страну'
                                          f'и просто в повседневной жизни.</b>',
                                  reply_markup=markups.eng_menu, parse_mode='html')
    await callback.message.delete()


@dp.callback_query_handler(Text('germ'))
async def prog_python(callback: types.CallbackQuery):
    await callback.bot.send_photo(chat_id=callback.message.chat.id, photo='https://i1.wp.com/flagsweb.com/Flag_'
                                                                          'Emoji/Germany_Flag_Emoji.png',
                                  caption=f'<b>Курс по данному языку позволяет в полной мере изучить немецкий язык'
                                          f'для дальнейшего его применения в рабочей сфере, переезде в другую страну'
                                          f'и просто в повседневной жизни.</b>',
                                  reply_markup=markups.germany_menu, parse_mode='html')
    await callback.message.delete()


@dp.callback_query_handler(Text('jap'))
async def prog_python(callback: types.CallbackQuery):
    await callback.bot.send_photo(chat_id=callback.message.chat.id, photo='https://www.clipartmax.com/png/full/446'
                                                                          '-4464809_japanese-png-tsurugaoka-'
                                                                          'hachiman-g%C5%AB.png',
                                  caption=f'<b>Курс по данному языку позволяет в полной мере изучить японский язык'
                                          f'для дальнейшего его применения в рабочей сфере, переезде в другую страну'
                                          f'и просто в повседневной жизни.</b>',
                                  reply_markup=markups.japanese_menu, parse_mode='html')
    await callback.message.delete()


@dp.callback_query_handler(Text('poland'))
async def prog_python(callback: types.CallbackQuery):
    await callback.bot.send_photo(chat_id=callback.message.chat.id, photo='https://dltaw1vhj9zy5.cloudfront.net/2018/09'
                                                                          '/Poland_round_flag.jpg',
                                  caption=f'<b>Курс по данному языку позволяет в полной мере изучить польский язык'
                                          f'для дальнейшего его применения в рабочей сфере, переезде в другую страну'
                                          f'и просто в повседневной жизни.</b>',
                                  reply_markup=markups.poland_menu, parse_mode='html')
    await callback.message.delete()


# --Price--

@dp.callback_query_handler(Text('addcourse'))
async def purchase(callback: types.CallbackQuery):
    await callback.message.answer(text="<b>Отлично!👍 "
                                       "\nВы успешно записаны на курс.✅</b>", parse_mode='html',
                                  reply_markup=markups.back_to_main_menu)
    time.sleep(2)
    await callback.message.answer(text="<b>\nДанный курс отлично подойдет для проработки и закрепления навыков, "
                                       "даже если вы абсолютный новичок, стоимость "
                                       "данного курса будет составлять <strike>27 990</strike> "
                                       " <u>24 750 р.</u> с учетом <u>15%</u> скидки."
                                       "\nДля покупки вам потребуется совершить платеж по данным реквизитам "
                                       ", затем нажать на кнопку <u>'Проверка платежа'</u>."
                                       "\nРеквизиты **************. "
                                       "\nБлагодарим вас за то, что выбираете нас❤!️</b>", parse_mode='html',
                                  reply_markup=markups.check_purch)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
