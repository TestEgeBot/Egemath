#-*-coding: utf8-*-
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

import sqlite3


var1_but = InlineKeyboardButton("Вариант 1", callback_data="var1")#Создаем объект InlineKeyboardButton. У данного объекта имеется 2 параметра: Текст и callbackdata(то что будет отсылаться серверу при нажатии кнопки) данное действие происходит с 1 по 44 строку.
var2_but = InlineKeyboardButton("Вариант 2", callback_data="var2")
var3_but = InlineKeyboardButton("Вариант 3", callback_data="var3")

zad1_but = InlineKeyboardButton("Задание 1", callback_data="zad1")
zad2_but = InlineKeyboardButton("Задание 2", callback_data="zad2")
zad3_but = InlineKeyboardButton("Задание 3", callback_data="zad3")
zad4_but = InlineKeyboardButton("Задание 4", callback_data="zad4")
zad5_but = InlineKeyboardButton("Задание 5", callback_data="zad5")
zad6_but = InlineKeyboardButton("Задание 6", callback_data="zad6")
zad7_but = InlineKeyboardButton("Задание 7", callback_data="zad7")
zad8_but = InlineKeyboardButton("Задание 8", callback_data="zad8")
zad9_but = InlineKeyboardButton("Задание 9", callback_data="zad9")
zad10_but = InlineKeyboardButton("Задание 10", callback_data="zad10")
zad11_but = InlineKeyboardButton("Задание 1", callback_data="zad11")
zad12_but = InlineKeyboardButton("Задание 2", callback_data="zad12")
zad13_but = InlineKeyboardButton("Задание 3", callback_data="zad13")
zad14_but = InlineKeyboardButton("Задание 4", callback_data="zad14")
zad15_but = InlineKeyboardButton("Задание 5", callback_data="zad15")
zad16_but = InlineKeyboardButton("Задание 6", callback_data="zad16")
zad17_but = InlineKeyboardButton("Задание 7", callback_data="zad17")
zad18_but = InlineKeyboardButton("Задание 8", callback_data="zad18")
zad19_but = InlineKeyboardButton("Задание 9", callback_data="zad19")
zad20_but = InlineKeyboardButton("Задание 10", callback_data="zad20")
zad21_but = InlineKeyboardButton("Задание 1", callback_data="zad21")
zad22_but = InlineKeyboardButton("Задание 2", callback_data="zad22")
zad23_but = InlineKeyboardButton("Задание 3", callback_data="zad23")
zad24_but = InlineKeyboardButton("Задание 4", callback_data="zad24")
zad25_but = InlineKeyboardButton("Задание 5", callback_data="zad25")
zad26_but = InlineKeyboardButton("Задание 6", callback_data="zad26")
zad27_but = InlineKeyboardButton("Задание 7", callback_data="zad27")
zad28_but = InlineKeyboardButton("Задание 8", callback_data="zad28")
zad29_but = InlineKeyboardButton("Задание 9", callback_data="zad29")
zad30_but = InlineKeyboardButton("Задание 10", callback_data="zad30")
back_but = InlineKeyboardButton("Назад", callback_data="back")

Var_keyboard = InlineKeyboardMarkup()#Создаем обьект разметки клавиатуры:
Var_keyboard.add(var1_but).add(var2_but).add(var3_but)

Var1_keyboard = InlineKeyboardMarkup()#Создаем обьект разметки клавиатуры:
Var1_keyboard.add(zad1_but).add(zad2_but).add(zad3_but).add(zad4_but).add(zad5_but).add(zad6_but).add(zad7_but).add(zad8_but).add(zad9_but).add(zad10_but)#Метод add() добавляет данный элемент к набору

Var2_keyboard = InlineKeyboardMarkup()#Создаем обьект разметки клавиатуры:
Var2_keyboard.add(zad11_but).add(zad12_but).add(zad13_but).add(zad14_but).add(zad15_but).add(zad16_but).add(zad17_but).add(zad18_but).add(zad19_but).add(zad20_but)

Var3_keyboard = InlineKeyboardMarkup()#Создаем обьект разметки клавиатуры:
Var3_keyboard.add(zad21_but).add(zad22_but).add(zad23_but).add(zad24_but).add(zad25_but).add(zad26_but).add(zad27_but).add(zad28_but).add(zad29_but).add(zad30_but)

token = "5623475434:AAHom73zP8B-Q-kPygfteRVA-Fj9XxTRDyY"#Токен который мы получили у @BotFather

conn = sqlite3.connect("BD.db")#Подключаемся к бд
cursor = conn.cursor()#объект который позволяет выполнять любые операции чтения\записи в бд

bot = Bot(token=token)#Создаем объект бота
dp = Dispatcher(bot)#Создаем экземпляр диспетчер

