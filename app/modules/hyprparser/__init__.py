"""
Custom Hyprland Configuration Parser

A replacement for hyprparser-py with full Hyprland config format support.
Provides backward-compatible API for seamless integration.
"""

from .data_types import Setting, Color, Bezier, Gradient
from .manager import HyprData

__all__ = ['Setting', 'Color', 'Bezier', 'Gradient', 'HyprData']