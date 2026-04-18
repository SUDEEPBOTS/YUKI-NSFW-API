import asyncio
import aiohttp
import os
from pyrogram import Client, filters
from pyrogram.types import Message
from PIL import Image

# --- CONFIGURATION ---
API_ID = 38674666  # Tera API ID
API_HASH = "b4f0fbf8fb560c4bc9e7b9f3698e474c" # Tera API Hash
BOT_TOKEN = "8154444104:AAEI8YsZTsheFSdLL2ej0"

# EK-DUM SAHI ENDPOINT: /check
NSFW_API_URL = "https://suspended-twisted-hans-acquisitions.trycloudflare.com/check" 

app = Client("nsfw_test_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

async def check_nsfw(file_path):
    """API pe file bhej kar result nikalne ke liye"""
    try:
        async with aiohttp.ClientSession() as session:
            with open(file_path, 'rb') as f:
                data = aiohttp.FormData()
                data.add_field('file', f)
                async with session.post(NSFW_API_URL, data=data) as resp:
                    if resp.status == 200:
                        return await resp.json()
                    else:
                        return {"error": f"API Error: {resp.status}"}
    except Exception as e:
        return {"error": str(e)}

@app.on_message(filters.private & (filters.sticker | filters.photo))
async def nsfw_handler(client, message: Message):
    m = await message.reply_text("🔎 **Scanning... Sabr karo...**")
    
    # File download path
    file_path = await message.download()
    
    # Agar sticker hai (WebP), toh use JPG mein convert karna padega kyunki NudeNet ko WebP pasand nahi
    if message.sticker:
        img = Image.open(file_path).convert("RGB")
        new_file_path = file_path + ".jpg"
        img.save(new_file_path, "JPEG")
        os.remove(file_path) # Purana webp delete kar do
        file_path = new_file_path

    # API Check
    result = await check_nsfw(file_path)
    
    if "error" in result:
        await m.edit_text(f"❌ **Error:** {result['error']}")
    else:
        # JSON parsing as per your OpenAPI schema
        is_nsfw = result.get("nsfw", False)
        score = result.get("score", 0.0) * 100
        labels = result.get("labels", [])
        
        status_text = "🔞 **NSFW DETECTED**" if is_nsfw else "✅ **SAFE**"
        labels_text = ", ".join(labels) if labels else "None"
        
        report = (
            f"📊 **NSFW Scan Report**\n"
            f"━━━━━━━━━━━━━━━━━━━\n"
            f"📍 **Status:** {status_text}\n"
            f"📈 **Confidence:** {score:.2f}%\n"
            f"🏷 **Labels:** `{labels_text}`\n"
            f"━━━━━━━━━━━━━━━━━━━"
        )
        await m.edit_text(report)

    # Cleanup: File delete karo scan ke baad taaki VPS full na ho
    if os.path.exists(file_path):
        os.remove(file_path)

print("✅ Test Bot Started! Send me a photo or sticker in DM.")
app.run()
