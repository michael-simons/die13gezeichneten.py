# -*- coding: utf-8 -*-

from flask import Flask, render_template, session, redirect, url_for, request
import copy
import operator

app = Flask(__name__)
app.secret_key = 'tfX8LvBJeTyumBnK'

def a1(antwort, s):
    if antwort == 1:
        s['Naehr'] +=1
        s['Alchim'] +=1
        s['Blut'] +=1
        s['Stein'] +=1
        s['Gold'] +=1
        s['Glas'] +=1
        s['Holz'] +=1
        s['Rausch'] +=1
        s['Eisen'] +=1
        s['Gewoben']+=1
        s['Ton']+=1
    elif antwort == 2:
        s['Wort']+=1
    elif antwort == 3:
        s['Verborgen']+=1
        
def a2(antwort, s):
    if antwort == 1:
        s['Wort']+=1
    elif antwort == 2:
        s['Naehr'] +=1
    elif antwort == 3:
        s['Rausch'] +=1
        s['Alchim'] +=1
    elif antwort == 4:
        s['Blut'] +=1
    elif antwort == 5:
        s['Verborgen']+=1
        
def a3(antwort, s):
    if antwort == 1:
        s['Eisen'] +=1
    elif antwort == 2:
        s['Ton']+=1
    elif antwort == 3:
        s['Gold'] +=1
    elif antwort == 4:
        s['Rausch'] +=1
    elif antwort == 5:
        s['Gewoben']+=1
    elif antwort == 6:
        s['Blut'] +=1
        
def a4(antwort, s):
    if antwort == 1:
        s['Eisen'] +=1
    elif antwort == 2:
        s['Glas'] +=1
    elif antwort == 3:
        s['Holz'] +=1
    elif antwort == 4:
        s['Gewoben']+=1
    elif antwort == 5:
        s['Wort']+=1
    elif antwort == 6:
        s['Rausch'] +=1
    elif antwort == 7:
        s['Stein'] +=1
        s['Glas'] +=1
        
def a5(antwort, s):
    if antwort == 1:
        s['Gewoben']+=1
    elif antwort == 2:
        s['Stein'] +=1
    elif antwort == 3:
        s['Holz'] +=1
    elif antwort == 4:
        s['Verborgen']+=1
        
def a6(antwort, s):
    if antwort == 1:
        s['Alchim'] +=1
        s['Blut'] +=1
    elif antwort == 2:
        s['Naehr'] +=1
    elif antwort == 3:
        s['Verborgen']+=1
    elif antwort == 4:
        s['Rausch'] +=1
    elif antwort == 5:
        s['Gold'] +=1
        
def a7(antwort, s):
    if antwort == 1:
        s['Wort']+=1
    elif antwort == 2:
        s['Blut'] +=1
        s['Eisen'] +=1
    elif antwort == 3:
        s['Verborgen']+=1
        
def a8(antwort, s):
    if antwort == 1:
        s['Naehr'] +=1
    elif antwort == 2:
        s['Ton']+=1
    elif antwort == 3:
        s['Gold'] +=1
    elif antwort == 4:
        s['Wort']+=1
    elif antwort == 5:
        s['Glas'] +=1

def a9(antwort, s):
    if antwort == 1:
        s['Gold'] +=1
        s['Glas'] +=1
    elif antwort == 2:
        s['Holz'] +=1
    elif antwort == 3:
        s['Naehr'] +=1
    elif antwort == 4:
        s['Alchim'] +=1
    elif antwort == 5:
        s['Eisen'] +=1
    
def a10(antwort, s):
    if antwort == 1:
        s['Ton']+=1
    elif antwort == 2:
        s['Gewoben']+=1
    elif antwort == 3:
        s['Stein'] +=1
    elif antwort == 4:
        s['Alchim'] +=1
    
def a11(antwort, s):
    if antwort == 1:
        s['Holz'] +=1
    elif antwort == 2:
        s['Ton']+=1
    elif antwort == 3:
        s['Glas'] +=1
    elif antwort == 4:
        s['Stein'] +=1

