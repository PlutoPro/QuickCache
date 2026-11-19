import asyncio

store = {}

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"Connection from {addr}")

    try:
        while True:
            data = await reader.read(100)
            if not data:
                break

            message = data.decode().strip()
            if not message:
                continue

            print(f"Received {message} from {addr}")

            parts = message.split()
            command = parts[0].upper()
            args = parts[1:]

            if command == "SET" and len(args) == 2:
                key, value = args
                store[key] = value
                response = f"OK: {key} set to {value}\n"
            elif command == "GET" and len(args) == 1:
                key = args[0]
                value = store.get(key, "Key not found")
                response = f"{key}: {value}\n"
            elif command == "DEL" and len(args) == 1:
                key = args[0]
                if key in store:
                    del store[key]
                    response = f"OK: {key} deleted\n"
                else:
                    response = f"ERROR: {key} not found\n"
            else:
                response = "ERROR: Use 'SET <key> <value>', 'GET <key>', or 'DEL <key>'\n"

            writer.write(response.encode())
            await writer.drain()
    except ConnectionResetError:
        pass
    finally:
        print(f"Closing connection from {addr}")
        writer.close()
        await writer.wait_closed()

async def main():
    server = await asyncio.start_server(handle_client, '127.0.0.1', 8888)
    print("Serving on 127.0.0.1:8888...")
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nServer stopped.")
