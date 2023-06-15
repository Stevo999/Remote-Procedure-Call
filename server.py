from xmlrpc.server import SimpleXMLRPCServer

def add(i, j):
    return i + j

def sort(array):
    return sorted(array)

server = SimpleXMLRPCServer(("localhost", 8000))
server.register_function(add, "add")
server.register_function(sort, "sort")

print("Server listening on port 8000...")
server.serve_forever()

