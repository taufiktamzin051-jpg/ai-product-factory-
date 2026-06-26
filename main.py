import os
import google.generativeai as genai

# Konfigurasi
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def get_pro_model():
    # Kita berikan prioritas tertinggi pada model 2.0 atau 2.5
    # Jika Google memperbarui API ke versi 2.5, cukup tambahkan di daftar priority
    priority = ['gemini-2.0-flash-exp', 'gemini-1.5-pro-latest', 'gemini-1.5-flash']
    
    available_models = {m.name: m for m in genai.list_models() if 'generateContent' in m.supported_generation_methods}
    
    for p in priority:
        # Mencoba mencari kecocokan nama model
        for name in available_models.keys():
            if p in name:
                return name
                
    return 'gemini-1.5-flash' # Default terakhir

# Inisialisasi model
model_name = get_pro_model()
model = genai.GenerativeModel(model_name)

print(f"Menggunakan model: {model_name}")

# Eksekusi
prompt = "Tuliskan 1 ide produk digital untuk pemula."
response = model.generate_content(prompt)

with open("produk_terbaru.md", "w", encoding="utf-8") as f:
    f.write(response.text)
