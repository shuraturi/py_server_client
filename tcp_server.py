import socket

def main():
    # Serving on localhost with port and buffer size
    SERVER_IP = "127.0.0.1"
    SERVER_PORT = 22835
    BUFFER_SIZE = 1024

    try:
        # Create TCP socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind and listen
        server_socket.bind((SERVER_IP, SERVER_PORT))
        server_socket.listen(5)
        print(f"TCP Server running on {SERVER_IP}:{SERVER_PORT}")

        while True:
            # Accept a client connection
            client_conn, client_addr = server_socket.accept()
            print(f"Connected by {client_addr}")

            try:
                while True:
                    # Receive data from client
                    data = client_conn.recv(BUFFER_SIZE)
                    if not data:
                        print(f"Client {client_addr} disconnected.")
                        break

                    message = data.decode().strip()

                    # Handle exit
                    if message.lower() == "exit":
                        print(f"Client {client_addr} requested disconnect.")
                        break

                    # Process input
                    if not message.isdigit():
                        response = "Invalid input! Please enter a number."
                    else:
                        num = int(message)
                        response = f"{num} is even." if num % 2 == 0 else f"{num} is odd."

                    # Send response
                    client_conn.sendall(response.encode())

            except ConnectionResetError:
                print(f"Client {client_addr} unexpectedly disconnected.")
            finally:
                # Close client connection
                client_conn.close()

    # Handle keyboard interrupt ctrl+c or any other errors
    except KeyboardInterrupt:
        print("\nServer shutting down...")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close listening socket
        server_socket.close()
        print("Server socket closed.")

# If guard used in case the program is imported in another file
if __name__ == "__main__":
    main()
