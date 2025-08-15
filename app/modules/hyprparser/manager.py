"""
HyprData manager class - the main interface for configuration management.

Provides backward-compatible API matching hyprparser-py for seamless integration
with existing widgets and application code.
"""

from typing import Dict, Optional, Any, Union
from .parser import HyprlandConfigParser
from .data_types import Setting, Color, Bezier, Gradient


class HyprDataManager:
    """Main configuration manager - matches hyprparser-py HyprData API."""
    
    def __init__(self, config_path: Optional[str] = None):
        self.parser = HyprlandConfigParser(config_path)
        self._loaded = False
        self._ensure_loaded()
    
    def _ensure_loaded(self):
        """Ensure configuration is loaded."""
        if not self._loaded:
            self.parser.load()
            self._loaded = True
    
    @property
    def beziers(self) -> Dict[str, Bezier]:
        """Get dictionary of all bezier curves."""
        self._ensure_loaded()
        return self.parser.beziers.copy()
    
    def get_option(self, path: str) -> Optional[Setting]:
        """
        Get a configuration option by path.
        
        Args:
            path: Configuration path like "general:gaps_in" or "decoration:rounding"
            
        Returns:
            Setting object if found, None otherwise
        """
        self._ensure_loaded()
        return self.parser.settings.get(path)
    
    def set_option(self, path: str, value: Any) -> bool:
        """
        Set a configuration option.
        
        Args:
            path: Configuration path like "general:gaps_in"
            value: New value for the setting
            
        Returns:
            True if successful
        """
        self._ensure_loaded()
        
        # Convert value to appropriate type if needed
        if isinstance(value, Color):
            parsed_value = value
        elif isinstance(value, str) and (value.startswith('rgba(') or value.startswith('#')):
            try:
                parsed_value = Color.from_rgba_string(value) if value.startswith('rgba(') else Color.from_hex(value)
            except:
                parsed_value = value
        else:
            parsed_value = value
        
        # Create or update the setting
        self.parser.settings[path] = Setting(path, parsed_value)
        return True
    
    def new_option(self, setting: Setting) -> bool:
        """
        Add a new configuration option.
        
        Args:
            setting: Setting object to add
            
        Returns:
            True if successful
        """
        self._ensure_loaded()
        self.parser.settings[setting.section] = setting
        return True
    
    def save_all(self) -> bool:
        """
        Save all configuration changes to file.
        
        Returns:
            True if successful
        """
        self._ensure_loaded()
        return self.parser.save()
    
    def reload(self) -> bool:
        """
        Reload configuration from file.
        
        Returns:
            True if successful
        """
        self._loaded = False
        return self.parser.load()
    
    def get_all_settings(self) -> Dict[str, Setting]:
        """Get all configuration settings."""
        self._ensure_loaded()
        return self.parser.settings.copy()
    
    def add_bezier(self, name: str, x0: float, y0: float, x1: float, y1: float) -> bool:
        """
        Add a new bezier curve.
        
        Args:
            name: Name of the bezier curve
            x0, y0, x1, y1: Bezier control points
            
        Returns:
            True if successful
        """
        self._ensure_loaded()
        bezier = Bezier(name, (x0, y0, x1, y1))
        self.parser.beziers[name] = bezier
        return True
    
    def remove_bezier(self, name: str) -> bool:
        """
        Remove a bezier curve.
        
        Args:
            name: Name of bezier curve to remove
            
        Returns:
            True if successful
        """
        self._ensure_loaded()
        if name in self.parser.beziers:
            del self.parser.beziers[name]
            return True
        return False
    
    def get_bezier(self, name: str) -> Optional[Bezier]:
        """
        Get a bezier curve by name.
        
        Args:
            name: Name of the bezier curve
            
        Returns:
            Bezier object if found, None otherwise
        """
        self._ensure_loaded()
        return self.parser.beziers.get(name)
    
    def has_option(self, path: str) -> bool:
        """Check if an option exists."""
        self._ensure_loaded()
        return path in self.parser.settings
    
    def remove_option(self, path: str) -> bool:
        """Remove an option."""
        self._ensure_loaded()
        if path in self.parser.settings:
            del self.parser.settings[path]
            return True
        return False
    
    def get_section_options(self, section: str) -> Dict[str, Setting]:
        """Get all options for a specific section."""
        self._ensure_loaded()
        section_options = {}
        for path, setting in self.parser.settings.items():
            if path.startswith(f"{section}:"):
                section_options[path] = setting
        return section_options
    
    def clear_section(self, section: str) -> bool:
        """Clear all options in a section."""
        self._ensure_loaded()
        paths_to_remove = [path for path in self.parser.settings.keys() if path.startswith(f"{section}:")]
        for path in paths_to_remove:
            del self.parser.settings[path]
        return True
    
    def export_config(self) -> str:
        """Export current configuration as string."""
        self._ensure_loaded()
        return self.parser._generate_config_content()
    
    def import_config(self, config_content: str) -> bool:
        """
        Import configuration from string.
        
        Args:
            config_content: Configuration content as string
            
        Returns:
            True if successful
        """
        try:
            # Save current config as backup
            original_lines = self.parser.raw_lines.copy()
            original_settings = self.parser.settings.copy()
            original_beziers = self.parser.beziers.copy()
            
            # Parse new config
            self.parser.raw_lines = config_content.split('\n')
            self.parser.settings.clear()
            self.parser.beziers.clear()
            self.parser._parse_config()
            
            return True
            
        except Exception as e:
            # Restore backup on error
            self.parser.raw_lines = original_lines
            self.parser.settings = original_settings
            self.parser.beziers = original_beziers
            print(f"Error importing config: {e}")
            return False


# Create singleton instance to match hyprparser-py API
HyprData = HyprDataManager()