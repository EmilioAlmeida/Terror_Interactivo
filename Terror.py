pages = [
    "Soñaba que caía a un pozo profundo,\nno dejaba de caer... me desperte de golpe y pensé  SIGO CAYENDO! \nEscuché ruidos extraños y voces dentro de mi casa... \nQué harías en mi lugar?\n1) Quedarme quieto bajo las sábanas\n2) Huir corriendo al baño y mojarme la cara\n3) Pedir ayuda",
    "Page 1) Me quede inmóvil, esperando a que el sueño pase...\nDe repente cortaron la luz, mucha oscuridad... \nHubo mucho ruido... Sentí que algo me golpeaba la cabeza... \nFIN",
    "Page 2) Salí corriendo por las escaleras hacia el baño... de repente se apagaron todas las luces y escuché las voces acercarse \ntropecé cayendo al suelo, logré entrar al baño... \nQué vas a hacer?\n4) Bloquear la puerta\n5) Esconderme en dentro de la bañera\n6) Saltar por la ventana",
    "Page 3) Quise pedir ayuda, no había señal en mi móvil, cortaron la línea del teléfono fijo y cuando quise abrir la ventana para gritar, \nsentí un fuerte golpe en la cabeza y me desmayé. \nFIN",
    "Page 4) Me senté detrás de la puerta estirándome para bloquearla \nSentí que una mano me apretaba el hombro, quedé mudo de horror... FIN",
    "Page 5) Dentro de la bañera me quede inmóvil, esperando a que los extraños se vayan de casa... \nDe repente reconocí una voz, no era buen presagio \nSE abrío la puerta del baño, corrieron la cortina de la ducha y se me heló la sangre al ver ese rostro \nFIN",
    "Page 6) Salté por la ventana... Había mucha gente en la calle, \nví como desde mi casa unos ojos brillaban en la oscuridad al mirarme... TO BE CONTINUED..."
]

def showPage(pageNumber):
    text = pages[pageNumber]
    print(text)
    response = input()
    showPage(int(response))

showPage(0)

