import pico
from pico import PicoApp
from hko_9day import get9dayJson
from hko_current import getCurrentJson

@pico.expose()
def getReport():
	nineDayForcast = get9dayJson()
	currentWeather = getCurrentJson()
	return ("{ currentWeather: %s ,  forcast :  %s }" %(currentWeather, nineDayForcast))

app = PicoApp()
app.register_module(__name__)

#for testing only
#print(getReport())
