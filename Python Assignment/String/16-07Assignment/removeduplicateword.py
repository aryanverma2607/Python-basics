'''
7. Remove Duplicate Words from a String

Voice Assistant Noise Correction Systemn

A voice assistant records spoken commands from users.

Due to microphone disturbance and network lag, some words are repeated multiple times.

The company wants a Python program that removes duplicate words while maintaining the original order.

``
hello hello how are are you
```

Output:

```
hello how are you
```
'''	
string=input("Input :").split()
new=""
visited=""
for i in range(len(string)):
    ch=string[i]
    if ch not in visited:
        if i+1<len(string):
            for j in range(len(string)):
                if ch==string[j]:
                    continue
                else:
                    new=new+string[i]+" "
                visited=visited+string[i]
                break
print(new)	


























