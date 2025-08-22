from ..imports import Adw, Gtk
from ..widgets import (
    PreferencesGroup,
    TextEntryRow,
    SwitchRow,
)

variables_page = Adw.PreferencesPage.new()

# Toolkit Backend Variables
settings_toolkit = PreferencesGroup(
    "Toolkit Backends", "Configure application toolkit backends for Wayland compatibility."
)

settings_gdk_backend = TextEntryRow(
    "GDK Backend",
    "GTK backend preference. Use 'wayland,x11' for Wayland first, X11 fallback.",
    "env:GDK_BACKEND",
    "wayland,x11"
)

settings_qt_qpa_platform = TextEntryRow(
    "Qt Platform",
    "Qt platform preference. Use 'wayland;xcb' for Wayland first, X11 fallback.",
    "env:QT_QPA_PLATFORM",
    "wayland;xcb"
)

settings_sdl_videodriver = TextEntryRow(
    "SDL Video Driver",
    "SDL video driver. Use 'wayland' for native Wayland support.",
    "env:SDL_VIDEODRIVER",
    "wayland"
)

settings_clutter_backend = TextEntryRow(
    "Clutter Backend",
    "Clutter backend for GNOME applications.",
    "env:CLUTTER_BACKEND",
    "wayland"
)

# Qt Configuration Variables
settings_qt = PreferencesGroup(
    "Qt Configuration", "Configure Qt-specific environment variables."
)

settings_qt_wayland_decoration = SwitchRow(
    "Disable Qt Wayland Decoration",
    "Disable Qt's built-in window decorations on Wayland.",
    "env:QT_WAYLAND_DISABLE_WINDOWDECORATION",
)

settings_qt_auto_screen_scale = SwitchRow(
    "Qt Auto Screen Scale",
    "Enable automatic screen scaling for Qt applications.",
    "env:QT_AUTO_SCREEN_SCALE_FACTOR",
)

settings_qt_platform_theme = TextEntryRow(
    "Qt Platform Theme",
    "Qt platform theme. Common options: qt5ct, qt6ct, gtk2, kde.",
    "env:QT_QPA_PLATFORMTHEME",
    "qt6ct"
)

settings_qt_style_override = TextEntryRow(
    "Qt Style Override",
    "Override Qt style. Popular options: kvantum, breeze, fusion.",
    "env:QT_STYLE_OVERRIDE",
    "kvantum"
)

# XDG Specification Variables
settings_xdg = PreferencesGroup(
    "XDG Desktop Specification", "Configure XDG desktop environment identification."
)

settings_xdg_current_desktop = TextEntryRow(
    "Current Desktop",
    "Current desktop environment identifier.",
    "env:XDG_CURRENT_DESKTOP",
    "Hyprland"
)

settings_xdg_session_type = TextEntryRow(
    "Session Type",
    "Session type identifier.",
    "env:XDG_SESSION_TYPE",
    "wayland"
)

settings_xdg_session_desktop = TextEntryRow(
    "Session Desktop",
    "Desktop session identifier.",
    "env:XDG_SESSION_DESKTOP",
    "Hyprland"
)

# Cursor and Theme Variables
settings_theming = PreferencesGroup(
    "Cursor &amp; Theming", "Configure cursor and theme environment variables."
)

settings_xcursor_theme = TextEntryRow(
    "X Cursor Theme",
    "X11 cursor theme name.",
    "env:XCURSOR_THEME",
    "Adwaita"
)

settings_xcursor_size = TextEntryRow(
    "X Cursor Size",
    "X11 cursor size in pixels.",
    "env:XCURSOR_SIZE",
    "24"
)

settings_hyprcursor_theme = TextEntryRow(
    "Hypr Cursor Theme", 
    "Hyprland-specific cursor theme.",
    "env:HYPRCURSOR_THEME",
    ""
)

settings_hyprcursor_size = TextEntryRow(
    "Hypr Cursor Size",
    "Hyprland-specific cursor size.",
    "env:HYPRCURSOR_SIZE",
    "24"
)

settings_gtk_theme = TextEntryRow(
    "GTK Theme",
    "GTK theme name for manual theme setting.",
    "env:GTK_THEME",
    ""
)

