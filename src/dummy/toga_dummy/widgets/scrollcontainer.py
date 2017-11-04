from .base import Widget


class ScrollContainer(Widget):
    def create(self):
        self._action('create ScrollContainer')

    def set_content(self, widget):
        self._action('set content', widget=widget)

    def apply_sub_layout(self):
        self._action('apply_sub_layout')

    def set_vertical(self, value):
        self._set_value('vertical', value)

    def set_horizontal(self, value):
        self._set_value('horizontal', value)