questions = [
    [
        u"Womit arbeitest du lieber?", [
            u"Den Händen",
            u"Dem Kopf",
            u"Am liebsten gar nicht"
        ],
        a1
    ],
    [
        u"Was ist das Highlight deines Tages?", [
            u"Ein gutes Buch lesen",
            u"Etwas Gutes essen",
            u"Mit Freunden einen trinken",
            u"Sport",
            u"Wenn ich dir das verraten würde, müsste ich dich töten."
        ],
        a2
    ],
    [
        u"Deine Freunde schenken dir einen Workshop zum Geburtstag. Über welchen freust du dich?", [
            u"Schmieden!",
            u"Töpfern!",
            u"Schmuckbasteln!",
            u"Bierbrauen!",
            u"Nähen!",
            u"Ein Fechtseminar"
        ],
        a3
    ],
    [
        u"Wofür würdest du in deinem Haushalt wirklich Geld in die Hand nehmen?", [
            u"Ein tolles japanisches Schneidemesser",
            u"Das passende Glas für alle Gelegenheiten",
            u"Neue Möbel",
            u"Haushalskram? Pah! Ich brauche Klamotten!",
            u"Ich brauche vor allen Dingen Bücher!",
            u"Einen guten Whiskey",
            u"Ich bin ein Bastler, ich baue immer an meinem Zuhause herum"
        ] ,
        a4
    ],
    [
        u"Du machst Urlaub. Wo übernachtest du?", [
            u"In einem Zelt",
            u"In einem Hotel",
            u"In einer Blockhütte",
            u"Ich nehm’s wie’s kommt, notfalls penn ich im Auto."
        ],
        a5
    ],
    [
        u"Du arbeitest in einem Labor und hast die Wahl:", [
            u"Ich suche nach dem Unsterblichkeitselixier.",
            u"Ich forsche nach Nährlösung, die den Hunger besiegt.",
            u"Ich möchte einen Trank, der unsichtbar macht.",
            u"Ich braue einen Liebeszauber.",
            u"Ich möchte Blei zu Gold machen."
        ],
        a6
    ],
    [
        u"Was ist mächtiger?", [
            u"Die Feder",
            u"Das Schwert",
            u"Das kannst du beides vergessen, im Notfall hilft nur Verschlagenheit."
        ],
        a7
    ],
    [
        u"Einbrecher entwenden, worin dein Herzblut steckt. Was ist es?", [
            u"Sie haben meinen Nutzgarten verwüstet!",
            u"Sie haben mein Porzellan zertrümmert!",
            u"Sie haben meinen Schmuck gestohlen!",
            u"Sie haben meinen Laptop geklaut!",
            u"Sie haben meine Fensterscheiben eingeschlagen!"
        ],
        a8
    ],
    [
        u"Die Weihnachtsbäume sind aus. Du hast deiner Familie versprochen, dass du einen mitbringst. Was tust du?", [
            u"Ich nehme einen künstlichen und behänge ihn mit so viel Kugeln und Bling-Bling, dass sie es nicht merken.",
            u"Ich war immer schon gut mit der Laubsäge – das sieht nachher sicher nett aus.",
            u"Das gute Essen wird meine Familie drüber hinwegtrösten. Ich kaufe extra opulent ein.",
            u"Stattdessen kaufe ich einfach zu Silvester mehr Feuerwerk.",
            u"Ich stelle einfach einen Haufen Kerzenleuchter auf."
        ],
        a9
    ],
    [
        u"Alltagskram, bei dem es deiner Meinung nach Verbesserungspotenzial gibt:", [
            u"Geschirr, das nicht zerbricht",
            u"Kleidung, die nicht zerreißt",
            u"Straßen, die keine Schlaglöcher kriegen",
            u"Zahnpasta, von der ich WIRKLICH keine Parodontose kriege"
        ],
        a10
    ],
    [
        u"Wie willst du beerdigt werden?", [
            u"Ich will den Klassiker: Gebt mir einen Sarg!",
            u"Ich möchte zu Erde werden – äschert mich ein und verstreut mich.",
            u"Wie Schneewittchen und Lenin: in einem Glassarg!",
            u"Ich hätte gern eine Pyramide."
        ],
        a11
    ]
]

