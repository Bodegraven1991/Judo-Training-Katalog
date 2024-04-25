# In diesem File sind die Dictionaries zu finden, in denen die Informationen zu den verschiedenen Übungen zu finden sind.

# Dictionary für all die verschiedenen Überkategorien
kat_list = ['Aufwärmen', 'Reaktion', 'Spiel', 'Entspannung', 'Fallübung', 'Mut', 'Teamwork', 'Körperspannung', 'Körperverständnis', 'Wettkampf', 'Haltegriff', 'Randori']

# Initialisieren der Kategorienlisten. Diese werden bei den verschiedenen Übungsformen nach und nach gefüllt.
aufw_list = []
reak_list = []
spiel_list = []
fall_list = []
mut_list = []
spannung_list = []
verständnis_list = []
wettkampf_list = []
haltegriff_list = []
randori_list = []
teamwork_list = []
entspannung_list = []

# Initialisierung des Dictionarys für den Trainingsplan
training_dict = {'Übung': ['Kategorie', 'Dauer [min]', 'Trainingsgeräte']}

# Ab hier kommen die Dictionaries für die einzelnen Übungen

# Übung: Schattenlauf
schattenlauf_dict = {
    'Titel:': 'Schattenlauf',
    'Kategorie:': 'Aufwärmen, Reaktion',
    'Dauer [min]:': 5,
    'Trainingsgeräte:': '-',
    'Beschreibung:': '''
Das Eltern-Kind-Paar teilt sich in einen Vorahnenden und einen Schatten. Die Übung besteht darin, 
dass der Schatten aufmerksam beobachtet, und die Bewegungen des Vorahnenden genau wiederholt. 
Nach einer gewissen Zeit wechselt die Rolle. Bei dem Spiel ist “alles” erlaubt: 
Es darf geklettert, gerollt, gehüpft, gekrabbelt werden.
'''}
aufw_list.append('Schattenlauf')
reak_list.append('Schattenlauf')

# Übung: Feuer, Wasser, Blitz
fwb_dict = {
    'Titel:': 'Feuer, Wasser, Blitz',
    'Kategorie:': 'Aufwärmen, Spiel',
    'Dauer [min]:': 5,
    'Trainingsgeräte:': 'ggf. Weichbodenmatte',
    'Beschreibung:': '''
Eltern und Kinder laufen in der Halle durcheinander. Auf ein bestimmtes Kommando hin, 
muss an einen bestimmten Ort gerannt und eine bestimmte Aktion durchgeführt werden. 
Beispiel: Feuer: in eine Hallenecke laufen. Wasser: auf eine Weichbodenmatte springen. 
Blitz: auf der Judomatte auf den Bauch legen. Alternativen: auf eine Bank klettern, 
auf einem Bein stehen. Das Spiel dient dem Aufwärmen, funktioniert aber auch oft gut, 
um gerade neuen Kindern ein wenig Nervosität zu nehmen.
'''}
aufw_list.append('Feuer,Wasser,Blitz')
spiel_list.append('Feuer,Wasser,Blitz')

# Übung: Mattenklappen
mattenklappen_dict = {
    'Titel:': 'Mattenklappen',
    'Kategorie:': 'Aufwärmen, Fallübung, Mut',
    'Dauer [min]:': 5,
    'Trainingsgeräte:': 'Weichbodenmatten',
    'Beschreibung:': '''
Die großen Weichbodenmatten werden aufgestellt, Eltern und Kinder stellen sich auf 
eine Seite davon und drücken gegen die Matte, sodass sie gemeinsam mit ihr umfallen. 
Die Übung den Kindern eigentlich immer Spaß, weil die Matten so schön laut knallen 
und weil man noch oft mit der Matte ein wenig rutscht. Außerdem ist die Übung dazu gedacht, 
den Kindern ein wenig die Angst vor dem Gefühl des Fallens zu nehmen.
'''}
aufw_list.append('Mattenklappen')
fall_list.append('Mattenklappen')
mut_list.append('Mattenklappen')

# Übung: Auf-die-Matte-springen
mattespringen_dict = {
    'Titel:': 'Auf-die-Matte-springen',
    'Kategorie:': 'Aufwärmen, Fallübung, Mut',
    'Dauer [min]:': 5,
    'Trainingsgeräte:': 'Weichbodenmatten',
    'Beschreibung:': '''
Eltern und Kinder dürfen frei und so wild wie sie wollen auf die Weichbodenmatten springen. 
Das dient zum einen dem Aufwärmen, aber zum anderen auch dazu die Angst vor dem Fallen 
abzubauen. Wir haben festgestellt, dass es nicht empfehlenswert ist, wenn die Kinder 
(auch vorsichtig) auf die Matte geschmissen werden. Dadurch, dass sie noch nicht so eine 
gute Körperspannung haben, tun sie sich eigentlich immer weh, auch wenn man ganz behutsam ist.
'''}
aufw_list.append('Auf-die-Matte-springen')
fall_list.append('Auf-die-Matte-springen')
mut_list.append('Auf-die-Matte-springen')

