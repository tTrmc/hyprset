from ..imports import Adw, HyprData
from ..constants import TOAST_TIMEOUT_INFINITE
import weakref
from typing import List, Any


class CustomToastOverlay:
    def __init__(self) -> None:
        # Use weak references to avoid memory leaks
        self._instances: List[weakref.ReferenceType[Any]] = []
        self.changes = 0
        self._instance = Adw.ToastOverlay.new()
        self.toast = Adw.Toast.new('You have 0 unsaved changes!')
        self.toast.connect('button-clicked', self.save_changes)
        self.toast.set_button_label('Save now')
        self.toast.set_timeout(TOAST_TIMEOUT_INFINITE)

    @property
    def instance(self) -> Adw.ToastOverlay:
        return self._instance

    def show_toast(self) -> None:
        self.instance.add_toast(self.toast)

    def hide_toast(self) -> None:
        self.toast.dismiss()

    def add_change(self) -> None:
        self.changes += 1
        self.toast.set_title(f'You have {self.changes} unsaved changes!')
        return self.show_toast()

    def del_change(self) -> None:
        self.changes -= 1
        self.toast.set_title(f'You have {self.changes} unsaved changes!')
        if self.changes == 0:
            return self.hide_toast()

    # After calling this function, each widget updates its new default value.
    def register_instance(self, instance: Any) -> None:
        """Register a widget instance for change tracking."""
        # Clean up dead references
        self._instances = [ref for ref in self._instances if ref() is not None]
        
        # Add new instance with weak reference
        self._instances.append(weakref.ref(instance))
    
    def save_changes(self, *_) -> None:
        self.changes = 0
        self.hide_toast()

        # Update all registered instances, cleaning up dead references
        live_instances = []
        for ref in self._instances:
            instance = ref()
            if instance is not None:
                if hasattr(instance, 'update_default'):
                    instance.update_default()
                live_instances.append(ref)
        
        self._instances = live_instances
        return HyprData.save_all()


ToastOverlay = CustomToastOverlay()