# Hyprland-Specific Variables
settings_hyprland = PreferencesGroup(
    "Hyprland Specific", "Hyprland-specific environment variables."
)

settings_hyprland_config = TextEntryRow(
    "Hyprland Config Path",
    "Custom path to Hyprland configuration file.",
    "env:HYPRLAND_CONFIG",
    ""
)

settings_no_sd_vars = SwitchRow(
    "Disable Systemd Variables",
    "Disable management of variables in systemd and dbus activation environments.",
    "env:HYPRLAND_NO_SD_VARS",
)

# Aquamarine Variables
settings_aquamarine = PreferencesGroup(
    "Aquamarine (AQ)", "Aquamarine backend configuration variables."
)

settings_aq_trace = SwitchRow(
    "Enable AQ Tracing",
    "Enable verbose logging for Aquamarine backend.",
    "env:AQ_TRACE",
)

settings_aq_drm_devices = TextEntryRow(
    "AQ DRM Devices",
    "Explicit list of DRM devices (GPUs) to use. Colon-separated paths.",
    "env:AQ_DRM_DEVICES",
    ""
)

settings_aq_no_atomic = SwitchRow(
    "Disable Atomic Mode Setting",
    "Use legacy DRM interface instead of atomic mode setting.",
    "env:AQ_NO_ATOMIC",
)

# Information Section
settings_info = PreferencesGroup(
    "Environment Variables Information", "Important notes about environment variable configuration."
)

# Create informational text widget
info_text = """Environment Variable Configuration:

Syntax: env = VARIABLE_NAME,value

Important Notes:
* Do NOT add quotes around values
* Values are treated as raw strings
* Changes require Hyprland restart to take effect
* Use hyprctl reload to apply some changes

Common Patterns:
* Toolkit backends: Use comma/semicolon separated fallbacks
* Boolean values: Use 1 for true, 0 for false (or unset)
* Paths: Use absolute paths without quotes

For uwsm users:
* Avoid setting variables in hyprland.conf
* Use ~/.config/uwsm/env for toolkit variables
* Use ~/.config/uwsm/env-hyprland for HYPR*/AQ_* variables

View current environment: printenv | grep -E '(GDK|QT|XDG|HYPR|AQ_)'"""

# Create a scrollable text view for the information
info_scrolled = Gtk.ScrolledWindow()
info_scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
info_scrolled.set_min_content_height(300)
info_scrolled.set_max_content_height(300)

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

# Add all toolkit widgets to the group
toolkit_widgets = [
    settings_gdk_backend,
    settings_qt_qpa_platform,
    settings_sdl_videodriver,
    settings_clutter_backend,
]

for widget in toolkit_widgets:
    settings_toolkit.add(widget)

# Add all Qt widgets to the group
qt_widgets = [
    settings_qt_wayland_decoration,
    settings_qt_auto_screen_scale,
    settings_qt_platform_theme,
    settings_qt_style_override,
]

for widget in qt_widgets:
    settings_qt.add(widget)

# Add all XDG widgets to the group
xdg_widgets = [
    settings_xdg_current_desktop,
    settings_xdg_session_type,
    settings_xdg_session_desktop,
]

for widget in xdg_widgets:
    settings_xdg.add(widget)

# Add all theming widgets to the group
theming_widgets = [
    settings_xcursor_theme,
    settings_xcursor_size,
    settings_hyprcursor_theme,
    settings_hyprcursor_size,
    settings_gtk_theme,
]

for widget in theming_widgets:
    settings_theming.add(widget)

# Add all Hyprland widgets to the group
hyprland_widgets = [
    settings_hyprland_config,
    settings_no_sd_vars,
]

for widget in hyprland_widgets:
    settings_hyprland.add(widget)

# Add all Aquamarine widgets to the group
aquamarine_widgets = [
    settings_aq_trace,
    settings_aq_drm_devices,
    settings_aq_no_atomic,
]

for widget in aquamarine_widgets:
    settings_aquamarine.add(widget)

# Add all groups to the page
for group in [
    settings_toolkit,
    settings_qt,
    settings_xdg,
    settings_theming,
    settings_hyprland,
    settings_aquamarine,
    settings_info,
]:
    variables_page.add(group)