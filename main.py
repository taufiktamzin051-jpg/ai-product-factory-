import os
import sys
import time
import datetime
import tweepy
import requests
from google import genai

# Inisialisasi
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Jadwal
JADWAL = {0: "E-book", 1: "Notion Template", 2: "Graphic Asset", 3: "Course Outline", 4: "UI/UX Kit", 5: "Worksheet", 6: "Newsletter"}

def run_factory():
    # 1. Tentukan jenis
    jenis = JADWAL.get(datetime.datetime.now().weekday(), "Digital Asset")
    print(f"🚀 Memproduksi: {jenis}")

    # 2. Generate
    judul = client.models.generate_content(model="gemini-2.0-flash", contents=f"Title for {jenis} in English").text.strip()
    time.sleep(5)
    isi = client.models.generate_content(model="gemini-2.0-flash", contents=f"Description for '{judul}'").text

    # 3. Gumroad
    res = requests.post("https://api.gumroad.com/v2/products", data={
        "access_token": os.getenv("GUMROAD_ACCESS_TOKEN"),
        "product[name]": judul, "product[description]": isi, "product[price]": 0, "product[published]": "true"
    })
    
    if res.status_code == 200:
        url = res.json()['product']['url']
        # 4. Twitter
        auth = tweepy.OAuth1UserHandler(os.getenv("TWITTER_CONSUMER_KEY"), os.getenv("TWITTER_CONSUMER_SECRET"), os.getenv("TWITTER_ACCESS_TOKEN"), os.getenv("TWITTER_ACCESS_SECRET"))
        tweepy.API(auth).update_status(f"New {jenis}: {judul}! Get it here: {url}")
        print("✅ Selesai!")
    else:
        print(f"❌ Error: {res.text}")

if __name__ == "__main__":
    run_factory()
    sys.exit(0) # Memaksa program berhenti seketika
    
