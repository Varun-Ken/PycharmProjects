import random
upper="QWERTYUIOPAASDFGHJKLZXCVBNM"
lower="qwertyuiopasdfghjklzxcvbnm"
num="1234567890"
symbol=",.!@#$%^&*()_+-="
all=upper+lower+symbol+num
length=14
password="".join(random.sample(all,length))
print("Generated Password=",password)