import logging

import azure.functions as func
from flask import Flask, jsonify, request
from crypto_utils import aes_encrypt, aes_decrypt

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


@app.route("/")
def index():
    logger.info("Received request to index endpoint.")
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
    logger.info("Received request to encrypt endpoint.")

    # Extract data from JSON body
    request_data = request.get_json()

    # Check if 'plain_text' and 'encryption_key' fields are present in the JSON
    if "plain_text" not in request_data or "encryption_key" not in request_data:
        error_msg = "Missing 'plain_text' or 'encryption_key' in the request body"
        logger.error(error_msg)
        return jsonify({"error": error_msg}), 400

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

    logger.info("Encryption successful.")

    # Return JSON response
    return jsonify(response)


@app.route("/decrypt", methods=["POST"])
def decrypt():
    logger.info("Received request to decrypt endpoint.")

    # Extract data from JSON body
    request_data = request.get_json()

    # Check if 'encrypted_text' and 'encryption_key' fields are present in the JSON
    if "encrypted_text" not in request_data or "encryption_key" not in request_data:
        error_msg = "Missing 'encrypted_text' or 'encryption_key' in the request body"
        logger.error(error_msg)
        return jsonify({"error": error_msg}), 400

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

    logger.info("Decryption successful.")

    # Return JSON response
    return jsonify(response)


# Create an Azure Function which serves the above routes in our WSGI runtime (Gunicorn)
app = func.WsgiFunctionApp(app=app.wsgi_app, http_auth_level=func.AuthLevel.ANONYMOUS)
