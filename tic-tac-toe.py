from tkinter import *
import tkinter.messagebox

def checked(i) :
      global player
      button = list[i]

      if button["text"] != "     " :
            return
      button["text"] = player 
      button["bg"] = "yellow"

      if player == "X" :
            player = "O"
            button["bg"] = "yellow"
      else :
            player = "X"
            button["bg"] = "lightgreen"
            ifWin()
    
def ifWin():
      if(list[0]["text"==list[1]["text"]==list[2]["text"] != "     "):
                 win_ms()
      if(list[3]["text"==list[4]["text"]==list[5]["text"] != "     "):
                 win_ms()
      if(list[6]["text"==list[7]["text"]==list[8]["text"] != "     "):
                 win_ms()
      if(list[0]["text"==list[3]["text"]==list[6]["text"] != "     "):
                 win_ms()
      if(list[1]["text"==list[4]["text"]==list[7]["text"] != "     "):
                 win_ms()
      if(list[2]["text"==list[5]["text"]==list[8]["text"] != "     "):
                 win_ms()
      if(list[0]["text"==list[4]["text"]==list[8]["text"] != "     "):
                 win_ms()
      if(list[2]["text"==list[4]["text"]==list[6]["text"] != "     "):
                 win_ms()                 
def win_ms():
      if player == "X":
                 tkinter.messagebox.showinfo("Winner","player O")
                 quit()
                 tkinter.messagebox.showinfo("Winner","player X")
                 quit()
   
window = Tk()
player = "X"
list= []

for i in range(9) :
      b = Button(window, text="     ", command=lambda k=i: checked(k))
      b.grid(row=i//3, column=i%3)
      list.append(b)

window.mainloop()


