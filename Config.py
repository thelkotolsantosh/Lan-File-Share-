"""
Configuration settings for LAN File Share
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Base configuration"""
    
    # Flask settings
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    DEBUG = os.getenv('FLASK_DEBUG', True)
    ENV = os.getenv('FLASK_ENV', 'development')
    
    # Server settings
    SERVER_PORT = int(os.getenv('SERVER_PORT', 5000))
    SERVER_HOST = os.getenv('SERVER_HOST', '0.0.0.0')
    
    # File upload settings
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', 'shared_files')
    MAX_FILE_SIZE = int(os.getenv('MAX_FILE_SIZE_MB', 500)) * 1024 * 1024  # Convert MB to bytes
    
    # Allowed file extensions
    ALLOWED_EXTENSIONS_STR = os.getenv(
        'ALLOWED_EXTENSIONS',
        'txt,pdf,png,jpg,jpeg,gif,mp4,mp3,zip,rar,doc,docx,xls,xlsx,pptx,csv,exe,apk'
    )
    ALLOWED_EXTENSIONS = set(ALLOWED_EXTENSIONS_STR.split(','))
    
    # Create upload folder if it doesn't exist
    @staticmethod
    def init_app():
        """Initialize application settings"""
        if not os.path.exists(Config.UPLOAD_FOLDER):
            os.makedirs(Config.UPLOAD_FOLDER)


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False


class TestingConfig(Config):
    """Testing configuration"""
    DEBUG = True
    TESTING = True
    UPLOAD_FOLDER = 'test_files'


# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}


def get_config():
    """Get the appropriate configuration based on environment"""
    env = os.getenv('FLASK_ENV', 'development')
    return config.get(env, config['default'])
