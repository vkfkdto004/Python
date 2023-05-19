from tkinter import *

root = Tk()
root.title("Jeffkim GUI")
root.geometry("640x480+300+100")

txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END, "글자를 입력하세요")

e = Entry(root, width=30)
e.pack()
e.insert(0, "한 줄만 입력하세요")

def btncmd():
    #내용 출력
    print(txt.get("1.0", END)) 
    print(e.get())
    # END = 처음부터 끝까지 모든 텍스트 내용을 가져오는것
    # 1 = 첫번째 라인 // 0 = 0번째 column 위치

    #내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)
   
btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()