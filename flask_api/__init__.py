from flask import Flask, jsonify, request

from flask_api.crypto_utils.module import aes_encrypt, aes_decrypt

app = Flask(__name__)


@app.route("/")
def index():
    return (
        "Welcome to Hvalfangst Crypto API!\n\n"
        "Available Endpoints:\n"
        "1. POST /encrypt - Encrypt text\n"
        "   Use this endpoint to encrypt plain text with a provided encryption key.\n\n"
        "2. POST /decrypt - Decrypt text\n"
        "   Use this endpoint to decrypt encrypted text with a provided encryption key.\n"
    )


@app.route("/encrypt", methods=["POST"])
def encrypt():
    # Extract data from JSON body
    request_data = request.get_json()

    # Check if 'plain_text' and 'encryption_key' fields are present in the JSON
    if "plain_text" not in request_data or "encryption_key" not in request_data:
        return jsonify({"error": "Missing 'plain_text' or 'encryption_key' in the request body"}), 400

    plain_text = request_data["plain_text"]
    encryption_key = request_data["encryption_key"]

    # Encrypt plain text using key provided in request body
    encrypted_text = aes_encrypt(encryption_key, plain_text)

    # Prepare response JSON
    response = {
        "mode": "encrypt",
        "plain_text": plain_text,
        "encrypted_text": encrypted_text
    }

    # Return JSON response
    return jsonify(response)


@app.route("/decrypt", methods=["POST"])
def decrypt():
    # Extract data from JSON body
    request_data = request.get_json()

    # Check if 'encrypted_text' and 'encryption_key' fields are present in the JSON
    if "encrypted_text" not in request_data or "encryption_key" not in request_data:
        return jsonify({"error": "Missing 'encrypted_text' or 'encryption_key' in the request body"}), 400

    encrypted_text = request_data["encrypted_text"]
    encryption_key = request_data["encryption_key"]

    # Decrypt encrypted text using key provided in request body
    plain_text = aes_decrypt(encryption_key, encrypted_text)

    # Prepare response JSON
    response = {
        "mode": "decrypt",
        "encrypted_text": encrypted_text,
        "plain_text": plain_text
    }

    # Return JSON response
    return jsonify(response)


if __name__ == "__main__":
    app.run()
