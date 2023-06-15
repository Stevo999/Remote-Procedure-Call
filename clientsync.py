




from xmlrpc.client import ServerProxy

server = ServerProxy("http://localhost:8000")

result = server.add(3, 4)
print("Addition result:", result)

array = [9, 2, 5, 1, 7]
sorted_array = server.sort(array)
print("Sorted array:", sorted_array)

