
while True:
    analogValue = 2048
    analogValue2 = 2048
    write4921(analogValue2, spi2, cs2) #in testing right now
    write4921(analogValue, spi1, cs1)
    time.sleep(2)
