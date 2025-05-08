def predict_personal(text):
    # Basit kontrol: belli kelimeler içeriyor mu?
    keywords = ["nasılsın", "adın ne", "kimsin", "ne yapıyorsun", "selam"]
    return any(word in text.lower() for word in keywords)
