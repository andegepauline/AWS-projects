from flask import Flask

# Create a Flask web app instance
app = Flask(__name__)

# Define a route at the root URL
@app.route('/')
def home():
    return "Nothing beats a Jet Two holiday! Right now, you can save 50 pounds per person!Thats 200 pounds off for a family of four!!"

# Run the app on host 0.0.0.0 (needed inside containers)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) #launches a server on port 5000 that listens for requests
