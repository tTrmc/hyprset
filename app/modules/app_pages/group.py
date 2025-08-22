from ..imports import Adw
from ..widgets import (
    ColorExpanderRow,
    PreferencesGroup,
    SpinRow,
    SwitchRow,
    TextEntryRow,
)

group_page = Adw.PreferencesPage.new()

# Group Border Configuration
settings_group_borders = PreferencesGroup(
    "Group Borders", "Configure border colors for grouped windows."
)

settings_group_border_active = ColorExpanderRow(
    "Active Group Border",
    "Border color for the active group (focused group).",
    "group:col.border_active",
)

settings_group_border_inactive = ColorExpanderRow(
    "Inactive Group Border", 
    "Border color for inactive groups (unfocused groups).",
    "group:col.border_inactive",
)

settings_group_border_locked_active = ColorExpanderRow(
    "Locked Active Group Border",
    "Border color for the active group when locked.",
    "group:col.border_locked_active",
)

settings_group_border_locked_inactive = ColorExpanderRow(
    "Locked Inactive Group Border",
    "Border color for inactive groups when locked.",
    "group:col.border_locked_inactive",
)

# Groupbar Configuration
settings_groupbar = PreferencesGroup(
    "Groupbar", "Configure the groupbar appearance and behavior."
)

settings_groupbar_enabled = SwitchRow(
    "Enable Groupbar",
    "Enables groupbars (the window group titlebar).",
    "group:groupbar:enabled",
)

settings_groupbar_font_family = TextEntryRow(
    "Font Family",
    "Font family for the groupbar text.",
    "group:groupbar:font_family",
    "Sans"
)

settings_groupbar_font_size = SpinRow(
    "Font Size",
    "Font size for the groupbar text.",
    "group:groupbar:font_size",
    min=6,
    max=72,
)

settings_groupbar_gradients = SwitchRow(
    "Enable Gradients",
    "Whether to draw gradients under the titles.",
    "group:groupbar:gradients",
)

settings_groupbar_height = SpinRow(
    "Groupbar Height",
    "Height of the groupbar.",
    "group:groupbar:height",
    min=10,
    max=200,
)

settings_groupbar_priority = SpinRow(
    "Priority",
    "Priority of the groupbar over other decorations. Higher values mean higher priority.",
    "group:groupbar:priority",
    min=0,
    max=10,
)

settings_groupbar_render_titles = SwitchRow(
    "Render Titles",
    "Whether to render titles in the groupbar.",
    "group:groupbar:render_titles",
)

settings_groupbar_scrolling = SwitchRow(
    "Enable Scrolling",
    "Whether scrolling in the groupbar changes group active window.",
    "group:groupbar:scrolling",
)

settings_groupbar_stacked = SwitchRow(
    "Stacked Layout", 
    "Whether to use a stacked layout for the groupbar.",
    "group:groupbar:stacked",
)

settings_groupbar_text_color = ColorExpanderRow(
    "Text Color",
    "Controls the group bar text color.",
    "group:groupbar:text_color",
)

# Groupbar Colors
settings_groupbar_colors = PreferencesGroup(
    "Groupbar Colors", "Configure colors for active and inactive groupbar tabs."
)

settings_groupbar_col_active = ColorExpanderRow(
    "Active Tab Color",
    "Active groupbar tab color.",
    "group:groupbar:col.active",
)

settings_groupbar_col_inactive = ColorExpanderRow(
    "Inactive Tab Color", 
    "Inactive groupbar tab color.",
    "group:groupbar:col.inactive",
)

settings_groupbar_col_locked_active = ColorExpanderRow(
    "Locked Active Tab Color",
    "Active groupbar tab color when the group is locked.",
    "group:groupbar:col.locked_active",
)

settings_groupbar_col_locked_inactive = ColorExpanderRow(
    "Locked Inactive Tab Color",
    "Inactive groupbar tab color when the group is locked.",
    "group:groupbar:col.locked_inactive",
)

# Add all group border widgets to the group
group_border_widgets = [
    settings_group_border_active,
    settings_group_border_inactive, 
    settings_group_border_locked_active,
    settings_group_border_locked_inactive,
]

for widget in group_border_widgets:
    settings_group_borders.add(widget)

# Add all groupbar widgets to the group
groupbar_widgets = [
    settings_groupbar_enabled,
    settings_groupbar_font_family,
    settings_groupbar_font_size,
    settings_groupbar_gradients,
    settings_groupbar_height,
    settings_groupbar_priority,
    settings_groupbar_render_titles,
    settings_groupbar_scrolling,
    settings_groupbar_stacked,
    settings_groupbar_text_color,
]

for widget in groupbar_widgets:
    settings_groupbar.add(widget)

# Add all groupbar color widgets
groupbar_color_widgets = [
    settings_groupbar_col_active,
    settings_groupbar_col_inactive,
    settings_groupbar_col_locked_active,
    settings_groupbar_col_locked_inactive,
]

for widget in groupbar_color_widgets:
    settings_groupbar_colors.add(widget)

# Add all groups to the page
for group in [
    settings_group_borders,
    settings_groupbar,
    settings_groupbar_colors,
]:
    group_page.add(group)