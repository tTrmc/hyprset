"""
Application constants and configuration values.

This module centralizes all magic numbers and configuration constants
used throughout the application for better maintainability.
"""

# Application Configuration
APP_ID = 'com.tokyob0t.hyprset'
APP_NAME = 'hyprset'
APP_VERSION = '0.1.0'

# Window Configuration
DEFAULT_WINDOW_WIDTH = 700
DEFAULT_WINDOW_HEIGHT = 360
MIN_WINDOW_WIDTH = 400
MIN_WINDOW_HEIGHT = 300

# Responsive Design
MOBILE_BREAKPOINT = 900  # px - when to collapse sidebar

# Color Constants
DEFAULT_HEX_LENGTH = 6
FULL_HEX_LENGTH = 8  # Including alpha
RGB_MAX_VALUE = 255
ALPHA_MAX_VALUE = 255

# Bezier Editor
BEZIER_EDITOR_WIDTH = 400
BEZIER_EDITOR_HEIGHT = 400
BEZIER_EDITOR_WINDOW_HEIGHT = 700
BEZIER_CONTROL_POINT_RADIUS = 10
BEZIER_GRID_SIZE = 20
BEZIER_CANVAS_SIZE = 300
BEZIER_CANVAS_OFFSET = 50

# File Paths
DEFAULT_CONFIG_DIR = '.config/hypr'
DEFAULT_CONFIG_FILE = 'hyprland.conf'
BACKUP_SUFFIX = '.backup'

# Toast Configuration
TOAST_TIMEOUT_INFINITE = 0

# CSS and Styling
CSS_FILE = 'style.css'
SCSS_FILE = 'style.scss'

# Limits and Validation
MAX_GAP_VALUE = 100
MAX_BORDER_SIZE = 20
MAX_SHADOW_RANGE = 50
MAX_OPACITY = 1.0
MIN_OPACITY = 0.0