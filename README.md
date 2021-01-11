# Convex Polygon Bot

Convex Polygon Bot és un bot de Telegram que ens permet fer diverses operacions i representacions gràfiques amb poligons convexos

## Per començar

Per tal de fer funcionar correctament el Convex Polygon Bot, primer haurem d'instal·lar els paquets necessaris. Les úniques llibreries usades que no són estàndards de Python són ```python-telegram-bot``` i ```pillow```. Les podem instal·lar executant la comanda  ```python -m pip install -r requirements.txt``` en Unix/macOS i ```py -m pip install -r requirements.txt``` en Windows.

### Prerequisits

Per executar el nostre programa és indispensable tenir instal·lat ```Python3```. Si no el tenim instal·lat ho podem fer executant:
```
sudo apt install python3.8
```
També, per tal d'instal·lar els paquets necessaris per executar el nostre programa, hem d'assegurar-nos de tenir l'instal·lador de paquets PIP.

Ho podem comprovar executant:
```
python -m pip --version
```
Si no està insta·lat ho podem fer executant:
```
apt install python3-pip
```
### Instal·lació

Per tal de fer funcionar correctament el Convex Polygon Bot, primer haurem d'instal·lar els paquets necessaris. Les úniques llibreries usades que no són estàndards de Python són ```python-telegram-bot``` i ```pillow```. Les podem instal·lar executant la comanda  ```python -m pip install -r requirements.txt``` en Unix/macOS i ```py -m pip install -r requirements.txt``` en Windows.


## Execució

A continuació, els passos a seguir per a fer funcionar el Bot

### Posada en marxa

Per tal de posar en marxa el bot en la nostra màquina haurem d'executar el fitxer ```bot.py```.

```
python3 bot.py
```

### Usar el bot

