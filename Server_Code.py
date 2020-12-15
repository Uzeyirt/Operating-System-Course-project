#Uzeyir Topaloglu 2079424
#Esmafer Direybatogullari 2015998
import threading
import os
import socket
is_TCP_CONNECTION_LOCK_Available = True
TCP_IP = '127.0.0.1'
TCP_PORT = 5555
BUFFER_SIZE = 1024

def acquire_lock():
    is_TCP_CONNECTION_LOCK_Available = False

def release_lock():
    is_TCP_CONNECTION_LOCK_Available = True

def Purification(Impure_List):
    Pure_List =[] # I will take all txt files and collect them in this array
    for element in Impure_List :
        if element[-4:] =='.txt':
            Pure_List.append(element)

    return Pure_List

def SearchFile(FileName,PathofFile,search_word,s):
    Words =[]
    counter=1
    FullPath =PathofFile + FileName
    FileContent = open(FullPath).read()   #read full file
    lines=FileContent.split('\n')  #create array of lines
    for line in lines:
        Words =Words + line.split(' ')   #creating array of words
    for word in Words:
        if word==search_word:
            s.send ((str(counter) +'. ' + str(search_word) + ' for ' + str(FileName) + ' was founded '))
            counter+=1
def Connection_Thread_Function():
    while is_TCP_CONNECTION_LOCK_Available == False:
        number = 5 #it means nothing (just waiting for lock)

    acquire_lock()
    print('Ready for connection ! ')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)
    conn, addr = s.accept()

    while 1:
        data = conn.recv(BUFFER_SIZE)
        if not data: break
        TCP_input = data.split(' ')
        SearchWord = TCP_input[0]
        DctPath = TCP_input[1]
        break

    conn.close()

    Threads = []

    # Important note:DctPath should end with backslash     (shouldn`t forget last backslash)
    FileList = os.listdir(DctPath)  # collect files which are in that directory and put them into an array(not only txt files)
    FileList = Purification(FileList)  # Eliminate files that are not txt files

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Server need to send Search results to client,
    s.connect((TCP_IP, 6666))  # so it is sender now

    for File in FileList:
        thread = threading.Thread(target=SearchFile, args=(File, DctPath, SearchWord,s))  # assingment of threads to txt files to make search operation
        Threads.append(thread)

    for thread in Threads:  # initialize threads
        thread.start()
    for thread in Threads:  # main process waits for termination of all threats
        thread.join()

    s.close()
    release_lock()
    print('connection has been terminated ! ')
# start of Main process

Connection_Thread_List = []
Connection_Thread_1 = threading.Thread(target=Connection_Thread_Function())
Connection_Thread_List.append(Connection_Thread_1)
Connection_Thread_2 = threading.Thread(target=Connection_Thread_Function())
Connection_Thread_List.append(Connection_Thread_2)
Connection_Thread_3 = threading.Thread(target=Connection_Thread_Function())
Connection_Thread_List.append(Connection_Thread_3)
for Connection_Thread in Connection_Thread_List:
    Connection_Thread.start()
for Connection_Thread in Connection_Thread_List:
    Connection_Thread.join()

