from abc import ABC, abstractmethod


class Notifier():
    def notify(self, user, message):
        print(f"Base notifier for {user} with message: '{message}'.")


class Decorator(Notifier):
    wrappe: Notifier

    def __init__(self, notifier: Notifier):
        self.wrappe = notifier

    def notify(self, user, message):
        print(f"Base decorator notifier for {user} with message: '{message}'.")
        self.wrappe.notify(user, message)


class EmailNotifier(Decorator):
    def notify(self, user, message):
        self.wrappe.notify(user, message)
        print(f"Notify {user} with message: '{message}' by email.")


class PhoneNotifier(Decorator):
    def notify(self, user, message):
        self.wrappe.notify(user, message)
        print(f"Notify {user} with message: '{message}' by phone.")


class VKNotifier(Decorator):
    def notify(self, user, message):
        self.wrappe.notify(user, message)
        print(f"Notify {user} with message: '{message}' by VK.")


multy_notifier: Notifier = Notifier()
multy_notifier = PhoneNotifier(multy_notifier)
multy_notifier = EmailNotifier(multy_notifier)
multy_notifier = VKNotifier(multy_notifier)
multy_notifier.notify('Alexandr', 'Hello, world!')
