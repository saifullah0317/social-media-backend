import sys
import os
from sqlalchemy import text

# Add the src directory to the Python module search path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src_path = os.path.join(project_root, "src")
sys.path.append(src_path)

from app import app
from database import db
from database.models import User, Comment, Content, Post, Reaction

def test_db_connection():
    """Test the database connection by executing a simple query."""
    try:
        with app.app_context():
            # Simple query to verify the connection
            result = db.session.execute(text("SELECT 1"))
            print("Database connection successful!")
    except Exception as e:
        print(f"Database connection failed: {e}")

def create_tables():
    """Create database tables."""
    with app.app_context():
        db.create_all()
        print("Tables created successfully!")

if __name__ == '__main__':
    test_db_connection()
    create_tables()
