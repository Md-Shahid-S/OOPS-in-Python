''' 
Design an abstract class Notification for a notification system used in an app like Swiggy:

Abstract methods: send(recipient, message) and get_delivery_status()
A concrete method log_notification(recipient, message) that prints a timestamped log entry
Create three concrete subclasses: SMSNotification, EmailNotification, and PushNotification
Each should implement send() differently — SMS prints "Sending SMS to +91...", 
Email prints "Sending email to ...@...", Push prints "Pushing to device ID..."
Build a NotificationService class with a method notify_all(notifications, recipient, message) 
that takes a list of notification objects and sends all of them — demonstrating that it works against the abstraction, 
not any specific implementation
'''