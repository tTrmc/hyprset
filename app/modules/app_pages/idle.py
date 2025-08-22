from ..imports import Adw, Gtk
from ..widgets import (
    PreferencesGroup,
    SwitchRow,
)

idle_page = Adw.PreferencesPage.new()

# General Idle Settings
settings_general = PreferencesGroup(
    "General Idle Settings", "Configure general idle behavior and inhibitors."
)

settings_ignore_dbus_inhibit = SwitchRow(
    "Ignore DBus Inhibit",
    "Ignore dbus-sent idle inhibit events (e.g., from Firefox or Steam).",
    "hypridle:ignore_dbus_inhibit",
)

settings_ignore_systemd_inhibit = SwitchRow(
    "Ignore Systemd Inhibit",
    "Ignore systemd-inhibit --what=idle inhibitors.",
    "hypridle:ignore_systemd_inhibit",
)

settings_ignore_wayland_inhibit = SwitchRow(
    "Ignore Wayland Inhibit",
    "Ignore Wayland protocol idle inhibitors.",
    "hypridle:ignore_wayland_inhibit",
)

# Information Section
settings_info = PreferencesGroup(
    "Hypridle Configuration", "Guide for setting up idle management with hypridle."
)

# Create informational text widget
info_text = """Hypridle Configuration:

Configuration File: ~/.config/hypr/hypridle.conf

Basic Structure:
general {
    lock_cmd = loginctl lock-session
    unlock_cmd = loginctl unlock-session
    before_sleep_cmd = loginctl lock-session
    after_sleep_cmd = hyprctl dispatch dpms on
}

listener {
    timeout = 300  # 5 minutes in seconds
    on-timeout = hyprctl dispatch dpms off
    on-resume = hyprctl dispatch dpms on
}

Common General Options:
* lock_cmd - Command to run on dbus lock event
* unlock_cmd - Command to run on dbus unlock event
* before_sleep_cmd - Command before system sleep
* after_sleep_cmd - Command after system wake
* ignore_dbus_inhibit - Ignore apps preventing idle
* ignore_systemd_inhibit - Ignore systemd inhibitors
* ignore_wayland_inhibit - Ignore Wayland inhibitors

Listener Examples:

# Dim screen after 2.5 minutes
listener {
    timeout = 150
    on-timeout = brightnessctl -s set 10
    on-resume = brightnessctl -r
}

# Lock screen after 5 minutes
listener {
    timeout = 300
    on-timeout = loginctl lock-session
}

# Turn off screen after 5.5 minutes
listener {
    timeout = 330
    on-timeout = hyprctl dispatch dpms off
    on-resume = hyprctl dispatch dpms on
}

# Suspend after 10 minutes
listener {
    timeout = 600
    on-timeout = systemctl suspend
}

Common Commands:
* brightnessctl -s set 10 - Dim screen to 10%
* brightnessctl -r - Restore brightness
* hyprctl dispatch dpms off/on - Screen off/on
* loginctl lock-session - Lock screen
* systemctl suspend - Suspend system
* notify-send "message" - Show notification

Startup Configuration:
Add to hyprland.conf: exec-once = hypridle

Or enable as systemd service:
systemctl --user enable --now hypridle.service

Notes:
* Timeouts are in seconds
* Multiple listeners supported
* Commands run in shell context
* Config file is required for hypridle to run"""

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
    "Quick Commands", "Useful commands for managing hypridle."
)

# Check hypridle status button
check_status_button = Gtk.Button()
check_status_button.set_label("Check Hypridle Status")
check_status_button.add_css_class("pill")
check_status_button.set_tooltip_text("Check if hypridle is running")

def on_check_status_clicked(button):
    import subprocess
    try:
        result = subprocess.run(['pgrep', 'hypridle'], capture_output=True)
        if result.returncode == 0:
            subprocess.Popen(['x-terminal-emulator', '-e', 'sh', '-c', 'echo "hypridle is running"; systemctl --user status hypridle.service; read -p "Press Enter to continue..."'])
        else:
            subprocess.Popen(['x-terminal-emulator', '-e', 'sh', '-c', 'echo "hypridle is not running"; read -p "Press Enter to continue..."'])
    except:
        pass

check_status_button.connect("clicked", on_check_status_clicked)

# Edit hypridle config button
edit_hypridle_button = Gtk.Button()
edit_hypridle_button.set_label("Edit hypridle.conf")
edit_hypridle_button.add_css_class("pill")
edit_hypridle_button.set_tooltip_text("Open hypridle.conf for idle configuration")

def on_edit_hypridle_clicked(button):
    import subprocess
    import os
    config_path = os.path.expanduser("~/.config/hypr/hypridle.conf")
    # Create config file if it doesn't exist
    if not os.path.exists(config_path):
        os.makedirs(os.path.dirname(config_path), exist_ok=True)
        with open(config_path, 'w') as f:
            f.write("# Hypridle configuration\n")
            f.write("general {\n")
            f.write("    lock_cmd = loginctl lock-session\n")
            f.write("    before_sleep_cmd = loginctl lock-session\n")
            f.write("}\n\n")
            f.write("# Example listener - lock screen after 5 minutes\n")
            f.write("listener {\n")
            f.write("    timeout = 300\n")
            f.write("    on-timeout = loginctl lock-session\n")
            f.write("}\n")
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

edit_hypridle_button.connect("clicked", on_edit_hypridle_clicked)

# Restart hypridle button
restart_hypridle_button = Gtk.Button()
restart_hypridle_button.set_label("Restart Hypridle")
restart_hypridle_button.add_css_class("pill")
restart_hypridle_button.set_tooltip_text("Restart hypridle service")

def on_restart_hypridle_clicked(button):
    import subprocess
    try:
        # Try systemd service first
        subprocess.run(['systemctl', '--user', 'restart', 'hypridle.service'])
    except:
        try:
            # Fallback to manual restart
            subprocess.run(['pkill', 'hypridle'])
            subprocess.Popen(['hypridle'])
        except:
            pass

restart_hypridle_button.connect("clicked", on_restart_hypridle_clicked)

# Create button row
button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
button_box.set_homogeneous(True)
button_box.set_margin_top(12)
button_box.set_margin_bottom(12)
button_box.set_margin_start(12)  
button_box.set_margin_end(12)

button_box.append(check_status_button)
button_box.append(edit_hypridle_button)
button_box.append(restart_hypridle_button)

commands_row = Adw.ActionRow()
commands_row.set_child(button_box)

settings_commands.add(commands_row)

# Add settings to groups
settings_general.add(settings_ignore_dbus_inhibit)
settings_general.add(settings_ignore_systemd_inhibit)
settings_general.add(settings_ignore_wayland_inhibit)

# Add all groups to the page
for group in [
    settings_general,
    settings_info,
    settings_commands,
]:
    idle_page.add(group)