import turtle
import Recttest
import line

#sort key function
def sortF(e):
    return e.y

#draws rectangle object
def draw(rectangle, t):
    t.up()
    t.setx(rectangle.x)
    t.sety(rectangle.y)
    t.setheading(0)
    t.down()
    t.fd(rectangle.w)
    t.rt(90)
    t.fd(rectangle.h)
    t.rt(90)
    t.fd(rectangle.w)
    t.rt(90)
    t.fd(rectangle.h)


##CREATE SCREEEN AND TURTLE##
s = turtle.getscreen()
t = turtle.Turtle()

#Object intiation
object = Recttest.Rectangle(-100,100,50,50)
object_2 = Recttest.Rectangle(25,75,50,50)
object_3 = Recttest.Rectangle(300,300,25,25)

#Line object, to be phased out
l_1 = line.Line(-100,100,50)
l_2 = line.Line(25,75,50)
l_3 = line.Line(300,300,25)

#Draw initial rectangles
draw(object, t)
draw(object_2, t)
draw(object_3, t)
t.pencolor("red")

#list objects
line_list = [l_1,l_2,l_3]
object_list = [object, object_2, object_3]

#sort objects by y axis, objects higher above will appear first
object_list.sort(reverse=True, key=sortF)
line_list.sort(reverse=True, key=sortF)

#Decide if new rectangle needed
check = line_list[0].compare(line_list[1])
if check is True:
    print('mistake')
else:
    draw(object_3, t)

check = line_list[1].compare(line_list[2])
if check is True:
    new_h = abs(object_list[1].y - object_list[2].y)
    new_object = Recttest.Rectangle(object_list[1].x, object_list[1].y, new_h, object_list[1].w)
    draw(new_object, t)

    #know that we are at the end
    next_object = Recttest.Rectangle(object_list[1].x, object_list[1].y-new_h, object_list[1].h-new_h, abs(abs(object_list[1].x) + (object_list[2].x + object_list[2].w)))
    #print(next_object.x, next_object.y, next_object.h, next_object.w)
    draw(next_object, t)

    #last
    last_object = Recttest.Rectangle(object_list[2].x, object_list[2].y - next_object.h, object_list[2].h-next_object.h, object_list[2].w)
    draw(last_object, t)

turtle.done()