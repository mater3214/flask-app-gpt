from pyngrok import ngrok
ngrok.set_auth_token("2lltjbVBAmhIzxIGeBs8WIx2zNh_62Rhe3Jq2nHsNXcRv5B6R") # get key from ngrok
public_url = ngrok.connect(5000)
print(f" * ngrok tunnel \"{public_url}\" -> \"http://127.0.0.1:5000\"")

from flask import Flask, request, jsonify

app = Flask(__name__)

# Route to analyze sentiment using OpenAI GPT
@app.route("/idea", methods=["POST"])
def idae():
    try:
        # Extract the OpenAI API key and the text to analyze from the POST request

        text = request.json.get("text")

        # Set the OpenAI API key
        # openai.api_key = os.getenv("OPENAI_API_KEY")
        openai.api_key = "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" # api key

        # Make a request to the OpenAI GPT-3.5 API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {
                    "role": "system",
                    # prompt
                    "content": "ขยายคำย่อของประโยคภาษาอังฤกษให้หน่อย:",
                },
                {"role": "user", "content": text},
            ],
        )

        # Extract the sentiment from the response
        idea_response = response["choices"][0]["message"]["content"].strip()


        return jsonify({"idea": idea_response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

public_url = ngrok.connect(5000)
print(f" * ngrok tunnel \"{public_url}\" -> \"http://127.0.0.1:5000\"")

app.run()
