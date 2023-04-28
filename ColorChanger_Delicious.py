# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 17:34:08 2023

@author: monji
"""
#import
import tkinter


#tkクラス作成
tki = tkinter.Tk()
#画面サイズ
tki.geometry("800x500")
#画面タイトル
tki.title("ColorChanger")

def com(a, b, c):
    Com = [int(255 - a), int(255 - b), int(255 - c)]
    return Com
    

def reset_click():
    txt_main.delete(0, tkinter.END)
    txt_R.delete(0,tkinter.END)
    txt_G.delete(0,tkinter.END)
    txt_B.delete(0,tkinter.END)
    txt_ana1.delete(0,tkinter.END)
    txt_ana2.delete(0,tkinter.END)
    txt_ana3.delete(0,tkinter.END)
    txt_ana4.delete(0,tkinter.END)
    txt_bri.delete(0,tkinter.END)
    txt_rev.delete(0,tkinter.END)
    txt_In.delete(0,tkinter.END)
    
    lbl_main["bg"] = "#cecfff"
    lbl_ana1["bg"] = "#cecfff"
    lbl_ana2["bg"] = "#cecfff"
    lbl_ana3["bg"] = "#cecfff"
    lbl_ana4["bg"] = "#cecfff"
    lbl_rev["bg"] = "#cecfff"
    lbl_In["bg"] = "#cecfff"
    
    lbl_main["fg"] = "#000000"
    lbl_ana1["fg"] = "#000000"
    lbl_ana2["fg"] = "#000000"
    lbl_ana3["fg"] = "#000000"
    lbl_ana4["fg"] = "#000000"
    lbl_rev["fg"] = "#000000"
    lbl_In["fg"] = "#000000"
        
def btn_click():
    txt_ana1.delete(0,tkinter.END)
    txt_ana2.delete(0,tkinter.END)
    txt_ana3.delete(0,tkinter.END)
    txt_ana4.delete(0,tkinter.END)
    txt_bri.delete(0,tkinter.END)
    txt_rev.delete(0,tkinter.END)
    txt_In.delete(0,tkinter.END)
    txt_main.delete(0,tkinter.END)
    #R_input = int(txt_R.get(), base=16)
    #G_input = int(txt_G.get(), base=16)
    #B_input = int(txt_B.get(), base=16)
    
    R_input = str(txt_R.get())
    G_input = str(txt_G.get())
    B_input = str(txt_B.get())
    
    R_input = int(R_input, base=16)
    G_input = int(G_input, base=16)
    B_input = int(B_input, base=16)

    RGB_Max = max(R_input, G_input, B_input)
    RGB_Min = min(R_input, G_input, B_input)

    """
    類似色
    """
    #以下RGB -> HSV変換
    #色相
    if max(R_input, G_input, B_input) == R_input:
        H = 60 * ((G_input - B_input) / (RGB_Max - RGB_Min))
    elif  max(R_input, G_input, B_input) == G_input:
        H = (60 * ((B_input - R_input) / (RGB_Max - RGB_Min))) + 120
    else:
        H = (60 * ((R_input - G_input) / (RGB_Max - RGB_Min))) + 240
        
    print(H)
        
    #彩度
    S = (RGB_Max -RGB_Min) / RGB_Max * 100

    #明度
    V = RGB_Max / 255 * 100

    #以下類似色算出
    ana_HSV = [H - 40, H - 20, H + 20, H + 40]
    for i in range(4):
        if ana_HSV[i] < 0:
            ana_HSV[i] += 360
        if ana_HSV[i] > 360:
            ana_HSV[i] -= 360

        print("ana_HSV[i]:", ana_HSV[i])

    hsv_max = V * 255 / 100
    hsv_min = hsv_max - ((S / 255) * hsv_max)

    ana_rgb = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(4):
        if ana_HSV[i] >= 0 and ana_HSV[i] < 60:
            ana_rgb[i][0] = int(hsv_max)
            ana_rgb[i][1] = int((ana_HSV[i] / 60) * (hsv_max - hsv_min) + hsv_min)
            ana_rgb[i][2] = int(hsv_min)
        
        elif ana_HSV[i] >= 60 and ana_HSV[i] < 120:
            ana_rgb[i][0] = int(((120 - ana_HSV[i]) / 60) * (hsv_max - hsv_min) + hsv_min)
            ana_rgb[i][1] = int(hsv_max)
            ana_rgb[i][2] = int(hsv_min)
        
        elif ana_HSV[i] >= 120 and ana_HSV[i] < 180:
            ana_rgb[i][0] = int(hsv_min)
            ana_rgb[i][1] = int(hsv_max)
            ana_rgb[i][2] = int(((ana_HSV[i] - 120) / 60) * (hsv_max - hsv_min) + hsv_min)
        
        elif ana_HSV[i] >= 180 and ana_HSV[i] < 240:
            ana_rgb[i][0] = int(hsv_min)
            ana_rgb[i][1] = int(((240 - ana_HSV[i]) / 60) * (hsv_max - hsv_min) + hsv_min)
            ana_rgb[i][2] = int(hsv_max)
            
        elif ana_HSV[i] >= 240 and ana_HSV[i] < 300:
            ana_rgb[i][0] = int(((ana_HSV[i] - 240) / 60) * (hsv_max - hsv_min) + hsv_min)
            ana_rgb[i][1] = int(hsv_min)
            ana_rgb[i][2] = int(hsv_max)
            
        elif ana_HSV[i] >= 300 and ana_HSV[i] < 360:
            ana_rgb[i][0] = int(hsv_max)
            ana_rgb[i][1] = int(hsv_min)
            ana_rgb[i][2] = int(((360 - ana_HSV[i]) / 60) * (hsv_max - hsv_min) + hsv_min)

    """
    輝度
    """
    brightness = int(RGB_Max * 100 / 255)

    """
    反転色
    """
    RGB_reverse = [int(255 - R_input), int(255 - G_input), int(255 - B_input)]

    """
    補色
    """
    RGB_com = [int((RGB_Max + RGB_Min) - R_input), int((RGB_Max + RGB_Min) - G_input), int((RGB_Max + RGB_Min) - B_input)]
    
    """
    テキストボックスにぶち込む
    """
    num_main = str(f'{R_input:02x}')+str(f'{G_input:02x}')+str(f'{B_input:02x}')
    
    num_ana1 = str(f'{ana_rgb[0][0]:02x}')+str(f'{ana_rgb[0][1]:02x}')+str(f'{ana_rgb[0][2]:02x}')
    num_ana2 = str(f'{ana_rgb[1][0]:02x}')+str(f'{ana_rgb[1][1]:02x}')+str(f'{ana_rgb[1][2]:02x}')
    num_ana3 = str(f'{ana_rgb[2][0]:02x}')+str(f'{ana_rgb[2][1]:02x}')+str(f'{ana_rgb[2][2]:02x}')
    num_ana4 = str(f'{ana_rgb[3][0]:02x}')+str(f'{ana_rgb[3][1]:02x}')+str(f'{ana_rgb[3][2]:02x}')
    
    num_rev = str(f'{RGB_reverse[0]:02x}')+str(f'{RGB_reverse[1]:02x}')+str(f'{RGB_reverse[2]:02x}')
    
    num_In = str(f'{RGB_com[0]:02x}')+str(f'{RGB_com[1]:02x}')+str(f'{RGB_com[2]:02x}')
    
    Tom_main = str(f'{com(R_input, G_input, B_input)[0]:02x}')+str(f'{com(R_input, G_input, B_input)[1]:02x}')+str(f'{com(R_input, G_input, B_input)[2]:02x}')
    
    Tom_ana1 = str(f'{com(ana_rgb[0][0], ana_rgb[0][1], ana_rgb[0][2])[0]:02x}')+str(f'{com(ana_rgb[0][0], ana_rgb[0][1], ana_rgb[0][2])[1]:02x}')+str(f'{com(ana_rgb[0][0], ana_rgb[0][1], ana_rgb[0][2])[2]:02x}')
    Tom_ana2 = str(f'{com(ana_rgb[1][0], ana_rgb[1][1], ana_rgb[1][2])[0]:02x}')+str(f'{com(ana_rgb[1][0], ana_rgb[1][1], ana_rgb[1][2])[1]:02x}')+str(f'{com(ana_rgb[1][0], ana_rgb[1][1], ana_rgb[1][2])[2]:02x}')
    Tom_ana3 = str(f'{com(ana_rgb[2][0], ana_rgb[2][1], ana_rgb[2][2])[0]:02x}')+str(f'{com(ana_rgb[2][0], ana_rgb[2][1], ana_rgb[2][2])[1]:02x}')+str(f'{com(ana_rgb[2][0], ana_rgb[2][1], ana_rgb[2][2])[2]:02x}')
    Tom_ana4 = str(f'{com(ana_rgb[3][0], ana_rgb[3][1], ana_rgb[3][2])[0]:02x}')+str(f'{com(ana_rgb[3][0], ana_rgb[3][1], ana_rgb[3][2])[1]:02x}')+str(f'{com(ana_rgb[3][0], ana_rgb[3][1], ana_rgb[3][2])[2]:02x}')
    
    Tom_rev = str(f'{com(RGB_reverse[0], RGB_reverse[1], RGB_reverse[2])[0]:02x}')+str(f'{com(RGB_reverse[0], RGB_reverse[1], RGB_reverse[2])[1]:02x}')+str(f'{com(RGB_reverse[0], RGB_reverse[1], RGB_reverse[2])[2]:02x}')
    
    Tom_com = str(f'{com(RGB_com[0], RGB_com[1], RGB_com[2])[0]:02x}')+str(f'{com(RGB_com[0], RGB_com[1], RGB_com[2])[1]:02x}')+str(f'{com(RGB_com[0], RGB_com[1], RGB_com[2])[2]:02x}')
    
    txt_main.insert(0, str(num_main))
    
    txt_ana1.insert(0, str(num_ana1))
    txt_ana2.insert(0, str(num_ana2))
    txt_ana3.insert(0, str(num_ana3))
    txt_ana4.insert(0, str(num_ana4))
    txt_bri.insert(0, str(brightness))
    txt_rev.insert(0, str(num_rev))
    txt_In.insert(0, str(num_In))
    
    txt_R.delete(0,tkinter.END)
    txt_G.delete(0,tkinter.END)
    txt_B.delete(0,tkinter.END)
    
    lbl_main["bg"] = "#"+str(num_main)
    lbl_ana1["bg"] = "#"+str(num_ana1)
    lbl_ana2["bg"] = "#"+str(num_ana2)
    lbl_ana3["bg"] = "#"+str(num_ana3)
    lbl_ana4["bg"] = "#"+str(num_ana4)
    lbl_rev["bg"] = "#"+str(num_rev)
    lbl_In["bg"] = "#"+str(num_In)
    
    lbl_main["fg"] = "#"+str(Tom_main)
    lbl_ana1["fg"] = "#"+str(Tom_ana1)
    lbl_ana2["fg"] = "#"+str(Tom_ana2)
    lbl_ana3["fg"] = "#"+str(Tom_ana3)
    lbl_ana4["fg"] = "#"+str(Tom_ana4)
    lbl_rev["fg"] = "#"+str(Tom_rev)
    lbl_In["fg"] = "#"+str(Tom_com)
    
"""
ラベル
"""
#入力部
lbl = tkinter.Label(tki,text = "R", background="#cecfff")
lbl.place(x=70, y=45)
lbl = tkinter.Label(tki,text = "G", background="#cecfff")
lbl.place(x=70, y=75)
lbl = tkinter.Label(tki,text = "B", background="#cecfff")
lbl.place(x=70, y=105)

#境界
lbl = tkinter.Label(tki,text = "-入力--------------", font=("Myrica M", "20", "bold"))
lbl.place(x=70, y=10)
lbl = tkinter.Label(tki,text = "-実行結果----------", font=("Myrica M", "20", "bold"))
lbl.place(x=70, y=130)

#出力部
lbl_main =tkinter.Label(tki,text = "Main Color", background="#cecfff", font=("Myrica M", "10", "bold"))
lbl_main.place(x=70, y=170)
lbl_ana1 = tkinter.Label(tki,text = "類似色Ⅰ", background="#cecfff", font=("Myrica M", "10", "bold"))
lbl_ana1.place(x=70, y=230)
lbl_ana2 = tkinter.Label(tki,text = "類似色Ⅱ", background="#cecfff", font=("Myrica M", "10", "bold"))
lbl_ana2.place(x=235, y=230)
lbl_ana3 = tkinter.Label(tki,text = "類似色Ⅲ", background="#cecfff", font=("Myrica M", "10", "bold"))
lbl_ana3.place(x=400, y=230)
lbl_ana4 = tkinter.Label(tki,text = "類似色Ⅳ", background="#cecfff", font=("Myrica M", "10", "bold"))
lbl_ana4.place(x=565, y=230)

lbl_bri = tkinter.Label(tki,text = "輝度", bg="#cecfff", font=("Myrica M", "10", "bold"))
lbl_bri.place(x=70, y=290)
lbl_rev = tkinter.Label(tki,text = "反転色", bg="#cecfff", font=("Myrica M", "10", "bold"))
lbl_rev.place(x=235, y=290)
lbl_In = tkinter.Label(tki,text = "補色", bg="#cecfff", font=("Myrica M", "10", "bold"))
lbl_In.place(x=400, y=290)

"""
テキストボックス
"""
#入力部
txt_R = tkinter.Entry(width = 20)
txt_R.place(x=100, y=45)
txt_G = tkinter.Entry(width = 20)
txt_G.place(x=100, y=75)
txt_B = tkinter.Entry(width = 20)
txt_B.place(x=100, y=105)

#出力部
txt_main = tkinter.Entry(width = 20)
txt_main.place(x=70, y=200)
txt_ana1 = tkinter.Entry(width = 20)
txt_ana1.place(x=70, y=260)
txt_ana2 = tkinter.Entry(width = 20)
txt_ana2.place(x=235, y=260)
txt_ana3 = tkinter.Entry(width = 20)
txt_ana3.place(x=400, y=260)
txt_ana4 = tkinter.Entry(width = 20)
txt_ana4.place(x=565, y=260)

txt_bri = tkinter.Entry(width = 20)
txt_bri.place(x=70, y=320)
txt_rev = tkinter.Entry(width = 20)
txt_rev.place(x=235, y=320)
txt_In = tkinter.Entry(width = 20)
txt_In.place(x=400, y=320)

"""
ボタン
"""
btn = tkinter.Button(tki,text="出力", command=btn_click, bg="#fffd8f")
btn.place(x=250, y=70)

btn = tkinter.Button(tki,text="Reset", command=reset_click, bg="#7092be", font="10")
btn.place(x=70, y=360)

tki.mainloop()