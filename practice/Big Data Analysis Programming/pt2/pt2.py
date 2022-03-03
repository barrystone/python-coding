import turtle
t=turtle

t.showturtle()
t.speed(20)

# 36 square
t.color('purple')
t.up()
t.setpos(-150,0)
t.down()
for i in range(0,36):
    for j in range(4):
        t.forward(100) 
        t.left(90) 
    t.left(10)

## Stop warning sign
t.up()
t.setpos(150,200)
t.down()
t.color('red')
t.begin_fill()
for i in range(6):   
  t.forward(90)  
  t.left(300)
t.end_fill()

t.up()
t.setpos(155,190)
t.down()
t.color('white')
t.width(4)
for i in range(6):   
  t.forward(80)  
  t.left(300)

t.up()
t.setpos(200,95)
t.down()
t.color('white')
style = ('serif', 50, 'bold')
t.write('STOP', font=style, align='center')
t.hideturtle()



input("Press enter to exit.")