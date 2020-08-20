def isNStraightHand(hand, W):
    hand.sort()
    check = 0
    while hand:
        for i in range(W):
            if hand[0]+i not in hand:
                return False
        temp = hand[0]
        for i in range(W):
            hand.remove(temp+i)
            
    return True
    

l = list(map(int,input().strip().split(',')))
n = int(input())
print(isNStraightHand(l,n))