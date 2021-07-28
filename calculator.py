from tkinter import *
from tkinter import font 
import math
from tkinter.font import BOLD, Font

'''FUNCTIONS'''
#function to take input in the entry box
def click_button(num):
    global cal_operator 
    cal_operator += str(num) #str converts into string
    text_input.set(cal_operator) #to set the calculated value
   
#function to clear everything
def clear_button():
    global cal_operator
    cal_operator = ''
    text_input.set('')
    text_input2.set('')

#to delete one button
def button_delete():
    global cal_operator
    text = cal_operator[:-1]
    cal_operator = text
    text_input.set(text)

#to evaluate
def button_equal():
    try :
        global cal_operator

        temp = str(eval(cal_operator))
        text_input2.set(temp)
        cal_operator = temp
    except:
        text_input2.set("error")
        cal_operator = ""


   
#MAIN BODY
   
root  = Tk()
root.configure(bg = "black" , bd = 10) #the main body format
root.title("Calculator")

# by using stringvar we can change the texts
text_input = StringVar()
text_input2 = StringVar()
cal_operator = ""

#abbreviations of some operations
e = math.exp
sin  = math.sin
cos = math.cos
asin = math.asin
acos = math.acos
log = math.log10
π = math.pi

#the box which takes input
input = Entry(root , font=('arial', 14), width= 28, fg = "white" ,  bg="black" , bd = 5 , justify=RIGHT , textvariable = text_input , relief = GROOVE)
input.grid(row=1, column=0 , columnspan=5 )

#the box which shows output
res = Entry(root ,font=('arial', 14), width= 28, fg = "white" , bd = 5 ,  bg="black" , justify=RIGHT , textvariable = text_input2 , relief = GROOVE)
res.grid(row=2, column=0 , columnspan=5 )

#the whole calculator will show result in decimal system
lab = Label(root , text = 'DECIMAL' , font = ('arial' , 6 , BOLD))
lab.grid(row = 0)

#to set the font of my texts 
myfont = font.Font(family='Helvetica' , size= 8,  weight=BOLD)

button_parameter = {'bd':5, 'fg':'#000', 'bg':'#BBB', 'font':('sans-serif', 20, 'bold')}

#Set the buttons:

button_1 = Button(root , button_parameter  , text=' 1 ', width = 7, height = 2, fg = 'black', bg='dark grey' , font = myfont , relief = RAISED, command = lambda:click_button('1'))
button_1.grid(row = 6, column = 0 , padx = 1 , pady = 1)

button_2 = Button(root , button_parameter , text=' 2 ', width = 7, height = 2, fg = 'black', bg='dark grey' , font = myfont , relief = RAISED, command = lambda:click_button('2'))
button_2.grid(row = 6, column = 1 , padx = 1 , pady = 1)

button_3 = Button(root , button_parameter , text=' 3 ', width = 7, height = 2, fg = 'black', bg='dark grey' , font = myfont , relief = RAISED, command = lambda:click_button('3') )
button_3.grid(row = 6, column = 2 , padx = 1 , pady = 1)

button_4 = Button(root , button_parameter , text=' 4 ', width = 7, height = 2, fg = 'black', bg='dark grey' , font = myfont , relief = RAISED, command = lambda:click_button('4'))
button_4.grid(row = 5 , column = 0 , padx = 1 , pady = 1)

button_5 = Button(root , button_parameter , text=' 5 ', width = 7, height = 2, fg = 'black', bg='dark grey' , font = myfont , relief = RAISED, command = lambda:click_button('5'))
button_5.grid(row = 5 , column = 1 , padx = 1 , pady = 1)

button_6 = Button(root , button_parameter , text=' 6 ', width = 7, height = 2, fg = 'black', bg='dark grey' , font = myfont , relief = RAISED, command = lambda:click_button('6'))
button_6.grid(row = 5 , column = 2 , padx = 1 , pady = 1)

button_7 = Button(root , button_parameter , text=' 7 ', width = 7, height = 2, fg = 'black', bg='dark grey' , font = myfont , relief = RAISED, command = lambda:click_button('7'))
button_7.grid(row = 4 , column = 0 , padx = 1 , pady = 1)

button_8 = Button(root , button_parameter , text=' 8 ', width = 7, height = 2, fg = 'black', bg='dark grey' , font = myfont , relief = RAISED, command = lambda:click_button('8'))
button_8.grid(row = 4 , column = 1 , padx = 1 , pady = 1)

button_9 = Button(root , button_parameter , text=' 9 ', width = 7, height = 2, fg = 'black', bg='dark grey' , font = myfont , relief = RAISED, command = lambda:click_button('9'))
button_9.grid(row = 4 , column = 2  , padx = 1 , pady = 1)

button_0 = Button(root , button_parameter , text=' 0 ', width = 7, height = 2, fg = 'black', bg='dark grey' , font = myfont , relief = RAISED, command = lambda:click_button('0'))
button_0.grid(row = 7, column = 1 , padx = 1 , pady = 1)

