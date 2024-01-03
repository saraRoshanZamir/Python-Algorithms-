def find_index(member,num):
    index = member.index(num)
    i=index//8
    j=index-(i*8)
    return(i,j)
