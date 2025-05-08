import requests

# API'nin çalıştığı adres (localhost veya sunucu IP'si)
url = "http://168.231.111.1:5000/chat"  # Sunucuya deploy ettiysen adresi güncelle

# Test mesajı
payload = {
    "message": "kürdistan nedir"
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print("Durum:", response.status_code)
print("Cevap:", response.json())