Podem accedir al xat amb el el Convex Polygon Bot fent click [aquí](https://t.me/polygonsarnaubot)

#### Comandes

Llistat de comandes bàsiques per a interactuar amb el bot

* ```/start``` - Inicialitza el bot.
* ```/instructions``` - Proporciona informació sobre les comandes del bot.
* ```/documentation``` - Proporciona la documentació del projecte.
* ```/author``` - Autor del projecte.
* ```/savedPolygons``` - Retorna els polígons creats fins al moment.
* ```readExpr()``` - No és una comanda executable. Serà el handler encarregat de llegir qualsevol missatge que no correspongui amb les comandes anteriors i passar-lo a l'evaluador de la nova gramàtica 

#### Gramàtica

Per tal d'interactuar amb la classe ```ConvexPoligon``` hem creat un llenguatge de programació que soporta la creació de polígons convexos, operacions i altres funcionalitats.

##### Assignacions

La comanda d'assignació associa una variable amb un polígon convexe. Si l'identificador no existeix es crearà un poligon nou. En cas contrari es sobreescriurà l'existent

##### Comanda ```print```

Imprimeix un ```string``` simple, un polígon existent o el polígon resultant d'una operació de polígons.

##### Comandes per obtenir informació d'un polígon

* ```area``` - retorna l'àrea d'un polígon.
* ```perimeter``` - retorna el perímetre d'un polígon.
* ```vertices``` - retorna el nombre de vèrtex d'un polígon.
* ```centroid``` - retorna el punt central d'un polígon.

##### Color

La comanda ```color``` acompanyada del codi de color i l'identificador d'un polígon ens permet canviar el color d'aquell polígon. El color per defecte és gris.

##### Comandes de comparació

* ```inside``` - donats dos polígons indica si el primer es troba dins del segon.
* ```equal``` - donats dos polígons indica si són iguals.

##### Comanda ```draw```

Donat un nom de fitxer amb extensió ```.png``` i una llista d'identificadors indefinida de polígons retorna una imatge amb els polígons dibuixats amb el color corresponent.

##### Operadors

* ```*``` - representa la intersecció entre dos polígons.
* ```+``` - representa la unió entre dos polígons.
* ```#``` - operador unari que retorna la bounding box (o capsa englobant) d'un polígon en forma de quatre vèrtex.
* ```!n``` - retorna un polígon creat a partir de ```n``` punts aleatoris dins del rang ([0,1]²). No es garanteix que el polígon convex resultant tingui n punts ja que és possible que alguns d'ells quedin a dintre del convex hull i, per tant, no s'incloguin al polígon.

##### Exemple

Script d'exemple:

```
// sample script
p1 := [0 0  0 1  1 1  0.2 0.8] //one separation space between x and y components, two between points
color p1, {1 0 0}
print p1
area p1
perimeter p1
vertices p1
centroid p1

print "---"

p2 := [0 0  1 0  1 1]
color p2, {0 1 0}
print p2
equal p1, p2
inside p1, p2
inside [0.8 0.2], p2

draw "image.png", p1, p2

print "---"

print p1 + p2                           // convex union
print p1 * p2                           // intersection
print #p2                               // bounding box
equal p1 + p2, #p2                      // complex operations
p3 := #((p1 + p2) * [0 0  1 0  1 1])    // complex operations

p3 := [-0.5 -0.5  -0.5 0.5  0.5 0.5  0.5 -0.5]
color p3, {0 0 1}
draw "image.png", p1, p2, p3

r := !100                               // convex polygon made with 100 random points
```

output corresponent:

```
0.000 0.000 0.000 1.000 1.000 1.000
0.500
3.414
3
0.333 0.667
---
0.000 0.000 1.000 1.000 1.000 0.000
no
no
yes
---
0.000 0.000 0.000 1.000 1.000 1.000 1.000 0.000
0.000 0.000 1.000 1.000
0.000 0.000 0.000 1.000 1.000 1.000 1.000 0.000
yes
```


## Arxius principals

Breu explicació dels arxius principals del projecte

### Arxiu ```bot.py```

Arxiu que s'encarrega d'executar el bot de Telegram i d'establir la comunicació entre l'usuari i l'evaluador de la nostra gramàtica. Cada cop que s'inicialitza (o es reinicia) el bot es crea una nova instància de la classe EvalPolygon i, per tant, s'esborren tots els polígons que s'havien creat previament. Per comunicar-se amb l'evaluador, el bot captura tots els missatges que li envia l'usuari i, si no corresponen amb cap comanda predefinida, convertirà el text del missatge en un ```InputStream()``` que enviarà a la classe EvalPolygon. El resultat obtingut es retornarà a l'usuari en forma de missatge.

### Arxiu ```Polygons.py```

Implementa la classe ConvexPoligon i totes les seves operacions. És usada per ```EvalPolygon``` per a crear els polígons i efectuar operacions en funció de les comandes rebudes des del bot.

#### Classe ```ConvexPolygon```

La classe ```ConvexPolygon``` consta dels dos atributs privats ```points``` i ```color``` que representen, respectivament, els punts que formen el polígon, mitjançant una llista de tuples de dos ```floats```, i el color amb que s'ha de representar, amb una tupla de tres enters dins del rang [0,255]. Dins del codi es pot trobar una descripció més detallada de cada funció que implementa la classe.

### Arxiu ```EvalPolygon.py```

Aquest arxiu implementa la classe ```EvalPolygon``` que funciona com a intèrpret de la gramàtica definida en el fitxer ```Polygon.g```. La classe disposa d'un atribut que representa un diccionari on es guardaran totes les instàncies de la classe ConvexPolygon creades amb l'identificador corresponent desat com a key. Els mètodes definits en aquesta classe evaluen els arbres de cada expressió rebuda, els interpreten i en retornen el resultat corresponent.

## Desenvolupat amb

* [Python3](https://docs.python.org/3/) - Per a la classe ConvexPolygon i el bot de Telegram
* [ANTLR4](https://www.antlr.org/) - Per a crear la gramàtica del nou llenguatge de programació


## Autor

* **Arnau Junquera Orozco** - *Llenguatges de Programació, Curs 2020/21 Q1* 

