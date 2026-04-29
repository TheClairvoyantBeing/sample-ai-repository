"""
recreate_db.py

Utility script to drop and recreate the database schema.
Run this when you need a clean slate (e.g. after model changes).

Usage:
    python recreate_db.py
"""

from app import db, create_app

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()
    print("Database recreated successfully.")
