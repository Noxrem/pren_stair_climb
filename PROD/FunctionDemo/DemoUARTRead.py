import UARTAccess

access = UARTAccess.UARTAccess()
message = access.read()
print('******************Message below**********************')
print(message)
