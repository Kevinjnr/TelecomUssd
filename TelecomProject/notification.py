from plyer import notification


def send_notification(title: str, message: str, channel: str):
    """
    Sends a notification to users via their preferred channels and logs the message to a text file.

    Parameters
    ----------
    title : str
        The title of the notification.
    message : str
        The content of the notification message.
    channel : str
        The delivery channel or location (used for logging).

    Notes
    -----
    This method is responsible for sending notifications and appending the message to a log file.
    """
    # Send notification using the appropriate method (e.g., email, SMS, push notification)
    notification.notify(
        title=title,
        message=message,
        timeout=30  # Example: Notification timeout
    )

    # Log the notification message to a text file
    # notification / ConsoleSms.txt
    with open(f'notification/{channel}.txt', 'a', encoding='utf-8') as file:
        file.write(str(message))
        file.write('\n')
