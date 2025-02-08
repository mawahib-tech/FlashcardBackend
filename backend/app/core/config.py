class Config:
    SECRET_KEY = "your_secret_key_here"
    DEBUG = True
    DATABASE_URL = "sqlite:///your_database.db"
    API_VERSION = "v1"
    
    @staticmethod
    def init_app(app):
        pass  # Placeholder for any app initialization logic if needed