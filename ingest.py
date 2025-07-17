import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

# .env dosyasından API anahtarını yükle
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# PDF dosya yolu
PDF_PATH = "hukuk_metni.pdf"

def ingest_pdf():
    # PDF'i sayfa sayfa yükle
    loader = PyPDFLoader(PDF_PATH)
    pages = loader.load()

    # Sayfaları küçük parçalara böl (token sayısı < 300K garantili)
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=700,       # 🔧 Her parça max 700 karakter
        chunk_overlap=100     # 🔁 Önceki parça ile 100 karakter örtüşme
    )
    chunks = text_splitter.split_documents(pages)

    print(f"✅ Toplam {len(chunks)} parça üretildi. Embed ediliyor...")

    # OpenAI embedding
    embedding = OpenAIEmbeddings()

    # Chroma vektör veri tabanı oluştur
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embedding,
        persist_directory="./db"
    )
    vectorstore.persist()

    print("✅ Vektör veri tabanı başarıyla oluşturuldu.")

if __name__ == "__main__":
    ingest_pdf()
