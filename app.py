app=[1,9,5,0,20,-4,12,16,7]
objetivo=12
for x in app:
    for y in range(1,len(app)):
        z=objetivo-app[y]-x
        if z!=0:
            continue
        print(x,app[y])