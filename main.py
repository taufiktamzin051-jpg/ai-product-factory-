import os
from datetime import datetime
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

try:
    # Mengambil model pertama yang tersedia di akun Anda
    models = [m for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    if not models:
        raise Exception("Tidak ada model yang ditemukan di akun Anda.")
    
    # Pilih model pertama yang tersedia
    model = genai.GenerativeModel(models[0].name)
    print(f"Menggunakan model: {models[0].name}")
    
    response = model.generate_content("Tuliskan 1 ide produk digital unik untuk pemula.")
    
    file_name = f"produksi_{datetime.now().strftime('%Y-%m-%d')}.md"
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(response.text)
    print(f"File berhasil dibuat: {file_name}")

except Exception as e:
    print(f"Error: {e}")