@dp.message_handler(commands = ["start"])#Декоратор @message_handler реагирует на входящие сообщение.
async def start_command(message: types.Message):#Пишем асинхронную функцию которая обрабатывает декоратор
	cursor.execute(f"INSERT INTO user VALUES({message.from_user.id}, 0, 0, 0, 0)")
	await bot.send_message(message.from_user.id, "Выберите вариант:", reply_markup=Var_keyboard)#Отправляем сообщение пользователю


@dp.callback_query_handler(lambda c: c.data == "var1")#ожидаем callback и принимает lambda-функцию для фильтрации
async def var1(callback_query: types.CallbackQuery):
	await bot.answer_callback_query(callback_query.id)
	await bot.send_message(callback_query.from_user.id, "выберите задание:", reply_markup=Var1_keyboard)#Предлагаем пользователю выбрать задание

@dp.callback_query_handler(lambda c: c.data == "var2")
async def var2(callback_query: types.CallbackQuery):
	await bot.answer_callback_query(callback_query.id)
	await bot.send_message(callback_query.from_user.id, "выберите задание:", reply_markup=Var2_keyboard)

@dp.callback_query_handler(lambda c: c.data == "var3")
async def var3(callback_query: types.CallbackQuery):
	await bot.answer_callback_query(callback_query.id)
	await bot.send_message(callback_query.from_user.id, "выберите задание:", reply_markup=Var3_keyboard)

@dp.callback_query_handler(lambda c: c.data == "zad1")
async def zad1(callback_query: types.CallbackQuery):
	await bot.answer_callback_query(callback_query.id)
	cursor.execute(f"UPDATE user SET page=1 WHERE id={callback_query.from_user.id}")
	conn.commit()#Метод commit() используется для обеспечения согласованности изменений, внесенных в базу данных.
	cursor.execute(f"SELECT text FROM var WHERE id=1")
	text = cursor.fetchone()[0]#пишем метод fetchone который возвращает одну строку данных.
	await callback_query.message.delete()#Удаляем сообщение
	await bot.send_message(callback_query.from_user.id, text)
	await bot.send_photo(callback_query.from_user.id, open("1.jpg", "rb"))#Отправляем 1 фото(задание) пользователю

@dp.callback_query_handler(lambda c: c.data == "zad2")
async def zad2(callback_query: types.CallbackQuery):
	await bot.answer_callback_query(callback_query.id)
	cursor.execute(f"UPDATE user SET page=2 WHERE id={callback_query.from_user.id}")
	conn.commit()
	cursor.execute(f"SELECT text FROM var WHERE id=2")
	text = cursor.fetchone()[0]
	await callback_query.message.delete()
	await bot.send_message(callback_query.from_user.id, text)
	await bot.send_photo(callback_query.from_user.id, open("2.jpg", "rb"))

@dp.callback_query_handler(lambda c: c.data == "zad3")
async def zad3(callback_query: types.CallbackQuery):
	await bot.answer_callback_query(callback_query.id)
	cursor.execute(f"UPDATE user SET page=3 WHERE id={callback_query.from_user.id}")
	conn.commit()
	cursor.execute(f"SELECT text FROM var WHERE id=3")
	text = cursor.fetchone()[0]
	await callback_query.message.delete()
	await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(lambda c: c.data == "zad4")
async def zad4(callback_query: types.CallbackQuery):
	await bot.answer_callback_query(callback_query.id)
	cursor.execute(f"UPDATE user SET page=4 WHERE id={callback_query.from_user.id}")
	conn.commit()
	cursor.execute(f"SELECT text FROM var WHERE id=4")
	text = cursor.fetchone()[0]
	await callback_query.message.delete()
	await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(lambda c: c.data == "zad5")
async def zad5(callback_query: types.CallbackQuery):
	await bot.answer_callback_query(callback_query.id)
	cursor.execute(f"UPDATE user SET page=5 WHERE id={callback_query.from_user.id}")
	conn.commit()
	cursor.execute(f"SELECT text FROM var WHERE id=5")
	text = cursor.fetchone()[0]
	await callback_query.message.delete()
	await bot.send_message(callback_query.from_user.id, text)
	await bot.send_photo(callback_query.from_user.id, open("5.jpg", "rb"))

@dp.callback_query_handler(lambda c: c.data == "zad6")
async def zad6(callback_query: types.CallbackQuery):
	await bot.answer_callback_query(callback_query.id)
	cursor.execute(f"UPDATE user SET page=6 WHERE id={callback_query.from_user.id}")
	conn.commit()
	cursor.execute(f"SELECT text FROM var WHERE id=6")
	text = cursor.fetchone()[0]
	await callback_query.message.delete()
	await bot.send_message(callback_query.from_user.id, text)
	await bot.send_photo(callback_query.from_user.id, open("6.jpg", "rb"))

