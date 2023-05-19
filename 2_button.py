from tkinter import *

root = Tk()
root.title("Jeffkim GUI")

btn1 = Button(root, text="버튼1")
btn1.pack()

btn2 = Button(root, padx=5, pady= 10, text="버튼2") #글자수에 따라서 크기가 자율로 바뀜
btn2.pack()

btn3 = Button(root, padx=10, pady= 5, text="버튼3")
btn3.pack()

btn4 = Button(root, width=10 , height= 3, text="버튼4") # 글자수에 따라서 크기가 바뀌지 않음
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="버튼5") # fg(포그라운드) = 글자 색, bg(백그라운드)= 배경색
btn5.pack()

photo = PhotoImage(file="C:/Users/김준섭/Desktop/GUI_/image.png")
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("버튼이 클릭되었어요")

btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

root.mainloop()