# Übung: Elternklettern
elternklettern_dict = {
    'Titel:': 'Elternklettern',
    'Kategorie:': 'Körperspannung, Mut',
    'Dauer [min]:': 3,
    'Trainingsgeräte:': '-',
    'Beschreibung:': '''
Das Elternteil stellt sich im Jigotai (tief in den Knien, sodass sie Knie im rechten Winkel 
stehen) und das Kind klettert eigenständig auf dem Elternteil herum. Das Elternteil gibt 
dabei nur Unterstützung, wenn es notwendig ist. Varianten: 1) Das Kind klettern auf der 
Bauchseite hoch und dann seitlich einmal herum. 2) Das Kind klettert auf die Schultern hoch. 
3) Das Kind klettert den Rücken hoch, auf die Schulter und dann kopfüber den Bauch wieder 
herunter (hierbei ist natürlich mehr Unterstützung notwendig.
'''}
spannung_list.append('Elternklettern')
mut_list.append('Elternklettern')

# Übung: Reiten
reiten_dict = {
    'Titel:': 'Reiten',
    'Kategorie:': 'Körperverständnis und -spannung, Mut',
    'Dauer [min]:': 5,
    'Trainingsgeräte:': '-',
    'Beschreibung:': '''
Die Kinder dürfen auf dem Rücken der Eltern reiten. Wenn das Kind sich sicher fühlt, 
darf man auch über Hindernisse krabbeln. Varianten für den Sitz des Kindes: 
flach auf dem Rücken Bauch liegend, Rücken auf Rücken, sitzend, Damensitz, 
auf dem Rücken kniend, auf dem Rücken stehend.
'''}
spannung_list.append('Reiten')
verständnis_list.append('Reiten')
mut_list.append('Reiten')

umdiebank_dict = {
    'Titel:': 'Um die Bank rollen',
    'Kategorie:': 'Fallübung',
    'Dauer [min]:': 3,
    'Trainingsgeräte:': '-',
    'Beschreibung:': '''
Elternteil macht eine hohe Bank und das Kind legt sich quer auf den Rücken. 
Das Elternteil greift dann mit dem kopfseitigen Arm um den Kopf des Kindes und 
legt die Hand in den Nacken. Das Kind kann dann um die Bank herumgeführt werden, 
sodass es auf dem Rücken unter der Bank landet. Ist ein langsames Heranführen an 
das Überkopf-sein.
'''}
fall_list.append('Um die Bank rollen')

purzelbaum_dict = {
    'Titel:': 'Um die Bank rollen',
    'Kategorie:': 'Fallübung, Körperverständnis',
    'Dauer [min]:': 5,
    'Trainingsgeräte:': '-',
    'Beschreibung:': '''
Die Teilnehmer sollen Purzelbäume machen. Wer es gut kann, darf gerne den 
Rückwärtspurzelbaum ausprobieren. Den werden wenige (auch von den Eltern) hinbekommen, 
aber es ist eine gute Übung, um Körperverständnis aufzubauen.
'''}
fall_list.append('Purzelbaum')
verständnis_list.append('Purzelbaum')

mäusefalle_dict = {
    'Titel:': 'Mäusefalle',
    'Kategorie:': 'Spiel, Haltegriff, Wettkampf',
    'Dauer [min]:': 5,
    'Trainingsgeräte:': '-',
    'Beschreibung:': '''
Die Erwachsenen machen eine hohe Bank. Die Kinder sollen darunter durchkriechen. 
Anfänger kriechen erst einmal auf dem Bauch, aber später sollen sie sich auf dem 
Rücken unter der Bank durchschieben. Wenn das Kind zur Hälfte unter der Bank ist, 
schnappt die Mäusefalle zu: Die hohe Bank wird ganze eng und klein gemacht 
(quasi ein Mune Gatame). Das Kind muss sich jetzt durch Rausdrehen und -winden befreien. 
Die Übung soll die Angst davor nehmen, am Boden fixiert zu werden und ist eine Vorstufe 
von dem Befreien aus Haltegriffen. Gleichzeitig ist es schon ein schönes Rangel-Spiel.
'''}
spiel_list.append('Mäusefalle')
wettkampf_list.append('Mäusefalle')
haltegriff_list.append('Mäusefalle')

drachenschatz_dict = {
    'Titel:': 'Drachenschatz',
    'Kategorie:': 'Spiel, Randori, Wettkampf',
    'Dauer [min]:': 10,
    'Trainingsgeräte:': 'Schätze (zB. Bälle)',
    'Beschreibung:': '''
Zu zweit braucht man einen Schatz (wir nehmen immer Bälle). Einer ist der Drache, 
der den Schatz verteidigen muss. Der andere ist ein Ritter, der den Schatz stehlen will. 
Dabei darf nicht aufgestanden werden. Der Schatz darf unter dem Drachen versteckt werden, 
aber auch z.B. hinter dem Rücken. Ein schönes Spiel, um auf Bodenrandori vorzubereiten. 
Die Kinder tun sich nicht so schnell weh, weil sie sich auf den Ball konzentrieren und 
nicht so sehr auf den Gegner.
'''}
spiel_list.append('Drachenschatz')
wettkampf_list.append('Drachenschatz')
randori_list.append('Drachenschatz')

tierenachmachen_dict = {
    'Titel:': 'Tiere nachmachen',
    'Kategorie:': 'Aufwärmen, Körperverständnis',
    'Dauer [min]:': 5,
    'Trainingsgeräte:': '-',
    'Beschreibung:': '''
Es werden Sportübungen in Bahnen gemacht, aber das ganze wird als so verpackt, 
dass man Tiere nachahmt. Dabei kann man gerne die Kinder Tiere vorschlagen lassen, 
zB nach ihrem Lieblingstier fragen. Bei uns beliebte Beispiele: Giraffe = ganz groß machen, 
auf Zehenspitzen laufen, Spinne/Krebs = Spinnengang (für Krebs natürlich seitlich), 
Gecko = flach auf dem Boden krabbeln, Gürteltier = Purzelbaum, Robbe = robben, 
Shrimp = Hüfte rausschieben, Gepard = schnell rennen, Känguru = hopsen, Frosch = tief hopsen, 
Storch = Storchengang. Der Fantasie sind keine Grenzen gesetzt.
'''}
aufw_list.append('Tiere nachmachen')
verständnis_list.append('Tiere nachmachen')

