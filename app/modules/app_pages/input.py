from ..imports import Setting, Adw, Gtk, HyprData
from ..widgets import (
    PreferencesGroup,
    SpinRow,
    SwitchRow,
    TextEntryRow,
)

input_page = Adw.PreferencesPage.new()

# Keyboard Configuration
settings_keyboard = PreferencesGroup(
    "Keyboard", "Configure keyboard layout, model, and behavior."
)

settings_keyboard_layout = TextEntryRow(
    "Keyboard Layout",
    "Appropriate XKB keymap parameter. For example: us,cz",
    "input:kb_layout",
    "us"
)

settings_keyboard_variant = TextEntryRow(
    "Keyboard Variant", 
    "Appropriate XKB keymap parameter. For example: ,qwerty",
    "input:kb_variant"
)

settings_keyboard_model = TextEntryRow(
    "Keyboard Model",
    "Appropriate XKB keymap parameter",
    "input:kb_model"
)

settings_keyboard_options = TextEntryRow(
    "Keyboard Options",
    "Appropriate XKB keymap parameter. For example: grp:alt_shift_toggle",
    "input:kb_options"
)

settings_keyboard_rules = TextEntryRow(
    "Keyboard Rules",
    "Appropriate XKB keymap parameter",
    "input:kb_rules"
)

settings_keyboard_repeat_rate = SpinRow(
    "Repeat Rate",
    "The rate of repeating keys in Hz.",
    "input:repeat_rate",
    min=1,
    max=100,
)

settings_keyboard_repeat_delay = SpinRow(
    "Repeat Delay", 
    "Delay before a key starts repeating (in ms).",
    "input:repeat_delay",
    min=100,
    max=2000,
)

settings_keyboard_numlock_by_default = SwitchRow(
    "NumLock by Default",
    "Engage numlock by default.",
    "input:numlock_by_default",
)

# Mouse Configuration
settings_mouse = PreferencesGroup(
    "Mouse", "Configure mouse behavior and sensitivity."
)

settings_mouse_sensitivity = SpinRow(
    "Mouse Sensitivity",
    "Sets the mouse sensitivity. Value between -1.0 and 1.0.",
    "input:sensitivity",
    data_type=float,
    min=-1.0,
    max=1.0,
)

settings_mouse_accel_profile = TextEntryRow(
    "Acceleration Profile",
    "Sets mouse acceleration profile. adaptive or flat.",
    "input:accel_profile",
    "adaptive"
)

settings_mouse_force_no_accel = SwitchRow(
    "Force No Acceleration",
    "Force no cursor acceleration. This bypasses most of your pointer settings to get as raw of a signal as possible.",
    "input:force_no_accel",
)

settings_mouse_left_handed = SwitchRow(
    "Left Handed",
    "Switches RMB and LMB.",
    "input:left_handed",
)

settings_mouse_scroll_method = TextEntryRow(
    "Scroll Method",
    "Sets the scroll method. 2fg, edge, on_button_down, no_scroll",
    "input:scroll_method",
    "2fg"
)

settings_mouse_scroll_button = SpinRow(
    "Scroll Button",
    "Sets the scroll button. Has to be an int, cannot be a string.",
    "input:scroll_button",
    min=0,
    max=10,
)

settings_mouse_natural_scroll = SwitchRow(
    "Natural Scroll",
    "Inverts scrolling direction. When enabled, scrolling down scrolls in the opposite direction.",
    "input:natural_scroll",
)

# Focus Behavior
settings_focus = PreferencesGroup(
    "Focus Behavior", "Configure window focus and cursor behavior."
)

settings_focus_follow_mouse = SpinRow(
    "Follow Mouse",
    "Cursor focus mode. 0 - disabled, 1 - loose, 2 - strict, 3 - always on top.",
    "input:follow_mouse",
    min=0,
    max=3,
)

settings_focus_mouse_refocus = SwitchRow(
    "Mouse Refocus",
    "If disabled, mouse focus won't switch to the hovered window unless the mouse crosses a window boundary.",
    "input:mouse_refocus",
)

settings_focus_float_switch_override_focus = SwitchRow(
    "Float Switch Override Focus",
    "If enabled, focus will change to the window under the cursor when changing from tiled-to-floating and vice versa.",
    "input:float_switch_override_focus",
)

settings_focus_special_fallthrough = SwitchRow(
    "Special Fallthrough",
    "If enabled, having only floating windows in the special workspace will not block focusing windows in the regular workspace.",
    "input:special_fallthrough",
)

# Touchpad Configuration  
settings_touchpad = PreferencesGroup(
    "Touchpad", "Configure touchpad behavior and gestures."
)

