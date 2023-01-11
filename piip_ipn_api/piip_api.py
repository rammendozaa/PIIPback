from piip.setup import create_application

app = create_application(__name__)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