addition = Button(root , button_parameter , text=' + ', width = 7, height = 2, fg = 'white',bg = 'green' , font = myfont , relief = RAISED, command = lambda:click_button('+'))
addition.grid(row = 6,  column = 3 , padx = 1 , pady = 1)

substraction = Button(root , button_parameter , text=' - ' , width = 7, height = 2, fg = 'white',bg = 'green' , font = myfont , relief = RAISED, command = lambda:click_button('-'))
substraction.grid(row = 5 , column = 3 , padx = 1 , pady = 1)

multiply= Button(root , button_parameter , text=' x ', width = 7, height = 2, fg = 'white',bg = 'green' , font = myfont , relief = RAISED, command = lambda:click_button('*'))
multiply.grid(row = 4 , column = 3 , padx = 1 , pady = 1 )

division = Button(root , button_parameter , text=' / ', width = 7, height = 2, fg = 'white',bg = 'green' , font = myfont , relief = RAISED, command = lambda:click_button('/'))
division.grid(row = 3 , column = 3 , padx = 1 , pady = 1)

sin_theta = Button(root , button_parameter , text=' sin ', width = 7, height = 2, fg = 'white',bg = 'green' , font = myfont , relief = RAISED, command = lambda:click_button('sin('))
sin_theta.grid(row = 3 , column= 1 , padx = 1 , pady = 1)

cos_theta = Button(root , button_parameter , text=' cos ', width = 7, height = 2, fg = 'white',bg = 'green' , font = myfont , relief = RAISED, command = lambda:click_button('cos('))
cos_theta.grid(row = 3 , column= 2 , padx = 1 , pady = 1)

decimal = Button(root , button_parameter , text=' . ', width = 7, height = 2, fg='white', bg = 'green' , font = myfont , relief = RAISED, command = lambda:click_button('.'))
decimal.grid(row = 8, column = 2 , padx = 1 , pady = 1)

exponent= Button(root , button_parameter , text=' e^x ', width = 7, height = 2, fg = 'white',bg = 'green' , font = myfont , relief = RAISED, command = lambda:click_button('e('))
exponent.grid(row = 7, column = 3 , padx = 1 , pady = 1)

bracket_1 = Button(root , button_parameter , text=' ( ', width = 7, height = 2, fg = 'white',bg = 'green' , font = myfont , relief = RAISED, command = lambda:click_button('('))
bracket_1.grid(row = 8, column = 0 , padx = 1 , pady = 1)

bracket_2 = Button(root , button_parameter , text=' ) ', width = 7, height = 2, fg = 'white',bg = 'green' , font = myfont , relief = RAISED, command = lambda:click_button(')'))
bracket_2.grid(row = 8, column = 1 , padx = 1 , pady = 1)

power = Button(root , button_parameter, text=' x^y ', width = 7, height = 2, fg = 'white',bg = 'green' , font = myfont , relief = RAISED, command = lambda:click_button('**'))
power.grid(row = 3 , column = 0 , padx = 1 , pady = 1)

log_10= Button(root , button_parameter , text=' log ', width = 7, height = 2, fg = 'white',bg = 'green' , font = myfont , relief = RAISED, command = lambda:click_button('log('))
log_10.grid(row = 6, column = 4 , padx = 1 , pady = 1)

sin_inverse= Button(root , button_parameter , text=' sinh ', width = 7, height = 2, fg = 'white',bg = 'green' , font = myfont , relief = RAISED, command = lambda:click_button('asin('))
sin_inverse.grid(row = 4 , column = 4 , padx = 1 , pady = 1)

cos_inverse= Button(root , button_parameter , text=' cosh ', width = 7, height = 2, fg = 'white',bg = 'green' , font = myfont , relief = RAISED, command = lambda:click_button('acos(') )
cos_inverse.grid(row = 5 , column = 4 , padx = 1 , pady = 1)

pi= Button(root , button_parameter , text=' π ', width = 7, height = 2, fg = 'white',bg = 'green' , font = myfont , relief = RAISED, command = lambda:click_button('π') )
pi.grid(row = 7, column = 4 , padx = 1 , pady = 1)

DEL= Button(root , button_parameter , text=' DEL ', width = 7, height = 2, fg='black', bg='grey' , font = myfont , relief = RAISED, command = button_delete)
DEL.grid(row = 7, column = 0 , padx = 1 , pady = 1)

mod= Button(root , button_parameter , text=' mod ', width = 7, height = 2, fg = 'white',bg = 'green' , font = myfont , relief = RAISED, command = lambda:click_button('%'))
mod.grid(row = 3, column = 4 , padx = 1 , pady = 1)


clear = Button(root , button_parameter , text=' C ', width = 7, height = 2 , fg='black', bg='grey' , font = myfont , relief = RAISED, command = clear_button)
clear.grid(row = 7, column = 2 , padx = 1 , pady = 1)

equal = Button(root , button_parameter , text=' = ', width = 16, height = 2, fg='black', bg='grey' , font = myfont , relief = RAISED, command = button_equal)
equal.grid(row = 8, column = 3, padx = 1 , pady = 1 , columnspan=2)


root.mainloop()