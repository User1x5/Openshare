import zipfile
import socket
import json
import os

version = "0.1"
name = "OpenShare"  # will change this to bakashare april fools

tcp_port = 2763

print(name, version)


def menu():
    print("""
    [1] Send something
    [2] Receive something
    [3] Settings
    [4] About
    [5] Exit
    """)

    choice = input("Select an option: ")

    if choice == "1":
        print("Send mode selected!")
        send()

    elif choice == "2":
        print("Receive mode selected!")
        receive()

    elif choice == "3":
        print("Settings selected!")

    elif choice == "4":
        print(name, version)  # NO HARD CODING

    elif choice == "5":
        print("Goodbye!")

    else:
        print("Invalid option!")


def receive():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", tcp_port))
    server.listen()

    print("OpenShare is ready to receive!")

    connection, address = server.accept()

    print("Connected by:", address[0])

    recvbytes = connection.recv(1024)
    recvstring = recvbytes.decode()
    rheader = json.loads(recvstring)

    total = rheader["size"]
    filename = os.path.basename(rheader["filename"])

    print(f"Header received! total bytes: {total}, Name: {filename}")

    connection.sendall(b"OK")

    received = b""

    while len(received) < total:
        chunk = connection.recv(1024)

        if not chunk:
            print("Transfer interrupted!")
            connection.close()
            server.close()
            return

        received += chunk

    print("File successfully received")

    with open(filename, "wb") as file:
        file.write(received)

    if rheader["type"]:  # Type is SPECIFICALLY for only folders so it applies
        print("Folder transferred")
        with zipfile.ZipFile(filename, "r", zipfile.ZIP_DEFLATED) as archive:
            archive.extractall(filename, "_opensharefolder")
            print("Folder decompressed in the current dir")
    connection.close()
    server.close()

    print("All done! :)")


def send():
    print("Which type of file to send?")
    print("1: File")
    print("2: Folder")
    sel = input("> ")

    if sel == "1":
        ipaddr = input("Receiver IP address: ")

        filename = input("File to send: ")

        if not os.path.isfile(filename):
            print("File not found!")
            return

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        with open(filename, "rb") as file:
            data = file.read()

        size = len(data)

        header = {"size": size, "filename": os.path.basename(filename), "type": "file"}

        jheader = json.dumps(header)

        try:
            client.connect((ipaddr, tcp_port))

            print("Sending header...")
            client.sendall(jheader.encode())

            response = client.recv(2)

            if response.decode() == "OK":
                print("Accepted, sending now.")
                client.sendall(data)
                print("Transfer sent!")

            else:
                print("Receiver rejected the transfer.")

        except OSError as error:
            print("Connection error:", error)

        finally:
            client.close()

    elif sel == "2":
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ipaddr = input("Receiver IP: ")
        foldy = input("Folder to send: ")  # bfb
        if os.path.isdir(foldy):
            with zipfile.ZipFile(
                "opensharefoldy.zip", "w", zipfile.ZIP_DEFLATED
            ) as archive:
                for root, dirs, files in os.walk(foldy):
                    for filename in files:
                        filepath = os.path.join(root, filename)
                        archive.write(filepath)

            with open("opensharefoldy.zip", "rb") as folder:  # Get specifications
                data = folder.read()
                size = len(data)
                folder.close

            print("Fetching receiver")

            try:
                client.connect((ipaddr, tcp_port))

                header = {
                    "filename": os.path.basename(foldy),
                    "size": size,
                    "type": "zip",
                }  # i think this just removes the dir tree
                jheader = json.dumps(header)
                client.sendall(jheader.encode())

                response = client.recv(
                    3
                )  # I never explained this, but i did 3 instead of 2 for good measure

                if response.decode() == "OK":
                    print("Receiver accepted, sending.")
                    client.sendall(
                        data
                    )  # Since it is on binary and its on bits its fine, and it also works because its just

                else:
                    print("Receiver canceled transfer")

            except OSError as error:
                print("Something went wrong! Error: ", error)


menu()
