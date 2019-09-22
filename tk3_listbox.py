# 创建一个listbox，还有一个label，当鼠标选中listbox内的选项后，
# 点击按钮label能够显示出来列表内选中的内容
import tkinter as tk
#创建一个窗口定义名称和尺寸
window = tk.Tk()
# window.title('practice listbox')
# window.geometry('500x300')

# #创建输入框show就是输入时显示的字符
# # e = tk.Entry(window, show="*")
# # e = tk.Entry(window, show=None)


# # 创建一个label标签显示
# var1 = tk.StringVar()
# l = tk.label(window,bg='green',font=('arial',12),width=10,
#     textvariable=var1)
# l.pack()
# #创建按钮

# b1 = tk.Button(window, text='show', width=15,
#               height=2, command=show)
# b1.pack()


# #创建listbox
# var2 = tk.StringVar()#创建tk型变量
# var2.set((1,2,3,4,5))
# t = tk.listbox(window, listvariable=var2)
# t.pack()

#窗口循环
window.mainloop()
