import socket
import sys
import json
import time
import random
import board
import busio
import adafruit_adxl34x

HOST = '192.168.43.206'  # The server's hostname or IP address
PORT = 8090              # The port used by the server

def setup():
    '''Funkcja setup startuje bazę danych wysylajac nazwe tabeli do servera '''
    
    #słownik z danymi
    x={"table_name":16}

    #konwersja do jsona
    data = json.dumps(x)
    

    # Create a socket (SOCK_STREAM means a TCP socket)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
    # Connect to server and send data
        sock.connect((HOST, PORT))
        sock.sendall(bytes(data,encoding="utf-8"))
    finally:
        sock.close()

def loop():
    '''Funkcja loop w pętli wysyła dane na serwer '''

    # i2c = busio.I2C(board.SCL, board.SDA)
    # accelerometer = adafruit_adxl34x.ADXL345(i2c)
    X,Y,Z=0,0,0

    
        
    while True:
        

        #losowanie danych 
        X=float(str(round(random.randint(-10,10), 2)))
        Y=float(str(round(random.randint(-10,20), 2)))
        Z=float(str(round(random.randint(-20,10), 2)))

        #Pobieranie danych z akcelerometra 
        # X=float(str(round(accelerometer.acceleration[0], 2)))
        # Y=float(str(round(accelerometer.acceleration[1], 2)))
        # Z=float(str(round(accelerometer.acceleration[2], 2)))

        #pobrane dane w słowniku
        measurements ={"sensor_x": X, "sensor_y":Y, "sensor_z":Z, "table_name":16}
        
        #pobrane dane do jsona
        data = json.dumps(measurements)

        # Create a socket (SOCK_STREAM means a TCP socket)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            sock.connect((HOST, PORT))
            sock.sendall(bytes(data,encoding="utf-8"))
        except:
            print("Error!")
            time.sleep(5)
        finally:
            sock.close()
        
        print(data)
        time.sleep(1)


setup()
loop()