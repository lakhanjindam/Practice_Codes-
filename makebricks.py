def make_bricks(small, big, goal):

    rem = goal%5
    if (small+big*5)>=goal and rem<=small:
        return True
    else:
        return False

    
print(make_bricks(3,2,9))