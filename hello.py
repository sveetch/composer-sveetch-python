from pathlib import Path

from project_composer.compose import Composer
from project_composer.processors import ClassProcessor


class MessagerBase:
    """
    Application messages collector
    """
    def load(self):
        return []

    def get_messages(self):
        output = ""

        messages = self.load()

        output = "\n".join([
            "Hello {}".format(m) for m in messages
        ])

        return output


class MessageProcessor(ClassProcessor):
    """
    Processor for enabled application settings classes for a Django project.
    """
    def get_module_path(self, name):
        """
        Return a Python path for a module name.

        Arguments:
            name (string): Module name.

        Returns:
            string: Module name prefixed with repository path if it is not empty else
            returns just the module name.
        """
        return "{base}.{part}".format(
            base=self.composer.get_application_base_module_path(name),
            part="messages",
        )


if __name__ == "__main__":
    # Setup logging to debug what is going on during processing
    import logging
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
    logging.debug("🚀 Starting")

    # Initialize composer with the manifest and the message processor
    _composer = Composer(Path("./pyproject.toml").resolve(),
        processors=[MessageProcessor],
    )

    # Resolve dependency order
    _composer.resolve_collection(lazy=False)

    # Search for all enabled message classes
    _classes = _composer.call_processor("MessageProcessor", "export")

    # Let's see the application collection as defined from manifest
    print()
    print("collection:", _composer.manifest.collection)

    # Let's see the application list correctly ordered from dependency resolving
    print()
    print("apps:", _composer.apps)

    # Let's see the final class list
    print()
    print("_classes:", [cls for cls in _classes])

    # Reverse the list since Python class order is from the last to the first
    _classes.reverse()

    # Add the base messager as the base inheritance
    _COMPOSED_CLASSES = _classes + [MessagerBase]

    # Compose the final messager from found classes
    Messager = type(
        "Messager",
        tuple(_COMPOSED_CLASSES),
        {}
    )

    # Use messager to collect all messages in the right order
    messager = Messager()
    messages = messager.get_messages()

    # And finally output all collected messages
    print()
    print(messages)
