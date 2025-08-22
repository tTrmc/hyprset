from ..imports import Adw, Gtk
from ..widgets import (
    PreferencesGroup,
    SwitchRow,
)

binds_page = Adw.PreferencesPage.new()

# Keybinding General Settings
settings_general = PreferencesGroup(
    "General Keybinding Settings", "Configure general keybinding behavior."
)

settings_resolve_binds_by_sym = SwitchRow(
    "Resolve Binds by Symbol",
    "Determines how keybinds act when multiple layouts are used. If enabled, keybinds will use the symbols.",
    "input:resolve_binds_by_sym",
)

# Add general settings to group
settings_general.add(settings_resolve_binds_by_sym)

# Information Section
settings_info = PreferencesGroup(
    "Keybinding Information", "Quick reference for Hyprland keybinding syntax and common patterns."
)

# Create informational text widget
info_text = """<b>Hyprland Keybinding Syntax:</b>

<tt>bind = MODIFIERS, KEY, DISPATCHER, PARAMS</tt>

<b>Common Modifiers:</b>
" SUPER (Windows key)
" SHIFT
" ALT
" CTRL
" SUPER_SHIFT (combination)

<b>Bind Types:</b>
" <tt>bind</tt> - Standard keybind
" <tt>bindm</tt> - Mouse movement bind
" <tt>bindl</tt> - Locked bind (works with inhibitor active)
" <tt>bindr</tt> - Release bind (on key release)
" <tt>binde</tt> - Repeat bind (press and hold)
" <tt>bindd</tt> - Bind with description

<b>Common Dispatchers:</b>
" <tt>exec</tt> - Execute command
" <tt>killactive</tt> - Close active window
" <tt>togglefloating</tt> - Toggle window floating
" <tt>fullscreen</tt> - Toggle fullscreen
" <tt>workspace</tt> - Switch workspace
" <tt>movetoworkspace</tt> - Move window to workspace
" <tt>movefocus</tt> - Move focus (l/r/u/d)
" <tt>movewindow</tt> - Move window (l/r/u/d)

<b>Example Keybindings:</b>
<tt>bind = SUPER, Q, killactive,</tt>
<tt>bind = SUPER, Return, exec, alacritty</tt>
<tt>bind = SUPER, F, togglefloating,</tt>
<tt>bind = SUPER, 1, workspace, 1</tt>
<tt>bindm = SUPER, mouse:272, movewindow</tt>
<tt>bindm = SUPER, mouse:273, resizewindow</tt>

<b>Note:</b> This page shows general settings only. 
For detailed keybinding management, edit your <tt>hyprland.conf</tt> file directly.
You can view current binds with: <tt>hyprctl binds</tt>"""

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
# Clean up the markup for plain text display
clean_text = info_text.replace('<b>', '').replace('</b>', '').replace('<tt>', '').replace('</tt>', '').replace('•', '*')
buffer.set_text(clean_text)

info_scrolled.set_child(info_textview)

# Create action row to contain the scrolled window
info_row = Adw.ActionRow()
info_row.set_child(info_scrolled)

settings_info.add(info_row)

# Quick Commands Section
settings_commands = PreferencesGroup(
    "Quick Commands", "Useful commands for managing keybindings."
)

# View current binds button
view_binds_button = Gtk.Button()
view_binds_button.set_label("View Current Keybinds")
view_binds_button.add_css_class("pill")
view_binds_button.set_tooltip_text("Run 'hyprctl binds' to view current keybindings")

def on_view_binds_clicked(button):
    import subprocess
    try:
        subprocess.Popen(['hyprctl', 'binds'])
    except FileNotFoundError:
        # Hyprctl not found, show in terminal instead
        subprocess.Popen(['x-terminal-emulator', '-e', 'hyprctl binds'])
    except:
        pass

view_binds_button.connect("clicked", on_view_binds_clicked)

# Edit config button
edit_config_button = Gtk.Button()
edit_config_button.set_label("Edit hyprland.conf")
edit_config_button.add_css_class("pill")
edit_config_button.set_tooltip_text("Open hyprland.conf for keybinding configuration")

def on_edit_config_clicked(button):
    import subprocess
    import os
    config_path = os.path.expanduser("~/.config/hypr/hyprland.conf")
    try:
        # Try to open with default text editor
        subprocess.Popen(['xdg-open', config_path])
    except:
        try:
            # Fallback to common editors
            subprocess.Popen(['gedit', config_path])
        except:
            try:
                subprocess.Popen(['nano', config_path])
            except:
                pass

edit_config_button.connect("clicked", on_edit_config_clicked)

# Reload config button
reload_config_button = Gtk.Button()
reload_config_button.set_label("Reload Configuration")
reload_config_button.add_css_class("pill")
reload_config_button.set_tooltip_text("Reload Hyprland configuration")

def on_reload_config_clicked(button):
    import subprocess
    try:
        subprocess.run(['hyprctl', 'reload'])
    except:
        pass

reload_config_button.connect("clicked", on_reload_config_clicked)

# Create button row
button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
button_box.set_homogeneous(True)
button_box.set_margin_top(12)
button_box.set_margin_bottom(12)
button_box.set_margin_start(12)  
button_box.set_margin_end(12)

button_box.append(view_binds_button)
button_box.append(edit_config_button)
button_box.append(reload_config_button)

commands_row = Adw.ActionRow()
commands_row.set_child(button_box)

settings_commands.add(commands_row)

# Add all groups to the page
for group in [
    settings_general,
    settings_info,
    settings_commands,
]:
    binds_page.add(group)