from tkinter import *

root = Tk()
root.title("Jeffkim GUI")
root.geometry("640x480+300+100")

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="C:/Users/김준섭/Desktop/GUI_/image.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또 만나요")

    #  Garbage Collection : 불필요한 메모리 공간 해제 라는 기능때문에 전역 변수로 만들어야 이미지 변환 가능
    global photo2
    photo2 = PhotoImage(file="C:/Users/김준섭/Desktop/GUI_/image2.png")
    label2.config(image=photo2)

btn = Button(root, text="클릭", command=change)
btn.pack()

root.mainloop()