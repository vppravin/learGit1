arr=[2,7,11,15]
target=9
hash={}
for i in range (len(arr)):
    print("Loop number", i)
    temp=target-arr[i]
    print("temp :",temp)
    print("Hashing value",hash.get(temp))
    if temp in hash:
       print("Gone inside")
       print(hash.get(temp),i)
       break;
    else:
        print("Skipped the inside part, Adding element")
        hash[arr[i]]=i
        print(hash)
print(type(arr))
