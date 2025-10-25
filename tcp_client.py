import socket

def main():
    # Server IP address & port to connect to
    SERVER_IP = "127.0.0.1"
    SERVER_PORT = 22835
    BUFFER_SIZE = 1024

    try:
        # Create TCP socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to server
        client_socket.connect((SERVER_IP, SERVER_PORT))
        print(f"Connected to TCP server at {SERVER_IP}:{SERVER_PORT}")
        print("Type 'exit' to quit.\n")

        while True:
            # Get user input
            message = input("Enter a number: ").strip()

            if message.lower() == "exit":
                print("Disconnecting...")
                break

            # Send data to server
            client_socket.sendall(message.encode())

            # Receive and display response
            response = client_socket.recv(BUFFER_SIZE).decode()
            print("Server response:", response)

    except ConnectionRefusedError:
        print("Server is unavailable. Make sure the server is running.")
    except KeyboardInterrupt:
        print("\nClient terminated by user.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close socket
        client_socket.close()
        print("Connection closed.")

if __name__ == "__main__":
    main()
