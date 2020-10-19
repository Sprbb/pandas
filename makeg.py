import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

# Lees de data in en merge de datum en tijdcel. Zorg dat de datum vooraanstaat ipv de maand.
tempvocht_data = pd.read_csv('tempvocht.csv', parse_dates=[['Datum', 'Tijd']], dayfirst=True)
# Informeer welk type variabelen gevuld zijn.
tempvocht_data.info()
# maak een figuur aan en assen om op te plotten
fig, ax1 = plt.subplots()
# Plot de data voor de linker Y-as
ax1.plot(tempvocht_data['Datum_Tijd'], tempvocht_data['Temperatuur'])
# Grafiektitel
ax1.set_title('Temperatuurverloop 19/20')
# As-label X-as
ax1.set_xlabel('Tijd')
# As-label linker Y-as
ax1.set_ylabel('Temperatuur')
# De twin aanmaken
ax2 = ax1.twinx()
# Plot de data voor de rechter Y-as
ax2.plot(tempvocht_data['Datum_Tijd'], tempvocht_data['Luchtvochtigheid'])
# As-label rechter Y-as
ax2.set_ylabel('Relatieve luchtvochtigheid')
#plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=50))
# beautify the x-labels
plt.gcf().autofmt_xdate()
# Laat de plot zien.
plt.show()