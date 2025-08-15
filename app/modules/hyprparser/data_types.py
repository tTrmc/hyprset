"""
Data type classes for Hyprland configuration values.

Provides Setting, Color, Bezier, and Gradient classes that match
the hyprparser-py API for backward compatibility.
"""

from typing import Any, Tuple, Union
import re


class Setting:
    """Represents a single configuration setting with a path and value."""
    
    def __init__(self, section: str, value: Any):
        self.section = section
        self.value = value
    
    def __str__(self) -> str:
        return f"Setting({self.section}, {self.value})"
    
    def __repr__(self) -> str:
        return self.__str__()


class Color:
    """Represents a color value with RGBA components."""
    
    def __init__(self, r: Union[str, int], g: Union[str, int], b: Union[str, int], a: Union[str, int]):
        # Convert to integers if strings are provided
        self.r = int(r, 16) if isinstance(r, str) else int(r)
        self.g = int(g, 16) if isinstance(g, str) else int(g) 
        self.b = int(b, 16) if isinstance(b, str) else int(b)
        self.a = int(a, 16) if isinstance(a, str) else int(a)
        
        # Ensure values are in valid range
        self.r = max(0, min(255, self.r))
        self.g = max(0, min(255, self.g))
        self.b = max(0, min(255, self.b))
        self.a = max(0, min(255, self.a))
    
    @property
    def hex(self) -> str:
        """Returns the hex representation without # prefix."""
        return f"{self.r:02X}{self.g:02X}{self.b:02X}{self.a:02X}"
    
    @classmethod
    def from_hex(cls, hex_str: str) -> 'Color':
        """Create Color from hex string (with or without # prefix)."""
        hex_str = hex_str.lstrip('#').upper()
        
        # Ensure we have 8 characters (RRGGBBAA)
        if len(hex_str) == 6:
            hex_str += 'FF'  # Add full opacity if not specified
        elif len(hex_str) != 8:
            hex_str = hex_str.ljust(8, '0')[:8]
        
        return cls(
            hex_str[0:2], hex_str[2:4], 
            hex_str[4:6], hex_str[6:8]
        )
    
    @classmethod
    def from_rgba_string(cls, rgba_str: str) -> 'Color':
        """Create Color from rgba(r,g,b,a) string."""
        # Extract numbers from rgba string
        numbers = re.findall(r'\d+\.?\d*', rgba_str)
        if len(numbers) >= 3:
            r, g, b = map(int, numbers[:3])
            a = int(float(numbers[3]) * 255) if len(numbers) > 3 else 255
            return cls(r, g, b, a)
        return cls(0, 0, 0, 255)
    
    def to_rgba_string(self) -> str:
        """Convert to rgba(r,g,b,a) string format."""
        return f"rgba({self.r},{self.g},{self.b},{self.a/255:.2f})"
    
    def __str__(self) -> str:
        return f"#{self.hex}"
    
    def __repr__(self) -> str:
        return f"Color({self.r}, {self.g}, {self.b}, {self.a})"


class Bezier:
    """Represents a bezier curve for animations."""
    
    def __init__(self, name: str, points: Tuple[float, float, float, float]):
        self.name = name
        self.points = points  # (x0, y0, x1, y1)
    
    @property
    def x0(self) -> float:
        return self.points[0]
    
    @property 
    def y0(self) -> float:
        return self.points[1]
    
    @property
    def x1(self) -> float:
        return self.points[2]
    
    @property
    def y1(self) -> float:
        return self.points[3]
    
    def to_config_string(self) -> str:
        """Convert to Hyprland config format: bezier = name, x0, y0, x1, y1"""
        return f"bezier = {self.name}, {self.x0}, {self.y0}, {self.x1}, {self.y1}"
    
    @classmethod
    def from_config_string(cls, config_line: str) -> 'Bezier':
        """Parse from Hyprland config line."""
        # Remove 'bezier = ' prefix and split by comma
        parts = config_line.replace('bezier = ', '').split(',')
        if len(parts) >= 5:
            name = parts[0].strip()
            points = tuple(float(p.strip()) for p in parts[1:5])
            return cls(name, points)
        raise ValueError(f"Invalid bezier config: {config_line}")
    
    def __str__(self) -> str:
        return f"Bezier({self.name}, {self.points})"
    
    def __repr__(self) -> str:
        return self.__str__()


class Gradient:
    """Represents a gradient with multiple colors."""
    
    def __init__(self, colors: list = None, angle: float = 0.0):
        self.colors = colors or []
        self.angle = angle
    
    def add_color(self, color: Color, position: float = None):
        """Add a color to the gradient."""
        self.colors.append({'color': color, 'position': position})
    
    def to_config_string(self) -> str:
        """Convert to Hyprland gradient format."""
        color_strings = []
        for color_info in self.colors:
            color = color_info['color']
            color_strings.append(f"rgba({color.r:02x}{color.g:02x}{color.b:02x}{color.a:02x})")
        
        if self.angle != 0:
            color_strings.append(f"{self.angle}deg")
        
        return " ".join(color_strings)
    
    def __str__(self) -> str:
        return f"Gradient({len(self.colors)} colors, {self.angle}°)"
    
    def __repr__(self) -> str:
        return self.__str__()