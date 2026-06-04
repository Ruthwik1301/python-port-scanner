# Python Port Scanner

A fast, multi-threaded TCP port scanner built from scratch in Python.
Scans a target host for open ports, grabs service banners, and exports results to CSV.

## Features
- Multi-threaded scanning for fast results
- Banner grabbing on open ports
- CSV export with timestamp
- Configurable port range via CLI

## Demo
==================================================
Target  : scanme.nmap.org
Ports   : 1 - 1024
Started : 2026-06-04 12:13:42
[OPEN] Port 22
[OPEN] Port 80     HTTP/1.1 200 OK
Scan complete. 2 open port(s) found.
Results saved → results.csv

## Usage
```bash
python3 scanner.py <target> -s <start_port> -e <end_port> -o <output.csv>
```

## Examples
```bash
# Scan ports 1-1024
python3 scanner.py scanme.nmap.org -s 1 -e 1024

# Scan and save results
python3 scanner.py scanme.nmap.org -s 1 -e 1024 -o results.csv
```

## Skills demonstrated
- Python socket programming
- Multi-threading
- Network fundamentals
- CLI tool design

## Disclaimer
Only scan hosts you have permission to scan.
scanme.nmap.org is provided by Nmap for legal testing.

## Author
T.Ruthwik — B.Tech CS, NIT Andhra Pradesh , 3rd year.