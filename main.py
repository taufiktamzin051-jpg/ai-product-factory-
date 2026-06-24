import os
import time
import tweepy
import requests
from google import genai

# Inisialisasi
print("Memulai inisialisasi...")
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def run_factory():
    print("Pabrik mulai beroperasi...")
    
    # 1. Generate konten
    print("Menghubungi Gemini...")
    judul_res = client.models.generate_content(model="gemini-2.0-flash", contents="Buatkan judul produk digital")
    judul = judul_res.text.strip()
    
    # 2. Upload ke Gumroad
    print(f"Mencoba upload ke Gumroad: {judul}...")
    url = "https://api.gumroad.com/v2/products"
    data = {
        "access_token": os.getenv("GUMROAD_ACCESS_TOKEN"),
        "product[name]": judul,
        "product[price]": 0,
        "product[published]": "true"
    }
    res = requests.post(url, data=data)
    print(f"Status Gumroad: {res.status_code} - {res.text}")
    
    # 3. Tweet ke Twitter
    print("Mencoba posting ke Twitter...")
    auth = tweepy.OAuth1UserHandler(
        os.getenv("TWITTER_CONSUMER_KEY"), os.getenv("TWITTER_CONSUMER_SECRET"),
        os.getenv("TWITTER_ACCESS_TOKEN"), os.getenv("TWITTER_ACCESS_SECRET")
    )
    api = tweepy.API(auth)
    api.update_status(f"Produk baru: {judul} telah rilis!")
    print("Berhasil posting!")

if __name__ == "__main__":
    try:
        run_factory()
    except Exception as e:
        print(f"Terjadi error: {e}")
    
