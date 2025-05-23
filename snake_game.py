from random import randint
from tkinter import *

class Snake:
    def __init__(self):
        self.body_size=BODY_SIZE
        self.coordinates=[]
        self.squares=[]
        for i in range(0,BODY_SIZE):
            self.coordinates.append([0,0])

        for x, y in self.coordinates:
            square=canvas.create_rectangle( x,y, x+SPACE_SIZE, y+SPACE_SIZE , fill=SNAKE_COLOR, tag="snake" )
            self.squares.append(square)

class Food:
    def __init__(self):
        x=randint(0,GAME_WITH//SPACE_SIZE-1)*SPACE_SIZE
        y=randint(0,GAME_HEIGHT//SPACE_SIZE-1)*SPACE_SIZE
        self.coordinates=[x,y]
        canvas.create_oval(x,y, x+SPACE_SIZE, y+SPACE_SIZE , fill=FOOD_COLOR, tag="food"  )

def next_turn(snake,food):
    global score, SNAKE_COLOR
    x,y=snake.coordinates[0]
    if direction=="up":
        y-=SPACE_SIZE
    elif direction=="down":
        y+=SPACE_SIZE
    elif direction=="left":
        x-=SPACE_SIZE
    elif direction=="right":
        x+=SPACE_SIZE

    if score >= 60:
        SNAKE_COLOR= "#ff1578"
    elif score>=50:
        SNAKE_COLOR = "#fa0000"
    elif score>=40:
        SNAKE_COLOR = "#ff7e00"
    elif score>=30:
        SNAKE_COLOR = "#FFFF00"
    elif score>=25:
        SNAKE_COLOR = "#00ff00"
    elif score>=20:
        SNAKE_COLOR = "#a3007b"
    elif score>= 15:
        SNAKE_COLOR = "#a300ff"
    elif score>= 10:
        SNAKE_COLOR = "#00ffff"
    elif score >= 5:
        SNAKE_COLOR= "#0063ff"
    else:
        SNAKE_COLOR= "green"

    snake.coordinates.insert(0,[x,y])
    square=canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOR)
    snake.squares.insert(0,square)
    if x==food.coordinates[0] and y==food.coordinates[1]:
        score+=1
        label.config(text=f"امتیاز:{score}",font=("B Elm",30))
        canvas.delete("food")
        food=Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    if check_game_over(snake):
        game_over()
    else:
        window.after(SLOWNESS,next_turn,snake,food)


def check_game_over(snake):
    x,y=snake.coordinates[0]
    if x<0 or x>GAME_WITH:
        return  True
    if y<0 or y>GAME_HEIGHT:
        return  True
    for sq in snake.coordinates[1:]:
        if x==sq[0] and y==sq[1]:
            return True
    return False
def game_over():
    canvas.delete()
    canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,font=("Terminal",60),text=" سرم اخ",fill="#DF1A2F",tag="gameover")

def change_direction(new_dir):
    global direction
    if new_dir == "left":
        if direction != "right":
            direction = new_dir
    if new_dir == "right":
        if direction != "left":
            direction = new_dir
    if new_dir == "up":
        if direction != "down":
            direction = new_dir
    if new_dir == "down":
        if direction != "up":
            direction = new_dir

def restart_program():
    global snake, food, score, direction
    canvas.delete("all")
    score = 0
    direction = "down"
    label.config(text=f"امتیاز:{score}", font=("B Elm", 30))

    snake = Snake()
    food = Food()
    next_turn(snake, food)

#------------------------------
GAME_WITH=700
GAME_HEIGHT=600
SPACE_SIZE=25
SLOWNESS=200
BODY_SIZE=2
SNAKE_COLOR="yellow"
FOOD_COLOR="red"
BACKGROUND_COLOR="black"
score=0
direction="down"
#------------------------------
window=Tk()
window.title("  مار کبری"+" امتیاز های:5و10و15و20و25و30و40و50و60رنگت عوض میشه")
window.resizable(False,False)
label=Label(window,text=f"امتیاز:{score}",font=("B Elm",30))
label.pack()
canvas=Canvas(window,bg=BACKGROUND_COLOR,height=GAME_HEIGHT,width=GAME_WITH)
canvas.pack()

restart=Button(window,text="شروع مجدد", font=("B Badr", 14), bg="white", fg="green", command=restart_program)
restart.pack(pady=10)


window.update()

window_width=window.winfo_width()
window_height=window.winfo_height()
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()
x=int((screen_width/2)-(window_width/2))
y=int((screen_height/2)-window_height/2)
window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.bind("<Left>",lambda event:change_direction("left"))
window.bind("<Right>",lambda event:change_direction("right"))
window.bind("<Up>",lambda event:change_direction("up"))
window.bind("<Down>",lambda event:change_direction("down"))

snake=Snake()
food=Food()
next_turn(snake,food)
window.mainloop()
