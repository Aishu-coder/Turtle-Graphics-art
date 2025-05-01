from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.listen()


def move():
    tim.fd(30)


def bk():
    tim.backward(50)


def clear():
    tim.home()
    tim.clear()


def colockwise():
    tim.right(10)


def ccw():
    tim.left(10)


screen.onkey(key='W', fun=move)
screen.onkey(key='S', fun=bk)
screen.onkey(key='A', fun=colockwise)
screen.onkey(clear, 'C')
screen.onkey(ccw, 'D')
'''function 'move' is passed into another function and notice that the parenthesis are avoided ,because using parenthesis
will trigger the function and function gets called.this is known as higher order function.in this case it is recommended 
that to use keyword arguments. '''
screen.exitonclick()
