"""
Utility functions for Hyprland configuration parsing and manipulation.
"""

import re
from typing import Union, Tuple, Optional


def normalize_color_format(color_str: str) -> str:
    """
    Normalize color string to consistent format.
    
    Args:
        color_str: Color in various formats (hex, rgba, etc.)
        
    Returns:
        Normalized color string
    """
    color_str = color_str.strip()
    
    # Handle hex colors
    if color_str.startswith('#'):
        return color_str.upper()
    elif len(color_str) in (6, 8) and all(c in '0123456789abcdefABCDEF' for c in color_str):
        return f"#{color_str.upper()}"
    
    # Handle rgba colors
    if color_str.startswith('rgba(') and color_str.endswith(')'):
        return color_str.lower()
    
    return color_str


def parse_bezier_points(points_str: str) -> Tuple[float, float, float, float]:
    """
    Parse bezier points from string format.
    
    Args:
        points_str: Points as comma-separated string "x0,y0,x1,y1"
        
    Returns:
        Tuple of four float values
    """
    parts = [p.strip() for p in points_str.split(',')]
    if len(parts) != 4:
        raise ValueError(f"Expected 4 bezier points, got {len(parts)}")
    
    try:
        return tuple(float(p) for p in parts)
    except ValueError as e:
        raise ValueError(f"Invalid bezier points format: {e}")


def validate_config_path(path: str) -> bool:
    """
    Validate configuration path format.
    
    Args:
        path: Configuration path like "section:option"
        
    Returns:
        True if valid format
    """
    # Basic validation - should contain at least one colon
    if ':' not in path:
        return False
    
    # Check for valid characters (alphanumeric, underscore, colon)
    if not re.match(r'^[a-zA-Z0-9_:]+$', path):
        return False
    
    return True


def escape_config_value(value: str) -> str:
    """
    Escape special characters in configuration values.
    
    Args:
        value: Value to escape
        
    Returns:
        Escaped value
    """
    # Escape # characters
    return value.replace('#', '##')


def unescape_config_value(value: str) -> str:
    """
    Unescape special characters in configuration values.
    
    Args:
        value: Value to unescape
        
    Returns:
        Unescaped value
    """
    # Unescape # characters
    return value.replace('##', '#')


def format_config_line(key: str, value: Union[str, int, float, bool], indent: int = 0) -> str:
    """
    Format a configuration line.
    
    Args:
        key: Configuration key
        value: Configuration value
        indent: Indentation level (spaces)
        
    Returns:
        Formatted configuration line
    """
    indent_str = ' ' * indent
    
    # Format value based on type
    if isinstance(value, bool):
        formatted_value = 'yes' if value else 'no'
    elif isinstance(value, str):
        formatted_value = escape_config_value(value)
    else:
        formatted_value = str(value)
    
    return f"{indent_str}{key} = {formatted_value}"


def parse_section_name(line: str) -> Optional[str]:
    """
    Parse section name from a line.
    
    Args:
        line: Configuration line
        
    Returns:
        Section name if found, None otherwise
    """
    line = line.strip()
    if line.endswith('{'):
        return line[:-1].strip()
    return None


def is_section_end(line: str) -> bool:
    """
    Check if line is a section end marker.
    
    Args:
        line: Configuration line
        
    Returns:
        True if line is '}'
    """
    return line.strip() == '}'


def is_comment_line(line: str) -> bool:
    """
    Check if line is a comment.
    
    Args:
        line: Configuration line
        
    Returns:
        True if line is a comment
    """
    line = line.strip()
    return line.startswith('#') and not line.startswith('##')


def is_empty_line(line: str) -> bool:
    """
    Check if line is empty or whitespace only.
    
    Args:
        line: Configuration line
        
    Returns:
        True if line is empty
    """
    return not line.strip()


def extract_inline_section(key: str) -> Tuple[Optional[str], str]:
    """
    Extract section and option from inline format (section::option).
    
    Args:
        key: Configuration key that might contain inline section
        
    Returns:
        Tuple of (section, option) or (None, key) if no inline section
    """
    if '::' in key:
        parts = key.split('::', 1)
        return parts[0], parts[1]
    return None, key