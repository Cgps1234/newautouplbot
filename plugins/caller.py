import os
import sys
from pyrogram import Client as bot
from constant import buttom
from master.buttom import *
from modules import appx_master
from constant import msg
from config import Config
from master import key
##Code Written By @ItsMeMaster
##Code Written By @ItsMeMaster

@bot.on_callback_query()
async def callback_handler(bot, callback_query):
    data = callback_query.data
    call_msg = callback_query.message
    a = callback_query.answer
    if call_msg.chat.id != Config.ADMIN_ID:
        return await a("You are not authorized to use this bot", show_alert=True)
    if data == "home":
        await call_msg.edit_reply_markup(buttom.home())
    elif data == "close":
        await call_msg.delete()
    elif data == "TUTORIAL_VIDEO":
        await bot.send_video(call_msg.chat.id, video="https://files.catbox.moe/jx3jkx.mp4", caption="✅<b>This is the Tutorial Video for the bot.</b>")
    elif data == "restart":
        await a("🔄 Restarting bot... 🚀", show_alert=True)
        os.execl(sys.executable, sys.executable, *sys.argv)
    elif data.startswith("abatch_"):
        await key.handle_app_paid(bot, data, call_msg, a)
    elif data == "delete_batch":
        x = await show_all_batches_buttom_delete(call_msg.chat.id)
        if x:
            await call_msg.edit_reply_markup(x)
        else:
            await a(BATCH_NOT_FOUND, show_alert=True)
    elif data == "show_batch":
        x = await show_all_batches_buttom(call_msg.chat.id)
        if x:
            await call_msg.edit_reply_markup(x)
        else:
            await a(BATCH_NOT_FOUND, show_alert=True)
    elif data == "back":
        await call_msg.edit_reply_markup(buttom.home())
    elif data == "manage_batch":
        x = await show_all_batches_buttom_manage(call_msg.chat.id)
        if x:
            await call_msg.edit_reply_markup(x)
        else:
            await a(BATCH_NOT_FOUND, show_alert=True)
    elif data.startswith("appx_"):
        api = data.split("_")[1]
        await a(f"You Selected {api}", show_alert=True)
        await appx_master.add_batch(bot, call_msg, f"https://{api}")
    elif data.startswith("dbatch_"):
        course_id = data.split("_")[1]
        await a("Deleting batch from database...", show_alert=True)
        await call_msg.delete()
        await delete_batch(bot, call_msg.chat.id, int(course_id))
    elif data.startswith("vbatch_"):
        course_id = data.split("_")[1]
        await a("Fetching batch statistics...", show_alert=True)
        await get_batch_statistics(bot, call_msg.chat.id, int(course_id))
    elif data.startswith("mbatch_"):
        course_id = data.split("_")[1]
        await call_msg.delete()
        await a("Managing batch settings...", show_alert=True)
        await manage_batch(bot, call_msg, int(course_id))

    elif data == "appxlist":
        await a("Loading Apps...Select an alphabet to see the apps", show_alert=True)
        caption = f"{msg.APP.format(Config.USERLINK)}\n<b>__Welcome! Select an alphabet to see the apps:__</b>"
        await call_msg.edit_caption(caption=caption, reply_markup = key.gen_alpha_paid_kb())
    elif data.startswith("alphapaid_"):
        letter = data.split('_')[1]
        markup, current_page, total_pages = await key.gen_apps_paid_kb(letter)
        await call_msg.edit_caption(caption=f"{msg.APP.format(Config.USERLINK)}\n__Apps starting with__  {letter}:\n\n(Page: {current_page}/{total_pages})",reply_markup=markup)
    elif data.startswith("forwardpaid_"):
        parts = data.split('_')[1:]
        letter , page = parts[0], int(parts[1])
        await key.appx_page_paid(call_msg, letter, page)
    elif data.startswith("previouspaid_"):
        parts = data.split('_')[1:]
        letter , page = parts[0], int(parts[1])
        await key.appx_page_paid(call_msg, letter, page)
