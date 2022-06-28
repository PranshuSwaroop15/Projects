import time
from plyer import notification
if __name__ == '__main__':
    while True:
        notification.notify(
            title="All Day Reminder",
            message="Today you have to"
                    "you havent completed it"
                    "not completed till now",
            timeout = 5
        )
        time.sleep(60*60)
