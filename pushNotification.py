import os


def display_notification(title, text):
    if os.name == "nt":
        from win10toast import ToastNotifier
        toastNotif = ToastNotifier()
        toastNotif.show_toast(title,  text, threaded=True)
    elif os.name == "posix":
        from pync import Notifier
        Notifier.notify(text, title)