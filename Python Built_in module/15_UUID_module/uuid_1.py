import uuid

id = uuid.uuid1()

print(id)

c = uuid.uuid4()
print(c)

x=uuid.uuid5(uuid.NAMESPACE_DNS,"amazon.com")
y=uuid.uuid3(uuid.NAMESPACE_DNS,"Linkedin.com")
print(y)
print(x)

a=uuid.uuid4()
print((a.hex))

print(a.urn)   #URN representation
