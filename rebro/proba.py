a,b=50,20
k = 1.25
amin = float(a) / k
amax = float(a) * k
bmin = float(b) / k
bmax = float(b) * k
print(amin > float(50) > amax or bmin > float(20) > bmax)
