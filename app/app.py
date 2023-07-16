import psutil
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    cpu_percent = psutil.cpu_percent()
    mem_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage('/').percent
    Message = None
    if cpu_percent > 80 or mem_percent > 80:
        Message = "Detected high CPU/Memory usage."
    return render_template('index.html',
                           cpu_percent=cpu_percent,
                           mem_percent=mem_percent,
                           disk_percent=disk_percent,
                           message=Message)


if __name__ == '__main__':
    app.run(debug=True,
            host='0.0.0.0',
            port=5000)
