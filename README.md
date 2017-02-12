# HomeWork
from tkinter import*
root = Tk()    
def callback(event):
    try:
        a2 = int(textA.get('1.0', END))
        b2 = int(textB.get('1.0', END))
        c2 = int(textC.get('1.0', END))
        
        dscr = b2**2 - 4*a2*c2
        textDiscriminant.delete('1.0', END)
        textDiscriminant.insert(1.0, str(dscr))
        
        textPr.delete('1.0', END)
        textSum.delete('1.0', END)
        
        
        textX1.delete('1.0', END)
    
        textX2.delete('1.0', END)

        if dscr > 0:
            if b2 == c2 == 0:
                textX1.insert(1.0, 'x2 = 0')
                textX2.insert(1.0, str('-'))
            elif c2 == 0 and b2 != 0:
                textX1.insert(1.0, '0')
                textX2.insert(1.0, str( round((b2*(-1) / a2), 4) ) )
            elif b2 == 0 and c2 != 0:
                if ( (c2 * (-1)) / a2) < 0:
                    text1.insert(1.0, '-')
                    text2.insert(1.0, '-')
                else:
                    textX1.insert(1.0, str( round(((c2 * (-1)) / a2) ** 0.5, 4) ) )
                    textX2.insert(1.0, str( (-1) * ((c2 * (-1)) / a2) ** 0.5 ) )
            else:
                textX1.insert(1.0, str( round( ((b2*(-1)) + dscr ** 0.5) / (2*a2), 4) ) )
                textX2.insert(1.0, str( round( ((b2*(-1)) - dscr ** 0.5) / (2*a2), 4)  ) )
        elif dscr == 0:
            if (b2 / (2 * a2)) == 0:
                textX1.insert(1.0, 'x2 = 0.0')
            else:
                textX1.insert(1.0, 'x2 = ' + str( (-1) * (b2 / (2 * a2)) ) )
            textX2.insert(1.0, '-')
        else:
            textX1.insert(1.0, '-')
            textX2.insert(1.0, '-')
            
    except ZeroDivisionError:
        print('Деление на ноль(может быть, a = 0?)!')
    except Exception:
        print('Неправильный ввод!')

def cb(event):

    
    a2 = int(textA.get('1.0', END))
    b2 = int(textB.get('1.0', END))
    c2 = int(textC.get('1.0', END))
    dscr = b2**2 - 4*a2*c2







dscr = 0

root.geometry('250x320')

buttonReshit=Button(root,text='решить',width=6,height=1,bg='lightblue',fg='black',font='arial 14')


x1 = Label(root, text = 'x1 = ')
x2 = Label(root, text = 'x2 = ')
prLabel = Label(root, text = 'x1 * x2 = ')
sumLabel = Label(root, text = 'x1 + x2 = ')
discriminantLabel = Label(root, text = 'D = ')

abc = Label(root, text = 'ax^2 + bx + c = 0')
a = Label(root, text = 'A = ')
b = Label(root, text = 'B = ')
c = Label(root, text = 'C = ')

p = Label(root, text = '')
u = Label(root, text = '')





textA = Text(root, height=1, width=20, font='Arial 10')
textB = Text(root, height=1, width=20, font='Arial 10')
textC = Text(root, height=1, width=20, font='Arial 10')
textDiscriminant = Text(root, height=1, width=20, font='Arial 10')
textX1 = Text(root, height = 1, width = 20, font = 'Arial 10')
textX2 = Text(root, height = 1, width = 20, font = 'Arial 10')
textPr = Text(root, height = 1, width = 20, font = 'Arial 10')
textSum = Text(root, height = 1, width = 20, font = 'Arial 10')


textA.insert(1.0,'0')
textB.insert(1.0,'0')
textC.insert(1.0,'0')
textDiscriminant.insert(1.0,'')
textX1.insert(1.0,'')
textX2.insert(1.0,'')
textPr.insert(1.0,'')
textSum.insert(1.0,'')





abc.grid(row = 1, column = 1)
a.grid(row = 2, column = 1)
b.grid(row = 3, column = 1)
c.grid(row = 4, column = 1)
p.grid(row = 5, column = 1)
u.grid(row = 6, column = 1)


textA.grid(row = 2, column = 2)
textB.grid(row = 3, column = 2)
textC.grid(row = 4, column = 2)
textDiscriminant.grid(row = 8, column = 2)
textX1.grid(row = 9, column = 2)
textX2.grid(row = 10, column = 2)


x1.grid(row = 9, column = 1)
x2.grid(row = 10, column = 1)

discriminantLabel.grid(row = 8, column = 1)

buttonReshit.grid(row = 7, column = 1)


buttonReshit.bind("<Button-1>", callback)


root.mainloop()
