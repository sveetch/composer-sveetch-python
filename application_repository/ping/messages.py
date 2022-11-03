from project_composer.marker import EnabledApplicationMarker


class PingMessage(EnabledApplicationMarker):
    def load(self):
        messages = super().load()
        messages.append("Ping")

        return messages
