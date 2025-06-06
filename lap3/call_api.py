import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.rsa import Ui_MainWindow # Assuming ui.rsa contains Ui_MainWindow generated from a .ui file
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btngenerate.clicked.connect(self.call_api_gen_keys)
        self.ui.btnencrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btndecrypt.clicked.connect(self.call_api_decrypt)
        self.ui.btnsign.clicked.connect(self.call_api_sign)
        self.ui.btnverify.clicked.connect(self.call_api_verify)

    def call_api_gen_keys(self):
        url = "http://127.0.0.1:5000/api/rsa/generate_keys"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText(data["message"])
                msg.exec_()
            else:
                print("Error while calling API")
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText(f"Error: {response.status_code}\n{response.text}")
                msg.exec_()
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(f"Request Error: {e}")
            msg.exec_()

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/encrypt"
        payload = {
            "message": self.ui.txtvanban.toPlainText(),
            "key_type": "public" # Assuming public key is used for encryption by default
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txtmahoa.setText(data["encrypted_message"])

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
                error_message = f"Error: {response.status_code}"
                try:
                    error_data = response.json()
                    if "error" in error_data:
                        error_message += f"\n{error_data['error']}"
                    elif "message" in error_data: # Some APIs might return 'message' for errors
                        error_message += f"\n{error_data['message']}"
                    else:
                        error_message += f"\n{response.text}"
                except ValueError: # If response is not JSON
                    error_message += f"\n{response.text}"

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText(error_message)
                msg.exec_()
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(f"Request Error: {e}")
            msg.exec_()

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/decrypt"
        payload = {
            "ciphertext": self.ui.txtmahoa.toPlainText(),
            "key_type": "private" # Assuming private key is used for decryption by default
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txtvanban.setText(data["decrypted_message"])

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
                error_message = f"Error: {response.status_code}"
                try:
                    error_data = response.json()
                    if "error" in error_data:
                        error_message += f"\n{error_data['error']}"
                    elif "message" in error_data:
                         error_message += f"\n{error_data['message']}"
                    else:
                        error_message += f"\n{response.text}"
                except ValueError:
                    error_message += f"\n{response.text}"

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText(error_message)
                msg.exec_()
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(f"Request Error: {e}")
            msg.exec_()

    def call_api_sign(self):
        url = "http://127.0.0.1:5000/api/rsa/sign"
        payload = {
            "message": self.ui.txtthongtin.toPlainText(), # Assuming txt_info is for message to be signed
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txtsign.setText(data["signature"]) # Assuming txt_sign is for displaying signature

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Signed Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
                error_message = f"Error: {response.status_code}"
                try:
                    error_data = response.json()
                    if "error" in error_data:
                        error_message += f"\n{error_data['error']}"
                    elif "message" in error_data:
                         error_message += f"\n{error_data['message']}"
                    else:
                        error_message += f"\n{response.text}"
                except ValueError:
                    error_message += f"\n{response.text}"

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText(error_message)
                msg.exec_()
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(f"Request Error: {e}")
            msg.exec_()

    def call_api_verify(self):
        url = "http://127.0.0.1:5000/api/rsa/verify"
        payload = {
            "message": self.ui.txtthongtin.toPlainText(), # Assuming txt_info is the original message
            "signature": self.ui.txtsign.toPlainText() # Assuming txt_sign holds the signature
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                if data["is_verified"]:
                    msg.setText("Verified Successfully")
                else:
                    msg.setText("Verification Failed")
                msg.exec_()
            else:
                print("Error while calling API")
                error_message = f"Error: {response.status_code}"
                try:
                    error_data = response.json()
                    if "error" in error_data:
                        error_message += f"\n{error_data['error']}"
                    elif "message" in error_data: # Handle cases where API returns error in 'message'
                        error_message += f"\n{error_data['message']}"
                    else:
                        error_message += f"\n{response.text}"
                except ValueError:
                    error_message += f"\n{response.text}"

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText(error_message)
                msg.exec_()
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(f"Request Error: {e}")
            msg.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())