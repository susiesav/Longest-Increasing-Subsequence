

a = [0,1,7,3,2,4,9]
a = [18, 2,8,4,10,2,3,4,10]
a = [0, 1,2,3,1,2,3,4,5]
a = [0,1,7,3,2,4,9]


#dont forget to make it delete duplicate
def red_one (a2,l,length):
    print("called")
    a2 = list(a2)
    is_looping = True
    if sorted(a2) == a2:
                length.append(len(a2))
                print ("list1 is sorted, length", length)

    else:
        for x in range(l):
            print(a2,l)
            for i in range(l):
                a3 = list(a2)
                a3.pop(i)
                print("SUBlist", a3)
                if sorted(a3) == a3:
                     length.append(len(a3))
                     is_looping = False
                     break
                      
                l = len(a3)

                if is_looping:
                    red_one(a3,l,length)

            if not is_looping:
                break

    return length

            

#driver
a = [0,1,7,3,2,4,9]
a2 = list(a)
l = len(a2)
length = []
length = red_one(a2,l,length)
maxlength = max(length)
print("max length is", maxlength)


