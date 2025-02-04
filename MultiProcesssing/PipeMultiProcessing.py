# multiprocessing.Pipe: It provides a two-way communication channel between two processes.
# This is a more direct way of passing data between processes, but it only works between two processe
#  (unlike Queue or Manager which can be shared by many processes).

# Pipe allows two processes to communicate with each other directly by sending and receiving messages. 
# It's a low-level mechanism for IPC.

import multiprocessing
import time

def sender(conn):
    time.sleep(1)
    message = "Hello from sender"
    print(f"Sender sending message: {message}")
    conn.send(message)
    conn.close()

def receiver(conn):
    message = conn.recv()
    print(f"Receiver received message: {message}")

if __name__ == "__main__":
    parent_conn, child_conn = multiprocessing.Pipe()

    sender_process = multiprocessing.Process(target=sender, args=(child_conn,))
    receiver_process = multiprocessing.Process(target=receiver, args=(parent_conn,))

    sender_process.start()
    receiver_process.start()

    sender_process.join()
    receiver_process.join()

    print("Both sender and receiver processes finished.")
