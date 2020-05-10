#!/usr/bin/env python

import serial
import time
import sys

class RFID_CR522U:

	InitializePort = 0x0101;
	SetDeviceNodeNumber = 0x0102;
	ReadDeviceNodeNumber = 0x0103;
	ReadDeviceMode = 0x0104;
	SetBuzzerBeep =  0x0106;
	SetLedcolor = 0x0107;
	SetReaderWorkingStatus = 0x0108;
	SetAntennaStatus = 0x010c;
	MifareRequest = 0x0201;
	MifareAnticollision = 0x0202;
	MifareSelect = 0x0203;
	MifareHlta = 0x0204;
	MifareAuthentication1 = 0x0206;
	MifareAuthentication2 = 0x0207;
	MifareRead = 0x0208;
	MifareWrite = 0x0209;
	MifareInitval = 0x020A;
	MifareReadBalance = 0x020B;
	MifareDecrement = 0x020C;
	MifareIncrement = 0x020D;
	MifareRestore = 0x020E;
	MifareTransfer = 0x020F;
	MifareUltraLightAnticoll = 0x0212;
	MifareUltraLightWrite = 0x0213;

	def __init__ (self, dev='/dev/ttyUSB0'):
		self.ser = serial.Serial(dev, 19200, timeout=1, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE);
		#self.ser = serial.Serial(dev, 19200, timeout=1, );	#Init UART 19200,8,N,1 ,  time out 1s
		# ( port , 19200, timeout=1, parity=serial.PARITY_EVEN, rtscts=1);


	def CR522_BuzzerBeep (self):
		values = bytearray([0xaa, 0xbb , 0x06 , 0x00 0x00 , 0x00 , 0x07 , 0x01 ,0x03 ,0x05]);
		ser.write(values);
		#need read for verify?

	def CR522_LEDGREEN_ON (self):

	def CR522_LEDGREEN_OFF (self):	#Need Test
		values = bytearray([0xaa, 0xbb , 0x06 , 0x00 0x00 , 0x00 , 0x07 , 0x01 ,0x03 ,0x05]);
		ser.write(values);
		#need read for verify?
