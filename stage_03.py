with open('artifacts_01.txt','r') as f:
    text = f.read()
    print(text)

with open('artifacts_02.txt', 'w+') as f:
    f.write("Hello World")

print("End of stage 03")