
# Original script acquired from https://github.com/adafruit/Adafruit_Python_MCP3008
# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import time

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

def readadc(channel):
	if (channel==0): return mcp.read_adc(0)
	elif (channel==1):
		degrees = ((float(mcp.read_adc(1)))/1024)*100
		return degrees
	elif (channel==2): 
                volts = (mcp.read_adc(2)*3.3)/float(1023)
		return volts
	else :
		print("Eish!")
