def Tower(n, f,t,h):
    if n == 0:
        return
    Tower(n-1,f,h,t)
    print('Move disk',n,'from ',f,'to',t)
    Tower(n-1,h,t,f)

n = 3
Tower(n,'A','C','B')
    