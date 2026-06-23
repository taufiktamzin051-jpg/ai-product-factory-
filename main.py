import os
from google import genai
import tweepy

# 1. Setup Klien & API
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# 2. Setup Twitter
auth = tweepy.OAuth1UserHandler(
    os.getenv("TWITTER_CONSUMER_KEY"), os.getenv("TWITTER_CONSUMER_SECRET"),
    os.getenv("TWITTER_ACCESS_TOKEN"), os.getenv("TWITTER_ACCESS_SECRET")
)
api = tweepy.API(auth)

def execute():
    # Generate konten (Langsung, tanpa loop)
    # Gunakan model paling ringan agar jarang kena limit kuota
    prompt = "Buat tweet tips singkat produktivitas AI, max 280 karakter."
    response = client.models.generate_content(model="gemini-2.0-flash-lite", contents=prompt)
    
    # Posting ke Twitter
    api.update_status(response.text)
    print("Sukses: Konten sudah diposting!")

if __name__ == "__main__":
    execute()
