import socket
import threading
import argparse
import csv
from datetime import datetime

open_ports = []
lock = threading.Lock()

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))

        if result == 0:
            try:
                sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
                banner = sock.recv(1024).decode(errors="ignore").strip()
            except:
                banner = ""

            with lock:
                open_ports.append((port, banner))
                print(f"  [OPEN] Port {port:<6} {banner[:50]}")

        sock.close()

    except socket.error:
        pass

def run_scan(target, start_port, end_port):
    print(f"\n{'='*50}")
    print(f"  Target  : {target}")
    print(f"  Ports   : {start_port} - {end_port}")
    print(f"  Started : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*50}\n")

    threads = []
    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(target, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

def save_results(target, filename):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Port", "Banner", "Scanned At"])
        for port, banner in sorted(open_ports):
            writer.writerow([port, banner, datetime.now().strftime('%Y-%m-%d %H:%M:%S')])
    print(f"  Results saved → {filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Python Port Scanner")
    parser.add_argument("target", help="Target IP or hostname")
    parser.add_argument("-s", "--start", type=int, default=1, help="Start port")
    parser.add_argument("-e", "--end", type=int, default=1024, help="End port")
    parser.add_argument("-o", "--output", help="Save results to CSV file")
    args = parser.parse_args()

    run_scan(args.target, args.start, args.end)
    print(f"\n  Scan complete. {len(open_ports)} open port(s) found.")

    if args.output:
        save_results(args.target, args.output)