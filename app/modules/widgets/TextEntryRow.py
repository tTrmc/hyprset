from .CustomToastOverlay import ToastOverlay
from ..imports import Adw, Gtk, HyprData, Setting
from typing import Any


class TextEntryRow(Adw.ActionRow):
    def __init__(self, title: str, subtitle: str, section: str, placeholder: str = "") -> None:
        super().__init__()
        
        ToastOverlay.register_instance(self)
        
        self.set_title(title)
        self.set_subtitle(subtitle)
        
        # Create entry widget
        self.entry = Gtk.Entry()
        self.entry.set_valign(Gtk.Align.CENTER)
        if placeholder:
            self.entry.set_placeholder_text(placeholder)
        
        # Add entry to the row
        self.add_suffix(self.entry)
        
        self.section = section
        
        # Load current value from config
        opt = HyprData.get_option(self.section)
        
        if not opt:
            opt = Setting(self.section, "")
            HyprData.new_option(opt)
        
        # Set current value
        current_value = str(opt.value) if opt.value else ""
        self.entry.set_text(current_value)
        self._default = current_value
        
        # Connect signals
        self.entry.connect("activate", self.on_activated)
        self.entry.connect("changed", self.on_changed)
    
    def on_activated(self, *_: Any) -> None:
        """Called when enter is pressed."""
        self.save_value()
    
    def on_changed(self, *_: Any) -> None:
        """Called when text changes."""
        # Update toast based on whether value changed
        current_text = self.entry.get_text()
        if current_text != self._default:
            ToastOverlay.add_change()
        else:
            ToastOverlay.del_change()
    
    def save_value(self) -> None:
        """Save the current value to config."""
        current_text = self.entry.get_text()
        HyprData.set_option(self.section, current_text)
    
    def update_default(self, *_: Any) -> None:
        """Update the default value (called after saving)."""
        self._default = self.entry.get_text()