import socket

def main():
    # Serving on localhost with port and buffer size
    SERVER_IP = "127.0.0.1"
    SERVER_PORT = 22834
    BUFFER_SIZE = 1024

    # Creating UDP socket for the server to use
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind((SERVER_IP, SERVER_PORT))
        print(f"UDP Server is running on {SERVER_IP}:{SERVER_PORT}")

        # Loop to keep server running and respond to connected clients
        while True:
            try:
                # Wait for data from client
                data, client_address = server_socket.recvfrom(BUFFER_SIZE)
                message = data.decode().strip()

                # Handle exit command
                if message.lower() == "exit":
                    print(f"Client {client_address} disconnected.")
                    continue

                # Check if input is a valid number, if it is responds back
                if not message.isdigit():
                    response = "Invalid input! Please send a valid integer."
                else:
                    number = int(message)
                    response = f"{number} is even." if number % 2 == 0 else f"{number} is odd."

                # Send result back to client
                server_socket.sendto(response.encode(), client_address)

            # Handle keyboard interrupt ctrl+c or any other errors
            except KeyboardInterrupt:
                print("\nServer shutting down...")
                break
            except Exception as e:
                print(f"Error: {e}")

# If guard used in case the program is imported in another file
if __name__ == "__main__":
    main()
