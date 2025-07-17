# ⚖️ LexAI – Hukuk Destek Chatbotu

LexAI, Türkiye Cumhuriyeti kanunlarına dayalı büyük ölçekli PDF dökümanlarını analiz ederek kullanıcılara doğal dilde hukuki danışmanlık hizmeti sunan bir yapay zeka chatbot projesidir.  
Projede OpenAI GPT-3.5-Turbo, LangChain, ChromaDB ve modern Flask arayüzü kullanılmaktadır.

---

## 🚀 Özellikler

- 📄 1000+ sayfalık PDF içeriğiyle etkileşim kurar
- 🤖 GPT-3.5-Turbo destekli soru-cevap
- 🧠 Belge tabanlı RAG (Retrieval Augmented Generation)
- 🗂️ ChromaDB vektör veritabanı ile hızlı arama
- 🔒 OpenAI API ile güvenli LLM bağlantısı
- 🎨 Responsive ve animasyonlu Flask + HTML + CSS UI
- 🟥 Adalet Bakanlığı temalı, oval tasarım ve sade kırmızı-beyaz-siyah stil
- 📥 PDF yükleme destekli içerik hazırlığı (ingest pipeline)

---

## 🖼️ Arayüz Görselleri

<p align="center">
  <img src="screenshots/chat_demo.gif" width="80%" alt="LexAI Chat Arayüzü">
</p>

---

## 📂 Proje Yapısı

```bash
hukuk_chatbot/
│
├── app.py                  # Flask backend
├── ingest.py               # PDF -> Vektör veritabanı
├── requirements.txt
├── Dockerfile
├── .env
│
├── templates/
│   └── index.html          # Ana arayüz
├── static/
│   ├── style.css           # Tasarım dosyası
│   └── script.js           # Giriş animasyonu
├── db/                     # Chroma vektör verisi (otomatik oluşur)
└── pdfs/                   # Yüklenecek PDF klasörü
