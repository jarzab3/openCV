__AUTHOR__=u"DK"

import cv2
import numpy as np
import socket
import sys
import pickle
import struct


def StartStreamSending():
    u"""
    Funkcja przesyłająca stream z lokalnej kamery[0] na serwer.
    """
    UDP_IP = "10.3.254.31"
    UDP_PORT = 8012
    cap=cv2.VideoCapture(0)
    clientsocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    ret,frame=cap.read()
    #result, img_str = cv2.imencode('.jpeg', frame)
    #img_str2 = np.array(img_str)

    #pik = pickle.Pickler()
    #frame = np.reshape(frame, (240,320,3))
    data = np.array(frame)
    dataToSend = pickle.dumps(data)
    size = sys.getsizeof(dataToSend)
    print(size)
    print(type(dataToSend));

    clientsocket.sendto(dataToSend, (UDP_IP, UDP_PORT))

StartStreamSending()