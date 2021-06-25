from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
	Lasiya2 = InlineKeyboardMarkup([
		[InlineKeyboardButton("Tutorial", url="https://t.me/Fallenflower_of_Telegram/11")],
		 ])
	help_image = "https://telegra.ph/file/d87cfafd042561735d129.jpg"
	await message.reply_photo(help_image,  caption="**♔Help**\n• Just Send your Youtube video url⛓ \n• And i will give Method list to select your choice😋",reply_markup=Lasiya2)