@dp.callback_query_handler(lambda c: c.data == "zad7")
async def zad7(callback_query: types.CallbackQuery):
	await bot.answer_callback_query(callback_query.id)
	cursor.execute(f"UPDATE user SET page=7 WHERE id={callback_query.from_user.id}")
	conn.commit()
	cursor.execute(f"SELECT text FROM var WHERE id=7")
	text = cursor.fetchone()[0]
	await callback_query.message.delete()
	await bot.send_message(callback_query.from_user.id, text)
	await bot.send_photo(callback_query.from_user.id, open("7.jpg", "rb"))

@dp.callback_query_handler(lambda c: c.data == "zad8")
async def zad8(callback_query: types.CallbackQuery):
	await bot.answer_callback_query(callback_query.id)
	cursor.execute(f"UPDATE user SET page=8 WHERE id={callback_query.from_user.id}")
	conn.commit()
	cursor.execute(f"SELECT text FROM var WHERE id=8")
	text = cursor.fetchone()[0]
	await callback_query.message.delete()
	await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(lambda c: c.data == "zad9")
async def zad9(callback_query: types.CallbackQuery):
	await bot.answer_callback_query(callback_query.id)
	cursor.execute(f"UPDATE user SET page=9 WHERE id={callback_query.from_user.id}")
	conn.commit()
	cursor.execute(f"SELECT text FROM var WHERE id=9")
	text = cursor.fetchone()[0]
	await callback_query.message.delete()
	await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(lambda c: c.data == "zad10")
async def zad10(callback_query: types.CallbackQuery):
	await bot.answer_callback_query(callback_query.id)
	cursor.execute(f"UPDATE user SET page=10 WHERE id={callback_query.from_user.id}")
	conn.commit()
	cursor.execute(f"SELECT text FROM var WHERE id=10")
	text = cursor.fetchone()[0]
	await callback_query.message.delete()
	await bot.send_message(callback_query.from_user.id, text)
	await bot.send_photo(callback_query.from_user.id, open("10.jpg", "rb"))

@dp.callback_query_handler(lambda c: c.data == "zad11")
async def zad11(callback_query: types.CallbackQuery):
	await bot.answer_callback_query(callback_query.id)
	cursor.execute(f"UPDATE user SET page=11 WHERE id={callback_query.from_user.id}")
	conn.commit()
	cursor.execute(f"SELECT text FROM var WHERE id=11")
	text = cursor.fetchone()[0]
	await callback_query.message.delete()
	await bot.send_message(callback_query.from_user.id, text)
	await bot.send_photo(callback_query.from_user.id, open("11.jpg", "rb"))

@dp.callback_query_handler(lambda c: c.data == "zad12")
async def zad12(callback_query: types.CallbackQuery):
	await bot.answer_callback_query(callback_query.id)
	cursor.execute(f"UPDATE user SET page=12 WHERE id={callback_query.from_user.id}")
	conn.commit()
	cursor.execute(f"SELECT text FROM var WHERE id=12")
	text = cursor.fetchone()[0]
	await callback_query.message.delete()
	await bot.send_message(callback_query.from_user.id, text)
	await bot.send_photo(callback_query.from_user.id, open("12.jpg", "rb"))

@dp.callback_query_handler(lambda c: c.data == "zad13")
async def zad13(callback_query: types.CallbackQuery):
	await bot.answer_callback_query(callback_query.id)
	cursor.execute(f"UPDATE user SET page=13 WHERE id={callback_query.from_user.id}")
	conn.commit()
	cursor.execute(f"SELECT text FROM var WHERE id=13")
	text = cursor.fetchone()[0]
	await callback_query.message.delete()
	await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(lambda c: c.data == "zad14")
async def zad14(callback_query: types.CallbackQuery):
	await bot.answer_callback_query(callback_query.id)
	cursor.execute(f"UPDATE user SET page=14 WHERE id={callback_query.from_user.id}")
	conn.commit()
	cursor.execute(f"SELECT text FROM var WHERE id=14")
	text = cursor.fetchone()[0]
	await callback_query.message.delete()
	await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(lambda c: c.data == "zad15")
async def zad15(callback_query: types.CallbackQuery):
	await bot.answer_callback_query(callback_query.id)
	cursor.execute(f"UPDATE user SET page=15 WHERE id={callback_query.from_user.id}")
	conn.commit()
	cursor.execute(f"SELECT text FROM var WHERE id=15")
	text = cursor.fetchone()[0]
	await callback_query.message.delete()
	await bot.send_message(callback_query.from_user.id, text)
	await bot.send_photo(callback_query.from_user.id, open("15.jpg", "rb"))

