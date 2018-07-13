import Adafruit_MCP3008
import Adafruit_GPIO.SPI as SPI
import time
#Hardware SPI configuration

SPI_PORT = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT,SPI_DEVICE))

print('Initialization MCP3008', 'press CTRL+C to exit')
print('Logging Fuel sender Resistance')
while True:
    mcpChannels = [0]*8
    for i in range(8):
        mcpChannels[i] = mcp.read_adc(i)
    print('Raw value = {0:>4}'.format(mcpChannels[0]))
    raw = mcpChannels[0]
    numPercent = (raw/1024)*100
    print('Fuel {0}% of 100%'.format(*numPercent))
    time.sleep(0.5)