emptyResult = {
        'Wort': 0,
        'Verborgen': 0,
        'Naehr': 0,
        'Alchim': 0,
        'Blut': 0,
        'Stein': 0,
        'Gold': 0,
        'Glas': 0,
        'Holz': 0,
        'Rausch': 0,
        'Eisen': 0,
        'Gewoben': 0,
        'Ton': 0
    }
    
zeichen = {
    'Wort': u"   ... Wortzeichen! Schau mal bei der Gilde der Dichter, Sänger, Schriftsteller, Buchdrucker vorbei!",
    'Verborgen': u"   ... Verborgene Zeichen! Jemandem wie dir steht in Sygna keine Gilde offen! Pass auf deinen Lebenswandel auf, sonst landest du am Ende noch beim Verborgenen Hof!",
    'Naehr': u"   ... Nährende Zeichen! Die Bäcker und Müller nehmen dich sicher gern auf! Oder aber die Heiler. Aber wir müssen dich vorwarnen: Letztere sind etwas umstritten!",
    'Alchim': u"   ... Alchimistische Zeichen! Die Gilde der Alchimisten und Sterndeuter oder die Gilde der Heiler nehmen dich sicher gerne auf!",
    'Blut': u"   ... Blutzeichen! Ein Schwertkämpfer! Die Goldene Gilde wäre etwas für dich. Oder du gehst zur Konkurrenz, den Stählernen Fechter, wenn dir ein Sitz im Rat nicht so wichtig ist.",
    'Stein': u"   ... Steinerne Zeichen! Die Zunft der Steinmetze erwartet dich!",
    'Gold': u"   ... Goldene Zeichen! Hier steht ein baldiger Schmuckschmiedegeselle vor uns!",
    'Glas': u"   ... Gläserne Zeichen! Die Zunft der Glasbläser sucht immer gute Leute!",
    'Holz': u"   ... Hölzerne Zeichen! Bewirb dich bei der erwürdigen Zunft der Schreiner und Zimmerleute!",
    'Rausch': u"   ... Rausch! Die Gilde der Kurtisanen ist Vergangenheit, aber bei den Braumeistern kannst du es auch heute noch zu etwas bringen!",
    'Eisen': u"   ... Eiserne Zeichen! Die Gilde der Klingenschmiede zum einen und die Gilde der Harnischermacher und Glockengießer zum anderen werden sich um dich reißen!",
    'Gewoben': u"   ... Gewobene Zeichen! Strebe danache, die Meisterschaft in deiner Kunst in der Weberzunft zu erlangen!",
    'Ton': "   ... Irdene Zeichne! In der Zunft der Töpfer wirst du machtvolle Zeichen in den Ton brennen können!"
}

@app.route('/')
def index():
    reset()
    return render_template('index.html')
    
@app.route('/gildenrat')
def gildenrat():
    return render_template('question.html', questionNumber=session['step']+1, question=questions[session['step']])
    
@app.route('/answer', methods=['POST'])
def answer():
    if session['step']+1 == len(questions):
        session['result'] = zeichen[max(session['answers'], key=lambda key: session['answers'][key])]
        url = 'result'
    else:
        # call answer method
        questions[session['step']][2](int(request.form['answer']),session['answers'])
        session['step'] += 1
        url = 'gildenrat'
    return redirect(url_for(url))
    
@app.route('/result')
def result():
    if session.get('result', 'n/a') == 'n/a':
        return redirect(url_for('index'))
    else:
        return render_template('result.html', result=session['result'])
    
@app.route('/reset', methods=['POST'])
def reset():
    session['step'] = 0
    session['answers'] = copy.deepcopy(emptyResult)
    return redirect(url_for('gildenrat'))