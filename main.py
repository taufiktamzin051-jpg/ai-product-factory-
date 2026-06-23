import os
import requests
from google import genai
import tweepy

# Setup
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# 1. Fungsi Upload ke Gumroad
def upload_ke_gumroad(judul, konten):
    with open("produk.txt", "w") as f:
        f.write(konten)
    
    url = "https://api.gumroad.com/v2/products"
    data = {
        "access_token": os.getenv("GUMROAD_ACCESS_TOKEN"),
        "product[name]": judul,
        "product[price]": 0,
        "product[description]": "Produk otomatis dari AI."
    }
    files = {"file": open("produk.txt", "rb")}
    return requests.post(url, data=data, files=files).json()

# 2. Fungsi Posting Twitter
def posting_twitter(pesan):
    auth = tweepy.OAuth1UserHandler(
        os.getenv("TWITTER_CONSUMER_KEY"), os.getenv("TWITTER_CONSUMER_SECRET"),
        os.getenv("TWITTER_ACCESS_TOKEN"), os.getenv("TWITTER_ACCESS_SECRET")
    )
    api = tweepy.API(auth)
    api.update_status(pesan)

# 3. Fungsi Utama
def execute():
    # Buat konten
    res = client.models.generate_content(model="gemini-2.0-flash-lite", contents="Buat e-book pendek tentang tips AI.")
    judul = "Tips AI Otomatis"
    
    # Upload ke Gumroad
    g_res = upload_ke_gumroad(judul, res.text)
    link = g_res['product']['short_url']
    
    # Posting ke Twitter
    posting_twitter(f"E-book baru tentang AI sudah rilis! Download gratis di sini: {link}")
    print("Selesai! Produk sudah terupload dan tweet sudah terkirim.")

if __name__ == "__main__":
    execute()
