####################################################################
#################### MILITIAS GUIDEBOOK README #####################
####################################################################


########################## ORDNER-STRUKTUR #########################
o dataentry
| - admin.py (which content is manageable through the admin-page)
| - apps.py
| - models.py (which fields in database)
| - tests.py
| - urls.py (which url leads to which view)
| - views.py (which view uses which template with what data)
| o migrations (stages of migrations)
| o static
| | o dataentry
| | | -- pictures
| | | -- css-files 
| | | - styling.css (main css file, change colors, widths etc here)
| | | o alt (old css version of militias-db page)
| | | o fonts
| | | o js (javascript files)
| o templates
| | o dataentry
| | | -- html files (for each page of militias-guidebook)
        (changes in content here)
| | | - welcome.html (starting page, different layout)
| | | - home.html (base page, reference for all other html-files)
        (changes in navigation, header, footer... in home and welcome)
o lokal
| - settings.py (base_dir, allowed hosts, debug mode, change database,
    language, time zone, static root and url, ...)
| - urls.py (admin, data urls, general url specification)
| - wsgi.py (for apache to run properly?)

HOW TO UPDATE DATENBANK
	- SQLiteStudio
	- Beide Datenbanken laden
	- Tabelle "dataentry_pgag" in militias-db kopieren (zB mit Strg+C)
	- In Guidebook einfügen (zB mit Strg+V)
	- Meldung mit "Nein" beantworten (wir brauchen die Beziehungen zu 
    den anderen Tabellen nicht, denn die werden nicht ausgelesen)
	- Neuen Namen vergeben, da ja schon eine "dataentry_pgag" existiert
	- Die alte "dataentry_pgag" löschen
  - Die neue "dataentry_pgag" umbenennen in "dataentry_pgag" (wichtig, 
    sonst wird die Tabelle nicht richtig ausgelesen)
    
HOW TO INHALTE AKTUALISIEREN
  - Gehe zu dataentry > static > templates > dataentry
  - Suche das passende Template zur Seite, die aktualisiert werden soll
  - Inhalte ändern (alles, was in HTML erlaubt ist)
