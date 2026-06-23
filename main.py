import os
import google.generativeai as genai
import requests

# Konfigurasi Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash-latest')

def buat_produk(topic):
    prompt = f"Tulis E-book panduan profesional tentang '{topic}'. Gunakan format Markdown yang rapi, mencakup problem-solution, langkah praktis, dan tips ahli. Jadikan konten ini premium dan siap jual."
    response = model.generate_content(prompt)
    return response.text

def run_factory():
    # Daftar topik yang akan diolah otomatis
    topics = ["AI Business Automation", "Digital Productivity Tools", "Passive Income via AI"]
    
    for topic in topics:
        print(f"--- Memulai produksi: {topic} ---")
        konten = buat_produk(topic)
        
        # Di sini skrip akan lanjut ke fungsi upload Gumroad & posting Twitter
        print(f"Produk '{topic}' berhasil dibuat!")
        # Simpan ke file .md atau langsung kirim ke API Gumroad
        with open(f"{topic}.md", "w") as f:
            f.write(konten)

if __name__ == "__main__":
    run_factory()
  
