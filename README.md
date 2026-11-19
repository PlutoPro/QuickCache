# QuickCache

QuickCache is a lightweight, asynchronous in-memory Key-Value cache server built in Python. It uses raw TCP sockets powered by Python's `asyncio` library to handle multiple concurrent client connections with zero external dependencies.

---

## Features

* **Asynchronous Concurrency:** Powered by Python's built-in `asyncio` event loop to manage multiple concurrent TCP connections efficiently.
* **Zero External Dependencies:** Built entirely with the Python Standard Library (`asyncio`).
* **Simple Text-Based Protocol:** Uses straightforward `SET` and `GET` commands over raw TCP.

---

## Getting Started

### Prerequisites

* Python **3.7+**

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com
   cd QuickCache
   ```

2. *(Optional)* Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

### Running the Server

Start the TCP server on `127.0.0.1:8888`:

```bash
python main.py
```

---

## Usage & Protocol

QuickCache communicates over raw TCP sockets rather than HTTP. Commands are plain-text, space-delimited strings terminated by a newline.

| Command | Syntax | Description | Example Response |
| :--- | :--- | :--- | :--- |
| **SET** | `SET <key> <value>` | Stores a value under the specified key. | `OK: name set to Alice` |
| **GET** | `GET <key>` | Retrieves the value for the specified key. | `name: Alice` or `name: Key not found` |

### Testing with Netcat (`nc`)

Connect to the running server from another terminal:

```bash
nc 127.0.0.1 8888
```

Send commands interactively:

```text
SET user_101 active
OK: user_101 set to active

GET user_101
user_101: active

GET missing_key
missing_key: Key not found
```

### Testing with Python

You can also connect programmatically using Python's `socket` module:

```python
import socket

with socket.create_connection(("127.0.0.1", 8888)) as sock:
    sock.sendall(b"SET language Python\n")
    print(sock.recv(1024).decode().strip())

    sock.sendall(b"GET language\n")
    print(sock.recv(1024).decode().strip())
```

---

## Roadmap

* [ ] Add `DELETE` command support
* [ ] Implement key expiration (TTL)
* [ ] Support values containing spaces or JSON payloads
* [ ] Add persistence / snapshotting to disk

---

## License

This project is open source and available under the [MIT License](LICENSE).
