from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(Filters.command(["tute"]))
async def start(client, message):
    await message.reply_text("To Use @Yourtube_cat_bot in Telegram📻 ⚜️ Go ⚜️ button to go youtube directly. 🥳",
                             reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("⚜️ Go ⚜️", url="https://t.me/Fallenflower_of_Telegram/11")]
        ]))
    
