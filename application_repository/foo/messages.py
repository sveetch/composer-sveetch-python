from project_composer.marker import EnabledApplicationMarker


class FooFirstMessage(EnabledApplicationMarker):
    def load(self):
        messages = super().load()
        messages.append("Foo first")

        return messages


class FooSecondMessage(EnabledApplicationMarker):
    def load(self):
        messages = super().load()
        messages.append("Foo second")

        return messages
