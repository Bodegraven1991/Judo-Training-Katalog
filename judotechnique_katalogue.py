import pandas as pd

import datetime

import judo_dictionaries as jd

# Initialisierung von Variablen, die später gebraucht werden
first_key_skipped = False

zeit = 0

# Funktion, um Übung dem Trainingsplan hinzuzufügen
def addtotrainlist(exercise, zeit=zeit):
    '''
    Hinzufügen von Übungen zum Trainingsplan.
    exercise = Name des Übungs-Dictionarys,
    zeit = fortlaufende Variable zeit, für die kommulierte Trainingsdauer,
    returns zeit
    '''
    jd.training_dict[exercise['Titel:']] = [exercise['Kategorie:'],exercise['Dauer [min]:'], exercise['Trainingsgeräte:']]

    zeit = zeit + exercise['Dauer [min]:']

    return zeit

# Start of the program loop
while True:
    print('''
Dieses Programm dient dem Zweck unsere Judo Übungsformen sortiert zu halten 
und bei der Trainingsforbereitung schnellen Zugriff auf sie zu haben. Wenn du das Programm
schließen möchtest, schreibe "Ende" oder "out" in dieser Abfrage und drücke Enter.
''')

# Abfrageebene 1
    abfrage1 = input('''Möchtest du 
(1) eine Übersicht bekommen oder 
(2) direkt nach einer Übungsform suchen
(3) dir den aktuellen Trainingsplan anzeigen lassen?
''')
    abfrage1 = abfrage1.lower()

    if abfrage1 == '1' or abfrage1 == '(1)' or abfrage1 == 'übersicht':

# Abfrageebene 2, falls in Ebene 1 Antwort (1) gegeben wurde.
        abfrage2 = input('''
Möchtest du 
(1) eine Auflistung aller verfügbaren Übungskategorien oder 
(2) eine Auflistung aller Übungsformen innerhalb einer Kategorie?
''')
        abfrage2 = abfrage2.lower()

# Falls in Ebene 2 Antwort (1) gewählt wurde -> Ausgabe aller möglichen Kategorien.
        if abfrage2 == '1' or abfrage2 == '(1)' or abfrage2 == 'kategorie':
            print()
            jd.kat_list.sort()

            for kat in jd.kat_list:
                print(kat)

            input()

# Falls in Ebene 2 Antwort (2) gewählt wurde --> Abfrage von welcher Kategorie man sich die Übungen auflisten lassen möchte.
        elif abfrage2 == '2' or abfrage2 == '(2)' or abfrage2 == 'übung':
# Abfrageebene 3
            abfrage3 = input('''
Die Übungen welcher Kategorie möchtest du aufgelistet bekommen?
''')
            abfrage3 = abfrage3.lower()

# Ausgabe der eingebenen Kategorieliste
            if abfrage3 == 'aufwärmen':
                print()
                jd.aufw_list.sort()

                for auf in jd.aufw_list:
                    print(auf)

                input()

            elif abfrage3 == 'reaktion':
                print()
                jd.reak_list.sort()

                for reak in jd.reak_list:
                    print(reak)

                input()

            elif abfrage3 == 'spiel':
                print()
                jd.spiel_list.sort()

                for spiel in jd.spiel_list:
                    print(spiel)

                input()

            elif abfrage3 == 'fallübung':
                print()
                jd.fall_list.sort()

                for fall in jd.fall_list:
                    print(fall)

                input()

            elif abfrage3 == 'mut':
                print()
                jd.mut_list.sort()

                for mut in jd.mut_list:
                    print(mut)

                input()

            elif abfrage3 == 'körperspannung':
                print()
                jd.spannung_list.sort()

                for spann in jd.spannung_list:
                    print(spann)

                input()

            elif abfrage3 == 'körperverständnis':
                print()
                jd.verständnis_list.sort()

                for verständnis in jd.verständnis_list:
                    print(verständnis)

                input()

            elif abfrage3 == 'wettkampf':
                print()
                jd.wettkampf_list.sort()

                for wettkampf in jd.wettkampf_list:
                    print(wettkampf)

                input()

            elif abfrage3 == 'haltegriff':
                print()
                jd.haltegriff_list.sort()

                for halten in jd.haltegriff_list:
                    print(halten)

                input()

            elif abfrage3 == 'randori':
                print()
                jd.randori_list.sort()

                for randori in jd.randori_list:
                    print(randori)

                input()

            elif abfrage3 == 'teamwork':
                print()
                jd.teamwork_list.sort()

                for team in jd.teamwork_list:
                    print(team)

                input()

            elif abfrage3 == 'entspannung':
                print()
                jd.entspannung_list.sort()

                for entsp in jd.entspannung_list:
                    print(entsp)

                input()

