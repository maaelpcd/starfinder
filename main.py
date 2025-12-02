from datetime import date, datetime

# Obtenir la date d'aujourd'hui
aujourdhui = date.today()
heure_actuelle = datetime.now().strftime("%H:%M:%S")
print(aujourdhui, heure_actuelle) 


