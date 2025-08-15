from .CustomToastOverlay import ToastOverlay
from ..imports import Adw, HyprData, Setting
from typing import Any


def SwitchRow(title: str, subtitle: str, section: str, *, invert: bool = False) -> Adw.SwitchRow:
    new_switchrow = Adw.SwitchRow(title = title, subtitle = subtitle)

    ToastOverlay.register_instance(new_switchrow)
    new_switchrow._invert = invert
    new_switchrow.section = section


    opt = HyprData.get_option(new_switchrow.section)

    if not opt:
        opt = Setting(new_switchrow.section, False)
        HyprData.new_option(opt)

    if new_switchrow._invert:
        new_switchrow.set_active(not opt.value)
    else:
        new_switchrow.set_active(bool(opt.value))

    new_switchrow._default = new_switchrow.get_active()

    def on_active(*args: Any, **kwargs: Any) -> bool:
        if new_switchrow.get_active() != new_switchrow._default:
            ToastOverlay.add_change()
        else:
            ToastOverlay.del_change()

        if new_switchrow._invert:
            return HyprData.set_option(
                new_switchrow.section, not new_switchrow.get_active()
            )

        return HyprData.set_option(new_switchrow.section, new_switchrow.get_active())

    def update_default(*args: Any, **kwargs: Any) -> None:
        new_switchrow._default = new_switchrow.get_active()

    new_switchrow.connect("notify::active", on_active)
    new_switchrow.update_default = update_default
    return new_switchrow