settings_touchpad_natural_scroll = SwitchRow(
    "Natural Scroll",
    "Inverts scrolling direction. When enabled, scrolling down scrolls in the opposite direction.",
    "input:touchpad:natural_scroll",
)

settings_touchpad_disable_while_typing = SwitchRow(
    "Disable While Typing",
    "Disable the touchpad while typing.",
    "input:touchpad:disable_while_typing",
)

settings_touchpad_clickfinger_behavior = SwitchRow(
    "Click Finger Behavior",
    "Button presses with 1, 2, or 3 fingers will be mapped to LMB, RMB, and MMB respectively.",
    "input:touchpad:clickfinger_behavior",
)

settings_touchpad_middle_button_emulation = SwitchRow(
    "Middle Button Emulation",
    "Sending LMB and RMB simultaneously will be interpreted as MMB.",
    "input:touchpad:middle_button_emulation",
)

settings_touchpad_tap_to_click = SwitchRow(
    "Tap to Click",
    "Tapping on the touchpad with 1, 2, or 3 fingers will send LMB, RMB, and MMB respectively.",
    "input:touchpad:tap-to-click",
)

settings_touchpad_drag_lock = SwitchRow(
    "Drag Lock",
    "When enabled, lifting the finger off for a short time while dragging will not drop the dragged item.",
    "input:touchpad:drag_lock",
)

settings_touchpad_tap_and_drag = SwitchRow(
    "Tap and Drag",
    "Sets the tap-and-drag mode.",
    "input:touchpad:tap-and-drag",
)

settings_touchpad_scroll_factor = SpinRow(
    "Scroll Factor",
    "Multiplier applied to the amount of scroll movement.",
    "input:touchpad:scroll_factor",
    data_type=float,
    min=0.1,
    max=10.0,
)

# Special Keys and Advanced Settings
settings_special = PreferencesGroup(
    "Advanced Settings", "Configure special key behavior and advanced options."
)

settings_special_resolve_binds_by_sym = SwitchRow(
    "Resolve Binds by Symbol",
    "Determines how keybinds act when multiple layouts are used. If enabled, keybinds will use the symbols.",
    "input:resolve_binds_by_sym",
)

settings_special_emulate_discrete_scroll = SpinRow(
    "Emulate Discrete Scroll",
    "Emulate discrete scrolling from high resolution scrolling. 0 to disable, 1 for logitech mice, 2 for other mice.",
    "input:emulate_discrete_scroll", 
    min=0,
    max=2,
)

settings_special_off_window_axis_events = SpinRow(
    "Off Window Axis Events",
    "Handles axis events around windows. 0 ignores axis events outside of windows, 1 sends them to the window below cursor, 2 sends them to the focused window.",
    "input:off_window_axis_events",
    min=0,
    max=2,
)

# Add all widgets to their respective groups
keyboard_widgets = [
    settings_keyboard_layout,
    settings_keyboard_variant, 
    settings_keyboard_model,
    settings_keyboard_options,
    settings_keyboard_rules,
    settings_keyboard_repeat_rate,
    settings_keyboard_repeat_delay,
    settings_keyboard_numlock_by_default,
]

mouse_widgets = [
    settings_mouse_sensitivity,
    settings_mouse_accel_profile,
    settings_mouse_force_no_accel,
    settings_mouse_left_handed,
    settings_mouse_scroll_method,
    settings_mouse_scroll_button,
    settings_mouse_natural_scroll,
]

focus_widgets = [
    settings_focus_follow_mouse,
    settings_focus_mouse_refocus,
    settings_focus_float_switch_override_focus,
    settings_focus_special_fallthrough,
]

touchpad_widgets = [
    settings_touchpad_natural_scroll,
    settings_touchpad_disable_while_typing,
    settings_touchpad_clickfinger_behavior,
    settings_touchpad_middle_button_emulation,
    settings_touchpad_tap_to_click,
    settings_touchpad_drag_lock,
    settings_touchpad_tap_and_drag,
    settings_touchpad_scroll_factor,
]

special_widgets = [
    settings_special_resolve_binds_by_sym,
    settings_special_emulate_discrete_scroll,
    settings_special_off_window_axis_events,
]

# Add widgets to groups
for widget in keyboard_widgets:
    settings_keyboard.add(widget)

for widget in mouse_widgets:
    settings_mouse.add(widget)

for widget in focus_widgets:
    settings_focus.add(widget)

for widget in touchpad_widgets:
    settings_touchpad.add(widget)

for widget in special_widgets:
    settings_special.add(widget)

# Add all groups to the page
for group in [
    settings_keyboard,
    settings_mouse,
    settings_focus,
    settings_touchpad,
    settings_special,
]:
    input_page.add(group)