import uuid
import re
from datetime import datetime
from functools import wraps
from flask import request, jsonify


def generate_conversation_id():
    """Generate a unique conversation ID."""
    return f"conv{uuid.uuid4().hex[:12]}"


def validate_request(required_fields):
    """
    Decorator to validate required JSON fields in a request.

    Args:
        required_fields (list): List of required field names
    """
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            data = request.get_json()
            if not data:
                return jsonify({
                    "status": False,
                    "error": "No JSON data provided"
                }), 400

            missing_fields = [
                field for field in required_fields
                if field not in data or not data[field]
            ]

            if missing_fields:
                return jsonify({
                    'success': False,
                    'error': "Missing required fields",
                    'missing_fields': missing_fields
                }), 400

            return f(*args, **kwargs)
        return wrapper
    return decorator


def sanitize_input(text):
    """
    Sanitize user input to prevent XSS and injection attacks.

    Args:
        text (str): Input text to sanitize

    Returns:
        str: Sanitized text
    """
    if not text:
        return ''

    # Remove script tags
    text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.DOTALL | re.IGNORECASE)
    # Remove javascript: protocol
    text = re.sub(r'javascript:', '', text, flags=re.IGNORECASE)

    return text.strip()


def format_timestamp(dt):
    """
    Format a datetime object as ISO string.

    Args:
        dt (datetime): Datetime to format

    Returns:
        str | None: ISO formatted string or None
    """
    if not dt:
        return None
    return dt.isoformat()


def truncate_text(text, max_length=100):
    """
    Truncate text to a maximum length.

    Args:
        text (str): Text to truncate
        max_length (int): Maximum character length

    Returns:
        str: Truncated text
    """
    if not text:
        return ''
    if len(text) <= max_length:
        return text
    return text[:max_length] + "..."


def error_response(message, status_code=400, **kwargs):
    """
    Build a standardised error JSON response.

    Args:
        message (str): Error message
        status_code (int): HTTP status code
        **kwargs: Additional key-value pairs to include

    Returns:
        tuple: Flask response tuple
    """
    response = {
        'success': False,
        'error': message
    }
    response.update(kwargs)
    return jsonify(response), status_code


def success_response(data=None, message=None, status_code=200):
    """
    Build a standardised success JSON response.

    Args:
        data: Response payload
        message (str): Optional success message
        status_code (int): HTTP status code

    Returns:
        tuple: Flask response tuple
    """
    response = {'success': True}

    if data is not None:
        response['data'] = data

    if message:
        response['message'] = message

    return jsonify(response), status_code


def get_client_ip():
    """Return the client's IP address, respecting forwarded headers."""
    if request.headers.get('X-Forwarded-For'):
        return request.headers.get('X-Forwarded-For').split(',')[0].strip()
    return request.remote_addr


def parse_bool(value):
    """
    Parse a value as boolean.

    Args:
        value: Value to parse

    Returns:
        bool: Parsed boolean
    """
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.lower() in ('true', '1', 'yes', 'on')
    return bool(value)
