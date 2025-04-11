from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = "sk-tu-clave"

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
