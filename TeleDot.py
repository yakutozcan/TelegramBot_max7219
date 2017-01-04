import telepot
import time
import max7219.led as led
from max7219.font import proportional, SINCLAIR_FONT, TINY_FONT, CP437_FONT

device = led.matrix(cascaded=1)

#smile
device.letter(0, 1)
chat_listen = {}

def handle(msg):
    command = msg['text']
    print 'Gelen: %s' % command
    words = command.split("/")
    #/ isaretinden sonraki mesajı yazdırır
    device.show_message(words[1], font=SINCLAIR_FONT, delay=0.08)
    #smile
    device.letter(0, 1)
    #Istenilen noktalari x,y kordinatlarinda yakar.
    #device.pixel(0, 0, 0, redraw=True)


bot = telepot.Bot('292346928:AAFkTCWYOBW7Xq19Utg8pCgs2fBXIRfKdcg')
bot.message_loop(handle)
print 'Bot Dinliyor ...'

while True:
    time.sleep(10)
