import os
import time
import requests
from google import genai
from google.genai import errors
import tweepy

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def execute():
    try:
        print("Mencoba membuat konten...")
        # Tambahkan delay kecil sebelum mulai agar tidak langsung memicu kuota
        time.sleep(5) 
        
        response = client.models.generate_content(
            model="gemini-2.0-flash-lite", 
            contents="Buat judul dan tips produktivitas AI singkat."
        )
        konten = response.text
        print("Konten berhasil dibuat.")
        
        # Lanjut proses upload Gumroad & Twitter di sini...
        # (Tambahkan fungsi upload Anda di bawah ini)
        
    except errors.ClientError as e:
        print(f"Error kuota terdeteksi, menunggu 60 detik sebelum mencoba lagi: {e}")
        time.sleep(60) # Tunggu 1 menit jika kena limit
        execute() # Coba lagi otomatis
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    execute()
