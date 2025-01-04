from plyer import notification

def send_notification(series_name):
    notification.notify(
        title="Nouvelle saison disponible !",
        message=f"La nouvelle saison de {series_name} est maintenant disponible !",
        timeout=10
    )
