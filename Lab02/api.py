from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher 
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayfairCipher
from cipher.transposition import TranspositionCipher
app = Flask(__name__)

#CAESAR CIPHER ALGORITM

caesar_cipher = CaesarCipher()

@app.route('/api/caesar/encrypt', methods=['POST'])
def caesar_encrypt():
    data = request.get_json()
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = caesar_cipher.encrypt(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route('/api/caesar/decrypt', methods=['POST'])
def caesar_decrypt():
    data = request.get_json()
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = caesar_cipher.decrypt(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

#VIGENERE CIPHER ALGORITM
viegenere_cipher = VigenereCipher()

@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.get_json()
    cipher_text = data['cipher_text']
    key = data['key']
    encrypted_text = viegenere_cipher.encrypt(cipher_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.get_json()
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = viegenere_cipher.decrypt(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})
RailfenceCipher = RailFenceCipher()
@app.route('/api/railfence/encrypt', methods=['POST'])
def encrypt():
    data = request.get_json()
    cipher_text = data['cipher_text']
    key = int(data['key'])
    encrypted_text = RailfenceCipher.encrypt(cipher_text, key)
    return jsonify({'encrypted_message': encrypted_text})
@app.route('/api/railfence/decrypt', methods=['POST'])
def decrypt():
    data = request.get_json()
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = RailfenceCipher.decrypt(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

PlayfairCipher = PlayfairCipher()

@app.route('/api/playfair/matrix', methods=['POST'])
def playfair_create_matrix():
    data = request.get_json()
    key = data['key']
    matrix = PlayfairCipher.create_playfair_matrix(key)
    return jsonify({'matrix': matrix})

@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.get_json()
    cipher_text = data['cipher_text']
    key = data['key']
    matrix = PlayfairCipher.create_playfair_matrix(key)
    encrypted_text = PlayfairCipher.encrypt(cipher_text, matrix)
    return jsonify({'encrypted_message': encrypted_text})

@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = request.get_json()
    cipher_text = data['cipher_text']
    key = data['key']
    matrix = PlayfairCipher.create_playfair_matrix(key)
    decrypted_text = PlayfairCipher.decrypt(cipher_text, matrix)
    return jsonify({'decrypted_message': decrypted_text})

transposition_cipher = TranspositionCipher()

@app.route("/api/transposition/encrypt", methods=["POST"])
def transposition_encrypt():
    data = request.get_json()
    plain_text = data.get("plain_text")
    key = data.get("key")
    
    if not isinstance(plain_text, str) or not isinstance(key, int):
        return jsonify({"error": "plain_text must be a string and num_rails must be an integer"}), 400
    
    encrypted_text = transposition_cipher.encrypt(plain_text, key)
    return jsonify({"encrypted_text": encrypted_text})

@app.route("/api/transposition/decrypt", methods=["POST"])
def transposition_decrypt():
    data = request.get_json()
    cipher_text = data.get("cipher_text")
    key = data.get("key")
    
    if not isinstance(cipher_text, str) or not isinstance(key, int):
        return jsonify({"error": "cipher_text must be a string and num_rails must be an integer"}), 400
    
    decrypted_text = transposition_cipher.decrypt(cipher_text, key)
    return jsonify({"decrypted_text": decrypted_text})

#main function
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)