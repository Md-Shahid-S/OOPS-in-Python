from abc import ABC, abstractmethod


class Notification(ABC):

    def __init__(self, recipient: str):
        self.recipient = recipient

    @abstractmethod
    def send(self, message: str):
        pass

    def __str__(self):
        return f"{self.__class__.__name__} → {self.recipient}"


class SMSNotification(Notification):
    def send(self, message: str):
        print(f"[SMS]   Sending to {self.recipient}: '{message}'")
        return True


class EmailNotification(Notification):
    def __init__(self, recipient: str, subject: str):
        super().__init__(recipient)
        self.subject = subject

    def send(self, message: str):
        print(f"[EMAIL] To: {self.recipient} | Subject: {self.subject}")
        print(f"        Body: {message}")
        return True


class PushNotification(Notification):
    def __init__(self, recipient: str, device_id: str):
        super().__init__(recipient)
        self.device_id = device_id

    def send(self, message: str):
        print(f"[PUSH]  Device {self.device_id}: '{message}'")
        return True


# ── The power of polymorphism ──
# This function doesn't know or care which notification type it receives.
# It just calls send() and the right version runs automatically.
def broadcast(notifications: list, message: str):
    print(f"\nBroadcasting: '{message}'")
    print("─" * 45)
    for notification in notifications:
        notification.send(message)


notifications = [
    SMSNotification("+91-9876543210"),
    EmailNotification("affu@gmail.com", "Order Confirmed"),
    PushNotification("Affu", "device-uuid-1234"),
    SMSNotification("+91-8765432109"),
]

broadcast(notifications, "Your order has been shipped!")
# All four objects respond to send() differently
# but the calling code never changes