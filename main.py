import os
import google.generativeai as genai

# Konfigurasi API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-2.0-flash')

def generate_and_save():
    # 1. Prompt Anda (Silakan ganti sesuai kebutuhan)
    prompt = "Buatkan 5 prompt marketing untuk menjual produk digital di Lemon Squeezy."
    
    # 2. Proses AI
    print("AI sedang bekerja...")
    response = model.generate_content(prompt)
    
    # 3. Simpan ke file
    file_name = "hasil_produksi.md"
    with open(file_name, "w", encoding="utf-8") as f:
        f.write("# Hasil Produksi AI\n\n")
        f.write(response.text)
    
    print(f"Berhasil! File {file_name} telah dibuat.")

if __name__ == "__main__":
    generate_and_save()
    