# Abfrageebene 2, falls in Ebene 1 die Antwort (2) gegeben wurde. Es wird nach dem Titel der Übungsform gefragt, für die man eine Detailübersicht bekommen möchte.
    elif abfrage1 == '2' or abfrage1 == '(2)' or abfrage1 == 'übungsform':
        abfrage4 = input('''
Wie ist der Titel der Übungsform?
''')
        abfrage4 = abfrage4.lower()

# Ausgabe der Übungsdetails der eingegeben Übungsform. Anschließende Abfrage, ob sie mithilfe der Funktion addtotrainlist dem Trainingsplan hinzugefügt werden soll.
        if abfrage4 == 'schattenlauf':
            print()

# Ausgabe der Details
            for key, value in jd.schattenlauf_dict.items():
                print(key, value)

# Abfrage, ob addtotrainlist ausgeführt werden soll
            abfrage_schattenlauf = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_schattenlauf = abfrage_schattenlauf.lower()

            if abfrage_schattenlauf == 'j' or abfrage_schattenlauf == 'ja':

                addtotrainlist(jd.schattenlauf_dict)
# Addition der Dauer der Übungs zur Gesamtdauer des Trainings.
                zeit = addtotrainlist(jd.schattenlauf_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'feuer, wasser, blitz':
            print()

            for key, value in jd.fwb_dict.items():
                print(key, value)

            abfrage_fwb = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_fwb = abfrage_fwb.lower()

            if abfrage_fwb == 'j' or abfrage_fwb == 'ja':

                addtotrainlist(jd.fwb_dict)
                zeit = addtotrainlist(jd.fwb_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'mattenklappen':
            print()

            for key, value in jd.mattenklappen_dict.items():
                print(key, value)

            abfrage_mattenklappen = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_mattenklappen = abfrage_mattenklappen.lower()

            if abfrage_mattenklappen == 'j' or abfrage_mattenklappen == 'ja':

                addtotrainlist(jd.mattenklappen_dict)
                zeit = addtotrainlist(jd.mattenklappen_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'auf-die-matte-springen':
            print()

            for key, value in jd.mattespringen_dict.items():
                print(key, value)

            abfrage_mattenspringen = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_mattenspringen = abfrage_mattenspringen.lower()

            if abfrage_mattenspringen == 'j' or abfrage_mattenspringen == 'ja':

                addtotrainlist(jd.mattespringen_dict)
                zeit = addtotrainlist(jd.mattespringen_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'elternklettern':
            print()

            for key, value in jd.elternklettern_dict.items():
                print(key, value)

            abfrage_elternklettern = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_elternklettern = abfrage_elternklettern.lower()

            if abfrage_elternklettern == 'j' or abfrage_elternklettern == 'ja':

                addtotrainlist(jd.elternklettern_dict)
                zeit = addtotrainlist(jd.elternklettern_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'reiten':
            print()

            for key, value in jd.reiten_dict.items():
                print(key, value)

            abfrage_reiten = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_reiten = abfrage_reiten.lower()

            if abfrage_reiten == 'j' or abfrage_reiten == 'ja':

                addtotrainlist(jd.reiten_dict)
                zeit = addtotrainlist(jd.reiten_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'um die bank rollen':
            print()

            for key, value in jd.umdiebank_dict.items():
                print(key, value)

            abfrage_umdiebank = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_umdiebank = abfrage_umdiebank.lower()

            if abfrage_umdiebank == 'j' or abfrage_umdiebank == 'ja':

                addtotrainlist(jd.umdiebank_dict)
                zeit = addtotrainlist(jd.umdiebank_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'purzelbaum':
            print()

            for key, value in jd.purzelbaum_dict.items():
                print(key, value)

            abfrage_purzelbaum = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_purzelbaum = abfrage_purzelbaum.lower()

            if abfrage_purzelbaum == 'j' or abfrage_purzelbaum == 'ja':

                addtotrainlist(jd.purzelbaum_dict)
                zeit = addtotrainlist(jd.purzelbaum_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'mäusefalle':
            print()

            for key, value in jd.mäusefalle_dict.items():
                print(key, value)

            abfrage_mäusefalle = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_mäusefalle = abfrage_mäusefalle.lower()

            if abfrage_mäusefalle == 'j' or abfrage_mäusefalle == 'ja':

                addtotrainlist(jd.mäusefalle_dict)
                zeit = addtotrainlist(jd.mäusefalle_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'drachenschatz':
            print()

            for key, value in jd.drachenschatz_dict.items():
                print(key, value)

            abfrage_drachenschatz = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_drachenschatz = abfrage_drachenschatz.lower()

            if abfrage_drachenschatz == 'j' or abfrage_drachenschatz == 'ja':

                addtotrainlist(jd.drachenschatz_dict)
                zeit = addtotrainlist(jd.drachenschatz_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'tiere nachmachen':
            print()

            for key, value in jd.tierenachmachen_dict.items():
                print(key, value)

            abfrage_tierenachmachen = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_tierenachmachen = abfrage_tierenachmachen.lower()

            if abfrage_tierenachmachen == 'j' or abfrage_tierenachmachen == 'ja':

                addtotrainlist(jd.tierenachmachen_dict)
                zeit = addtotrainlist(jd.tierenachmachen_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'löwenticken':
            print()

            for key, value in jd.löwenticken_dict.items():
                print(key, value)

            abfrage_löwenticken = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_löwenticken = abfrage_löwenticken.lower()

            if abfrage_löwenticken == 'j' or abfrage_löwenticken == 'ja':

                addtotrainlist(jd.löwenticken_dict)
                zeit = addtotrainlist(jd.löwenticken_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'babyaffen':
            print()

            for key, value in jd.babyaffen_dict.items():
                print(key, value)

            abfrage_babyaffen = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_babyaffen = abfrage_babyaffen.lower()

            if abfrage_babyaffen == 'j' or abfrage_babyaffen == 'ja':

                addtotrainlist(jd.babyaffen_dict)
                zeit = addtotrainlist(jd.babyaffen_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'hängebrücke':
            print()

            for key, value in jd.hängebrücke_dict.items():
                print(key, value)

            abfrage_hängebrücke = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_hängebrücke = abfrage_hängebrücke.lower()

            if abfrage_hängebrücke == 'j' or abfrage_hängebrücke == 'ja':

                addtotrainlist(jd.hängebrücke_dict)
                zeit = addtotrainlist(jd.hängebrücke_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'rasenmäher':
            print()

            for key, value in jd.rasenmäher_dict.items():
                print(key, value)

            abfrage_rasenmäher = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_rasenmäher = abfrage_rasenmäher.lower()

            if abfrage_rasenmäher == 'j' or abfrage_rasenmäher == 'ja':

                addtotrainlist(jd.rasenmäher_dict)
                zeit = addtotrainlist(jd.rasenmäher_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'kuscheltiere retten':
            print()

            for key, value in jd.tiereretten_dict.items():
                print(key, value)

            abfrage_tiereretten = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_tiereretten = abfrage_tiereretten.lower()

            if abfrage_tiereretten == 'j' or abfrage_tiereretten == 'ja':

                addtotrainlist(jd.tiereretten_dict)
                zeit = addtotrainlist(jd.tiereretten_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'haifische':
            print()

            for key, value in jd.haifische_dict.items():
                print(key, value)

            abfrage_haifische = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_haifische = abfrage_haifische.lower()

            if abfrage_haifische == 'j' or abfrage_haifische == 'ja':

                addtotrainlist(jd.haifische_dict)
                zeit = addtotrainlist(jd.haifische_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'atomspiel':
            print()

            for key, value in jd.atomspiel_dict.items():
                print(key, value)

            abfrage_atomspiel = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_atomspiel = abfrage_atomspiel.lower()

            if abfrage_atomspiel == 'j' or abfrage_atomspiel == 'ja':

                addtotrainlist(jd.atomspiel_dict)
                zeit = addtotrainlist(jd.atomspiel_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'baumfällen':
            print()

            for key, value in jd.baumfällen_dict.items():
                print(key, value)

            abfrage_baumfällen = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_baumfällen = abfrage_baumfällen.lower()

            if abfrage_baumfällen == 'j' or abfrage_baumfällen == 'ja':

                addtotrainlist(jd.baumfällen_dict)
                zeit = addtotrainlist(jd.baumfällen_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'cowboyspiel':
            print()

            for key, value in jd.cowboyspiel_dict.items():
                print(key, value)

            abfrage_cowboyspiel = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_cowboyspiel = abfrage_cowboyspiel.lower()

            if abfrage_cowboyspiel == 'j' or abfrage_cowboyspiel == 'ja':

                addtotrainlist(jd.cowboyspiel_dict)
                zeit = addtotrainlist(jd.cowboyspiel_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'robbe und eisbär':
            print()

            for key, value in jd.robbeeisbär_dict.items():
                print(key, value)

            abfrage_robbeeisbär = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_robbeeisbär = abfrage_robbeeisbär.lower()

            if abfrage_robbeeisbär == 'j' or abfrage_robbeeisbär == 'ja':

                addtotrainlist(jd.robbeeisbär_dict)
                zeit = addtotrainlist(jd.robbeeisbär_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'fischer, fischer':
            print()

            for key, value in jd.fischerfischer_dict.items():
                print(key, value)

            abfrage_fischerfischer = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_fischerfischer = abfrage_fischerfischer.lower()

            if abfrage_fischerfischer == 'j' or abfrage_fischerfischer == 'ja':

                addtotrainlist(jd.fischerfischer_dict)
                zeit = addtotrainlist(jd.fischerfischer_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'bahnenübungen':
            print()

            for key, value in jd.bahnen_dict.items():
                print(key, value)

            abfrage_bahnen = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_bahnen = abfrage_bahnen.lower()

            if abfrage_bahnen == 'j' or abfrage_bahnen == 'ja':

                addtotrainlist(jd.bahnen_dict)
                zeit = addtotrainlist(jd.bahnen_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'marionettenspiel':
            print()

            for key, value in jd.marionetten_dict.items():
                print(key, value)

            abfrage_marionetten = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_marionetten = abfrage_marionetten.lower()

            if abfrage_marionetten == 'j' or abfrage_marionetten == 'ja':

                addtotrainlist(jd.marionetten_dict)
                zeit = addtotrainlist(jd.marionetten_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'fischer holt die netze ein':
            print()

            for key, value in jd.fischernetz_dict.items():
                print(key, value)

            abfrage_fischernetz = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_fischernetz = abfrage_fischernetz.lower()

            if abfrage_fischernetz == 'j' or abfrage_fischernetz == 'ja':

                addtotrainlist(jd.fischernetz_dict)
                zeit = addtotrainlist(jd.fischernetz_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'druck fühlen':
            print()

            for key, value in jd.druckfühlen_dict.items():
                print(key, value)

            abfrage_druckfühlen = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_druckfühlen = abfrage_druckfühlen.lower()

            if abfrage_druckfühlen == 'j' or abfrage_druckfühlen == 'ja':

                addtotrainlist(jd.druckfühlen_dict)
                zeit = addtotrainlist(jd.druckfühlen_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'sortieren auf der bank':
            print()

            for key, value in jd.sortierenbank_dict.items():
                print(key, value)

            abfrage_sortierenbank = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_sortierenbank = abfrage_sortierenbank.lower()

            if abfrage_sortierenbank == 'j' or abfrage_sortierenbank == 'ja':

                addtotrainlist(jd.sortierenbank_dict)
                zeit = addtotrainlist(jd.sortierenbank_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'zeitungstanz':
            print()

            for key, value in jd.zeitungstanz_dict.items():
                print(key, value)

            abfrage_zeitungstanz = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_zeitungstanz = abfrage_zeitungstanz.lower()

            if abfrage_zeitungstanz == 'j' or abfrage_zeitungstanz == 'ja':

                addtotrainlist(jd.zeitungstanz_dict)
                zeit = addtotrainlist(jd.zeitungstanz_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'deckenwende':
            print()

            for key, value in jd.deckenwende_dict.items():
                print(key, value)

            abfrage_deckenwende = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_deckenwende = abfrage_deckenwende.lower()

            if abfrage_deckenwende == 'j' or abfrage_deckenwende == 'ja':

                addtotrainlist(jd.deckenwende_dict)
                zeit = addtotrainlist(jd.deckenwende_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'hexenticken':
            print()

            for key, value in jd.hexenticken_dict.items():
                print(key, value)

            abfrage_hexenticken = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_hexenticken = abfrage_hexenticken.lower()

            if abfrage_hexenticken == 'j' or abfrage_hexenticken == 'ja':

                addtotrainlist(jd.hexenticken_dict)
                zeit = addtotrainlist(jd.hexenticken_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'staffellauf':
            print()

            for key, value in jd.staffellauf_dict.items():
                print(key, value)

            abfrage_staffellauf = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_staffellauf = abfrage_staffellauf.lower()

            if abfrage_staffellauf == 'j' or abfrage_staffellauf == 'ja':

                addtotrainlist(jd.staffellauf_dict)
                zeit = addtotrainlist(jd.staffellauf_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'wäscheklammerklau':
            print()

            for key, value in jd.wäscheklammer_dict.items():
                print(key, value)

            abfrage_wäscheklammer = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_wäscheklammer = abfrage_wäscheklammer.lower()

            if abfrage_wäscheklammer == 'j' or abfrage_wäscheklammer == 'ja':

                addtotrainlist(jd.wäscheklammer_dict)
                zeit = addtotrainlist(jd.wäscheklammer_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'seitwärts aus dem kniestand':
            print()

            for key, value in jd.seitwärtsknie_dict.items():
                print(key, value)

            abfrage_seitwärtsknie = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_seitwärtsknie = abfrage_seitwärtsknie.lower()

            if abfrage_seitwärtsknie == 'j' or abfrage_seitwärtsknie == 'ja':

                addtotrainlist(jd.seitwärtsknie_dict)
                zeit = addtotrainlist(jd.seitwärtsknie_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'seitwärts am partner':
            print()

            for key, value in jd.seitwärtspartner_dict.items():
                print(key, value)

            abfrage_seitwärtspartner = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_seitwärtspartner = abfrage_seitwärtspartner.lower()

            if abfrage_seitwärtspartner == 'j' or abfrage_seitwärtspartner == 'ja':

                addtotrainlist(jd.seitwärtspartner_dict)
                zeit = addtotrainlist(jd.seitwärtspartner_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'kitzelhai':
            print()

            for key, value in jd.kitzelhai_dict.items():
                print(key, value)

            abfrage_kitzelhai = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_kitzelhai = abfrage_kitzelhai.lower()

            if abfrage_kitzelhai == 'j' or abfrage_kitzelhai == 'ja':

                addtotrainlist(jd.kitzelhai_dict)
                zeit = addtotrainlist(jd.kitzelhai_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'körperkreisel':
            print()

            for key, value in jd.körperkreisel_dict.items():
                print(key, value)

            abfrage_kreisel = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_kreisel = abfrage_kreisel.lower()

            if abfrage_kreisel == 'j' or abfrage_kreisel == 'ja':

                addtotrainlist(jd.körperkreisel_dict)
                zeit = addtotrainlist(jd.körperkreisel_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'knie über kopf':
            print()

            for key, value in jd.knieüberkopf_dict.items():
                print(key, value)

            abfrage_knieüberkopf = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_knieüberkopf = abfrage_knieüberkopf.lower()

            if abfrage_knieüberkopf == 'j' or abfrage_knieüberkopf == 'ja':

                addtotrainlist(jd.knieüberkopf_dict)
                zeit = addtotrainlist(jd.knieüberkopf_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'seitliche rolle':
            print()

            for key, value in jd.seitlicherolle_dict.items():
                print(key, value)

            abfrage_seitlicherolle = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_seitlicherolle = abfrage_seitlicherolle.lower()

            if abfrage_seitlicherolle == 'j' or abfrage_seitlicherolle == 'ja':

                addtotrainlist(jd.seitlicherolle_dict)
                zeit = addtotrainlist(jd.seitlicherolle_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'das freche sofa':
            print()

            for key, value in jd.frechessofa_dict.items():
                print(key, value)

            abfrage_frechessofa = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_frechessofa = abfrage_frechessofa.lower()

            if abfrage_frechessofa == 'j' or abfrage_frechessofa == 'ja':

                addtotrainlist(jd.frechessofa_dict)
                zeit = addtotrainlist(jd.frechessofa_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'reaktionsübungen':
            print()

            for key, value in jd.reaktionsübungen_dict.items():
                print(key, value)

            abfrage_reaktionsübungen = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_reaktionsübungen = abfrage_reaktionsübungen.lower()

            if abfrage_reaktionsübungen == 'j' or abfrage_reaktionsübungen == 'ja':

                addtotrainlist(jd.reaktionsübungen_dict)
                zeit = addtotrainlist(jd.reaktionsübungen_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'zwischen die beine springen':
            print()

            for key, value in jd.zwischendiebeine_dict.items():
                print(key, value)

            abfrage_zwischendiebeine = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_zwischendiebeine = abfrage_zwischendiebeine.lower()

            if abfrage_zwischendiebeine == 'j' or abfrage_zwischendiebeine == 'ja':

                addtotrainlist(jd.zwischendiebeine_dict)
                zeit = addtotrainlist(jd.zwischendiebeine_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'ballbrücke':
            print()

            for key, value in jd.ballbrücke_dict.items():
                print(key, value)

            abfrage_ballbrücke = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_ballbrücke = abfrage_ballbrücke.lower()

            if abfrage_ballbrücke == 'j' or abfrage_ballbrücke == 'ja':

                addtotrainlist(jd.ballbrücke_dict)
                zeit = addtotrainlist(jd.ballbrücke_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'burgerspiel':
            print()

            for key, value in jd.burgerspiel_dict.items():
                print(key, value)

            abfrage_burgerspiel = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_burgerspiel = abfrage_burgerspiel.lower()

            if abfrage_burgerspiel == 'j' or abfrage_burgerspiel == 'ja':

                addtotrainlist(jd.burgerspiel_dict)
                zeit = addtotrainlist(jd.burgerspiel_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'rugbykampf':
            print()

            for key, value in jd.rugbykampf_dict.items():
                print(key, value)

            abfrage_rugbykampf = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_rugbykampf = abfrage_rugbykampf.lower()

            if abfrage_rugbykampf == 'j' or abfrage_rugbykampf == 'ja':

                addtotrainlist(jd.rugbykampf_dict)
                zeit = addtotrainlist(jd.rugbykampf_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'ball auf dem schwungtuch':
            print()

            for key, value in jd.ballschwungtuch_dict.items():
                print(key, value)

            abfrage_ballschwungtuch = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_ballschwungtuch = abfrage_ballschwungtuch.lower()

            if abfrage_ballschwungtuch == 'j' or abfrage_ballschwungtuch == 'ja':

                addtotrainlist(jd.ballschwungtuch_dict)
                zeit = addtotrainlist(jd.ballschwungtuch_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'die wand':
            print()

            for key, value in jd.diewand_dict.items():
                print(key, value)

            abfrage_diewand = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_diewand = abfrage_diewand.lower()

            if abfrage_diewand == 'j' or abfrage_diewand == 'ja':

                addtotrainlist(jd.diewand_dict)
                zeit = addtotrainlist(jd.diewand_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'partner-bodenakrobatik':
            print()

            for key, value in jd.bodenakro_dict.items():
                print(key, value)

            abfrage_bodenakro = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_bodenakro = abfrage_bodenakro.lower()

            if abfrage_bodenakro == 'j' or abfrage_bodenakro == 'ja':

                addtotrainlist(jd.bodenakro_dict)
                zeit = addtotrainlist(jd.bodenakro_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'pyramide':
            print()

            for key, value in jd.pyramide_dict.items():
                print(key, value)

            abfrage_pyramide = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_pyramide = abfrage_pyramide.lower()

            if abfrage_pyramide == 'j' or abfrage_pyramide == 'ja':

                addtotrainlist(jd.pyramide_dict)
                zeit = addtotrainlist(jd.pyramide_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'dreier-randori':
            print()

            for key, value in jd.dreierrandori_dict.items():
                print(key, value)

            abfrage_dreierrandori = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_dreierrandori = abfrage_dreierrandori.lower()

            if abfrage_dreierrandori == 'j' or abfrage_dreierrandori == 'ja':

                addtotrainlist(jd.dreierrandori_dict)
                zeit = addtotrainlist(jd.dreierrandori_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'fahrrad fahren':
            print()

            for key, value in jd.fahrradfahren_dict.items():
                print(key, value)

            abfrage_fahrradfahren = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_fahrradfahren = abfrage_fahrradfahren.lower()

            if abfrage_fahrradfahren == 'j' or abfrage_fahrradfahren == 'ja':

                addtotrainlist(jd.fahrradfahren_dict)
                zeit = addtotrainlist(jd.fahrradfahren_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'traumreise':
            print()

            for key, value in jd.traumreise_dict.items():
                print(key, value)

            abfrage_traumreise = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_traumreise = abfrage_traumreise.lower()

            if abfrage_traumreise == 'j' or abfrage_traumreise == 'ja':

                addtotrainlist(jd.traumreise_dict)
                zeit = addtotrainlist(jd.traumreise_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'pizzabacken':
            print()

            for key, value in jd.pizzabacken_dict.items():
                print(key, value)

            abfrage_pizzabacken = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_pizzabacken = abfrage_pizzabacken.lower()

            if abfrage_pizzabacken == 'j' or abfrage_pizzabacken == 'ja':

                addtotrainlist(jd.pizzabacken_dict)
                zeit = addtotrainlist(jd.pizzabacken_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'reifenringen':
            print()

            for key, value in jd.reifenringen_dict.items():
                print(key, value)

            abfrage_reifenringen = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_reifenringen = abfrage_reifenringen.lower()

            if abfrage_reifenringen == 'j' or abfrage_reifenringen == 'ja':

                addtotrainlist(jd.reifenringen_dict)
                zeit = addtotrainlist(jd.reifenringen_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

# Ausgabe, falls in Abfrageebene 1 die Antwort (3) war -> Ausgabe des derzeitigen Trainingsplans.
    elif abfrage1 == '3' or abfrage1 == '(3)' or abfrage1 == 'Trainingsplan':
        print()

# Loopen durch das Trainingsplan-Dictionary und Ausgabe als formatierte Tabelle
        for x in jd.training_dict:
            key = x
            value1 = jd.training_dict[key][0]
            value2 = jd.training_dict[key][1]
            value3 = jd.training_dict[key][2]
            print(f"{key:<40} {value1:<40} {value2:<20} {value3:<40}")

# Ausgabe der aufkommulierten zeit Variable
        print('Das Training dauert etwa ' + (str(zeit)) + ' Minuten.')
        print()

# Abfrage, ob der derzeitige Trainingsplan als Excel File exportiert werden soll.
        abfrage_print = input('Soll der Trainingsplan als Excelsheet exporiert werden? (j/n)')
        abfrage_print = abfrage_print.lower()

        if abfrage_print == 'j' or abfrage_print == 'ja':

# Exportieren als Excel File
            data = {
                'Übung': [],
                'Kategorie': [],
                'Dauer [min]': [],
                'Trainingsgeräte': []
            }

            for x in jd.training_dict:
                key = x
                if not first_key_skipped:
                    first_key_skipped = True
                    continue  # Skip the first iteration

                data['Übung'].append(key)
                data['Kategorie'].append(jd.training_dict[key][0])
                data['Dauer [min]'].append(jd.training_dict[key][1])
                data['Trainingsgeräte'].append(jd.training_dict[key][2])

# Umformulieren des data Dictionaries als Pandas Data Frame
            df = pd.DataFrame(data)

# Erstellen einer Variablen mit dem aktuellen Datum
            current_date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
            current_date = current_date.replace(':', '_')

# Namen des neuen Files erstellen
            excel_file_path = current_date + '_Trainingsplan Judo.xlsx'

# Exportieren des Files
            df.to_excel(excel_file_path, index=False)

            print()

            print("Das Excelsheet wurde erfolgreich mit dem Namen " + excel_file_path + ' erstellt.')

            input()

# Beenden des Programmloops
    else:
        # Exit the program if the user inputs something other than the valid statements
        break
