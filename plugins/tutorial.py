from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(Filters.command(["tute"]))
async def start(client, message):
    await message.reply_text("To Use @Yourtube_cat_bot Just do it. ⚜️ Go ⚜️ button to go to Tutorial.. 🥳",
                             reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("⚜️ Go ⚜️", url="https://t.me/CatX_bot_hub")]
        ]))
    
