from ..imports import Adw
from ..widgets import (
    PreferencesGroup,
    SpinRow,
    SwitchRow,
)

gestures_page = Adw.PreferencesPage.new()

# Workspace Swipe Gestures
settings_workspace_swipe = PreferencesGroup(
    "Workspace Swipe", "Configure touchpad workspace switching gestures."
)

settings_workspace_swipe_enable = SwitchRow(
    "Enable Workspace Swipe",
    "Enable workspace swipe gesture with touchpad.",
    "gestures:workspace_swipe",
)

settings_workspace_swipe_fingers = SpinRow(
    "Swipe Fingers",
    "Number of fingers required for the workspace swipe gesture.",
    "gestures:workspace_swipe_fingers",
    min=2,
    max=5,
)

settings_workspace_swipe_distance = SpinRow(
    "Swipe Distance",
    "Distance in pixels for the workspace swipe gesture.",
    "gestures:workspace_swipe_distance",
    min=100,
    max=2000,
)

settings_workspace_swipe_invert = SwitchRow(
    "Invert Swipe Direction",
    "Invert the direction of the workspace swipe gesture.",
    "gestures:workspace_swipe_invert",
)

settings_workspace_swipe_min_speed_to_force = SpinRow(
    "Min Speed to Force",
    "Minimum speed in px per timepoint to force the change ignoring cancel ratio. Set to 0 to disable.",
    "gestures:workspace_swipe_min_speed_to_force",
    min=0,
    max=100,
)

settings_workspace_swipe_cancel_ratio = SpinRow(
    "Cancel Ratio",
    "How much the swipe has to proceed to commence it (0.0-1.0). If > ratio * distance, switch workspace, otherwise revert.",
    "gestures:workspace_swipe_cancel_ratio",
    data_type=float,
    min=0.0,
    max=1.0,
)

settings_workspace_swipe_create_new = SwitchRow(
    "Create New Workspaces",
    "Whether to create new workspaces when swiping beyond existing ones.",
    "gestures:workspace_swipe_create_new",
)

settings_workspace_swipe_direction_lock = SwitchRow(
    "Direction Lock",
    "If enabled, switching direction will be locked when you swipe past the direction_lock_threshold.",
    "gestures:workspace_swipe_direction_lock",
)

settings_workspace_swipe_direction_lock_threshold = SpinRow(
    "Direction Lock Threshold",
    "In px, the distance to travel before direction lock activates.",
    "gestures:workspace_swipe_direction_lock_threshold",
    min=10,
    max=500,
)

settings_workspace_swipe_forever = SwitchRow(
    "Continuous Swipe",
    "If enabled, swiping will not clamp at the first and last workspace (workspace must be wrapping for this to work).",
    "gestures:workspace_swipe_forever",
)

settings_workspace_swipe_use_r = SwitchRow(
    "Use R Parameter",
    "If enabled, swiping will use r to do a fall/spring animation, otherwise a simple linear animation will be used.",
    "gestures:workspace_swipe_use_r",
)

# Add all workspace swipe widgets to the group
workspace_swipe_widgets = [
    settings_workspace_swipe_enable,
    settings_workspace_swipe_fingers,
    settings_workspace_swipe_distance,
    settings_workspace_swipe_invert,
    settings_workspace_swipe_min_speed_to_force,
    settings_workspace_swipe_cancel_ratio,
    settings_workspace_swipe_create_new,
    settings_workspace_swipe_direction_lock,
    settings_workspace_swipe_direction_lock_threshold,
    settings_workspace_swipe_forever,
    settings_workspace_swipe_use_r,
]

for widget in workspace_swipe_widgets:
    settings_workspace_swipe.add(widget)

# Add all groups to the page
for group in [
    settings_workspace_swipe,
]:
    gestures_page.add(group)