löwenticken_dict = {
    'Titel:': 'Löwenticken',
    'Kategorie:': 'Spiel',
    'Dauer [min]:': 8,
    'Trainingsgeräte:': '-',
    'Beschreibung:': '''
Ein Teilnehmer ist Löwe und muss auf allen vieren die anderen fangen. Sobald mal vom Löwen 
am Bauch berührt wird, muss man auch auf alle viere und ist ein Löwe. Der letzte, 
der noch steht, ist neuer Löwe. Bei größeren Kindern (am besten sollten sie auch Judoanzüge 
haben) kann man das so spielen, dass der Löwe die Gejagten zu Boden reißen muss. 
Sobald man mit etwas anderem als den Füßen die Matte berührt, ist man Löwe.
'''}
spiel_list.append('Löwenticken')

babyaffen_dict = {
    'Titel:': 'Babyaffen',
    'Kategorie:': 'Körperspannung',
    'Dauer [min]:': 2,
    'Trainingsgeräte:': '-',
    'Beschreibung:': '''
Die Eltern krabbeln auf allen vieren und die Kinder hängen sich an den Bauch. 
Am besten mit den Beinen an der Hüfte des Elternteils festhalten und mit den 
Hängen am Nacken.
'''}
spannung_list.append('Babyaffen')

hängebrücke_dict = {
    'Titel:': 'Hängebrücke',
    'Kategorie:': 'Mut',
    'Dauer [min]:': 5,
    'Trainingsgeräte:': 'Weichbodenmatte',
    'Beschreibung:': '''
Immer zwei Eltern stehen sich gegenüber und halten sich so an den Händen, 
dass alle vier Hände zusammen eine Plattform ergeben. So stellen sich alle Elternpaare 
(auf einer Weichbodenmatte) nebeneinander und die Kinder dürfen darüber klettern 
und am Ende auf die Weichbodenmatte springen.
'''}
mut_list.append('Hängebrücke')

rasenmäher_dict = {
    'Titel:': 'Rasenmäher',
    'Kategorie:': 'Aufwärmen, Spiel',
    'Dauer [min]:': 3,
    'Trainingsgeräte:': 'Seile/Gürtel',
    'Beschreibung:': '''
Mehrere Schnüre werden zusammengebunden, sodass sie so lang sind, wie die Mattenfläche breit. 
Alle Teilnehmer müssen an ein Mattenende und die Schnur startet auf der Gegenseite. 
Die Teilnehmer müssen nun immer wieder ans andere Mattenende laufen und die Schnur kommt 
ihnen dabei entgegen. Entweder müssen sie drüber springen oder drunter durch tauchen.
'''}
aufw_list.append('Rasenmäher')
spiel_list.append('Rasenmäher')

tiereretten_dict = {
    'Titel:': 'Kuscheltiere retten',
    'Kategorie:': 'Körperspannung und -verständnis',
    'Dauer [min]:': 5,
    'Trainingsgeräte:': '-',
    'Beschreibung:': '''
Die Kinder sollen ein Kuscheltier zum Training mitbringen und mit diesem werden dann 
mehrere Übungen gemacht. Beispiele: 
(1) Sie sollen auf dem Rücken liegen, es mit den Füßen von einer hohen Matte holen, 
in die Hand nehmen und zurücklegen. 
(2) Sie sollen es auf dem Rücken liegend mit den Füßen aufheben und über dem Kopf 
wieder ablegen. 
(3) Auf dem Bauch liegend: mit den Händen von vor dem Kopf aufheben, 
auf den eigenen Rücken legen und wieder nach vorne legen. 
(4) Mit dem Kinn einklemmen und einen Purzelbaum machen. 
(5) Knien und es mit der Hand zwischen den eigenen Beinen durchschieben und 
dann eine Rolle machen.
'''}
spannung_list.append('Kuscheltiere retten')
verständnis_list.append('Kuscheltiere retten')

haifische_dict = {
    'Titel:': 'Haifische',
    'Kategorie:': 'Spiel, Wettkampf',
    'Dauer [min]:': 5,
    'Trainingsgeräte:': 'Weichbodenmatte',
    'Beschreibung:': '''
Es wird eine Weichbodenmatte in die Mitte der Mattenfläche gelegt und alle Teilnehmer 
bis auf einen müssen auf die Matte. Der eine Übrige ist der Hai und versucht sich 
einzelne Fische von der Matte zu ziehen. Wer von der Matte gezogen wurde, ist auch ein Hai. 
Das Spiel sollte nicht mit zu vielen Teilnehmern gespielt werden und die Kinder sollten 
schon etwas größer sein. Sonst ist es anfällig dafür, dass sich jemand weh tut.
'''}
spiel_list.append('Haifische')
wettkampf_list.append('Haifische')

