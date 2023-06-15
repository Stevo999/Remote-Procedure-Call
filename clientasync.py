from xmlrpc.client import ServerProxy, MultiCall

server = ServerProxy("http://localhost:8000")

multicall = MultiCall(server)
multicall.add(3, 4)
multicall.sort([9, 2, 5, 1, 7])

result_add = multicall.add()
result_sort = multicall.sort()

print("Addition result:", result_add)
print("Sorted array:", result_sort)

