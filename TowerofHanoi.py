


def TowerOfHanoi(n,start, end, other):
    if n <= 1:
        print("Disk 1 from ",start,"to ",end)
        return
    TowerOfHanoi(n-1, start, other, end)
    print("Disk",n,"from ",start,"to ",end)
    TowerOfHanoi(n-1,other,end,start)

n = 3
TowerOfHanoi(n, 'A', 'B', 'C')