atomspiel_dict = {
    'Titel:': 'Atomspiel',
    'Kategorie:': 'Körperverständnis, Spiel',
    'Dauer [min]:': 5,
    'Trainingsgeräte:': '-',
    'Beschreibung:': '''
Alle Teilnehmer laufen durcheinander, irgendwann kommt das Kommando Atom X und 
eine Ansage welche Körperteile insgesamt den Boden berühren dürfen. 
Dann müssen sich X Teilnehmer zusammenfinden und einen Weg finden, wie nur 
diese Körperteile den Boden berühren. Zum Beispiel: Atom 3, ein Kopf, zwei Füße, zwei Hände.
'''}
verständnis_list.append('Atomspiel')
spiel_list.append('Atomspiel')

baumfällen_dict = {
    'Titel:': 'Baumfällen',
    'Kategorie:': 'Fallübung, Körperspannung',
    'Dauer [min]:': 10,
    'Trainingsgeräte:': 'Weichbodenmatten',
    'Beschreibung:': '''
Es wird eine Geschichte mit mehreren aufeinanderfolgenden Übungen erzählt. 
Die Kinder wollen einen Baum fällen. 
(1) Dafür müssen sie zunächst auf den Baum klettern und ihn begutachten. 
Dafür stellen die Eltern sich im Jigotai hin und die Kinder sollen einmal drum herum klettern. 
(2) Dann wollen sie den Baum fällen. Dafür stellt sich einer ganz steif und 
gerade als Baum auf eine Weichbodenmatte, der andere darf dann den Baum fällen. 
Beim Umfallen muss der Baum ganz steif bleiben und sich nicht mit den Händen abfangen. 
(3) Als nächstes wollen sie den Baum nach Hause rollen, müssen aber feststellen, 
dass sie Äste beim Rollen stören. Der Baum legt die Arme als Äste raus und 
die Kinder sollen feststellen, dass das Rollen einfacher geht, wenn die Arme (Äste) 
entfernt sind. 
(4) Zuletzt kommt noch ein kleines Spielchen, wo wir eine Baumstamm-Transport-Maschine bauen. 
Die Eltern legen sich in einer Reihe quer nebeneinander und immer ein Kind nach dem anderen 
darf sich von der Seite drauflegen. Die Eltern rollen dann gleichzeitig in eine Richtung, 
sodass das Kind wie auf einem Förderband vorangetragen wird.
'''}
fall_list.append('Baumfällen')
spannung_list.append('Baumfällen')

cowboyspiel_dict = {
    'Titel:': 'Cowboyspiel',
    'Kategorie:': 'Haltegriff, Wettkampf',
    'Dauer [min]:': 5,
    'Trainingsgeräte:': '-',
    'Beschreibung:': '''
Vorübung für Kami Shio Gatame. Ein Cowboy ist gemütlich am Lagerfeuer eingeschlafen. 
Der Teilnehmer liegt auf dem Rücken und hat die Augen zu, stellt sich schlafend. 
Der andere spielt einen zweiten Cowboy, der sich flach auf dem Boden krabbelnd anschleicht 
und sich dann von oben auf den Schlafenden legt, um ihn festzuhalten. 
In dem Moment wacht der erste Cowboy auf und will sich natürlich befreien.
'''}
haltegriff_list.append('Cowboyspiel')
wettkampf_list.append('Cowboyspiel')

robbeeisbär_dict = {
    'Titel:': 'Robbe und Eisbär',
    'Kategorie:': 'Randori, Spiel, Wettkampf',
    'Dauer [min]:': 8,
    'Trainingsgeräte:': '-',
    'Beschreibung:': '''
Alle Teilnehmer außer einem sammeln sich an einem Matten Ende und sind Robben. 
Der übrig gebliebene ist auf der Gegenseite und ist ein Eisbär. Die Robben versuchen 
jetzt robbend auf die Gegenseite zu kommen und der Eisbär darf auf allen Vieren versuchen 
die Robben zu schnappen. Dann muss er sie auf den Rücken drehen. 
Wer auf den Rücken gedreht wurde, ist auch ein Eisbär.
'''}
randori_list.append('Robbe und Eisbär')
spiel_list.append('Robbe und Eisbär')
wettkampf_list.append('Robbe und Eisbär')

fischerfischer_dict = {
    'Titel:': 'Fischer, Fischer',
    'Kategorie:': 'Aufwärmen, Spiel',
    'Dauer [min]:': 5,
    'Trainingsgeräte:': '-',
    'Beschreibung:': '''
Alle Teilnehmer bis auf einen sammeln sich an einem Mattenende und der übrig gebliebene 
auf der Gegenseite. Die ersteren rufen "Fischer Fischer, wie tief ist das Wasser?" 
woraufhin der Fischer irgendeine Tiefe angeben darf. Dann fragen die ersteren 
"Und wie kommen wir da rüber?" Nun darf der Fischer angeben, wie sie rüberlaufen sollen 
(auf einem Bein springen, auf allen vieren, etc) und der Fischer versucht so viele Teilnehmer 
wie möglich auf die selbe weise zu fangen. Wer gefangen wird, 
gehört zur Mannschaft des Fischers.
'''}
aufw_list.append('Fischer, Fischer')
spiel_list.append('Fischer, Fischer')

bahnen_dict = {
    'Titel:': 'Bahnenübungen',
    'Kategorie:': 'Aufwärmen, Körperspannung',
    'Dauer [min]:': 5,
    'Trainingsgeräte:': '-',
    'Beschreibung:': '''
Sportübungen in Bahnen. Beispielsweise auf dem Bauch rüberziehen, 
auf dem Rücken rüberschieben oder Hüfte rausdrehen. Auch als Partnerübung: 
ein Partner steht und der andere liegt auf Bauch oder Rücken dahinter. 
Man greift mit den Händen die Knöchel des Stehenden und zieht sich ran. 
Dann macht der Stehende Schritte, bis die Arme des Liegenden wieder gestreckt sind.
'''}
aufw_list.append('Bahnenübungen')
spannung_list.append('Bahnenübungen')

