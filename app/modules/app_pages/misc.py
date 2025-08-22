from ..imports import Adw
from ..widgets import (
    PreferencesGroup,
    SpinRow,
    SwitchRow,
    TextEntryRow,
)

misc_page = Adw.PreferencesPage.new()

# Display and Rendering
settings_display = PreferencesGroup(
    "Display &amp; Rendering", "Configure display behavior and rendering options."
)

settings_vfr = SwitchRow(
    "Variable Frame Rate (VFR)",
    "Lower the amount of sent frames when nothing is happening on-screen. Power-saving feature.",
    "misc:vfr",
)

settings_vrr = SpinRow(
    "Variable Refresh Rate (VRR)",
    "0 = disabled, 1 = always enabled, 2 = only for fullscreen applications.",
    "misc:vrr",
    min=0,
    max=2,
)

settings_no_direct_scanout = SwitchRow(
    "Disable Direct Scanout",
    "Disables direct scanout for fullscreen applications. May improve compatibility but reduce performance.",
    "misc:no_direct_scanout",
)

settings_enable_swallow = SwitchRow(
    "Enable Window Swallowing",
    "Enables window swallowing (terminal windows disappearing when launching apps).",
    "misc:enable_swallow",
)

settings_swallow_regex = TextEntryRow(
    "Swallow Regex",
    "Class regex to be used for windows that should be swallowed.",
    "misc:swallow_regex",
    "^(Alacritty|kitty|footclient)$"
)

settings_swallow_exception_regex = TextEntryRow(
    "Swallow Exception Regex", 
    "Class regex to be used for windows that should not be swallowed by the above.",
    "misc:swallow_exception_regex",
    ""
)

# Power Management
settings_power = PreferencesGroup(
    "Power Management", "Configure DPMS and screen power behavior."
)

settings_mouse_move_enables_dpms = SwitchRow(
    "Mouse Move Enables DPMS",
    "Wake displays from DPMS sleep when the mouse moves.",
    "misc:mouse_move_enables_dpms",
)

settings_key_press_enables_dpms = SwitchRow(
    "Key Press Enables DPMS",
    "Wake displays from DPMS sleep when a key is pressed.",
    "misc:key_press_enables_dpms",
)

settings_always_follow_on_dnd = SwitchRow(
    "Always Follow on Drag &amp; Drop",
    "Will make mouse focus follow mouse when drag and dropping.",
    "misc:always_follow_on_dnd",
)

# Window Behavior
settings_window_behavior = PreferencesGroup(
    "Window Behavior", "Configure window focus and interaction behavior."
)

settings_layers_hog_keyboard_focus = SwitchRow(
    "Layers Hog Keyboard Focus",
    "If true, will make keyboard-interactive layers keep their focus on mouse move.",
    "misc:layers_hog_keyboard_focus",
)

settings_animate_manual_resizes = SwitchRow(
    "Animate Manual Resizes",
    "Animate manual window resizes/moves.",
    "misc:animate_manual_resizes",
)

settings_animate_mouse_windowdragging = SwitchRow(
    "Animate Mouse Window Dragging",
    "Animate windows being dragged by mouse.",
    "misc:animate_mouse_windowdragging",
)

settings_disable_autoreload = SwitchRow(
    "Disable Auto Reload",
    "Disable automatic config reload on config file changes.",
    "misc:disable_autoreload",
)

settings_focus_on_activate = SwitchRow(
    "Focus on Activate",
    "Whether Hyprland should focus an app that requests to be focused.",
    "misc:focus_on_activate",
)

settings_no_direct_scanout_fullscreen = SwitchRow(
    "No Direct Scanout Fullscreen",
    "Disable direct scanout for fullscreen windows.",
    "misc:no_direct_scanout_fullscreen",
)

# Background and Theming
settings_theming = PreferencesGroup(
    "Background &amp; Theming", "Configure Hyprland's default backgrounds and logos."
)

settings_force_default_wallpaper = SpinRow(
    "Force Default Wallpaper",
    "-1 = default, 0 or 1 = disable the anime mascot wallpapers.",
    "misc:force_default_wallpaper",
    min=-1,
    max=1,
)

settings_disable_hyprland_logo = SwitchRow(
    "Disable Hyprland Logo",
    "If enabled, disables the random Hyprland logo/anime girl background.",
    "misc:disable_hyprland_logo",
)

settings_background_color = SpinRow(
    "Background Color",
    "Background color in hex format (0xRRGGBB or 0xRRGGBBAA).",
    "misc:background_color",
    min=0,
    max=4294967295,  # 0xFFFFFFFF
)

# Performance and Rendering
settings_performance = PreferencesGroup(
    "Performance", "Performance and rendering optimization settings."
)

settings_render_ahead_of_time = SwitchRow(
    "Render Ahead of Time",
    "Render ahead of time. Can reduce latency at the cost of battery.",
    "misc:render_ahead_of_time",
)

settings_render_ahead_safezone = SpinRow(
    "Render Ahead Safezone",
    "How many milliseconds of safezone to add to rendering ahead of time.",
    "misc:render_ahead_safezone",
    min=0,
    max=100,
)

settings_allow_session_lock_restore = SwitchRow(
    "Allow Session Lock Restore",
    "Allow session lock to be restored after a crash.",
    "misc:allow_session_lock_restore",
)

settings_close_special_on_empty = SwitchRow(
    "Close Special on Empty",
    "Close the special workspace if the last window is closed.",
    "misc:close_special_on_empty",
)

# Add all display widgets to the group
display_widgets = [
    settings_vfr,
    settings_vrr,
    settings_no_direct_scanout,
    settings_enable_swallow,
    settings_swallow_regex,
    settings_swallow_exception_regex,
]

for widget in display_widgets:
    settings_display.add(widget)

# Add all power management widgets to the group
power_widgets = [
    settings_mouse_move_enables_dpms,
    settings_key_press_enables_dpms,
    settings_always_follow_on_dnd,
]

for widget in power_widgets:
    settings_power.add(widget)

# Add all window behavior widgets to the group
window_behavior_widgets = [
    settings_layers_hog_keyboard_focus,
    settings_animate_manual_resizes,
    settings_animate_mouse_windowdragging,
    settings_disable_autoreload,
    settings_focus_on_activate,
    settings_no_direct_scanout_fullscreen,
]

for widget in window_behavior_widgets:
    settings_window_behavior.add(widget)

# Add all theming widgets to the group
theming_widgets = [
    settings_force_default_wallpaper,
    settings_disable_hyprland_logo,
    settings_background_color,
]

for widget in theming_widgets:
    settings_theming.add(widget)

# Add all performance widgets to the group
performance_widgets = [
    settings_render_ahead_of_time,
    settings_render_ahead_safezone,
    settings_allow_session_lock_restore,
    settings_close_special_on_empty,
]

for widget in performance_widgets:
    settings_performance.add(widget)

# Add all groups to the page
for group in [
    settings_display,
    settings_power,
    settings_window_behavior,
    settings_theming,
    settings_performance,
]:
    misc_page.add(group)