@dp.callback_query_handler(lambda c: c.data == "zad16")
async def zad16(callback_query: types.CallbackQuery):
	await bot.answer_callback_query(callback_query.id)
	cursor.execute(f"UPDATE user SET page=16 WHERE id={callback_query.from_user.id}")
	conn.commit()
	cursor.execute(f"SELECT text FROM var WHERE id=16")
	text = cursor.fetchone()[0]
	await callback_query.message.delete()
	await bot.send_message(callback_query.from_user.id, text)
	await bot.send_photo(callback_query.from_user.id, open("16.jpg", "rb"))

@dp.callback_query_handler(lambda c: c.data == "zad17")
async def zad17(callback_query: types.CallbackQuery):
	await bot.answer_callback_query(callback_query.id)
	cursor.execute(f"UPDATE user SET page=17 WHERE id={callback_query.from_user.id}")
	conn.commit()
	cursor.execute(f"SELECT text FROM var WHERE id=17")
	text = cursor.fetchone()[0]
	await callback_query.message.delete()
	await bot.send_message(callback_query.from_user.id, text)
	await bot.send_photo(callback_query.from_user.id, open("17.jpg", "rb"))

@dp.callback_query_handler(lambda c: c.data == "zad18")
async def zad18(callback_query: types.CallbackQuery):
	await bot.answer_callback_query(callback_query.id)
	cursor.execute(f"UPDATE user SET page=18 WHERE id={callback_query.from_user.id}")
	conn.commit()
	cursor.execute(f"SELECT text FROM var WHERE id=18")
	text = cursor.fetchone()[0]
	await callback_query.message.delete()
	await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(lambda c: c.data == "zad19")
async def zad19(callback_query: types.CallbackQuery):
	await bot.answer_callback_query(callback_query.id)
	cursor.execute(f"UPDATE user SET page=19 WHERE id={callback_query.from_user.id}")
	conn.commit()
	cursor.execute(f"SELECT text FROM var WHERE id=19")
	text = cursor.fetchone()[0]
	await callback_query.message.delete()
	await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(lambda c: c.data == "zad20")
async def zad20(callback_query: types.CallbackQuery):
	await bot.answer_callback_query(callback_query.id)
	cursor.execute(f"UPDATE user SET page=20 WHERE id={callback_query.from_user.id}")
	conn.commit()
	cursor.execute(f"SELECT text FROM var WHERE id=20")
	text = cursor.fetchone()[0]
	await callback_query.message.delete()
	await bot.send_message(callback_query.from_user.id, text)
	await bot.send_photo(callback_query.from_user.id, open("20.jpg", "rb"))

@dp.callback_query_handler(lambda c: c.data == "zad21")
async def zad21(callback_query: types.CallbackQuery):
	await bot.answer_callback_query(callback_query.id)
	cursor.execute(f"UPDATE user SET page=21 WHERE id={callback_query.from_user.id}")
	conn.commit()
	cursor.execute(f"SELECT text FROM var WHERE id=21")
	text = cursor.fetchone()[0]
	await callback_query.message.delete()
	await bot.send_message(callback_query.from_user.id, text)
	await bot.send_photo(callback_query.from_user.id, open("21.jpg", "rb"))

@dp.callback_query_handler(lambda c: c.data == "zad22")
async def zad22(callback_query: types.CallbackQuery):
	await bot.answer_callback_query(callback_query.id)
	cursor.execute(f"UPDATE user SET page=22 WHERE id={callback_query.from_user.id}")
	conn.commit()
	cursor.execute(f"SELECT text FROM var WHERE id=22")
	text = cursor.fetchone()[0]
	await callback_query.message.delete()
	await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(lambda c: c.data == "zad23")
async def zad23(callback_query: types.CallbackQuery):
	await bot.answer_callback_query(callback_query.id)
	cursor.execute(f"UPDATE user SET page=23 WHERE id={callback_query.from_user.id}")
	conn.commit()
	cursor.execute(f"SELECT text FROM var WHERE id=23")
	text = cursor.fetchone()[0]
	await callback_query.message.delete()
	await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(lambda c: c.data == "zad24")
async def zad24(callback_query: types.CallbackQuery):
	await bot.answer_callback_query(callback_query.id)
	cursor.execute(f"UPDATE user SET page=24 WHERE id={callback_query.from_user.id}")
	conn.commit()
	cursor.execute(f"SELECT text FROM var WHERE id=24")
	text = cursor.fetchone()[0]
	await callback_query.message.delete()
	await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(lambda c: c.data == "zad25")
async def zad25(callback_query: types.CallbackQuery):
	await bot.answer_callback_query(callback_query.id)
	cursor.execute(f"UPDATE user SET page=25 WHERE id={callback_query.from_user.id}")
	conn.commit()
	cursor.execute(f"SELECT text FROM var WHERE id=25")
	text = cursor.fetchone()[0]
	await callback_query.message.delete()
	await bot.send_message(callback_query.from_user.id, text)
	await bot.send_photo(callback_query.from_user.id, open("25.jpg", "rb"))