marionetten_dict = {
    'Titel:': 'Marionettenspiel',
    'Kategorie:': 'Körperverständnis, Reaktion',
    'Dauer [min]:': 5,
    'Trainingsgeräte:': '-',
    'Beschreibung:': '''
Partnerübung. Ein Partner ist die Marionette und bewegt sich nicht mehr von selbst. 
Der andere darf die Marionette bewegen und versucht sie irgendwohin laufen zu lassen. 
Eventuell kann man auch versuchen die Marionette zu einer Weichbodenmatte laufen und 
sie dort fallen zu lassen.
'''}
verständnis_list.append('Marionettenspiel')
reak_list.append('Marionettenspiel')

fischernetz_dict = {
    'Titel:': 'Fischer holt die Netze ein',
    'Kategorie:': 'Haltegriff',
    'Dauer [min]:': 5,
    'Trainingsgeräte:': '-',
    'Beschreibung:': '''
Umdrehtechnik. Erst gegen eine Bank, später gegen eine Bauchlage. Seitlich zum Partner stehen. 
Einen Arm unter dem Kinn durchschieben und einen unter dem Bauch. Beide Hände greifen 
den Ellenbogen/ Oberarm des gegenüberliegenden Arms. Dann zieht man die Arme zu sich hin, 
während man mit dem eigenen Oberkörper oben schiebt.
'''}
haltegriff_list.append('Fischer holt die Netze ein')

druckfühlen_dict = {
    'Titel:': 'Druck fühlen',
    'Kategorie:': 'Körperverständnis, Reaktion',
    'Dauer [min]:': 5,
    'Trainingsgeräte:': '-',
    'Beschreibung:': '''
Partnerübung. Beide stehen sich gegenüber und legen die Handflächen aneinander. 
Ein Partner macht die Augen zu. Der Sehende führt den Blinden über den Druck der Handflächen. 
Wenn er schiebt, muss der Blinde rückwärts gehen, wenn der Druck weniger wird, 
muss der Blinde hinterher gehen.
'''}
verständnis_list.append('Druck fühlen')
reak_list.append('Druck fühlen')

sortierenbank_dict = {
    'Titel:': 'Sortieren auf der Bank',
    'Kategorie:': 'Körperverständnis, Spiel, Teamwork',
    'Dauer [min]:': 5,
    'Trainingsgeräte:': 'Bänke',
    'Beschreibung:': '''
Alle Teilnehmer stellen sich gemischt auf eine Bank. Nun sollen sie sich nach 
irgendeiner Vorgabe sortieren, ohne dass jemand den Boden neben der Bank berührt. 
Sortieren zB nach Größe, Alter, etc. Macht natürlich am meisten Spaß, 
wenn viele Teilnehmer da sind.
'''}
verständnis_list.append('Sortieren auf der Bank')
spiel_list.append('Sortieren auf der Bank')
teamwork_list.append('Sortieren auf der Bank')

zeitungstanz_dict = {
    'Titel:': 'Zeitungstanz',
    'Kategorie:': 'Körperverständnis, Spiel',
    'Dauer [min]:': 5,
    'Trainingsgeräte:': 'Papierzeitungen',
    'Beschreibung:': '''
Musik läuft und man tanzt zu zweit auf einer großen Zeitungsseite. 
Jedes Mal wenn die Musik stoppt, muss man die Zeitungsseite halbieren, 
ohne dabei die Matte zu berühren.
'''}
verständnis_list.append('Zeitungstanz')
spiel_list.append('Zeitungstanz')

deckenwende_dict = {
    'Titel:': 'Deckenwende',
    'Kategorie:': 'Teamwork, Spiel',
    'Dauer [min]:': 5,
    'Trainingsgeräte:': 'Große Wolldecke',
    'Beschreibung:': '''
Alle Teilnehmer stehen zusammen auf einer Decke. Diese Decke soll nun gewendet werden, 
ohne dass irgendjemand die Matte berührt.
'''}
teamwork_list.append('Deckenwende')
spiel_list.append('Deckenwende')

hexenticken_dict = {
    'Titel:': 'Hexenticken',
    'Kategorie:': 'Aufwärmen, Spiel',
    'Dauer [min]:': 8,
    'Trainingsgeräte:': '-',
    'Beschreibung:': '''
Einer muss fangen. Wer gefangen wird, muss sich durch eine Übung befreien oder muss 
befreit werden. Beispiele für selbst befreien: auf den Bauch legen und wieder aufstehen, 
Hampelmann machen, auf der Stelle hüpfen. Für befreit werden: breitbeinig hinstellen und 
der Befreiende muss durchtauchen, drum herum laufen (für später: muss mit einem Judowurf 
geworfen werden oder Uchikomi)
'''}
aufw_list.append('Hexenticken')
spiel_list.append('Hexenticken')

staffellauf_dict = {
    'Titel:': 'Staffellauf',
    'Kategorie:': 'Aufwärmen, Spiel',
    'Dauer [min]:': 8,
    'Trainingsgeräte:': 'Etwas zum Transportieren, ggf. Kästen',
    'Beschreibung:': '''
In zwei Teams muss an die Gegenseite der Matte gelaufen werden, um etwas hinzutragen bzw. 
es wieder abzuholen. Dabei kann man alle möglichen Sachen dazupacken: Kinder müssen getragen 
werden, Dreibeinlauf, Reiten, Weihnachtsedition (zu tragender Gegenstand ist ein Geschenk).
'''}
aufw_list.append('Staffellauf')
spiel_list.append('Staffellauf')

