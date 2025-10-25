import socket

def main():
    # Server IP address & port to connect to
    SERVER_IP = "127.0.0.1"
    SERVER_PORT = 22834
    BUFFER_SIZE = 1024

    # Create UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        client_socket.settimeout(5.0)  # prevent indefinite blocking

        print("UDP Client started. Type 'exit' to quit.")

        while True:
            try:
                # Get user input
                message = input("Enter a number: ").strip()
                if message.lower() == "exit":
                    client_socket.sendto(message.encode(), (SERVER_IP, SERVER_PORT))
                    print("Exiting client...")
                    break

                # Send message to server
                client_socket.sendto(message.encode(), (SERVER_IP, SERVER_PORT))

                # Receive server response
                response, _ = client_socket.recvfrom(BUFFER_SIZE)
                print("Server response:", response.decode())

            except socket.timeout:
                print("No response from server. Try again.")
            except KeyboardInterrupt:
                print("\nClient terminated by user.")
                break
            except Exception as e:
                print(f"Error: {e}")
                break

if __name__ == "__main__":
    main()
