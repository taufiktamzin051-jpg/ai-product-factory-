import os
from datetime import datetime
import google.generativeai as genai

# Konfigurasi
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

prompt = """
Buatkan konten produk digital "Cheat Sheet Panduan Strategi" untuk Pemilik Bisnis Digital Pemula.
Format:
[JUDUL PRODUK]
[MASALAH UTAMA]
[SOLUSI/CHEAT SHEET]
[HARGA SARAN]
[KEYWORD SEO]
"""

try:
    response = model.generate_content(prompt)
    file_name = f"produksi_{datetime.now().strftime('%Y-%m-%d')}.md"
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(response.text)
    print(f"Berhasil: {file_name}")
except Exception as e:
    print(f"Error AI: {e}")