wäscheklammer_dict = {
    'Titel:': 'Wäscheklammerklau',
    'Kategorie:': 'Randori, Wettkampf',
    'Dauer [min]:': 10,
    'Trainingsgeräte:': 'Wäscheklammern',
    'Beschreibung:': '''
Die beiden Partner sitzen Rücken an Rücken und beide verstecken irgendwo (AUSSEN!!) 
an der Kleidung eine Wäscheklammer. Bei Hajime drehen beide sich um und müssen 
die Wäscheklammer des anderen klauen und gleichzeitig die eigene verteidigen.
'''}
randori_list.append('Wäscheklammerklau')
wettkampf_list.append('Wäscheklammerklau')

seitwärtsknie_dict = {
    'Titel:': 'Seitwärts aus dem Kniestand',
    'Kategorie:': 'Fallübung',
    'Dauer [min]:': 3,
    'Trainingsgeräte:': '-',
    'Beschreibung:': '''
Vorübung für die Seitwärts-Fallschule. Aus dem Kniestand, ein Bein aufstellen und 
dann auf die Seite fallen. Für Anfänger besonders wichtig, dass das größte Augenmerk 
darauf liegt, wie sie landen (nicht mit Hand oder Ellenboden auffangen, sondern auf 
der Seite mit langem Arm, Kopf schützen).
'''}
fall_list.append('Seitwärts aus dem Kniestand')

seitwärtspartner_dict = {
    'Titel:': 'Seitwärts am Partner',
    'Kategorie:': 'Fallübung, Mut',
    'Dauer [min]:': 3,
    'Trainingsgeräte:': 'Tori braucht einen Judogi',
    'Beschreibung:': '''
Jemand, der gut führen kann, lässt die Teilnehmer in die Jacke greifen, 
damit sie eine eingesprungene Seitwärtsfallschule machen können.
'''}
fall_list.append('Seitwärts am Partner')
mut_list.append('Seitwärts am Partner')

kitzelhai_dict = {
    'Titel:': 'Kitzelhai',
    'Kategorie:': 'Entspannung, Spiel',
    'Dauer [min]:': 5,
    'Trainingsgeräte:': 'Schwungtuch',
    'Beschreibung:': '''
Das Schwungtuch wird ausgebreitet. Alle Teilnehmer setzen sich an den Rand und 
stecken ihre Füße unter das Tuch. Ein Kind ist der Kitzelhai und taucht unter das Tuch. 
Die anderen müssen nun große Wellen mit dem Tuch machen und der Kitzelhai krabbelt nun 
zu irgendjemandem hin und kitzelt die an den Füßen. Wer gekitzelt wurde, ist auch Kitzelhai. 
Eine Runde geht immer recht schnell, sodass viele Kinder mal anfangen können.
'''}
entspannung_list.append('Kitzelhai')
spiel_list.append('Kitzelhai')

körperkreisel_dict = {
    'Titel:': 'Körperkreisel',
    'Kategorie:': 'Körperverständnis',
    'Dauer [min]:': 2,
    'Trainingsgeräte:': '-',
    'Beschreibung:': '''
In den Schneidersitz setzen, mit den Händen die Knie festhalten und dann über die Seite 
auf den Rücken rollen und ohne Hände über die andere Seite wieder aufrichten 
(wie ein Kreisel dreht man sich). 
'''}
verständnis_list.append('Körperkreisel')

knieüberkopf_dict = {
    'Titel:': 'Knie über Kopf',
    'Kategorie:': 'Körperverständnis',
    'Dauer [min]:': 2,
    'Trainingsgeräte:': '-',
    'Beschreibung:': '''
Auf den Rücken legen und dann die Knie über den Kopf heben. Versuchen mit den Füßen 
oder sogar mit den Knien den Boden über dem Kopf zu berühren. Falls das klappt, 
kann man danach über eine Schulter durchrollen und sich auf den Bauch legen.
'''}
verständnis_list.append('Knie über Kopf')

seitlicherolle_dict = {
    'Titel:': 'Seitliche Rolle',
    'Kategorie:': 'Körperverständnis',
    'Dauer [min]:': 2,
    'Trainingsgeräte:': '-',
    'Beschreibung:': '''
Mit geraden Beinen hinsetzen, Kinn auf die Brust legen und dann seitlich über 
die Schultern rollen, sodass man am Ende in der gleichen Position wieder auf dem Hintern 
landet. 
'''}
verständnis_list.append('Seitliche Rolle')

frechessofa_dict = {
    'Titel:': 'Das freche Sofa',
    'Kategorie:': 'Haltegriff, Randori',
    'Dauer [min]:': 8,
    'Trainingsgeräte:': '-',
    'Beschreibung:': '''
Aka. das Killersofa. Vorübung zum Kuzure Kesa Gatame. Ein Teilnehmer ist das Sofa und 
legt sich auf den Rücken. Der andere Teilnehmer lehnt sich gemütlich an das Sofa an 
(Rücken-Bauch-Kontakt!). Dann deckt er sich mit einer Decke zu. Dafür nimmt er den Arm 
des Ukes auf seiner Seite und legt ihn sich über den Bauch. Nun will Tori Fernsehen gucken 
und sucht die Fernbedienung in der Sofaritze. Dafür steckt er die Hand unter die Achsel 
von Uke auf der anderen Seite. Nun sollte Tori in Kuzure Kesa Gatame Haltung sein. 
In diesem Moment wacht das freche Sofa auf und will dem sitzenden Tori entkommen. 
Tori versucht zu halten und Uke versucht, sich rauszudrehen oder -zuwinden.
'''}
haltegriff_list.append('Das freche Sofa')
randori_list.append('Das freche Sofa')

