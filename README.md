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

###Comandes

* ```/start``` - Inicialitza el bot.
* ```/instructions``` - Proporciona informació sobre les comandes del bot.
* ```/documentation``` - Proporciona la documentació del projecte.
* ```/author``` - Autor del projecte.
* ```readExpr()``` - No és una comanda executable. Serà el handler encarregat de llegir qualsevol missatge que no correspongui amb les comandes anteriors i passar-lo a l'evaluador de la nova gramàtica 


## Desenvolupat amb

* [Python3](https://docs.python.org/3/) - Per a la classe ConvexPolygon i el bot de Telegram
* [ANTLR4](https://www.antlr.org/) - Per a crear la gramàtica del nou llenguatge de programació


## Author

* **Arnau Junquera Orozco** - *Llenguatges de Programació, Curs 2020/21 Q1* 

