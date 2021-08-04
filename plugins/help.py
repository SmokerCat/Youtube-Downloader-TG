from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
	Lasiya2 = InlineKeyboardMarkup([
		[InlineKeyboardButton("ѕυρρσят", url="https://t.me/CatX_bot_hub")],
		 ])
	help_image = "https://telegra.ph/file/d87cfafd042561735d129.jpg"
	await message.reply_photo(help_image,  caption="**♔Help**\n• Copy Your Desired Video/Audio link from [Youtube](www.youtube.com) . \n• Send Link here..nd Select the Audio Quality from below buttons..After some time it get upload to here.. \n• For any help click below support button😊.. \n• Thank You For Using Our Service ",reply_markup=Lasiya2)