reaktionsübungen_dict = {
    'Titel:': 'Reaktionsübungen',
    'Kategorie:': 'Reaktion',
    'Dauer [min]:': 5,
    'Trainingsgeräte:': '-',
    'Beschreibung:': '''
Partnerübung. 
(1) Ein Partner muss eine offene Hand ausstrecken und der andere muss diese so schnell 
wie möglich treffen. Mal rechts, mal links. 
(2) Das gleiche kann mit dem Fuß wiederholt werden. Dabei soll aber nur leicht mit der 
Fußinnenseite gegen den Fuß gestubst werden. 
(3) Füße und Hände mischen. 
(4) Wenn die ausgestreckte Hand eine Faust ist, dann darf nicht gegengetippt werden.
'''}
reak_list.append('Reaktionsübungen')

zwischendiebeine_dict = {
    'Titel:': 'Zwischen die Beine springen',
    'Kategorie:': 'Körperverständnis',
    'Dauer [min]:': 3,
    'Trainingsgeräte:': '-',
    'Beschreibung:': '''
Elternteil setzt sich breitbeinig hin und hält das Kind an den Händen fest. 
Das Kind springt dann mit geschlossenen Beinen immer rechts-mitte-links-mitte.
'''}
verständnis_list.append('Zwischen die Beine springen')

ballbrücke_dict = {
    'Titel:': 'Ballbrücke',
    'Kategorie:': 'Körperspannung',
    'Dauer [min]:': 5,
    'Trainingsgeräte:': '(kleine) Bälle',
    'Beschreibung:': '''
Ein Teilnehmer legt sich auf den Bauch, er andere hat einen Ball. Der Ball wird dann 
seitlich zu dem Liegenden gerollt und dieser muss sich genau in dem richtigen Moment 
hochdrücken, dass der Ball unter ihm durchrollen kann.
'''}
spannung_list.append('Ballbrücke')

burgerspiel_dict = {
    'Titel:': 'Burgerspiel',
    'Kategorie:': 'Körperverständnis, Spiel',
    'Dauer [min]:': 8,
    'Trainingsgeräte:': '-',
    'Beschreibung:': '''
Die Teilnehmer laufen auf der Mattenfläche wild durcheinander. Dann gibt es 
verschiedene Kommandos. 
(1) Pommes: Alle laufen in die Mitte der Matte, heben die Hände hoch über den Kopf und 
springen zusammen auf der Stelle. 
(2) Hamburger: Drei Teilnehmer müssen sich übereinanderlegen. 
(3) Cheeseburger: Vier Teilnehmer müssen sich übereinanderlegen. 
(4) Doppelwopper: Fünf Teilnehmer müssen sich übereinanderlegen.
'''}
verständnis_list.append('Burgerspiel')
spiel_list.append('Burgerspiel')

rugbykampf_dict =  {
    'Titel:': 'Rugbykampf',
    'Kategorie:': 'Wettkampf, Spiel',
    'Dauer [min]:': 8,
    'Trainingsgeräte:': 'Kästen',
    'Beschreibung:': '''
Zu zweit hat man einen Korb (umgedrehter Kasten oder so). Ein Teilnehmer bekommt einen Ball 
und versucht diesen in den Korb zu legen. Der andere startet zwischen dem Korb und 
seinem Partner und versucht dies zu verhindern.
'''}
wettkampf_list.append('Rugbykampf')
spiel_list.append('Rugbykampf')

ballschwungtuch_dict = {
    'Titel:': 'Ball auf dem Schwungtuch',
    'Kategorie:': 'Teamwork, Spiel',
    'Dauer [min]:': 5,
    'Trainingsgeräte:': 'Schwungtuch',
    'Beschreibung:': '''
Alle Teilnehmer halten zusammen das Schwungtuch außen fest. Zusammen wird ein Ball auf 
dem Tuch hin und her gerollt. Entweder zu bestimmten Personen oder es wird versucht, 
das Loch in der Mitte zu treffen.
'''}
teamwork_list.append('Ball auf dem Schwungtuch')
spiel_list.append('Ball auf dem Schwungtuch')

diewand_dict = {
    'Titel:': 'Die Wand',
    'Kategorie:': 'Teamwork, Spiel',
    'Dauer [min]:': 10,
    'Trainingsgeräte:': 'Weichbodenmatte',
    'Beschreibung:': '''
Eine Weichbodenmatte wird auf der langen Seite aufgestellt. Alle Teilnehmer müssen auf 
eine Seite davon. Zwei dürfen sie an den kurzen Seiten festhalten. Dann müssen alle 
Teilnehmer über die Wand auf die andere Seite.
'''}
teamwork_list.append('Die Wand')
spiel_list.append('Die Wand')

