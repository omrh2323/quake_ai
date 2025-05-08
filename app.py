from flask import Flask, request, jsonify
from flask_cors import CORS
from predict_quake import predict_quake
from wiki_lookup import search_wikipedia
from predict_personal import predict_personal
import re

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    question = data.get("message", "").lower()

    if not question.strip():
        return jsonify({"reply": "Lütfen bir soru girin."})

    if any(k in question for k in ["nedir", "ne demek", "nasıl oluşur", "neden", "anlamı"]):
        return jsonify({"type": "info", "reply": search_wikipedia(question)})

    if predict_personal(question):
        return jsonify({"type": "personal", "reply": "Ben iyiyim, sen nasılsın? quakeAI olarak görevdeyim."})

    nums = [float(x) for x in re.findall(r"\d+\.\d+|\d+", question)]
    if len(nums) >= 3:
        mag, depth, interval = nums[:3]
        label, conf, msg = predict_quake(mag, depth, interval)
        return jsonify({"type": "data", "reply": msg})

    return jsonify({"reply": "Deprem tahmini için büyüklük, derinlik ve aralık gibi 3 sayı girin (örn: 5.6, 10, 0.3)."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
