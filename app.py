# from openai import OpenAI
import os

import openai
import requests
from dotenv import load_dotenv
from flask import Flask, jsonify, request

# Load environment variables from .env file
load_dotenv()i

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