bodenakro_dict = {
    'Titel:': 'Partner-Bodenakrobatik',
    'Kategorie:': 'Körperverständnis und -spannung, Mut',
    'Dauer [min]:': 8,
    'Trainingsgeräte:': '-',
    'Beschreibung:': '''
Verschiedene Partner-Akrobatikübungen. 
(1) Flieger: Das Elternteil legt sich auf den Rücken und hebt die Beine an. Das Kind kommt 
von der Fußseite und die Elternfüße werden an der Hüfte angesetzt. Man kann das Kind nun an 
den Händen fassen und hochziehen/-stemmen. Wenn das Kind genügen Körperspannung hat, kann 
man die Hände loslassen und es kann seine Arme wie ein Flieger ausbreiten. 
(2) Auf den Händen stehen: Das Elternteil liegt auf dem Rücken und das Kind kniet sich auf 
den Brustkorb mit dem Gesicht zu den Beinen des Elternteils. Das Elternteil zieht die Knie an, 
sodass das Kind sich daran festhalten kann. Nun greift man die Füße des Kindes und drückt es 
hoch. Es sollte nun etwa im 90° Winkel vorgebeugt auf den Händen stehen. Wenn das Kind sich 
traut, darf es die Knie loslassen und sich freihändig gerade hinstellen.
'''}
verständnis_list.append('Partner-Bodenakrobatik')
spannung_list.append('Partner-Bodenakrobatik')
mut_list.append('Partner-Bodenakrobatik')

pyramide_dict = {
    'Titel:': 'Pyramide',
    'Kategorie:': 'Körperverständnis, Mut',
    'Dauer [min]:': 5,
    'Trainingsgeräte:': '-',
    'Beschreibung:': '''
Alle Teilnehmer bilden zusammen eine Pyramide. Die Eltern machen in Reihe eine Bank mit 
dem Kopf in dieselbe Richtung. Die Kinder machen dann eine Bank zwischen zwei Elternteilen 
auf der zweiten Ebene.
'''}
verständnis_list.append('Pyramide')
mut_list.append('Pyramide')

dreierrandori_dict = {
    'Titel:': 'Dreier-Randori',
    'Kategorie:': 'Randori',
    'Dauer [min]:': 8,
    'Trainingsgeräte:': '-',
    'Beschreibung:': '''
Zwei Teilnehmer machen ein Bodenrandori. Wenn einer im Haltegriff liegt, darf er den 
dritten eintappen, der dann bei der Befreiung helfen darf.
'''}
randori_list.append('Dreier-Randori')

fahrradfahren_dict = {
    'Titel:': 'Fahrrad fahren',
    'Kategorie:': 'Körperverständnis, Reaktion',
    'Dauer [min]:': 2,
    'Trainingsgeräte:': '-',
    'Beschreibung:': '''
Beide Partner liegen auf dem Rücken, mit dem Kopf in entgegengesetzter Richtung. 
Die Füße werden gegeneinandergedrückt und die Knie müssen etwa im 90 ° Winkel gebeugt sein. 
Nun machen beide gemeinsam eine Bewegung, als würde man Fahrrad fahren. Das klappt nur, 
wenn man gut darauf achtet wie viel Druck man mit den Füßen gibt.
'''}
verständnis_list.append('Fahrrad fahren')
reak_list.append('Fahrrad fahren')

traumreise_dict = {
    'Titel:': 'Traumreise',
    'Kategorie:': 'Entspannung',
    'Dauer [min]:': 5,
    'Trainingsgeräte:': '-',
    'Beschreibung:': '''
Alle Teilnehmer legen sich auf den Rücken und schließen die Augen. Nun wird eine 
entspannende Geschichte erzählt, die man sich vor seinem inneren Auge vorstellen soll. 
In der Geschichte könnte es zum Beispiel darum gehen, wie man auf eine Wolke fliegt und 
was man dabei fühlt und sieht.
'''}
entspannung_list.append('Traumreise')

pizzabacken_dict = {
    'Titel:': 'Pizzabacken',
    'Kategorie:': 'Entspannung',
    'Dauer [min]:': 5,
    'Trainingsgeräte:': '-',
    'Beschreibung:': '''
Dies ist eine kleine Massageübung. Ein Partner liegt auf dem Rücken oder Bauch und 
ist der Pizzateig. Der andere Partner ist der Pizza-Bäcker. Der Pizzateig wird zuerst 
vorsichtig durchgeknetet und danach ausgerollt. Anschließend wir er mit Tomatensoße 
bestrichen (mit den Händen über den Körper streichen). Nun wird der Pizzateig mit 
verschiedenen Dingen belegt, was man mit kleinen Druckberührungen nachmacht. 
Danach wird die Pizza in den Ofen geschoben und man muss geduldig warte, bevor man sie 
danach verspeisen darf.
'''}
entspannung_list.append('Pizzabacken')

reifenringen_dict = {
    'Titel:': 'Reifenringen',
    'Kategorie:': 'Wettkampf',
    'Dauer [min]:': 8,
    'Trainingsgeräte:': 'HulaHoop-Reifen',
    'Beschreibung:': '''
(1) Ein kleiner HulaHoop-Reifen wird zwischen die Partner auf den Boden gelegt. 
Man fasst sich an den Händen an und muss nun versuchen, den anderen in den Reifen 
hineinzuziehen. Wer zuerst mit irgendeinem Körperteil das Innere des Reifens berührt, 
hat verloren. 
(2) Der Aufbau ist der gleiche, nur dass die Partner nun innerhalb des Rings 
stehen und versuchen müssen, sich gegenseitig herauszuschieben. Wer zuerst irgendwie 
die Fläche außerhalb des Rings berührt, verliert.
'''}
wettkampf_list.append('Reifenringen')