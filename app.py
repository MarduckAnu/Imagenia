from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Reemplazá esta línea con tu clave real si aún no la pegaste
openai.api_key = "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"

@app.route('/generar', methods=['POST'])
def generar_imagen():
    data = request.get_json()
    prompt = data.get("prompt", "")

    try:
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="512x512"
        )
        image_url = response['data'][0]['url']
        return jsonify({"url": image_url})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