@dp.callback_query_handler(lambda c: c.data == "zad26")
async def zad26(callback_query: types.CallbackQuery):
	await bot.answer_callback_query(callback_query.id)
	cursor.execute(f"UPDATE user SET page=26 WHERE id={callback_query.from_user.id}")
	conn.commit()
	cursor.execute(f"SELECT text FROM var WHERE id=26")
	text = cursor.fetchone()[0]
	await callback_query.message.delete()
	await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(lambda c: c.data == "zad27")
async def zad27(callback_query: types.CallbackQuery):
	await bot.answer_callback_query(callback_query.id)
	cursor.execute(f"UPDATE user SET page=27 WHERE id={callback_query.from_user.id}")
	conn.commit()
	cursor.execute(f"SELECT text FROM var WHERE id=27")
	text = cursor.fetchone()[0]
	await callback_query.message.delete()
	await bot.send_message(callback_query.from_user.id, text)
	await bot.send_photo(callback_query.from_user.id, open("27.jpg", "rb"))

@dp.callback_query_handler(lambda c: c.data == "zad28")
async def zad28(callback_query: types.CallbackQuery):
	await bot.answer_callback_query(callback_query.id)
	cursor.execute(f"UPDATE user SET page=28 WHERE id={callback_query.from_user.id}")
	conn.commit()
	cursor.execute(f"SELECT text FROM var WHERE id=28")
	text = cursor.fetchone()[0]
	await callback_query.message.delete()
	await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(lambda c: c.data == "zad29")
async def zad29(callback_query: types.CallbackQuery):
	await bot.answer_callback_query(callback_query.id)
	cursor.execute(f"UPDATE user SET page=29 WHERE id={callback_query.from_user.id}")
	conn.commit()
	cursor.execute(f"SELECT text FROM var WHERE id=29")
	text = cursor.fetchone()[0]
	await callback_query.message.delete()
	await bot.send_message(callback_query.from_user.id, text)

@dp.callback_query_handler(lambda c: c.data == "zad30")
async def zad30(callback_query: types.CallbackQuery):
	await bot.answer_callback_query(callback_query.id)
	cursor.execute(f"UPDATE user SET page=30 WHERE id={callback_query.from_user.id}")
	conn.commit()
	cursor.execute(f"SELECT text FROM var WHERE id=30")
	text = cursor.fetchone()[0]
	await callback_query.message.delete()
	await bot.send_message(callback_query.from_user.id, text)
	await bot.send_photo(callback_query.from_user.id, open("30.jpg", "rb"))

