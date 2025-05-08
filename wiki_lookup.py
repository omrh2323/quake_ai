import wikipedia

wikipedia.set_lang("tr")

def search_wikipedia(query):
    try:
        # "nedir", "ne demek" vb. kelimeleri temizle
        for word in ["nedir", "ne demek", "nasıl oluşur", "neden", "anlamı", "?"]:
            query = query.replace(word, "")
        query = query.strip()

        # En alakalı sayfa adını bul
        search_results = wikipedia.search(query)
        if not search_results:
            return "İlgili bir sayfa bulunamadı."

        # İlk sonucu özet olarak al
        page_title = search_results[0]
        return wikipedia.summary(page_title, sentences=2)

    except wikipedia.exceptions.DisambiguationError as e:
        return f"Birden fazla sonuç bulundu: {e.options[:3]}"
    except wikipedia.exceptions.PageError:
        return "İlgili bir sayfa bulunamadı."
    except Exception as e:
        return f"Hata: {str(e)}"
