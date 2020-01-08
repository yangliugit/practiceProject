# with open('E:\phone.txt','w') as f:
#     for i in range(50000):
#         phone = 18626330614 + i
#         f.write(str(phone)+'\n')
from random import randint
def phone():
    with open('E:\phone.txt','r') as f:
        phones = f.readlines()
    i = randint(0, 50000)
    return phones[i]

if __name__ == '__main__':
    print(phone())