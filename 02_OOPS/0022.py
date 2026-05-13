from abc import ABC, abstractmethod
from datetime import datetime

class Notification(ABC):
    
    @abstractmethod
    def send(self, recipient, message):
        pass

    @abstractmethod
    def get_delivery_status(self):
        pass

    def log_notification(self, recipient, message):
        # Moved datetime import to the top of the file for better practice
        print(f"{datetime.now()}: Notification sent to {recipient} with message: {message}")

class SMSNotification(Notification):
    def send(self, recipient, message):
        print(f"Sending SMS to +91{recipient}: {message}")
        self.log_notification(recipient, message)

    def get_delivery_status(self):
        return "SMS delivered"
    
class EmailNotification(Notification):
    def send(self, recipient, message):
        print(f"Sending email to {recipient}: {message}")
        self.log_notification(recipient, message)
        
    def get_delivery_status(self):
        return "Email delivered"

class PushNotification(Notification):
    def send(self, recipient, message):
        print(f"Pushing to device ID {recipient}: {message}")
        self.log_notification(recipient, message)

    def get_delivery_status(self):
        return "Push notification delivered"

class NotificationService:
    def notify_all(self, notifications, recipient, message):
        for notification in notifications:
            # Demonstrates working against the abstraction
            notification.send(recipient, message)

# Example usage
if __name__ == "__main__":
    # FIX: Instantiate the classes without arguments
    notifications = [
        SMSNotification(),
        EmailNotification(),
        PushNotification()
    ]
    
    service = NotificationService()
    
    # The service passes the recipient and message to the send() methods
    # Note: In a real system like Swiggy, "recipient" here would likely be a User Object 
    # that contains the user's phone number, email, and device ID, rather than a single string.
    service.notify_all(notifications, "User_12345", "Your order has been placed!")
    
