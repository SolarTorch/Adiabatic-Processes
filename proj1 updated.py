from __future__ import division

from visual import *
from visual.graph import *

import math

scene = display(center = (0,0,0), background = color.white)

ep = 0.1
w0 = 5.0

x = sphere(pos = vector(10e-10,0,0), radius = 2e-11, color = color.orange)
spring = helix(pos=vector(0,0,0), axis = x.pos, radius = 1e-11)
vel = vector(0,0,0)

def omg(t):
    #return 5
    #return 1/(t+1) + 2
    #return ep*t + w0
    #return 1/(t+2)
    return math.sin(t) + 2
    #return math.sin(math.pi*50*t)
    #return math.exp(t)
    #return 1/math.log(t+2)
    #return 1/(math.log(t+2)*(t+2))

def foo(w):
    return w**2
    
def acc(x,w):
    #return -w**2*mag(x)*norm(x)
    return -w**2*x


g1 = gdisplay(title = 'pos vs. time',
                    xtitle = 't',
                    ytitle = 'x',
                    foreground=color.black,
                    background= color.white)

g2 = gdisplay(title = 'vel vs. time',
                    xtitle = 't',
                    ytitle = 'v',
                    foreground=color.black,
                    background= color.white)

g3 = gdisplay(title = 'acc vs. time',
                    xtitle = 't',
                    ytitle = 'a',
                    foreground=color.black,
                    background= color.white)

g4 = gdisplay(title = 'w^2(t) vs. time',
                    xtitle = 't',
                    ytitle = 'w^2(t)',
                    foreground=color.black,
                    background= color.white)


g5 = gdisplay(title = 'eng vs. time',
                    xtitle = 't',
                    ytitle = 'E*10^17',
                    foreground=color.black,
                    background= color.white)


pos_gp = gcurve(gdisplay = g1, color = color.red)
vel_gp = gcurve(gdisplay = g2, color = color.blue)
acc_gp = gcurve(gdisplay = g3, color = color.black)
#foo_gp_1 = gcurve(gdiaplay = g4, color = color.cyan)
foo_gp_2 = gcurve(gdiaplay = g4, color = color.green)
eng_gp = gcurve(gdiaplay = g5, color = color.orange)
#rel_gp = gcurve(gdiaplay = g5, color = color.orange)

t = 0
dt = 10e-5
count = 0

f = open('sqrtdata.txt','w')

while(1):
    rate(100000000)
    w = omg(t)
    #b = foo(t)
    c = foo(w)
    x.pos += vel*dt/2
    vel += acc(x.pos,c)*dt
    x.pos += vel*dt/2
    spring.axis = x.pos

    E = (vel.x)**2/2 + c**2*(x.pos.x)**2/2
    
    pos_gp.plot(pos=(t, x.pos.x))
    vel_gp.plot(pos=(t, vel.x))
    acc_gp.plot(pos=(t, acc(x.pos,c).x))
    #foo_gp_1.plot(pos=(t, b))
    foo_gp_2.plot(pos=(t, c))
    eng_gp.plot(pos=(t, 10e17*E))
    #if(int(c)!=0 and int(E)!=0):
        #rel_gp.plot(pos=(t, E/c))
    

    count += 1

    if(count == 1000):
        f.write('{0:>.3f},  {1:>.3f},  {2:>.3f}\n'.format(E, c, t))
        count = 0


    t += dt


    if (t > 200):
        f.close()

