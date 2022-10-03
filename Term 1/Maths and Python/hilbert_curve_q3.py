def get_vertex_from_directions(v, dir):     # Calculate vertex from directions
    if dir == 'R':
        return ((v[0],v[1]+1))
    elif dir == 'L':
        return ((v[0],v[1]-1))
    elif dir == 'U':
        return ((v[0]-1,v[1]))
    elif dir == 'D':
        return ((v[0]+1,v[1]))
    
def left_rotate(unit):           # Rotate anticlockwise (from left side)
    unit.reverse()
    l=[]
    for i in range(0,len(unit)):
        if unit[i]=="R":
            l.append("D")
        elif unit[i]=="D":
            l.append("L")
        elif unit[i]=="L":
            l.append("U")
        elif unit[i]=="U":
            l.append("R")
    unit.reverse()
    return l
    

def right_rotate(unit):  #This is just 3 right rotations
    l = unit
    for i in range(3):
        l = left_rotate(l)
    return l
    
def get_pattern(left_pattern,right_pattern, unit):
    pattern=[]
    for i in range(len(left_pattern)):
        pattern.append(left_pattern[i])
    pattern.append("D")
    for i in range(len(unit)):
        pattern.append(unit[i])
    pattern.append("R")
    for i in range(len(unit)):
        pattern.append(unit[i])
    pattern.append("U")
    for i in range(len(right_pattern)):
        pattern.append(right_pattern[i])
    return pattern

def hilbert_curve():
    unit=['D','R','U']
    count=0
    for count in range(4):
        unit=get_pattern(left_rotate(unit),right_rotate(unit),unit)
        z = [(1,1)]
        for dir in unit:
            z.append(get_vertex_from_directions(z[-1],dir))
        print(z, end="\n\n")
    
hilbert_curve()
