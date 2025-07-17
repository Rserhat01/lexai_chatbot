# ✅ LEXAI Hukuk Chatbotu - Flask + OpenAI GPT API (gpt-3.5-turbo destekli)

import os
from flask import Flask, render_template, request, redirect, url_for, session
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from ner_intent import extract_entities, classify_intent
from uuid import uuid4

# Ortam değişkenlerini yükle
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Flask uygulaması
app = Flask(__name__)
app.secret_key = str(uuid4())

# LangChain zinciri oluştur
embedding = OpenAIEmbeddings()
vectorstore = Chroma(persist_directory="./db", embedding_function=embedding)
retriever = vectorstore.as_retriever()
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, chain_type="stuff")

@app.route("/", methods=["GET", "POST"])
def index():
    if "chat_log" not in session:
        session["chat_log"] = []

    if request.method == "POST":
        user_input = request.form.get("user_input")

        if user_input:
            answer = qa_chain.run(user_input)
            entities = extract_entities(user_input)
            intent = classify_intent(user_input)

            if "last_qa" in session and session["last_qa"]:
                session["chat_log"].append(session["last_qa"])

            session["last_qa"] = {
                "question": user_input,
                "answer": answer,
                "entities": entities,
                "intent": intent
            }
            session.modified = True

            return redirect(url_for("index"))

    return render_template("index.html", last_qa=session.get("last_qa"), chat_log=session.get("chat_log", []))

@app.route("/reset")
def reset():
    session.clear()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
