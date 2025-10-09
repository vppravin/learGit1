input1= "listen"
input2= "silent"
print("This Code will check wheather both the input string is anagram or not")
hashOne,hashTwo={},{}

if(len(input1) != len(input2)):
  print("Oops not an anagram")

else:

  for i in range(len(input1)):
     hashOne[input1[i]]=hashOne.get(input1[i],0)+1
     hashTwo[input2[i]]=hashTwo.get(input2[i],0)+1

for j in hashOne:
   if(hashOne[j]!= hashTwo.get(j,0)):
     print(hashone[j])
     print(hashTwo.get[j,0])
     print("Oops not a anagram")

print("Hurray its an anagram")
