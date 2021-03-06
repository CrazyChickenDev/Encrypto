"""
    The web version of encrypto
"""
from flask import Flask,render_template,request,redirect
from encryptMessage import Encryptor
app = Flask(__name__)
enc = Encryptor()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/encrypt',methods=["POST","GET"])
def encrypt():
    if request.method == "POST":
        msg = request.form['message']
        encrypted_message = enc.encrypt(msg)
        return render_template('dis_encrypted.html',msg=encrypted_message.decode())
    else:
        return redirect('/')        

@app.route('/decrypt',methods=["POST","GET"])
def decrypt():
    if request.method == "POST":
        msg = request.form['message'].encode()
        decrypted_message = enc.decrypt(msg,destroy=True)
        if decrypted_message == -1:
            return 'The message you seek is either never created or destroyed.'
        return render_template('dis_decrypted.html',msg=decrypted_message)
    else:
        return redirect('/')
if __name__ == '__main__':
    app.run()