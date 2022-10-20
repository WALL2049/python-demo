import turtle

t = turtle.Turtle()

def drawSpiral(t, lineLen):
    if lineLen > 0:
        t.forward(lineLen)
        t.right(90)
        drawSpiral(t, lineLen - 5)

if __name__ == '__main__':
    drawSpiral(t, 100)
    turtle.done()





