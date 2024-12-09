from plyer import notification


class Notification():
    def __init__(self):
        pass

    @staticmethod
    def notify(title, message, icon=None, timeout=10):
        notification.notify(
            title=title,
            message=message,
            app_icon=icon,  # e.g. 'C:\\icon_32x32.ico'
            timeout=timeout,  # seconds
        )
