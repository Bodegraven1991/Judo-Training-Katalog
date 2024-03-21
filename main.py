import pandas as pd

kat_list = ['Aufwärmen', 'Reaktion', 'Spiel', 'Entspannung', 'Fallübung', 'Mut', 'Teamwork', 'Körperspannung', 'Körperverständnis', 'Wettkampf', 'Haltegriff', 'Randori']
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

training_dict = {'Übung': ['Kategorie', 'Dauer [min]', 'Trainingsgeräte']}

first_key_skipped = False

zeit = 0

def addtotrainlist(exercise, zeit=zeit):
    training_dict[exercise['Titel:']] = [exercise['Kategorie:'],exercise['Dauer [min]:'], exercise['Trainingsgeräte:']]

    zeit = zeit + exercise['Dauer [min]:']

    return zeit

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

# Start of the program loop
while True:
    print('''
Dieses Programm dient dem Zweck unsere Judo Übungsformen sortiert zu halten 
und bei der Trainingsforbereitung schnellen Zugriff auf sie zu haben. Wenn du das Programm
schließen möchtest, schreibe "Ende" oder "out" in dieser Abfrage und drücke Enter.
''')

    abfrage1 = input('''Möchtest du 
(1) eine Übersicht bekommen oder 
(2) direkt nach einer Übungsform suchen
(3) dir den aktuellen Trainingsplan anzeigen lassen?
''')
    abfrage1 = abfrage1.lower()

    if abfrage1 == '1' or abfrage1 == '(1)' or abfrage1 == 'übersicht':

        abfrage2 = input('''
Möchtest du 
(1) eine Auflistung aller verfügbaren Übungskategorien oder 
(2) eine Auflistung aller Übungsformen innerhalb einer Kategorie?
''')
        abfrage2 = abfrage2.lower()

        if abfrage2 == '1' or abfrage2 == '(1)' or abfrage2 == 'kategorie':
            print()
            kat_list.sort()

            for kat in kat_list:
                print(kat)

            input()

        elif abfrage2 == '2' or abfrage2 == '(2)' or abfrage2 == 'übung':
            abfrage3 = input('''
Die Übungen welcher Kategorie möchtest du aufgelistet bekommen?
''')
            abfrage3 = abfrage3.lower()


            if abfrage3 == 'aufwärmen':
                print()
                aufw_list.sort()

                for auf in aufw_list:
                    print(auf)

                input()

            elif abfrage3 == 'reaktion':
                print()
                reak_list.sort()

                for reak in reak_list:
                    print(reak)

                input()

            elif abfrage3 == 'spiel':
                print()
                spiel_list.sort()

                for spiel in spiel_list:
                    print(spiel)

                input()

            elif abfrage3 == 'fallübung':
                print()
                fall_list.sort()

                for fall in fall_list:
                    print(fall)

                input()

            elif abfrage3 == 'mut':
                print()
                mut_list.sort()

                for mut in mut_list:
                    print(mut)

                input()

            elif abfrage3 == 'körperspannung':
                print()
                spannung_list.sort()

                for spann in spannung_list:
                    print(spann)

                input()

            elif abfrage3 == 'körperverständnis':
                print()
                verständnis_list.sort()

                for verständnis in verständnis_list:
                    print(verständnis)

                input()

            elif abfrage3 == 'wettkampf':
                print()
                wettkampf_list.sort()

                for wettkampf in wettkampf_list:
                    print(wettkampf)

                input()

            elif abfrage3 == 'haltegriff':
                print()
                haltegriff_list.sort()

                for halten in haltegriff_list:
                    print(halten)

                input()

            elif abfrage3 == 'randori':
                print()
                randori_list.sort()

                for randori in randori_list:
                    print(randori)

                input()

            elif abfrage3 == 'teamwork':
                print()
                teamwork_list.sort()

                for team in teamwork_list:
                    print(team)

                input()

            elif abfrage3 == 'entspannung':
                print()
                entspannung_list.sort()

                for entsp in entspannung_list:
                    print(entsp)

                input()

    elif abfrage1 == '2' or abfrage1 == '(2)' or abfrage1 == 'übungsform':
        abfrage4 = input('''
Wie ist der Titel der Übungsform?
''')
        abfrage4 = abfrage4.lower()

        if abfrage4 == 'schattenlauf':
            print()

            for key, value in schattenlauf_dict.items():
                print(key, value)

            abfrage_schattenlauf = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_schattenlauf = abfrage_schattenlauf.lower()

            if abfrage_schattenlauf == 'j' or abfrage_schattenlauf == 'ja':

                addtotrainlist(schattenlauf_dict)
                zeit = addtotrainlist(schattenlauf_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'feuer, wasser, blitz':
            print()

            for key, value in fwb_dict.items():
                print(key, value)

            abfrage_fwb = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_fwb = abfrage_fwb.lower()

            if abfrage_fwb == 'j' or abfrage_fwb == 'ja':

                addtotrainlist(fwb_dict)
                zeit = addtotrainlist(fwb_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'mattenklappen':
            print()

            for key, value in mattenklappen_dict.items():
                print(key, value)

            abfrage_mattenklappen = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_mattenklappen = abfrage_mattenklappen.lower()

            if abfrage_mattenklappen == 'j' or abfrage_mattenklappen == 'ja':

                addtotrainlist(mattenklappen_dict)
                zeit = addtotrainlist(mattenklappen_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'auf-die-matte-springen':
            print()

            for key, value in mattespringen_dict.items():
                print(key, value)

            abfrage_mattenspringen = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_mattenspringen = abfrage_mattenspringen.lower()

            if abfrage_mattenspringen == 'j' or abfrage_mattenspringen == 'ja':

                addtotrainlist(mattespringen_dict)
                zeit = addtotrainlist(mattespringen_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'elternklettern':
            print()

            for key, value in elternklettern_dict.items():
                print(key, value)

            abfrage_elternklettern = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_elternklettern = abfrage_elternklettern.lower()

            if abfrage_elternklettern == 'j' or abfrage_elternklettern == 'ja':

                addtotrainlist(elternklettern_dict)
                zeit = addtotrainlist(elternklettern_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'reiten':
            print()

            for key, value in reiten_dict.items():
                print(key, value)

            abfrage_reiten = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_reiten = abfrage_reiten.lower()

            if abfrage_reiten == 'j' or abfrage_reiten == 'ja':

                addtotrainlist(reiten_dict)
                zeit = addtotrainlist(reiten_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'um die bank rollen':
            print()

            for key, value in umdiebank_dict.items():
                print(key, value)

            abfrage_umdiebank = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_umdiebank = abfrage_umdiebank.lower()

            if abfrage_umdiebank == 'j' or abfrage_umdiebank == 'ja':

                addtotrainlist(umdiebank_dict)
                zeit = addtotrainlist(umdiebank_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'purzelbaum':
            print()

            for key, value in purzelbaum_dict.items():
                print(key, value)

            abfrage_purzelbaum = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_purzelbaum = abfrage_purzelbaum.lower()

            if abfrage_purzelbaum == 'j' or abfrage_purzelbaum == 'ja':

                addtotrainlist(purzelbaum_dict)
                zeit = addtotrainlist(purzelbaum_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'mäusefalle':
            print()

            for key, value in mäusefalle_dict.items():
                print(key, value)

            abfrage_mäusefalle = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_mäusefalle = abfrage_mäusefalle.lower()

            if abfrage_mäusefalle == 'j' or abfrage_mäusefalle == 'ja':

                addtotrainlist(mäusefalle_dict)
                zeit = addtotrainlist(mäusefalle_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'drachenschatz':
            print()

            for key, value in drachenschatz_dict.items():
                print(key, value)

            abfrage_drachenschatz = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_drachenschatz = abfrage_drachenschatz.lower()

            if abfrage_drachenschatz == 'j' or abfrage_drachenschatz == 'ja':

                addtotrainlist(drachenschatz_dict)
                zeit = addtotrainlist(drachenschatz_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'tiere nachmachen':
            print()

            for key, value in tierenachmachen_dict.items():
                print(key, value)

            abfrage_tierenachmachen = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_tierenachmachen = abfrage_tierenachmachen.lower()

            if abfrage_tierenachmachen == 'j' or abfrage_tierenachmachen == 'ja':

                addtotrainlist(tierenachmachen_dict)
                zeit = addtotrainlist(tierenachmachen_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'löwenticken':
            print()

            for key, value in löwenticken_dict.items():
                print(key, value)

            abfrage_löwenticken = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_löwenticken = abfrage_löwenticken.lower()

            if abfrage_löwenticken == 'j' or abfrage_löwenticken == 'ja':

                addtotrainlist(löwenticken_dict)
                zeit = addtotrainlist(löwenticken_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'babyaffen':
            print()

            for key, value in babyaffen_dict.items():
                print(key, value)

            abfrage_babyaffen = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_babyaffen = abfrage_babyaffen.lower()

            if abfrage_babyaffen == 'j' or abfrage_babyaffen == 'ja':

                addtotrainlist(babyaffen_dict)
                zeit = addtotrainlist(babyaffen_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'hängebrücke':
            print()

            for key, value in hängebrücke_dict.items():
                print(key, value)

            abfrage_hängebrücke = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_hängebrücke = abfrage_hängebrücke.lower()

            if abfrage_hängebrücke == 'j' or abfrage_hängebrücke == 'ja':

                addtotrainlist(hängebrücke_dict)
                zeit = addtotrainlist(hängebrücke_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'rasenmäher':
            print()

            for key, value in rasenmäher_dict.items():
                print(key, value)

            abfrage_rasenmäher = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_rasenmäher = abfrage_rasenmäher.lower()

            if abfrage_rasenmäher == 'j' or abfrage_rasenmäher == 'ja':

                addtotrainlist(rasenmäher_dict)
                zeit = addtotrainlist(rasenmäher_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'kuscheltiere retten':
            print()

            for key, value in tiereretten_dict.items():
                print(key, value)

            abfrage_tiereretten = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_tiereretten = abfrage_tiereretten.lower()

            if abfrage_tiereretten == 'j' or abfrage_tiereretten == 'ja':

                addtotrainlist(tiereretten_dict)
                zeit = addtotrainlist(tiereretten_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'haifische':
            print()

            for key, value in haifische_dict.items():
                print(key, value)

            abfrage_haifische = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_haifische = abfrage_haifische.lower()

            if abfrage_haifische == 'j' or abfrage_haifische == 'ja':

                addtotrainlist(haifische_dict)
                zeit = addtotrainlist(haifische_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'atomspiel':
            print()

            for key, value in atomspiel_dict.items():
                print(key, value)

            abfrage_atomspiel = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_atomspiel = abfrage_atomspiel.lower()

            if abfrage_atomspiel == 'j' or abfrage_atomspiel == 'ja':

                addtotrainlist(atomspiel_dict)
                zeit = addtotrainlist(atomspiel_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'baumfällen':
            print()

            for key, value in baumfällen_dict.items():
                print(key, value)

            abfrage_baumfällen = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_baumfällen = abfrage_baumfällen.lower()

            if abfrage_baumfällen == 'j' or abfrage_baumfällen == 'ja':

                addtotrainlist(baumfällen_dict)
                zeit = addtotrainlist(baumfällen_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'cowboyspiel':
            print()

            for key, value in cowboyspiel_dict.items():
                print(key, value)

            abfrage_cowboyspiel = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_cowboyspiel = abfrage_cowboyspiel.lower()

            if abfrage_cowboyspiel == 'j' or abfrage_cowboyspiel == 'ja':

                addtotrainlist(cowboyspiel_dict)
                zeit = addtotrainlist(cowboyspiel_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'robbe und eisbär':
            print()

            for key, value in robbeeisbär_dict.items():
                print(key, value)

            abfrage_robbeeisbär = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_robbeeisbär = abfrage_robbeeisbär.lower()

            if abfrage_robbeeisbär == 'j' or abfrage_robbeeisbär == 'ja':

                addtotrainlist(robbeeisbär_dict)
                zeit = addtotrainlist(robbeeisbär_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'fischer, fischer':
            print()

            for key, value in fischerfischer_dict.items():
                print(key, value)

            abfrage_fischerfischer = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_fischerfischer = abfrage_fischerfischer.lower()

            if abfrage_fischerfischer == 'j' or abfrage_fischerfischer == 'ja':

                addtotrainlist(fischerfischer_dict)
                zeit = addtotrainlist(fischerfischer_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'bahnenübungen':
            print()

            for key, value in bahnen_dict.items():
                print(key, value)

            abfrage_bahnen = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_bahnen = abfrage_bahnen.lower()

            if abfrage_bahnen == 'j' or abfrage_bahnen == 'ja':

                addtotrainlist(bahnen_dict)
                zeit = addtotrainlist(bahnen_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'marionettenspiel':
            print()

            for key, value in marionetten_dict.items():
                print(key, value)

            abfrage_marionetten = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_marionetten = abfrage_marionetten.lower()

            if abfrage_marionetten == 'j' or abfrage_marionetten == 'ja':

                addtotrainlist(marionetten_dict)
                zeit = addtotrainlist(marionetten_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'fischer holt die netze ein':
            print()

            for key, value in fischernetz_dict.items():
                print(key, value)

            abfrage_fischernetz = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_fischernetz = abfrage_fischernetz.lower()

            if abfrage_fischernetz == 'j' or abfrage_fischernetz == 'ja':

                addtotrainlist(fischernetz_dict)
                zeit = addtotrainlist(fischernetz_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'druck fühlen':
            print()

            for key, value in druckfühlen_dict.items():
                print(key, value)

            abfrage_druckfühlen = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_druckfühlen = abfrage_druckfühlen.lower()

            if abfrage_druckfühlen == 'j' or abfrage_druckfühlen == 'ja':

                addtotrainlist(druckfühlen_dict)
                zeit = addtotrainlist(druckfühlen_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'sortieren auf der bank':
            print()

            for key, value in sortierenbank_dict.items():
                print(key, value)

            abfrage_sortierenbank = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_sortierenbank = abfrage_sortierenbank.lower()

            if abfrage_sortierenbank == 'j' or abfrage_sortierenbank == 'ja':

                addtotrainlist(sortierenbank_dict)
                zeit = addtotrainlist(sortierenbank_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'zeitungstanz':
            print()

            for key, value in zeitungstanz_dict.items():
                print(key, value)

            abfrage_zeitungstanz = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_zeitungstanz = abfrage_zeitungstanz.lower()

            if abfrage_zeitungstanz == 'j' or abfrage_zeitungstanz == 'ja':

                addtotrainlist(zeitungstanz_dict)
                zeit = addtotrainlist(zeitungstanz_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'deckenwende':
            print()

            for key, value in deckenwende_dict.items():
                print(key, value)

            abfrage_deckenwende = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_deckenwende = abfrage_deckenwende.lower()

            if abfrage_deckenwende == 'j' or abfrage_deckenwende == 'ja':

                addtotrainlist(deckenwende_dict)
                zeit = addtotrainlist(deckenwende_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'hexenticken':
            print()

            for key, value in hexenticken_dict.items():
                print(key, value)

            abfrage_hexenticken = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_hexenticken = abfrage_hexenticken.lower()

            if abfrage_hexenticken == 'j' or abfrage_hexenticken == 'ja':

                addtotrainlist(hexenticken_dict)
                zeit = addtotrainlist(hexenticken_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'staffellauf':
            print()

            for key, value in staffellauf_dict.items():
                print(key, value)

            abfrage_staffellauf = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_staffellauf = abfrage_staffellauf.lower()

            if abfrage_staffellauf == 'j' or abfrage_staffellauf == 'ja':

                addtotrainlist(staffellauf_dict)
                zeit = addtotrainlist(staffellauf_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'wäscheklammerklau':
            print()

            for key, value in wäscheklammer_dict.items():
                print(key, value)

            abfrage_wäscheklammer = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_wäscheklammer = abfrage_wäscheklammer.lower()

            if abfrage_wäscheklammer == 'j' or abfrage_wäscheklammer == 'ja':

                addtotrainlist(wäscheklammer_dict)
                zeit = addtotrainlist(wäscheklammer_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'seitwärts aus dem kniestand':
            print()

            for key, value in seitwärtsknie_dict.items():
                print(key, value)

            abfrage_seitwärtsknie = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_seitwärtsknie = abfrage_seitwärtsknie.lower()

            if abfrage_seitwärtsknie == 'j' or abfrage_seitwärtsknie == 'ja':

                addtotrainlist(seitwärtsknie_dict)
                zeit = addtotrainlist(seitwärtsknie_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'seitwärts am partner':
            print()

            for key, value in seitwärtspartner_dict.items():
                print(key, value)

            abfrage_seitwärtspartner = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_seitwärtspartner = abfrage_seitwärtspartner.lower()

            if abfrage_seitwärtspartner == 'j' or abfrage_seitwärtspartner == 'ja':

                addtotrainlist(seitwärtspartner_dict)
                zeit = addtotrainlist(seitwärtspartner_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'kitzelhai':
            print()

            for key, value in kitzelhai_dict.items():
                print(key, value)

            abfrage_kitzelhai = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_kitzelhai = abfrage_kitzelhai.lower()

            if abfrage_kitzelhai == 'j' or abfrage_kitzelhai == 'ja':

                addtotrainlist(kitzelhai_dict)
                zeit = addtotrainlist(kitzelhai_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'körperkreisel':
            print()

            for key, value in körperkreisel_dict.items():
                print(key, value)

            abfrage_kreisel = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_kreisel = abfrage_kreisel.lower()

            if abfrage_kreisel == 'j' or abfrage_kreisel == 'ja':

                addtotrainlist(körperkreisel_dict)
                zeit = addtotrainlist(körperkreisel_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'knie über kopf':
            print()

            for key, value in knieüberkopf_dict.items():
                print(key, value)

            abfrage_knieüberkopf = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_knieüberkopf = abfrage_knieüberkopf.lower()

            if abfrage_knieüberkopf == 'j' or abfrage_knieüberkopf == 'ja':

                addtotrainlist(knieüberkopf_dict)
                zeit = addtotrainlist(knieüberkopf_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'seitliche rolle':
            print()

            for key, value in seitlicherolle_dict.items():
                print(key, value)

            abfrage_seitlicherolle = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_seitlicherolle = abfrage_seitlicherolle.lower()

            if abfrage_seitlicherolle == 'j' or abfrage_seitlicherolle == 'ja':

                addtotrainlist(seitlicherolle_dict)
                zeit = addtotrainlist(seitlicherolle_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'das freche sofa':
            print()

            for key, value in frechessofa_dict.items():
                print(key, value)

            abfrage_frechessofa = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_frechessofa = abfrage_frechessofa.lower()

            if abfrage_frechessofa == 'j' or abfrage_frechessofa == 'ja':

                addtotrainlist(frechessofa_dict)
                zeit = addtotrainlist(frechessofa_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'reaktionsübungen':
            print()

            for key, value in reaktionsübungen_dict.items():
                print(key, value)

            abfrage_reaktionsübungen = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_reaktionsübungen = abfrage_reaktionsübungen.lower()

            if abfrage_reaktionsübungen == 'j' or abfrage_reaktionsübungen == 'ja':

                addtotrainlist(reaktionsübungen_dict)
                zeit = addtotrainlist(reaktionsübungen_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'zwischen die beine springen':
            print()

            for key, value in zwischendiebeine_dict.items():
                print(key, value)

            abfrage_zwischendiebeine = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_zwischendiebeine = abfrage_zwischendiebeine.lower()

            if abfrage_zwischendiebeine == 'j' or abfrage_zwischendiebeine == 'ja':

                addtotrainlist(zwischendiebeine_dict)
                zeit = addtotrainlist(zwischendiebeine_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'ballbrücke':
            print()

            for key, value in ballbrücke_dict.items():
                print(key, value)

            abfrage_ballbrücke = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_ballbrücke = abfrage_ballbrücke.lower()

            if abfrage_ballbrücke == 'j' or abfrage_ballbrücke == 'ja':

                addtotrainlist(ballbrücke_dict)
                zeit = addtotrainlist(ballbrücke_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'burgerspiel':
            print()

            for key, value in burgerspiel_dict.items():
                print(key, value)

            abfrage_burgerspiel = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_burgerspiel = abfrage_burgerspiel.lower()

            if abfrage_burgerspiel == 'j' or abfrage_burgerspiel == 'ja':

                addtotrainlist(burgerspiel_dict)
                zeit = addtotrainlist(burgerspiel_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'rugbykampf':
            print()

            for key, value in rugbykampf_dict.items():
                print(key, value)

            abfrage_rugbykampf = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_rugbykampf = abfrage_rugbykampf.lower()

            if abfrage_rugbykampf == 'j' or abfrage_rugbykampf == 'ja':

                addtotrainlist(rugbykampf_dict)
                zeit = addtotrainlist(rugbykampf_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'ball auf dem schwungtuch':
            print()

            for key, value in ballschwungtuch_dict.items():
                print(key, value)

            abfrage_ballschwungtuch = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_ballschwungtuch = abfrage_ballschwungtuch.lower()

            if abfrage_ballschwungtuch == 'j' or abfrage_ballschwungtuch == 'ja':

                addtotrainlist(ballschwungtuch_dict)
                zeit = addtotrainlist(ballschwungtuch_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'die wand':
            print()

            for key, value in diewand_dict.items():
                print(key, value)

            abfrage_diewand = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_diewand = abfrage_diewand.lower()

            if abfrage_diewand == 'j' or abfrage_diewand == 'ja':

                addtotrainlist(diewand_dict)
                zeit = addtotrainlist(diewand_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'partner-bodenakrobatik':
            print()

            for key, value in bodenakro_dict.items():
                print(key, value)

            abfrage_bodenakro = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_bodenakro = abfrage_bodenakro.lower()

            if abfrage_bodenakro == 'j' or abfrage_bodenakro == 'ja':

                addtotrainlist(bodenakro_dict)
                zeit = addtotrainlist(bodenakro_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'pyramide':
            print()

            for key, value in pyramide_dict.items():
                print(key, value)

            abfrage_pyramide = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_pyramide = abfrage_pyramide.lower()

            if abfrage_pyramide == 'j' or abfrage_pyramide == 'ja':

                addtotrainlist(pyramide_dict)
                zeit = addtotrainlist(pyramide_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'dreier-randori':
            print()

            for key, value in dreierrandori_dict.items():
                print(key, value)

            abfrage_dreierrandori = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_dreierrandori = abfrage_dreierrandori.lower()

            if abfrage_dreierrandori == 'j' or abfrage_dreierrandori == 'ja':

                addtotrainlist(dreierrandori_dict)
                zeit = addtotrainlist(dreierrandori_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'fahrrad fahren':
            print()

            for key, value in fahrradfahren_dict.items():
                print(key, value)

            abfrage_fahrradfahren = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_fahrradfahren = abfrage_fahrradfahren.lower()

            if abfrage_fahrradfahren == 'j' or abfrage_fahrradfahren == 'ja':

                addtotrainlist(fahrradfahren_dict)
                zeit = addtotrainlist(fahrradfahren_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'traumreise':
            print()

            for key, value in traumreise_dict.items():
                print(key, value)

            abfrage_traumreise = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_traumreise = abfrage_traumreise.lower()

            if abfrage_traumreise == 'j' or abfrage_traumreise == 'ja':

                addtotrainlist(traumreise_dict)
                zeit = addtotrainlist(traumreise_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'pizzabacken':
            print()

            for key, value in pizzabacken_dict.items():
                print(key, value)

            abfrage_pizzabacken = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_pizzabacken = abfrage_pizzabacken.lower()

            if abfrage_pizzabacken == 'j' or abfrage_pizzabacken == 'ja':

                addtotrainlist(pizzabacken_dict)
                zeit = addtotrainlist(pizzabacken_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

        elif abfrage4 == 'reifenringen':
            print()

            for key, value in reifenringen_dict.items():
                print(key, value)

            abfrage_reifenringen = input('Soll die Übung zum Trainingsplan hinzugefügt werden? (j/n)')
            abfrage_reifenringen = abfrage_reifenringen.lower()

            if abfrage_reifenringen == 'j' or abfrage_reifenringen == 'ja':

                addtotrainlist(reifenringen_dict)
                zeit = addtotrainlist(reifenringen_dict, zeit)
                print('Das Training dauert jetzt etwa ' + (str(zeit)) + ' Minuten.')
                input()

    elif abfrage1 == '3' or abfrage1 == '(3)' or abfrage1 == 'Trainingsplan':
        print()

        for x in training_dict:
            key = x
            value1 = training_dict[key][0]
            value2 = training_dict[key][1]
            value3 = training_dict[key][2]
            print(f"{key:<40} {value1:<40} {value2:<20} {value3:<40}")

        print('Das Training dauert etwa ' + (str(zeit)) + ' Minuten.')
        print()

        abfrage_print = input('Soll der Trainingsplan als Excelsheet exporiert werden? (j/n)')
        abfrage_print = abfrage_print.lower()

        if abfrage_print == 'j' or abfrage_print == 'ja':

            data = {
                'Übung': [],
                'Kategorie': [],
                'Dauer [min]': [],
                'Trainingsgeräte': []
            }

            for x in training_dict:
                key = x
                if not first_key_skipped:
                    first_key_skipped = True
                    continue  # Skip the first iteration

                data['Übung'].append(key)
                data['Kategorie'].append(training_dict[key][0])
                data['Dauer [min]'].append(training_dict[key][1])
                data['Trainingsgeräte'].append(training_dict[key][2])

            df = pd.DataFrame(data)

            # Specify the file path for the Excel file
            excel_file_path = 'Trainingsplan Judo.xlsx'

            # Write the DataFrame to Excel
            df.to_excel(excel_file_path, index=False)

            print()

            print("Das Excelsheet wurde erfolgreich mit dem Namen " + excel_file_path + ' erstellt.')

            input()

    else:
        # Exit the program if the user inputs something other than the valid statements
        break
