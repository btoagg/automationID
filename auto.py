from flask import Flask, jsonify
import socket
import uuid
import platform
import psutil

app = Flask(__name__)

def get_devices_info():
    ip_address = socket.gethostbyname(socket.gethostname())
    mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0, 48, 8)])

    return {
        "cpu_usage": psutil.cpu_percent(interval=1),
        "ram_usage": psutil.virtual_memory().percent,
        "IP_address": ip_address,
        "mac_address": mac_address,
        "system": platform.system(),
        "machine": platform.machine()
    }

@app.route('/device_info', methods=["GET"])
def device_info():
    info = get_devices_info()
    return jsonify(info)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5800, debug=True)
