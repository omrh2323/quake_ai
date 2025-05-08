import numpy as np
from tensorflow.keras.models import load_model

# Modeli yükle
model = load_model("model/quake_classifier.h5")

# Etiket sırası -> LabelEncoder'ın sıralamasına göre
labels = ["ana şok", "artçı", "öncü"]

def predict_quake(magnitude, depth, interval_before):
    try:
        features = np.array([[magnitude, depth, interval_before]])
        probs = model.predict(features)[0]
        max_index = np.argmax(probs)
        confidence = probs[max_index] * 100
        label = labels[max_index]
        return (
            label,
            confidence,
            f"Bu deprem büyük ihtimalle {label} sınıfına giriyor. (Güven: %{confidence:.2f})"
        )
    except Exception as e:
        return ("bilinmiyor", 0.0, f"Hata oluştu: {str(e)}")
