import math

def fun1(x, y):
    return (x**2+y**2-1)**3-(x**2)*(y**3)

def fun2(x, y):
    return (x**2+(1.25*y-math.sqrt(abs(x)))**2-1.0)
              
def plot_heart(htype=0,inside=" ",outside="*",width=60,height=60):
    len_in=len(inside)
    len_out=len(outside)
    heart_str=""
    
    if htype==0:
        for y in range(int(height*1.3/2.4)+1, -int(height*1.1/2.4)-1, -1):
            in_tag=0
            out_tag=0
            for x in range(-int(width*1.3/2.2)-1, int(width*1.3/2.2)+1,1):
                if fun1(x*2.2/width,y*2.4/height) <=0:
                    heart_str=heart_str+(inside[in_tag])
                    in_tag=(in_tag+1)%len_in
                else:
                    heart_str=heart_str+(outside[out_tag])
                    out_tag=(out_tag+1)%len_out
            heart_str=heart_str+"\n"
    
    else:
        for y in range(int(height*1.3/2.4)+1, -int(height*1.1/2.4)-1, -1):
            in_tag=0
            out_tag=0
            for x in range(-int(width*1.2/2.4)-1, int(width*1.2/2.4)+1,1):
                if fun2(x*2.4/width,y*2.4/height) <=0:
                    heart_str=heart_str+(inside[in_tag])
                    in_tag=(in_tag+1)%len_in
                else:
                    heart_str=heart_str+(outside[out_tag])
                    out_tag=(out_tag+1)%len_out
            heart_str=heart_str+"\n"
    print(heart_str)

plot_heart(htype=0,inside="你",outside="我",width=120,height=60)