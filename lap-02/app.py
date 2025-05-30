from flask import Flask, render_template, request
from cipher.ceasar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher
from cipher.transposition import TranspositionCipher

app = Flask(__name__)

# Cipher instances
caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()
railfence_cipher = RailFenceCipher()
playfair_cipher = PlayFairCipher()
transposition_cipher = TranspositionCipher()

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Caesar routes
@app.route('/caesar')
def caesar():
    return render_template('caesar.html')

@app.route('/caesar/encrypt', methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    encrypted_text = caesar_cipher.encrypt_text(text, key)
    return render_template('caesar.html', result=encrypted_text, mode='encrypt')

@app.route('/caesar/decrypt', methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    decrypted_text = caesar_cipher.decrypt_text(text, key)
    return render_template('caesar.html', result=decrypted_text, mode='decrypt')

# Vigenere routes
@app.route('/vigenere')
def vigenere():
    return render_template('vigenere.html')

@app.route('/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    encrypted_text = vigenere_cipher.vigenere_encrypt(text, key)
    return render_template('vigenere.html', result=encrypted_text, mode='encrypt')

@app.route('/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    decrypted_text = vigenere_cipher.vigenere_decrypt(text, key)
    return render_template('vigenere.html', result=decrypted_text, mode='decrypt')

# Rail Fence routes
@app.route('/railfence')
def railfence():
    return render_template('railfence.html')

@app.route('/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    encrypted_text = railfence_cipher.rail_fence_encrypt(text, key)
    return render_template('railfence.html', result=encrypted_text, mode='encrypt')

@app.route('/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    decrypted_text = railfence_cipher.rail_fence_decrypt(text, key)
    return render_template('railfence.html', result=decrypted_text, mode='decrypt')

# Playfair routes
@app.route('/playfair')
def playfair():
    return render_template('playfair.html')

@app.route('/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted_text = playfair_cipher.playfair_encrypt(text, matrix)
    return render_template('playfair.html', result=encrypted_text, mode='encrypt')

@app.route('/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.playfair_decrypt(text, matrix)
    return render_template('playfair.html', result=decrypted_text, mode='decrypt')

# Transposition routes
@app.route('/transposition')
def transposition():
    return render_template('transposition.html')

@app.route('/transposition/encrypt', methods=['POST'])
def transposition_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    encrypted_text = transposition_cipher.encrypt(text, key)
    return render_template('transposition.html', result=encrypted_text, mode='encrypt')

@app.route('/transposition/decrypt', methods=['POST'])
def transposition_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    decrypted_text = transposition_cipher.decrypt(text, key)
    return render_template('transposition.html', result=decrypted_text, mode='decrypt')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
