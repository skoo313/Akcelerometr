import socket 
import threading
import json
import time
import influx_test_database as ifdb
# import client as cl
import datetime

HEADER = 2048                          # header to receive right data
PORT = 8090                            # port where we communicate
SERVER = '192.168.43.206'              # server is on my computer

ADDR = (SERVER, PORT)                                   
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET - IPV4, SOCK_STREAM - TCP
server.bind(ADDR)
buffer = []
db_name = 'akcelerometr_01'
db_user = 'test_01'
db_password = 'haslo'

#tryby działania: 1 oznacza start pomiaru
mode = "0"

#nazwa tabeli ustalana po wcisnieciu przycisku we wtyczce
table_name=""

def handle_client(conn, addr):
    global mode
    print(f"[NEW CONNECTION] {addr} connected.")
    
    try:
        message = conn.recv(HEADER).decode(FORMAT)
        #print()
        #print("message -> " + message +" <- ")
        #print()
        
        if(message and mode=="1"):            
            #print(addr[0])


            try:
                ifdb.setup_server_json(message,addr,db_name, db_user, db_password)
                print(f"Stworzono baze danych o nazwie:{db_name}")
            except:
                json_setup = json.loads(message) 
                  

                
                json_body = {
                        "measurement": table_name,
                        "tags": {
                            "name": table_name
                        },
                        "fields": {
                            "x" : json_setup["sensor_x"],
                            "y" : json_setup['sensor_y'],
                            "z" : json_setup["sensor_z"],

                            "current time" : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
                        }
                            }   
                buffer.append(json_body)
                

                
                if len(buffer) == 1:
                    print("OK")
                    ifdb.loop_server_json(buffer,addr,db_name)
                    buffer.clear()
        else: 
            print("wiadomosc jest pusta lub nie rozpoczęto pomiaru")
    except:
        print('handle_client problem ')


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

def listener(name,PORT):
    '''Funkcja obslugująca polaczenie z wtyczka. Jesli wcisniety jest 1szy odpala pomiar i pobiera czas potrzebny do nazwania tabeli'''
    global mode
    global table_name

    while True:

        print("THREAD "+str(name))
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((SERVER, PORT))
            s.listen(1)
            conn, addr = s.accept()
            s.close()
            with conn:

                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        print("dostalem pinga, thread "+str(name))
                        
                        #name to numer przycisku z wtyczki
                        mode = str(name)

                        if(mode=="1"): 
                            #nazwa tabeli
                            table_name = datetime.datetime.now().strftime("%Y-%m-%dX%H:%M:%S")
                        break
                    conn.sendall(data)

                stringdata = data.decode('utf-8', errors="ignore")
                #print()
                print(stringdata)
                time.sleep(0.1)
                # s.settimeout(20)
                # break

if __name__ == '__main__':
    
    # nasłuchiwanie na portach czy przyciski we wtyczce sa kliknięte
    PORTS = [8091,8092,8093]

    print("Starting Threads")
    x = threading.Thread(target=listener, args=(1,PORTS[0]))
    y = threading.Thread(target=listener, args=(2,PORTS[1]))
    z = threading.Thread(target=listener, args=(3,PORTS[2]))
    
    x.start()
    y.start()
    z.start()

    
    print("[STARTING] server is starting...")
    start()


    x.join()
    print("Main    : all done")
