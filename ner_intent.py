from transformers import pipeline

# Basit NER modeli
ner_pipe = pipeline("ner", model="dbmdz/bert-base-turkish-cased")

def extract_entities(text):
    results = ner_pipe(text)
    return [(r['word'], r['entity']) for r in results]

# Basit intent sınıflandırıcı (çok basitleştirilmiş)
def classify_intent(text):
    keywords = {
        "iş": "İş Hukuku",
        "boşanma": "Aile Hukuku",
        "ceza": "Ceza Hukuku",
        "miras": "Miras Hukuku",
        "kira": "Borçlar Hukuku"
    }
    for k in keywords:
        if k in text.lower():
            return keywords[k]
    return "Genel Hukuk"

# Test
if __name__ == "__main__":
    q = "İş sözleşmesini feshetmek istiyorum."
    print("Entities:", extract_entities(q))
    print("Intent:", classify_intent(q))
