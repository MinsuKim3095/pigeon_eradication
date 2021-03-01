import pigpio
from time import sleep
n_pulsewidth = 600 #(position)
pulsewidth = 10 #(stride)
pi = pigpio.pi()
default = open('/home/minsu/coordinates.txt', 'w+')
data ="nothing"
default_write = default.write(data)
default.close()
while True:
        f = open('/home/minsu/coordinates.txt', 'r')
        c = f.read()
        f.close()
        print(c)
        
        try:
                c = int(c)
        except ValueError:
                c = "nothing"
                
        if c != "nothing":
                if c < -30 :
                        n_pulsewidth -= 10
                        pi.set_servo_pulsewidth(18,n_pulsewidth)
                        print('*' * 20)
                        print('(2-1)Decrease by 1 degree to the right')
                        print('(2-1)Angle : ',(n_pulsewidth - 600)/10, ' degree' )
                        print('(2-1)Featured c : ',c)
                        print('*' * 20)
                        print('this is c <-30')
                        sleep(.5)

                elif -30 <= c <= 30:
                        print('*' * 20)
                        print('(2-2)Target is on center')
                        print('(2-2)degree is : ',(n_pulsewidth-600)/10,' degree')
                        print('(2-2)Featured c : ', c)
                        print('*' * 20)
                        pi.set_servo_pulsewidth(12,2200)
                        print('this is -30 < c <30')
                        sleep(3)
                        
                elif 30 < c :
                        n_pulsewidth += 10
                        pi.set_servo_pulsewidth(18,n_pulsewidth)
                        print('*' * 20)
                        print('(2-3)Increases by 1 degree to the left')
                        print('(2-3)Angle : ',(n_pulsewidth - 600)/10, ' degree' )
                        print('(2-3)Featured c : ',c)
                        print('this is 30 < c')
                        print('*' * 20)
                        sleep(.5)
        
        else :  #if c == 'nothing' :
                pi.set_servo_pulsewidth(12,600)
                n_pulsewidth += pulsewidth
                if n_pulsewidth >= 2400 :
                        pulsewidth = -pulsewidth
                        n_pulsewidth = 2400
                        
                elif n_pulsewidth <= 600 :
                        pulsewidth = -pulsewidth
                        n_pulsewidth = 600
                        
                pi.set_servo_pulsewidth(18,n_pulsewidth)
                print('*' * 20)
                print('(1-1) Rotation')
                print('(1-1) Angle :',(n_pulsewidth - 600)/10, ' degree')
                print('this is nothing detected')
                print('*' * 20)
                sleep(.1)
