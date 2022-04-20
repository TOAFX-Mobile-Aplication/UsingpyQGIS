import urllib.request
import zipfile
import os
from shutil import copyfile
from pathlib import Path

DOP_Kachelnummern=[3505616,3505614] #hier mit Komma getrennt alle Kachelnummern eingeben die abgerufen werden sollen


SpeicherordnerDOP="C:/Users/IvoP/Downloads/DOP/" ##Hier den Speicherort der DOP eintragen. Kein \ sondern / verwenden

for DOP in DOP_Kachelnummern:
    #Download der DOP Daten
    urllib.request.urlretrieve("https://geocloud.landesvermessung.sachsen.de/index.php/s/qibG253ZRoYsmO8/download?path=%2F&amp;&files="+"dop20c_"+str(DOP)+".zip", SpeicherordnerDOP+str(DOP)+".zip")

    #DOP entpacken --> es entsteht eine TIF Datei
    with zipfile.ZipFile(SpeicherordnerDOP+str(DOP)+".zip","r") as zip_ref:
        zip_ref.extractall(SpeicherordnerDOP)

    #ZIP DOP lÃ¶schen
    os.remove(SpeicherordnerDOP+str(DOP)+".zip")
    

tmpDOP = QgsRasterLayer(SpeicherordnerDOP+"dop20c_33350_5616.tif",str(DOP))
QgsProject.instance().addMapLayer(tmpDOP)

tmpDOP = QgsRasterLayer(SpeicherordnerDOP+"dop20c_33350_5614.tif",str(DOP))
QgsProject.instance().addMapLayer(tmpDOP)

print('FERTIG')