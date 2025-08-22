from ..imports import Adw, Gtk
from ..widgets import (
    PreferencesGroup,
    SwitchRow,
)

wallpaper_page = Adw.PreferencesPage.new()

# Wallpaper Settings
settings_wallpaper = PreferencesGroup(
    "Wallpaper Settings", "Configure wallpaper behavior and startup."
)

settings_force_default_wallpaper = SwitchRow(
    "Disable Hyprland Default Wallpaper",
    "Disable the anime mascot wallpapers. Enable this to prevent default wallpapers.",
    "misc:force_default_wallpaper",
)

settings_disable_hyprland_logo = SwitchRow(
    "Disable Hyprland Logo",
    "Disable the random Hyprland logo/anime girl background.",
    "misc:disable_hyprland_logo",
)

# Information Section
settings_info = PreferencesGroup(
    "Hyprpaper Configuration", "Guide for setting up wallpapers with hyprpaper."
)

# Create informational text widget
info_text = """Hyprpaper Configuration:

Configuration File: ~/.config/hypr/hyprpaper.conf

Basic Syntax:
preload = /path/to/wallpaper.jpg
wallpaper = monitor,/path/to/wallpaper.jpg

Examples:
# Preload wallpapers into memory
preload = ~/Pictures/wallpaper1.jpg
preload = ~/Pictures/wallpaper2.png

# Set wallpapers for specific monitors
wallpaper = DP-1,~/Pictures/wallpaper1.jpg
wallpaper = HDMI-1,~/Pictures/wallpaper2.png

# Set wallpaper for all monitors
wallpaper = ,~/Pictures/wallpaper.jpg

Display Modes:
* Default: cover (scales to fit screen)
* contain:/path/to/image - fit image within screen
* tile:/path/to/image - tile image across screen

Startup Configuration:
Add to hyprland.conf: exec-once = hyprpaper

Monitor Names:
Check monitor names with: hyprctl monitors

IPC Commands:
hyprctl hyprpaper preload "~/Pictures/image.jpg"
hyprctl hyprpaper wallpaper "DP-1,~/Pictures/image.jpg"
hyprctl hyprpaper wallpaper ",~/Pictures/image.jpg"

Memory Management:
You can unload wallpapers with:
hyprctl hyprpaper unload all
hyprctl hyprpaper unload unused
hyprctl hyprpaper unload "/path/to/image"

Advanced Features:
* Splash text overlay support
* Multiple wallpapers per session
* Dynamic wallpaper switching via IPC"""

# Create a scrollable text view for the information
info_scrolled = Gtk.ScrolledWindow()
info_scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
info_scrolled.set_min_content_height(400)
info_scrolled.set_max_content_height(400)

info_textview = Gtk.TextView()
info_textview.set_editable(False)
info_textview.set_cursor_visible(False)
info_textview.set_wrap_mode(Gtk.WrapMode.WORD)
info_textview.add_css_class("monospace")
info_textview.set_margin_top(12)
info_textview.set_margin_bottom(12)
info_textview.set_margin_start(12)
info_textview.set_margin_end(12)

buffer = info_textview.get_buffer()
buffer.set_text(info_text)

info_scrolled.set_child(info_textview)

# Create action row to contain the scrolled window
info_row = Adw.ActionRow()
info_row.set_child(info_scrolled)

settings_info.add(info_row)

# Quick Commands Section
settings_commands = PreferencesGroup(
    "Quick Commands", "Useful commands for managing wallpapers."
)

# View monitors button
view_monitors_button = Gtk.Button()
view_monitors_button.set_label("View Monitors")
view_monitors_button.add_css_class("pill")
view_monitors_button.set_tooltip_text("Run 'hyprctl monitors' to view available monitors")

def on_view_monitors_clicked(button):
    import subprocess
    try:
        subprocess.Popen(['x-terminal-emulator', '-e', 'sh', '-c', 'hyprctl monitors; read -p "Press Enter to continue..."'])
    except:
        try:
            subprocess.Popen(['hyprctl', 'monitors'])
        except:
            pass

view_monitors_button.connect("clicked", on_view_monitors_clicked)

# Edit hyprpaper config button
edit_hyprpaper_button = Gtk.Button()
edit_hyprpaper_button.set_label("Edit hyprpaper.conf")
edit_hyprpaper_button.add_css_class("pill")
edit_hyprpaper_button.set_tooltip_text("Open hyprpaper.conf for wallpaper configuration")

def on_edit_hyprpaper_clicked(button):
    import subprocess
    import os
    config_path = os.path.expanduser("~/.config/hypr/hyprpaper.conf")
    # Create config file if it doesn't exist
    if not os.path.exists(config_path):
        os.makedirs(os.path.dirname(config_path), exist_ok=True)
        with open(config_path, 'w') as f:
            f.write("# Hyprpaper configuration\n")
            f.write("# preload = /path/to/wallpaper.jpg\n")
            f.write("# wallpaper = monitor,/path/to/wallpaper.jpg\n")
    try:
        subprocess.Popen(['xdg-open', config_path])
    except:
        try:
            subprocess.Popen(['gedit', config_path])
        except:
            try:
                subprocess.Popen(['nano', config_path])
            except:
                pass

edit_hyprpaper_button.connect("clicked", on_edit_hyprpaper_clicked)

# Reload hyprpaper button
reload_hyprpaper_button = Gtk.Button()
reload_hyprpaper_button.set_label("Reload Hyprpaper")
reload_hyprpaper_button.add_css_class("pill")
reload_hyprpaper_button.set_tooltip_text("Reload hyprpaper configuration")

def on_reload_hyprpaper_clicked(button):
    import subprocess
    try:
        subprocess.run(['hyprctl', 'hyprpaper', 'reload'])
    except:
        # Try restarting hyprpaper if reload doesn't work
        try:
            subprocess.run(['pkill', 'hyprpaper'])
            subprocess.Popen(['hyprpaper'])
        except:
            pass

reload_hyprpaper_button.connect("clicked", on_reload_hyprpaper_clicked)

# Create button row
button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
button_box.set_homogeneous(True)
button_box.set_margin_top(12)
button_box.set_margin_bottom(12)
button_box.set_margin_start(12)  
button_box.set_margin_end(12)

button_box.append(view_monitors_button)
button_box.append(edit_hyprpaper_button)
button_box.append(reload_hyprpaper_button)

commands_row = Adw.ActionRow()
commands_row.set_child(button_box)

settings_commands.add(commands_row)

# Add settings to groups
settings_wallpaper.add(settings_force_default_wallpaper)
settings_wallpaper.add(settings_disable_hyprland_logo)

# Add all groups to the page
for group in [
    settings_wallpaper,
    settings_info,
    settings_commands,
]:
    wallpaper_page.add(group)