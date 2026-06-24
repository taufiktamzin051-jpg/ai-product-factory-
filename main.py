import os
import time
import tweepy
import requests
from google import genai
from google.genai import errors

# 1. Inisialisasi Gemini (Pastikan API Key sudah di GitHub Secrets)
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# 2. Fungsi Posting Twitter
def post_to_twitter(text):
    auth = tweepy.OAuth1UserHandler(
        os.getenv("TWITTER_CONSUMER_KEY"), os.getenv("TWITTER_CONSUMER_SECRET"),
        os.getenv("TWITTER_ACCESS_TOKEN"), os.getenv("TWITTER_ACCESS_SECRET")
    )
    api = tweepy.API(auth)
    api.update_status(text)
    print("✅ Twitter: Tweet berhasil diposting!")

# 3. Fungsi Upload Gumroad
def upload_ke_gumroad(title, description):
    print(f"🔄 Gumroad: Mengunggah produk '{title}'...")
    url = "https://api.gumroad.com/v2/products"
    data = {
        "access_token": os.getenv("GUMROAD_ACCESS_TOKEN"),
        "product[name]": title,
        "product[description]": description,
        "product[price]": 0,
        "product[published]": "true"
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("✅ Gumroad: Produk berhasil diunggah!")
    else:
        print(f"❌ Gumroad: Gagal! Error: {response.text}")
        raise Exception("Upload Gumroad Gagal")

# 4. Fungsi Utama
def run_factory():
    print("🚀 Pabrik mulai beroperasi...")
    
    # Generate Judul
    judul_res = client.models.generate_content(
        model="gemini-2.0-flash", 
        contents="Generate a high-converting digital product title for the US market in professional English."
    )
    judul = judul_res.text.strip()
    print(f"📄 Judul: {judul}")
    
    time.sleep(15) # JEDA PENTING: Mencegah error 429 (Quota Limit)
    
    # Generate Deskripsi
    isi_res = client.models.generate_content(
        model="gemini-2.0-flash", 
        contents=f"Write a compelling product description in English for: '{judul}'. Include features and benefits."
    )
    isi = isi_res.text
    
    # Eksekusi Proses
    upload_ke_gumroad(judul, isi)
    post_to_twitter(f"🚀 New digital product released: {judul}! Check it out and transform your workflow. #DigitalProduct #PassiveIncome")
    
    print("🎉 Selesai! Semua proses sukses.")

if __name__ == "__main__":
    try:
        run_factory()
    except errors.ClientError as e:
        print(f"⚠️ Error Gemini API (Quota/Limit): {e}")
    except Exception as e:
        print(f"⚠️ Terjadi error: {e}")
    
