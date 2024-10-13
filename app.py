from flask import Flask           
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    # Get the PORT from the environment (default to 5000 if not set)
    port = 5000
    # Bind to 0.0.0.0 for external access
    app.run(host='0.0.0.0', port=port)