"""
Models for this service
"""


class NotificationModel:
    """
    id: An integer identifier.
    message: A string message.
    ttl: A TTL (short for Time to Live), that is, a duration in seconds \
            that will indicate the time the notification message \
            has to be displayed on the OLED display.
    creation_date: A creation date and time. The timestamp will be added \
            automatically when adding a new notification to the collection.
    notification_category: A notification category description, \
            such as Warning or Information.
    displayed_times: An integer counter that indicates the number of times \
            when the notification message has been displayed \
            on the OLED display.
    displayed_once: A Boolean value that indicates whether the notification \
            message was displayed at least once on the OLED display.
    """
    def __init__(self, message, ttl, creation_date, notification_category):
        # We will automatically generate the new id
        self.id = 0
        self.message = message
        self.ttl = ttl
        self.creation_date = creation_date
        self.notification_category = notification_category
        self.displayed_times = 0
        self.displayed_once = False
