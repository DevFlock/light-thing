import eel
import yeelight

bulb = None

# Functions
@eel.expose
def connect(inputData):
    bulb = yeelight.Bulb(inputData)
    bulb.start_music(ip="192.168.1.68")
    bulb.toggle()

eel.init("src")
eel.start("index.html", size=(1200, 600))