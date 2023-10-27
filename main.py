import aiogram
from aiogram import Bot, Dispatcher, types
from aiogram import F
import aiogram.types
from bot_token import token
import asyncio
from asyncio import sleep
from parc_group_stage import all_stat_group_stage, stat_one_team_group_stage, set_teams
one_or_zero_one_inf = False

bot = Bot(token)
dp = Dispatcher()

@dp.message(commands=["start"])
async def on_message(message: aiogram.types.Message):
    await bot.send_message(message.from_user.id, f"hi, {message.from_user.last_name} {message.from_user.first_name} !. Я - бот Номадова и помогу разобраться в Инте!")
    await sleep(1)
    kb = [[aiogram.types.KeyboardButton(text="Статистика всех команд в группе")], [aiogram.types.KeyboardButton(text="Статистика команды в группе")]]
    keyboard = aiogram.types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kb, input_field_placeholder="Нажми кнопки для получения доступной боту информации")
    await message.answer("Что ты хотел бы узнать", reply_markup=keyboard)

    
@dp.message(F.text.lower() == "статистика всех команд в группе")
async def with_puree(message: types.Message):
    await bot.send_message(message.from_user.id, f"{all_stat_group_stage()}")
    await bot.send_message(message.from_user.id, f"Что-то еще? Я могу показать статистику по твоей любимой команде.")

@dp.message(F.text.lower() == "статистика команды в группе")
async def one_inf(message: types.Message):
    await bot.send_message(message.from_user.id, f"Напиши название команды")
        

@dp.message_handler(content_types=["text"])
async def one_inf_or_ralse(message: types.Message):
    print(message.text)
    if message.text not in set_teams:
        b = ""
        for x in set_teams:
            b+=f"{x}\n"
        await bot.send_message(message.from_user.id, f"К сожалению, такой тимы нет(\nВведи команду из этого списка:{b}")
    else:
        await bot.send_message(message.from_user.id, f"{stat_one_team_group_stage(message.text)}")
        await bot.send_message(message.from_user.id, f"Что-то еще?")





async def main():
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main())


