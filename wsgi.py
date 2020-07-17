"""Application entry point."""
from complaint import create_app

application = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

