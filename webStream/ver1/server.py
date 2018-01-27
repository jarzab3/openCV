import socket
import sys
import cv2
import pickle
import numpy as np

HOST=''
PORT=8089

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Socket created')

s.bind((HOST,PORT))
print('Socket bind complete')
s.listen(10)
print('Socket now listening')

conn, addr=s.accept()

while True:
    try:
        data=conn.recv(80)
        print(sys.getsizeof(data))
        print(data)
        print("\n")
        print("\n")
        # print("\n")
        frame=pickle.loads(data)
        # print(frame)
        # cv2.imshow('frame', frame)

    except KeyboardInterrupt:
        s.close()
        print("Close connection")
        break




















    # import socket
    # import sys
    # import cv2
    # import pickle
    # import numpy as np
    #
    # HOST = ''
    # PORT = 8089
    #
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # print('Socket created')
    #
    # s.bind((HOST, PORT))
    # print('Socket bind complete')
    # s.listen(10)
    # print('Socket now listening')
    #
    # conn, addr = s.accept()
    #
    # data = []
    #
    # while True:
    #     try:
    #
    #         packet = conn.recv(80)
    #
    #         if not packet:
    #             break
    #
    #         data.append(packet)
    #
    #         data_e = pickle.loads(packet)
    #
    #         data_arr = pickle.loads(b"".join(data))
    #
    #         print(data_e)
    #
    #     except KeyboardInterrupt:
    #         s.close()
    #         print("Close connection")
    #         break
    #
    # data_arr = pickle.loads(b"".join(data))
    # # data_arr = pickle.loads(packet)
    #
    # print(data_arr)
    #
    # # print(sys.getsizeof(data))
    #
    # data_arr = pickle.loads(data)
    #
    # frame = pickle.loads(data)
    #
    # # print(frame)
    #
    # cv2.imshow('frame', frame)
    # # s.close()
    #
    # # data = []
    # # while True:
    # #     packet = s.recv(4096)
    # # if not packet: break
    # # data.append(packet)
    # # data_arr = pickle.loads(b"".join(data))
    # # print(data_arr)
    # # s.close()
