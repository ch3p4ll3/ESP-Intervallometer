import bluetooth
from os import system


def scan_devices() -> list:
    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    devices = []

    for i, j in nearby_devices:
        devices.append((j, i))

    return devices


def connect_to_device(device_id) -> bluetooth.BluetoothSocket:
    bt_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    bt_socket.connect((device_id, 1))

    return bt_socket


def send_message(bt_socket, message) -> None:
    try:
        bt_socket.send(message)
    except:
        pass


def print_menu() -> None:
    system("clear")
    print("0) Single shot")
    print("1) Bulb")
    print("2) Timer bulb")
    print("3) Intervallometer")
    print("4) Stop")
    print("Something else for exit")


def parse_method(method, bt_sock) -> None:
    if method.isdigit():
        method = int(method)
        if method == 0:
            send_message(bt_sock, "singleShot#")
        elif method == 1:
            send_message(bt_sock, "Bulb#")
        elif method == 2:
            print("For how many seconds must the shutter remain open?")
            seconds = -1
            while seconds <= 0:
                try:
                    seconds = int(input("seconds: "))
                except ValueError:
                    pass

            send_message(bt_sock, f'timerBulb#{seconds}')
        elif method == 3:
            print("How many seconds between shots?")
            seconds = -1
            while seconds <= 0:
                try:
                    seconds = int(input("seconds: "))
                except ValueError:
                    pass

            print("How many shots?")
            shots = -1
            while shots <= 0:
                try:
                    shots = int(input("shots: "))
                except ValueError:
                    pass

            send_message(bt_sock, f'intervallometer#{seconds}#{shots}')
        elif method == 4:
            send_message(bt_sock, "stop")

    else:
        bt_sock.close()
        exit(0)


def main() -> None:
    system("clear")
    print("Scanning for devices")
    devices = scan_devices()
    for key, i in enumerate(devices):
        print(f'{key}) {i[0]} - {i[1]}')

    if len(devices) == 0:
        main()

    choice = input("Select device: ")

    if choice.isdigit():
        try:
            print(f'Connecting to {devices[int(choice)][0]}')
            bt_sock = connect_to_device(devices[int(choice)][1])
            while True:
                print_menu()
                method = input("-> ")
                parse_method(method, bt_sock)
        except IndexError:
            pass


if __name__ == '__main__':
    main()
