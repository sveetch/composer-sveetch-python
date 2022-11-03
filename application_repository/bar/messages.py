from project_composer.marker import EnabledApplicationMarker


class BarMessage(EnabledApplicationMarker):
    def load(self):
        messages = super().load()
        messages.append("Bar")

        return messages
