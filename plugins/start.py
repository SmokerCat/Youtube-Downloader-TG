from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    Lasiya = InlineKeyboardMarkup([
        
        [InlineKeyboardButton("Creator ❤", url="https://t.me/Readmeab")],
        [InlineKeyboardButton(
            "Report Problems 📋", url="https://t.me/CatX_bot_hub")],
        [InlineKeyboardButton(
            "Bot Updates ⚙",url="https://t.me/Cat_Telegram_Projects")]
    ])
    thumbnail_url = "https://telegra.ph/file/a488092b0f602ae43bbf0.jpg"
    await message.reply_photo(thumbnail_url, caption=f"Hellow <b>{message.from_user.first_name}</b>\n\n<b>I ᴀᴍ ᴀ Sɪᴍᴘʟᴇ Yᴏᴜᴛᴜʙᴇ ᴅᴏᴡɴʟᴏᴀᴅᴇʀ Bᴏᴛ Cᴏᴍᴘʟᴇᴛᴇ ʟʏ Wʀɪᴛᴛᴇɴ ɪɴ Pʏᴛʜᴏɴ🤖...</b>\n\nFᴏʀ Mᴏʀᴇ Hᴇʟᴘ ʜɪᴛ /help Bᴜᴛᴛᴏɴ✅<\b>\n\nTʜᴀɴᴋ Yᴏᴜ Fᴏʀ Usɪɴɢ Oᴜʀ Bᴏᴛ 🤗 Bʏ CatX_bots♥️", reply_markup=Lasiya)
    raise StopPropagation
