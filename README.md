⚖️ LexAI – Türkçe Hukuk Chatbotu
📚 1200+ sayfalık hukuk dokümanını anlayan, Türkçe sorulara cevap verebilen yapay zekâ destekli bir hukuk asistanı.


🚀 Özellikler
💬 Doğal Dil Anlayışı (Türkçe destekli LLM – OpenAI GPT-3.5 Turbo)

🧠 NER & Intent Analizi (BERT ile Türkçe varlık tanıma ve niyet sınıflandırma)

📄 PDF tabanlı bilgi çekme (LangChain + ChromaDB ile)

🧑‍⚖️ Hukuki içeriklerde bilgi sorgulama

🖥️ Şık Arayüz: Flask tabanlı, responsive ve Adalet Bakanlığı temasında

🐳 Docker desteği: Kolay kurulum ve dağıtım için hazır

🛠️ Kullanılan Teknolojiler
Python

LangChain

OpenAI API

Transformers (HuggingFace)

Flask

Docker

ChromaDB

🧪 Kurulum
bash
Kopyala
Düzenle
git clone https://github.com/kullaniciadi/lexai.git
cd lexai
pip install -r requirements.txt
.env dosyasını oluşturun:

env
Kopyala
Düzenle
OPENAI_API_KEY=your_api_key
Docker ile çalıştırmak için:
bash
Kopyala
Düzenle
docker build -t lexai-chatbot .
docker run -p 5000:5000 --env-file .env lexai-chatbot
🧠 Nasıl Çalışır?
ingest.py ile PDF içeriği vektör tabanına aktarılır

Kullanıcı sorusu alınır

NER & intent çıkarılır

LLM ve bilgi tabanı üzerinden cevap oluşturulur

Sonuç arayüzde gösterilir

🎯 Yol Haritası
✅ Sabit hukuk botu
🛠️ [Yolda] Sektör ve veri kaynağı seçilebilen dinamik chatbot yapısı
📊 Sağlık, finans, eğitim gibi farklı alanlarda yeniden kullanılabilir hale getirme


👤 Geliştirici
Serhat Bağlam
[Yönetim Bilişim Sistemleri • Veri Bilimci Adayı]
LinkedIn
