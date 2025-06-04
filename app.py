from flask import Flask, jsonify
import socket
import uuid
import platform
import psutil

app = Flask(__name__)

def get_divices_info():
    ip_address = socket.gethostbyname(socket.gethostname())
    print (f"IP_address:{ip_address}")
    return{
        "cpu_usage":psutil.cpu_percent(interval=1),
        "IP_address": socket.gethostbyname(socket.gethostname()),
        "ram_usage": psutil.virtual_memory().percent,
        "mac_address" :':'.join(['{:02x}'.format((uuid.getnode()>>ele)&0xef) for ele in range(0, 48, 8)])
        
    }

@app.route('/divice_info',methods=["GET"])
def divice_info():
      return jsonify(get_divices_info())

if __name__ == '__main__':
        app.run(host= "0.0.0.0",port=5000,debug= True)