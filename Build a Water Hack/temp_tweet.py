from twython import Twython
#from smbus import SMBus
import RPi.GPIO as GPIO
import Adafruit_DHT
import os
import time

# Twitter authentication
APP_KEY='VUGqmTnFSQydnzERvu4rQxSey'
APP_SECRET='8iFacfxFV88LEv05alzdI2fFvSDf1ssabJsd3PnMt6N2ltbYSt'
OAUTH_TOKEN='550493525-10yQqjUjKrsyiYiFP1K5O7yq0drySsJ0OPMs8bEY'
OAUTH_TOKEN_SECRET='X8Qnnq4ct3e22x3l3UDMr166ME9O4WQeYagk9QmGKiWRd'

# Twython object
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# I2C globals
#ADDR = 0x27
#bus = SMBus(1)

# Special characters
deg = u'\N{DEGREE SIGN}'

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

# Add data logging functionality
try:
    f = open('/home/pi/humidity.csv', 'a+')
    if os.stat('/home/pi/humidity.csv').st_size == 0:
        f.write('Date,Time,Temperature,Humidity\r\n')
except:
    pass

#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(LED, GPIO.IN)

# Main loop
while True:
    # get current system date and time
    datetime = time.strftime('%m/%d/%Y %H:%M:%S')
    day = time.strftime('%m/%d/%Y')
    tim = time.strftime('%H:%M:%S')
    
    # Read data from sensor
    #bus.write_byte(ADDR, 0x00)
    #ans = bus.read_i2c_block_data(ADDR, 0x00, 4)
    #GPIO.input(sensor)
    #print("Precheck")
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    #print("Here")
    humd = '{:.0f}'.format(humidity)
    temp = '{:.1f}'.format(temperature)
    
    if humd is not None and temp is not None:
        print(datetime)
        print('Temperature: ' + str(temp) + deg + 'C')
        print('Humidity: ' + str(humd) + '%')
        print(' ')
        f.write('{0},{1},{2:0.1f}*C,{3:0.1f}%\r\n'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'), temperature, humidity))
        
        msg = 'Boom! It is ' + datetime + \
          '. The temperature is ' + str(temp) + \
          deg + 'C, and the humidity is ' + \
          str(humd) + '%. You should wear a jacket today.'
        
        twitter.update_status(status=msg) 
        
    else:
        print("Failed to retrieve data from sensor")
    
    # Convert data
    #humd = ((ans[0] & 0x3f) << 8) + ans[1]
    #humd = humd * float('6.10e-3')
    #humd = '{:.0f}'.format(humd)
    #humd = 48
    
    # Convert temp to celsius
    #temp = (ans[2] << 8) + ans[3]
    #temp = temp >> 2
    #temp = (temp * float('1.006e-2')) - 40.0
    #temp = '{:.1f}'.format(temp)
    #temp = 23
    
    # Print date, time, temp, and humidity
    
    
    # Post to Twitter!

    
    # Delay (in seconds) before next message
    time.sleep(10)