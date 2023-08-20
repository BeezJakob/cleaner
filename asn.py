import threading
import socket

def reverse_ip_to_domain(ip):
    try:
        domain = socket.gethostbyaddr(ip)[0]
        print(f"{ip} => {domain}")
    except socket.herror:
        print(f"No domain found for IP: {ip}")

def main():
    filename = input("Enter the name of the text file containing IP addresses: ")
    num_threads = int(input("Enter the number of threads to use: "))

    with open(filename, 'r') as file:
        ip_addresses = file.read().splitlines()

    threads = []
    for ip in ip_addresses:
        t = threading.Thread(target=reverse_ip_to_domain, args=(ip,))
        threads.append(t)
        t.start()

        if len(threads) >= num_threads:
            for thread in threads:
                thread.join()
            threads = []

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