@dp.message_handler()
async def messages(message: types.Message):
	cursor.execute(f"SELECT page FROM user WHERE id={message.from_user.id}")
	page = cursor.fetchone()[0]
	if page == 1:
		cursor.execute(f"SELECT answer FROM var WHERE id={page}")
		answer = cursor.fetchone()[0]
		if answer == message.text:
			await bot.send_message(message.from_user.id, f"Правильно")
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var1_keyboard)
		else:
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var1_keyboard)
			await bot.send_message(message.from_user.id, f"Ответ неверный\nПравильный ответ:{answer}")
		await bot.send_message(5609089222, f"{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username}\nВариант 1 Задание 1\nОтвет:{message.text}\nПравильный ответ:{answer}")
	if page == 2:
		cursor.execute(f"SELECT answer FROM var WHERE id={page}")
		answer = cursor.fetchone()[0]
		if answer == message.text:
			await bot.send_message(message.from_user.id, f"Правильно")
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var1_keyboard)
		else:
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var1_keyboard)
			await bot.send_message(message.from_user.id, f"Ответ неверный\nПравильный ответ:{answer}")
		await bot.send_message(5609089222, f"{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username}\nВариант 1 Задание 2\nОтвет:{message.text}\nПравильный ответ:{answer}")
	if page == 3:
		cursor.execute(f"SELECT answer FROM var WHERE id={page}")
		answer = cursor.fetchone()[0]
		if answer == message.text:
			await bot.send_message(message.from_user.id, f"Правильно")
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var1_keyboard)
		else:
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var1_keyboard)
			await bot.send_message(message.from_user.id, f"Ответ неверный\nПравильный ответ:{answer}")
		await bot.send_message(5609089222, f"{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username}\nВариант 1 Задание 3\nОтвет:{message.text}\nПравильный ответ:{answer}")
	if page == 4:
		cursor.execute(f"SELECT answer FROM var WHERE id={page}")
		answer = cursor.fetchone()[0]
		if answer == message.text:
			await bot.send_message(message.from_user.id, f"Правильно")
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var1_keyboard)
		else:
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var1_keyboard)
			await bot.send_message(message.from_user.id, f"Ответ неверный\nПравильный ответ:{answer}")
		await bot.send_message(5609089222, f"{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username}\nВариант 1 Задание 4\nОтвет:{message.text}\nПравильный ответ:{answer}")
	if page == 5:
		cursor.execute(f"SELECT answer FROM var WHERE id={page}")
		answer = cursor.fetchone()[0]
		if answer == message.text:
			await bot.send_message(message.from_user.id, f"Правильно")
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var1_keyboard)
		else:
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var1_keyboard)
			await bot.send_message(message.from_user.id, f"Ответ неверный\nПравильный ответ:{answer}")
		await bot.send_message(5609089222, f"{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username}\nВариант 1 Задание 5\nОтвет:{message.text}\nПравильный ответ:{answer}")
	if page == 6:
		cursor.execute(f"SELECT answer FROM var WHERE id={page}")
		answer = cursor.fetchone()[0]
		if answer == message.text:
			await bot.send_message(message.from_user.id, f"Правильно")
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var1_keyboard)
		else:
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var1_keyboard)
			await bot.send_message(message.from_user.id, f"Ответ неверный\nПравильный ответ:{answer}")
		await bot.send_message(5609089222, f"{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username}\nВариант 1 Задание 6\nОтвет:{message.text}\nПравильный ответ:{answer}")
	if page == 7:
		cursor.execute(f"SELECT answer FROM var WHERE id={page}")
		answer = cursor.fetchone()[0]
		if answer == message.text:
			await bot.send_message(message.from_user.id, f"Правильно")
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var1_keyboard)
		else:
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var1_keyboard)
			await bot.send_message(message.from_user.id, f"Ответ неверный\nПравильный ответ:{answer}")
		await bot.send_message(5609089222, f"{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username}\nВариант 1 Задание 7\nОтвет:{message.text}\nПравильный ответ:{answer}")
	if page == 8:
		cursor.execute(f"SELECT answer FROM var WHERE id={page}")
		answer = cursor.fetchone()[0]
		if answer == message.text:
			await bot.send_message(message.from_user.id, f"Правильно")
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var1_keyboard)
		else:
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var1_keyboard)
			await bot.send_message(message.from_user.id, f"Ответ неверный\nПравильный ответ:{answer}")
		await bot.send_message(5609089222, f"{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username}\nВариант 1 Задание 8\nОтвет:{message.text}\nПравильный ответ:{answer}")
	if page == 9:
		cursor.execute(f"SELECT answer FROM var WHERE id={page}")
		answer = cursor.fetchone()[0]
		if answer == message.text:
			await bot.send_message(message.from_user.id, f"Правильно")
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var1_keyboard)
		else:
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var1_keyboard)
			await bot.send_message(message.from_user.id, f"Ответ неверный\nПравильный ответ:{answer}")
		await bot.send_message(5609089222, f"{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username}\nВариант 1 Задание 9\nОтвет:{message.text}\nПравильный ответ:{answer}")
	if page == 10:
		cursor.execute(f"SELECT answer FROM var WHERE id={page}")
		answer = cursor.fetchone()[0]
		if answer == message.text:
			await bot.send_message(message.from_user.id, f"Правильно")
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var1_keyboard)
		else:
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var1_keyboard)
			await bot.send_message(message.from_user.id, f"Ответ неверный\nПравильный ответ:{answer}")
		await bot.send_message(5609089222, f"{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username}\nВариант 1 Задание 10\nОтвет:{message.text}\nПравильный ответ:{answer}")
	if page == 11:
		cursor.execute(f"SELECT answer FROM var WHERE id={page}")
		answer = cursor.fetchone()[0]
		if answer == message.text:
			await bot.send_message(message.from_user.id, f"Правильно")
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var2_keyboard)
		else:
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var2_keyboard)
			await bot.send_message(message.from_user.id, f"Ответ неверный\nПравильный ответ:{answer}")
		await bot.send_message(5609089222, f"{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username}\nВариант 2 Задание 1\nОтвет:{message.text}\nПравильный ответ:{answer}")
	if page == 12:
		cursor.execute(f"SELECT answer FROM var WHERE id={page}")
		answer = cursor.fetchone()[0]
		if answer == message.text:
			await bot.send_message(message.from_user.id, f"Правильно")
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var2_keyboard)
		else:
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var2_keyboard)
			await bot.send_message(message.from_user.id, f"Ответ неверный\nПравильный ответ:{answer}")
		await bot.send_message(5609089222, f"{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username}\nВариант 2 Задание 2\nОтвет:{message.text}\nПравильный ответ:{answer}")
	if page == 13:
		cursor.execute(f"SELECT answer FROM var WHERE id={page}")
		answer = cursor.fetchone()[0]
		if answer == message.text:
			await bot.send_message(message.from_user.id, f"Правильно")
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var2_keyboard)
		else:
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var2_keyboard)
			await bot.send_message(message.from_user.id, f"Ответ неверный\nПравильный ответ:{answer}")
		await bot.send_message(5609089222, f"{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username}\nВариант 2 Задание 3\nОтвет:{message.text}\nПравильный ответ:{answer}")
	if page == 14:
		cursor.execute(f"SELECT answer FROM var WHERE id={page}")
		answer = cursor.fetchone()[0]
		if answer == message.text:
			await bot.send_message(message.from_user.id, f"Правильно")
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var2_keyboard)
		else:
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var2_keyboard)
			await bot.send_message(message.from_user.id, f"Ответ неверный\nПравильный ответ:{answer}")
		await bot.send_message(5609089222, f"{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username}\nВариант 2 Задание 4\nОтвет:{message.text}\nПравильный ответ:{answer}")
	if page == 15:
		cursor.execute(f"SELECT answer FROM var WHERE id={page}")
		answer = cursor.fetchone()[0]
		if answer == message.text:
			await bot.send_message(message.from_user.id, f"Правильно")
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var2_keyboard)
		else:
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var2_keyboard)
			await bot.send_message(message.from_user.id, f"Ответ неверный\nПравильный ответ:{answer}")
		await bot.send_message(5609089222, f"{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username}\nВариант 2 Задание 5\nОтвет:{message.text}\nПравильный ответ:{answer}")
	if page == 16:
		cursor.execute(f"SELECT answer FROM var WHERE id={page}")
		answer = cursor.fetchone()[0]
		if answer == message.text:
			await bot.send_message(message.from_user.id, f"Правильно")
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var2_keyboard)
		else:
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var2_keyboard)
			await bot.send_message(message.from_user.id, f"Ответ неверный\nПравильный ответ:{answer}")
		await bot.send_message(5609089222, f"{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username}\nВариант 2 Задание 6\nОтвет:{message.text}\nПравильный ответ:{answer}")
	if page == 17:
		cursor.execute(f"SELECT answer FROM var WHERE id={page}")
		answer = cursor.fetchone()[0]
		if answer == message.text:
			await bot.send_message(message.from_user.id, f"Правильно")
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var2_keyboard)
		else:
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var2_keyboard)
			await bot.send_message(message.from_user.id, f"Ответ неверный\nПравильный ответ:{answer}")
		await bot.send_message(5609089222, f"{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username}\nВариант 2 Задание 7\nОтвет:{message.text}\nПравильный ответ:{answer}")
	if page == 18:
		cursor.execute(f"SELECT answer FROM var WHERE id={page}")
		answer = cursor.fetchone()[0]
		if answer == message.text:
			await bot.send_message(message.from_user.id, f"Правильно")
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var2_keyboard)
		else:
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var2_keyboard)
			await bot.send_message(message.from_user.id, f"Ответ неверный\nПравильный ответ:{answer}")
		await bot.send_message(5609089222, f"{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username}\nВариант 2 Задание 8\nОтвет:{message.text}\nПравильный ответ:{answer}")
	if page == 19:
		cursor.execute(f"SELECT answer FROM var WHERE id={page}")
		answer = cursor.fetchone()[0]
		if answer == message.text:
			await bot.send_message(message.from_user.id, f"Правильно")
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var2_keyboard)
		else:
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var2_keyboard)
			await bot.send_message(message.from_user.id, f"Ответ неверный\nПравильный ответ:{answer}")
		await bot.send_message(5609089222, f"{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username}\nВариант 2 Задание 9\nОтвет:{message.text}\nПравильный ответ:{answer}")
	if page == 20:
		cursor.execute(f"SELECT answer FROM var WHERE id={page}")
		answer = cursor.fetchone()[0]
		if answer == message.text:
			await bot.send_message(message.from_user.id, f"Правильно")
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var2_keyboard)
		else:
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var2_keyboard)
			await bot.send_message(message.from_user.id, f"Ответ неверный\nПравильный ответ:{answer}")
		await bot.send_message(5609089222, f"{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username}\nВариант 2 Задание 10\nОтвет:{message.text}\nПравильный ответ:{answer}")
	if page == 21:
		cursor.execute(f"SELECT answer FROM var WHERE id={page}")
		answer = cursor.fetchone()[0]
		if answer == message.text:
			await bot.send_message(message.from_user.id, f"Правильно")
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var3_keyboard)
		else:
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var3_keyboard)
			await bot.send_message(message.from_user.id, f"Ответ неверный\nПравильный ответ:{answer}")
		await bot.send_message(5609089222, f"{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username}\nВариант 3 Задание 1\nОтвет:{message.text}\nПравильный ответ:{answer}")
	if page == 22:
		cursor.execute(f"SELECT answer FROM var WHERE id={page}")
		answer = cursor.fetchone()[0]
		if answer == message.text:
			await bot.send_message(message.from_user.id, f"Правильно")
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var3_keyboard)
		else:
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var3_keyboard)
			await bot.send_message(message.from_user.id, f"Ответ неверный\nПравильный ответ:{answer}")
		await bot.send_message(5609089222, f"{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username}\nВариант 3 Задание 2\nОтвет:{message.text}\nПравильный ответ:{answer}")
	if page == 23:
		cursor.execute(f"SELECT answer FROM var WHERE id={page}")
		answer = cursor.fetchone()[0]
		if answer == message.text:
			await bot.send_message(message.from_user.id, f"Правильно")
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var3_keyboard)
		else:
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var3_keyboard)
			await bot.send_message(message.from_user.id, f"Ответ неверный\nПравильный ответ:{answer}")
		await bot.send_message(5609089222, f"{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username}\nВариант 3 Задание 3\nОтвет:{message.text}\nПравильный ответ:{answer}")
	if page == 24:
		cursor.execute(f"SELECT answer FROM var WHERE id={page}")
		answer = cursor.fetchone()[0]
		if answer == message.text:
			await bot.send_message(message.from_user.id, f"Правильно")
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var3_keyboard)
		else:
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var3_keyboard)
			await bot.send_message(message.from_user.id, f"Ответ неверный\nПравильный ответ:{answer}")
		await bot.send_message(5609089222, f"{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username}\nВариант 3 Задание 4\nОтвет:{message.text}\nПравильный ответ:{answer}")
	if page == 25:
		cursor.execute(f"SELECT answer FROM var WHERE id={page}")
		answer = cursor.fetchone()[0]
		if answer == message.text:
			await bot.send_message(message.from_user.id, f"Правильно")
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var3_keyboard)
		else:
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var3_keyboard)
			await bot.send_message(message.from_user.id, f"Ответ неверный\nПравильный ответ:{answer}")
		await bot.send_message(5609089222, f"{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username}\nВариант 3 Задание 5\nОтвет:{message.text}\nПравильный ответ:{answer}")
	if page == 26:
		cursor.execute(f"SELECT answer FROM var WHERE id={page}")
		answer = cursor.fetchone()[0]
		if answer == message.text:
			await bot.send_message(message.from_user.id, f"Правильно")
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var3_keyboard)
		else:
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var3_keyboard)
			await bot.send_message(message.from_user.id, f"Ответ неверный\nПравильный ответ:{answer}")
		await bot.send_message(5609089222, f"{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username}\nВариант 3 Задание 6\nОтвет:{message.text}\nПравильный ответ:{answer}")
	if page == 27:
		cursor.execute(f"SELECT answer FROM var WHERE id={page}")
		answer = cursor.fetchone()[0]
		if answer == message.text:
			await bot.send_message(message.from_user.id, f"Правильно")
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var3_keyboard)
		else:
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var3_keyboard)
			await bot.send_message(message.from_user.id, f"Ответ неверный\nПравильный ответ:{answer}")
		await bot.send_message(5609089222, f"{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username}\nВариант 3 Задание 7\nОтвет:{message.text}\nПравильный ответ:{answer}")
	if page == 28:
		cursor.execute(f"SELECT answer FROM var WHERE id={page}")
		answer = cursor.fetchone()[0]
		if answer == message.text:
			await bot.send_message(message.from_user.id, f"Правильно")
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var3_keyboard)
		else:
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var3_keyboard)
			await bot.send_message(message.from_user.id, f"Ответ неверный\nПравильный ответ:{answer}")
		await bot.send_message(5609089222, f"{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username}\nВариант 3 Задание 8\nОтвет:{message.text}\nПравильный ответ:{answer}")
	if page == 29:
		cursor.execute(f"SELECT answer FROM var WHERE id={page}")
		answer = cursor.fetchone()[0]
		if answer == message.text:
			await bot.send_message(message.from_user.id, f"Правильно")
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var3_keyboard)
		else:
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var3_keyboard)
			await bot.send_message(message.from_user.id, f"Ответ неверный\nПравильный ответ:{answer}")
		await bot.send_message(5609089222, f"{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username}\nВариант 3 Задание 9\nОтвет:{message.text}\nПравильный ответ:{answer}")
	if page == 30:
		cursor.execute(f"SELECT answer FROM var WHERE id={page}")
		answer = cursor.fetchone()[0]
		if answer == message.text:
			await bot.send_message(message.from_user.id, f"Правильно")
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var3_keyboard)
		else:
			await bot.send_message(message.from_user.id, "выберите задание:", reply_markup=Var3_keyboard)
			await bot.send_message(message.from_user.id, f"Ответ неверный\nПравильный ответ:{answer}")
		await bot.send_message(5609089222, f"{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username}\nВариант 3 Задание 10\nОтвет:{message.text}\nПравильный ответ:{answer}")
	


if __name__ == "__main__":#Записываем конструкцию
	print("Bot Connected")#Выводим сообщение о начале работы
	executor.start_polling(dp)#Обращаемся к объкету executor и обращаемся к методу start_polling() и передаем в параметр объект