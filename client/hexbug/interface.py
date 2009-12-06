import serial

class HexBug(object):
  def __init__(self, serialLoc = '/dev/ttyUSB0'):
    self.serial = serial.Serial(serialLoc, 9600)

  def walkForward(self):
    self.serial.write('f')

  def walkReverse(self):
    self.serial.write('r')

  def spinLeft(self):
    self.serial.write('l')

  def spinRight(self):
    self.serial.write('R')

  def stopWalk(self):
    self.serial.write('s')

  def stopSpin(self):
    self.serial.write('S')

  def stopAll(self):
    self.serial.write('k')
