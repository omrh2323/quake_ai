import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import os

# CSV verisini oku
data = pd.read_csv("quake_data.csv")

# Girdi ve çıktı sütunlarını ayır
X = data[["magnitude", "depth", "interval_before"]].values
y_raw = data["label"]

# Etiketleri sayısala çevir (öncü = 0, ana şok = 1, artçı = 2)
encoder = LabelEncoder()
y = encoder.fit_transform(y_raw)

# Eğitim ve test verisi olarak böl
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modeli oluştur
model = Sequential([
    Dense(16, activation='relu', input_shape=(3,)),
    Dense(8, activation='relu'),
    Dense(3, activation='softmax')  # 3 sınıf için
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Eğit
model.fit(X_train, y_train, epochs=50, validation_data=(X_test, y_test))

# Model klasörü yoksa oluştur
os.makedirs("model", exist_ok=True)

# Kaydet
model.save("model/quake_classifier.h5")
print("Model başarıyla kaydedildi.")
