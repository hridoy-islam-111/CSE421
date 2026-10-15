# CSE421: Computer Networks

**Department of Computer Science and Engineering**  
**BRAC University (BRACU)**

---

## 📖 Course Description

**CSE421 (Computer Networks)** is an undergraduate core course designed to provide students with a comprehensive understanding of the principles, architecture, and operation of modern computer communication networks. 

The course explores how interconnected computing systems communicate reliably and efficiently across local and global networks. Students study network layered models, standard communication protocols, data transmission mechanics, routing algorithms, and end-to-end transport services. Alongside theoretical concepts, the course emphasizes practical implementations through network socket programming, packet inspection, and protocol analysis.

---

## 🎯 Key Learning Objectives & Topics

- **Network Architectures & Models:**
  - In-depth study of the **OSI 7-Layer Model** and the **TCP/IP Protocol Suite**.
  - Encapsulation, de-encapsulation, and data flow across layers.

- **Application Layer:**
  - Core network applications and protocols including HTTP, HTTPS, DNS, FTP, and SMTP.
  - Principles of network applications and client-server paradigm.
  - Network programming using **Python Socket API** (TCP/UDP sockets, client-server communication, multi-threading).

- **Transport Layer:**
  - Reliable data transfer mechanics, error detection, flow control, and congestion control.
  - Connection-oriented protocol (**TCP**) vs. connectionless protocol (**UDP**).
  - Three-way handshake, termination, sequence and acknowledgment numbers.

- **Network Layer:**
  - Packet forwarding vs. routing principles.
  - **IP Addressing:** IPv4 addressing, CIDR, subnetting, supernetting, and IPv6 transition.
  - Routing algorithms and protocols (Link-State/Dijkstra, Distance-Vector/Bellman-Ford, RIP, OSPF, BGP).

- **Data Link & Physical Layers:**
  - Framing, error detection and correction (Parity, Checksum, CRC).
  - Multiple Access Protocols (CSMA/CD, CSMA/CA), MAC addressing, and Ethernet switching.
  - Physical media, signaling, and transmission impairments.

- **Network Diagnostics & Analysis:**
  - Packet sniffing and traffic inspection using **Wireshark**.
  - Network topology design and simulations (e.g., Cisco Packet Tracer).

---

## 📂 Repository Structure

This repository contains lab tasks, socket programming implementations, and course-related projects for the **CSE421 Laboratory**:

* **`LAB 01/`**: Introduction to Socket Programming in Python
  * [`server.py`](LAB%2001/server.py) — Socket binding, listening, and accepting client connections over TCP.
  * [`client.py`](LAB%2001/client.py) — Establishing client connection and exchanging messages with the server.

---

## 🛠️ Tools & Technologies

* **Language:** Python 3.x
* **Core Libraries:** `socket`, `threading`, `sys`, `os`
* **Analysis Tools:** Wireshark, Cisco Packet Tracer, Command-line network utilities (`ping`, `traceroute`, `netstat`, `ipconfig`)

