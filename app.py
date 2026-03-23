from flask import Flask
import psutil
import platform

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <h1>🖥️ System Info Dashboard</h1>
    <ul>
    <li>OS: {platform.system()}</li>
    <li>CPU Usage: {psutil.cpu_percent()}%</li>
    <li>Memory Usage: {psutil.virtual_memory().percent}%</li>
    </ul>
     """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)