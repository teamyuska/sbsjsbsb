from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import BOT_USERNAME, BOT_NAME as bot
from helpers.filters import command, other_filters2
# EfsaneMusicVaves tarafından düzenlendi. 

@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, message: Message):
                await message.reply_photo(
                "https://telegra.ph/file/7016b36478a0b3680a0cc.jpg",
                caption=(f"""**👋SOA MUSİC Sizi Salamlayır👋🏻

ℹ️ Mən səsli söhbətlərdə musiqi oxuya bilən bir botam

✅BOTUN BÜTÜN QAYDALARINI ÖYRƏNMƏK ÜÇÜN BÜTÜN ƏMİRLƏRİMƏ BAS✅"""),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕Məni Qrupa Əlavə Et➕", url=f"https://t.me/soamusicbot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔊Asistant", url="https://t.me/SoaAsistant"
                    ),
                    InlineKeyboardButton(
                        "🆘Support", url="https://t.me/YuskaSup"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⚡Əmrlər" , callback_data= "cbbilgi"
                    ),
                    InlineKeyboardButton(
                        "⭐Kanal", url=f"https://t.me/YuskaProject"
                    )
                ]
                
           ]
        ),
    )
  


@Client.on_message(command(["bilgi", f"bilgi@{BOT_USERNAME}"]))
async def bilgi(_, message: Message):
      await message.reply_text(" ❗ Qeyd:\n Botun aktiv işləməsi üçün bu üç yetkini vermək lazımdır ⬇️:\n- Mesaj silmə yetkisi,\n- Bağlantı ilə dəvət etmə yetkisi,\n- Səsli səhbəti yönətmə yetkisi.", 
      reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "⚡Bütün Əmrlər", callback_data="herkes")
                 ],[                     
                     InlineKeyboardButton(
                         "🆘Admin Əmrləri", callback_data="admin")
                 ],[
                     InlineKeyboardButton(
                         "🔙Geri", callback_data="cbstart")
                 ],[
                     InlineKeyboardButton(
                         "🇦🇿Sahibim", url="https://t.me/g8zl8adam")
                 ]
             ]
         )
    )


@Client.on_callback_query(filters.regex("cbbilgi"))
async def cbbilgi(_, query: CallbackQuery):
    await query.edit_message_text(" ❗ Qeyd:\nBotun Aktiv İşləməsi Üçün Bu Üç Yetkini Vermək Lazımdır ⬇️\n- Mesaj Silmə Yetkisi.\n- Bağlantı İlə Dəvət Etmə Yetkisi.\n- Səsli Söhbəti Yönətmə Yetkisi.", 
    reply_markup=InlineKeyboardMarkup(
           [
               [
                     InlineKeyboardButton(
                         "⚡Bütün Əmrlər", callback_data="herkes")
                 ],[                     
                     InlineKeyboardButton(
                         "🆘Admin Əmrləri", callback_data="admin")
                 ],[
                     InlineKeyboardButton(
                         "🔙Geri", callback_data="cbstart")
                 ],[
                     InlineKeyboardButton(
                         "🇦🇿Sahibim", url="https://t.me/g8zl8adam")
                 ]
             ]
     ))


@Client.on_callback_query(filters.regex("herkes"))
async def herkes(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>\nBu botun hərkəs üçün əmr menyusu . 
    » /vplay =>  İstədiyiniz Videoları Sürətli Bir Şəkildə Axtarın. \n» /song => İstədiyiniz Musiqi Sürətli Bir Şəkildə Axtarın. \n» /play => Musiqi Oxutmaq Üçün Youtube Url'sinə Və Ya Musiqi Dosyasına Yanıt Verin. """,
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "🇦🇿Sahibim", url="https://t.me/g8zl8adam")
                 ],
                 [
                     InlineKeyboardButton(
                         "🔙Geri", callback_data="cbbilgi")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("admin"))
async def admin(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Salam {query.from_user.mention}!\nBu botun adminlər üçün əmr menyusu 🤩\n\n ▶️ /resume - Musiqi oxutmağa davam et\n 🔄 /skip - Sıraya alınmış musiqiyə keç\n ⏹ /end - Musiqi oxumanı dayandır\n 🔼 /promote - Botun sadəcə yönətici üçün olan əmrlərini istifadə üçün istifadəçiyə yetki ver\n 🔽 /demote - Botun yönətici əmrlərini istifadə edən istifadəçinin yetkisini al\n\n ⚪ /asistan - Musiqi asistanı qrupunuza qoşulur.\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "🇦🇿Sahibim", url="https://t.me/g8zl8adam")
                 ],
                 [
                     InlineKeyboardButton(
                         "️🔙Geri", callback_data="cbbilgi")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(f"""**👋SOA MUSİC Sizi Salamlayır👋🏻

ℹ️ Mən səsli söhbətlərdə musiqi oxuya bilən bir botam

✅BOTUN BÜTÜN QAYDALARINI ÖYRƏNMƏK ÜÇÜN BÜTÜN ƏMİRLƏRİMƏ BAS**""",
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕Məni Qrupa Əlavə Et➕", url=f"https://t.me/soamusicbot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔊Asistant", url="https://t.me/SoaAsistant"
                    ),
                    InlineKeyboardButton(
                        "🆘Support", url="https://t.me/YuskaSup"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⚡Əmrlər" , callback_data= "cbbilgi"
                    ),
                    InlineKeyboardButton(
                        "⭐Kanal", url=f"https://t.me/YuskaProject"
                    )
                ]
                
           ]
        ),
    )
