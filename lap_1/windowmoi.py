from tkinter import *
import time
import datetime
from opcua import Client, ua
import threading
from tkinter.ttk import *
from time import sleep
import tkinter  #khai bao thu vien tkinter
import Image    #khai bao thu vien xu ly anh
import cv2 as cv
import numpy as np
import random as rng
import PIL.Image, PIL.ImageTk   #khai bao thu vien PIL
import math     #khai bao thu vien toan hoc
import serial   #khai bao thu bien COM

from threading import Thread
import serial.tools.list_ports #khai bao thu vien cong COM


def write_value_int(value):
    client_node = client.get_node('ns=4;i=19')  # get node
    client_node_value = value
    client_node_dv = ua.DataValue(ua.Variant(client_node_value, ua.VariantType.Float))
    client_node.set_value(client_node_dv)
    print("Value of : " + str(client_node) + ' : ' + str(datetime.datetime.now()))

def write_value_int_1(value):
    client_node = client.get_node('ns=4;i=22')  # get node
    client_node_value = value
    client_node_dv = ua.DataValue(ua.Variant(client_node_value, ua.VariantType.Float))
    client_node.set_value(client_node_dv)
    print("Value of : " + str(client_node) + ' : ' + str(datetime.datetime.now()))

def write_value_int_2(value):
    client_node = client.get_node('ns=4;i=21')  # get node
    client_node_value = value
    client_node_dv = ua.DataValue(ua.Variant(client_node_value, ua.VariantType.Float))
    client_node.set_value(client_node_dv)
    print("Value of : " + str(client_node) + ' : ' + str(datetime.datetime.now()))

def write_value_int_3(value):
    client_node = client.get_node('ns=4;i=20')  # get node
    client_node_value = value
    client_node_dv = ua.DataValue(ua.Variant(client_node_value, ua.VariantType.Float))
    client_node.set_value(client_node_dv)
    print("Value of : " + str(client_node) + ' : ' + str(datetime.datetime.now()))


def write_value_int_node1(aa):
    write_value_int('ns=4;i=4', aa)

def write_value_int_node2(aa):
    write_value_int_1('ns=4;i=11', aa)

def write_value_int_node3(aa):
    write_value_int_2('ns=4;i=9', aa)

def write_value_int_node5(aa):
    write_value_int_3('ns=4;i=10', aa)

def connect_menu_init():
    global window, btn_connect, btn_refresh
    window = Tk()       #tao khung GUI ten window
    window.title("Giao dien quan sat he thong")
    window.geometry("1000x750")

    # Create main label for GUI
    lbl = Label(window, text="GIAO DIỆN QUA SÁT HỆ THỐNG", foreground="black", font=("Arial", 20))
    lbl.place(x=180, y=10)
    # Create label for connecting Ports
    #lbl_port = Label(window, text="Available Port(s): ", foreground="black", font=("Arial", 12))
    #lbl_port.place(x=450, y=70)
    #lbl_port = Label(window, text="Baude Rate: ", foreground="black", font=("Arial", 12))
    #lbl_port.place(x=450, y=140)
    # Create label for video frame
    lbl_video = Label(window, text="CAMERA:", foreground="black", font=("Arial", 15))
    lbl_video.place(x=40, y=70)
    # Create label for image frame
    lbl_image = Label(window, text="ẢNH CHỤP DETECT VẬT:", foreground="black", font=("Arial", 15))
    lbl_image.place(x=40, y=370)
    lbl_imagetool = Label(window, text="ẢNH CHỤP DETECT TOOL:", foreground="black", font=("Arial", 15))
    lbl_imagetool.place(x=400, y=370)
    # Create label for Coordination
    lbl_coord = Label(window, text="TỌA ĐỘ ĐỐI TƯỢNG:", foreground="black", font=("Arial", 15))
    lbl_coord.place(x=750, y=370)
    lbl_vat = Label(window, text="TỌA ĐỘ VẬT:", foreground="black", font=("Arial", 15))
    lbl_vat.place(x=750, y=400)
    lbl_x = Label(window, text="X:          (mm)", foreground="black", font=("Arial", 15))
    lbl_x.place(x=750, y=430)
    lbl_y = Label(window, text="Y:          (mm)", foreground="black", font=("Arial", 15))
    lbl_y.place(x=750, y=460)
    lbl_huongvat = Label(window, text="HƯỚNG CỦA VẬT:", foreground="black", font=("Arial", 15))
    lbl_huongvat.place(x=750, y=490)
    lbl_alpha = Label(window, text="Alpha =           ", foreground="black", font=("Arial", 15))
    lbl_alpha.place(x=750, y=520)
    lbl_tool = Label(window, text="TỌA ĐỘ TOOL:", foreground="black", font=("Arial", 15))
    lbl_tool.place(x=750, y=550)
    lbl_x1 = Label(window, text="X:         (mm)", foreground="black", font=("Arial", 15))
    lbl_x1.place(x=750, y=580)
    lbl_y1 = Label(window, text="Y:         (mm)", foreground="black", font=("Arial", 15))
    lbl_y1.place(x=750, y=610)
    lbl_huongtool = Label(window, text="HƯỚNG CỦA TOOL:", foreground="black", font=("Arial", 15))
    lbl_huongtool.place(x=750, y=640)
    lbl_beta = Label(window, text="Beta =           ", foreground="black", font=("Arial", 15))
    lbl_beta.place(x=750, y=670)
def update_frame():
    global canvas, photo, frame
    # Doc tu camera
    ret, frame = video.read()
    # Resize
    frame = cv.resize(frame, dsize=None, fx=0.5, fy=0.5)
    # convert color
    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)
    window.after(15, update_frame)
    return
def update_frametool():
    global canvas, photo, frametool
    # Doc tu camera
    ret, frametool = video.read()
    # Resize
    frametool = cv.resize(frametool, dsize=None, fx=0.5, fy=0.5)
    # convert color
    frametool = cv.cvtColor(frametool, cv.COLOR_BGR2RGB)
    photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frametool))
    canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)
    window.after(15, update_frametool)
    return


def image_processing():
    global im_save, x, y, z
    rng.seed(12345)
    img = cv.imread('filename.jpg', cv.IMREAD_COLOR)    # láº¥y áº£nh Ä‘Ã£ chá»¥p Ä‘Æ°á»£c lÆ°u tá»« file
    #cv.imshow("anh", img)
    cols, rows, n = img.shape   #height, width, color
    print(cols, rows, n)   # cols = 480, rows = 640, n = 3
    # create zero matrix
    new_img = np.zeros((cols, rows), dtype=np.uint8)
    # compare blue channel to create matrix contains object area
    for col in range(0, cols):
        for row in range(0, rows):
            if (row > 140) and (row < 300):
                if (col > 200) and (col < 460):
                    _blue = img[row, col, 2]
                    #print(_blue)
                    if _blue > 100:
                        new_img[row, col] = 255
                    else:
                        new_img[row, col] = 0
    #Create masked matrix
    kernel = cv.getStructuringElement(cv.MORPH_CROSS, (29, 29), (-1, -1))
    # Smooth Contours
    new_img = cv.morphologyEx(new_img, cv.MORPH_CLOSE, kernel)
    # Contours detect
    canny_img = cv.Canny(new_img, 50, 50, 3)
    contours, _ = cv.findContours(canny_img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    # Get the moments
    mu = [None] * len(contours)
    for i in range(len(contours)):
        mu[i] = cv.moments(contours[i])
    # Get the mass centers
    mc = [None] * len(contours)
    for i in range(len(contours)):
        # add 1e-5 to avoid division by zero
        mc[i] = (mu[i]['m10'] / (mu[i]['m00'] + 1e-5), mu[i]['m01'] / (mu[i]['m00'] + 1e-5))
    # Draw contours
    drawing = np.zeros((canny_img.shape[0], canny_img.shape[1], 3), dtype=np.uint8)
    for i in range(len(contours)):
        color = (rng.randint(0, 256), rng.randint(0, 256), rng.randint(0, 256))
        cv.drawContours(drawing, contours, i, color, 2)
    # Find the object's orientation
    coords = cv.findNonZero(new_img)
    box = cv.minAreaRect(coords)
    rect_point = np.array([])
    cv.boxPoints(box, rect_point)
    # a = rect_point[1].x - rect_point[0].x
    # edge1 = np.array()

    # Contour of the rectangle
    cnt = contours[0]
    # Fit bounding rectangle around contour
    rotatedRect = cv.minAreaRect(cnt)
    # getting centroid, width, height and angle of the rectangle contour
    (cx, cy), (width, height), angle = rotatedRect
    # centetoid of the rectangle contour
    cx = int(cx)
    cy = int(cy)
    # centroid of contour of rectangle
    #print(cx, cy)
    # Coordinates of object in camera frame
    x = round(-1.0783065*cx + 0.0000042244*cy + 438.825661066, 2)
    y = round(-0.0019104581*cx + 1.07660446166*cy - 101.9801822763, 2)
    z = 100
    #lbl_cx1 = Label(window, text=x, foreground="black", font=("Arial", 15))
    #lbl_cx1.place(x=530, y=550)
    #lbl_cy1 = Label(window, text=y, foreground="black", font=("Arial", 15))
    #lbl_cy1.place(x=530, y=580)
    print("toa do thuc CAM: ", x, y)
    distance = -311  # distance between camera frame and robot frame
    # Coordinates of object in robot frame
    x = int(-x) + distance
    y = int(-y)
    anphal = math.atan2(-y, -x)
    anphal = (anphal*180)/math.pi
    print("x: ", x, "\ny: ", y)
    lbl_cx = Label(window, text=x, foreground="black", font=("Arial", 15))
    lbl_cx.place(x=780, y=430)
    lbl_cy = Label(window, text=y, foreground="black", font=("Arial", 15))
    lbl_cy.place(x=780, y=460)
    '''if width > height:
        angle = angle + 90
    else:
        angle = angle'''
    #print("Angle: ", round((90-angle), 2))
    lbl_angle = Label(window, text=round((anphal), 2), foreground="black", font=("Arial", 15))
    lbl_angle.place(x=820, y=520)
    im = cv.drawContours(drawing, [cnt], 0, (0, 0, 255), 2)
    # draw center
    cv.circle(im, (cx, cy), 2, (200, 255, 0), 2)
    # Write coordinates and orientation of center
    #cv.putText(im, str("Angle: " + str(round((angle), 2))), (int(cx)+20, int(cy) + 25), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255),
               #1, cv.LINE_AA)
    #cv.putText(im, str("Center: " + str(cx) + "," + str(cy)), (int(cx), int(cy) - 20), cv.FONT_HERSHEY_SIMPLEX, 1,
               #(0, 255, 255), 1, cv.LINE_AA)
    im_save = cv.imwrite("file.jpg", im)


def pulse_calculating():
    global x, y, z, string_time, theta1_hientai, theta2_hientai,theta3_hientai, theta5_hientai
    d1 = 231
    a2 = 221.12
    d4 = 225
    d6 = 145
    print(x, y, z)
    theta1 = math.atan2(-y, -x)
    x = x + 100*math.cos(theta1)
    y = y + 100*math.sin(theta1)
    k = x*math.cos(theta1) + y*math.sin(theta1)
    h = z - d1
    cos_th3 = (k**2+h**2-a2**2-d4**2)/(2*a2*d4)
    sin_th3 = math.sqrt(1-cos_th3**2)
    theta3 = math.atan2(sin_th3, cos_th3)
    m = d4*sin_th3
    n = a2 + d4*cos_th3
    sin_th2 = -(k*n+h*m)/(m**2+n**2)
    cos_th2 = (h*n-k*m)/(m**2+n**2)
    print("z=",z, k, h, m, n, sin_th2, cos_th2 ,sin_th2/cos_th2)
    theta2 = math.atan2(-sin_th2, -cos_th2)
    theta2 = math.pi - abs(theta2)
    theta1 = int(round((theta1*180/math.pi), 0))
    theta2 = int(round((theta2*180/math.pi), 0))
    theta3 = int(round((theta3*180/math.pi), 0))
    theta5 = 90 - theta2 - theta3
    print(theta1, theta2, theta3, theta5)
    theta1_hientai = theta1
    theta2_hientai = theta2
    theta3_hientai = theta3
    theta5_hientai = theta5
    # Define the direction of each joint
    """theta1 = 180 - abs(theta1)
    theta2 = 180 - abs(theta2)
    if abs(theta3) >= 90:
        theta3 = 180 - abs(theta3)"""
    if theta1 >= 0:
        dir1 = 1
    else:
        dir1 = 0
    if theta2 >= 0:
        dir2 = 1
    else:
        dir2 = 0
    if theta3 >= 0:
        dir3 = 1
    else:
        dir3 = 0
    if theta5 >= 0:
        dir5 = 1
    else:
        dir5 = 0
        theta5 = -theta5
    if theta1 >= 10:
        str_theta1 = str(dir1) + str(theta1)
    else:
        str_theta1 = str(dir1) + "0" + str(theta1)
    if theta2 >= 10:
        str_theta2 = str(dir2) + str(theta2)
    else:
        str_theta2 = str(dir2) + "0" + str(theta2)
    if theta3 >= 10:
        str_theta3 = str(dir3) + str(theta3)
    else:
        str_theta3 = str(dir3) + "0" + str(theta3)
    if theta5 >= 10:
        str_theta5 = str(dir5) + str(theta5)
    else:
        str_theta5 = str(dir5) + "0" + str(theta5)
    """theta1 = 45
    theta2 = 45
    theta3 = 60
    theta5 = 90
    time_pulse1 = time_move / (2*(theta1*(100/14)) / (1.8/16))
    time_pulse2 = time_move / (2*(theta2*(77/14)) / (1.8/16))
    time_pulse3 = time_move / (2*(theta3*(61/14)) / (1.8/2))
    time_pulse5 = time_move / (2*(theta5*(45/10)) / (1.8/16))
    # Convert unit from second to millisecond
    time_pulse1 = int(round(round(time_pulse1,4)*10000,0))
    time_pulse2 = int(round(round(time_pulse2,4)*10000,0))
    time_pulse3 = int(round(round(time_pulse3,4)*10000,0))
    time_pulse5 = int(round(round(time_pulse5,4)*10000,0))"""
    # write a string to transfer
    string_time = str_theta1 + str_theta2 + str_theta3 + "000" + str_theta5
    #print(theta1, theta2, theta3, theta5)
    print(string_time)

def image_processingtool():
    global im_savetool, x1, y1, z1
    rng.seed(12345)
    imgtool = cv.imread('filenametool.jpg', cv.IMREAD_COLOR)    # láº¥y áº£nh Ä‘Ã£ chá»¥p Ä‘Æ°á»£c lÆ°u tá»« file
    #cv.imshow("anh", img)
    cols, rows, n = imgtool.shape
    print(cols, rows, n)
    # create zero matrix
    new_img = np.zeros((cols, rows), dtype=np.uint8)
    # compare blue channel to create matrix contains object area
    for col in range(0, cols):
        for row in range(0, rows):
            if (row > 140) and (row < 300):
                if (col > 200) and (col < 440):
                    _green = imgtool[row, col, 1]
                    #print(_green, row, col)
                    if _green > 120:
                        new_img[row, col] = 255
                    else:
                        new_img[row, col] = 0
    #Create masked matrix
    kernel = cv.getStructuringElement(cv.MORPH_CROSS, (29, 29), (-1, -1))
    # Smooth Contours
    new_img = cv.morphologyEx(new_img, cv.MORPH_CLOSE, kernel)
    # Contours detect
    canny_img = cv.Canny(new_img, 50, 50, 3)
    contours, _ = cv.findContours(canny_img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    # Get the moments
    mu = [None] * len(contours)
    for i in range(len(contours)):
        mu[i] = cv.moments(contours[i])
    # Get the mass centers
    mc = [None] * len(contours)
    for i in range(len(contours)):
        # add 1e-5 to avoid division by zero
        mc[i] = (mu[i]['m10'] / (mu[i]['m00'] + 1e-5), mu[i]['m01'] / (mu[i]['m00'] + 1e-5))
    # Draw contours
    drawing = np.zeros((canny_img.shape[0], canny_img.shape[1], 3), dtype=np.uint8)
    for i in range(len(contours)):
        color = (rng.randint(0, 256), rng.randint(0, 256), rng.randint(0, 256))
        cv.drawContours(drawing, contours, i, color, 2)
    # Find the object's orientation
    coords = cv.findNonZero(new_img)
    box = cv.minAreaRect(coords)
    rect_point = np.array([])
    cv.boxPoints(box, rect_point)
    # a = rect_point[1].x - rect_point[0].x
    # edge1 = np.array()

    # Contour of the rectangle
    cnt = contours[0]
    # Fit bounding rectangle around contour
    rotatedRect = cv.minAreaRect(cnt)
    # getting centroid, width, height and angle of the rectangle contour
    (cx, cy), (width, height), angle = rotatedRect
    # centetoid of the rectangle contour
    cx = int(cx)
    cy = int(cy)
    # centroid of contour of rectangle
    #print(cx, cy)
    # Coordinates of object in camera frame
    x1 = round(-1.0783065*cx + 0.0000042244*cy + 438.825661066, 2)
    y1 = round(-0.0019104581*cx + 1.07660446166*cy - 101.9801822763, 2)
    z1 = 100
    #lbl_cx1 = Label(window, text=x, foreground="black", font=("Arial", 15))
    #lbl_cx1.place(x=530, y=550)
    #lbl_cy1 = Label(window, text=y, foreground="black", font=("Arial", 15))
    #lbl_cy1.place(x=530, y=580)
    print("toa do thuc CAM: ", x1, y1)
    distance = -311  # distance between camera frame and robot frame
    # Coordinates of object in robot frame
    x1 = int(-x1) + distance
    y1 = int(-y1)
    beta = math.atan2(-y1, -x1)
    beta = (beta*180)/math.pi
    print("x: ", x1, "\ny: ", y1)
    lbl_cx = Label(window, text=x1, foreground="black", font=("Arial", 15))
    lbl_cx.place(x=780, y=580)
    lbl_cy = Label(window, text=y1, foreground="black", font=("Arial", 15))
    lbl_cy.place(x=780, y=610)
    '''if width > height:
        angle = angle + 90
    else:
        angle = angle'''
    #print("Angle: ", round((90-angle), 2))
    lbl_angle = Label(window, text=round((beta), 2), foreground="black", font=("Arial", 15))
    lbl_angle.place(x=820, y=670)
    im = cv.drawContours(drawing, [cnt], 0, (0, 255, 0), 2)
    # draw center
    cv.circle(im, (cx, cy), 2, (200, 255, 0), 2)
    # Write coordinates and orientation of center
    #cv.putText(im, str("Angle: " + str(round((angle), 2))), (int(cx)+20, int(cy) + 25), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255),
               #1, cv.LINE_AA)
    #cv.putText(im, str("Center: " + str(cx) + "," + str(cy)), (int(cx), int(cy) - 20), cv.FONT_HERSHEY_SIMPLEX, 1,
               #(0, 255, 255), 1, cv.LINE_AA)
    im_savetool = cv.imwrite("filetool.jpg", im)

def image_saving(): #lÆ°u áº£nh detect thÃ nh file
    global frame, img_tk, im_save
    frame = cv.resize(frame, dsize=None, fx=2, fy=2)
    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    img_save = cv.imwrite("filename.jpg", frame)
    print(img_save)
    image_processing()
    pulse_calculating()
    img_open = (Image.open(r'C:\Users\DELL\Desktop\pythonProject\file.jpg'))
    img_resize = img_open.resize((300, 300), PIL.Image.ANTIALIAS)
    img_tk = PIL.ImageTk.PhotoImage(img_resize)
    img_show = Button(window, text="", image=img_tk)
    img_show.place(x=40, y=400)

def image_savingtool():
    global frametool, img_tktool, im_savetool
    update_frametool()
    frametool = cv.resize(frametool, dsize=None, fx=2, fy=2)
    frametool = cv.cvtColor(frametool, cv.COLOR_BGR2RGB)
    img_savetool = cv.imwrite("filenametool.jpg", frametool)
    print(img_savetool)
    image_processingtool()
    img_open = (Image.open(r'C:\Users\DELL\Desktop\pythonProject\filetool.jpg'))
    img_resize = img_open.resize((300, 300), PIL.Image.ANTIALIAS)
    img_tktool = PIL.ImageTk.PhotoImage(img_resize)
    img_show = Button(window, text="", image=img_tktool)
    img_show.place(x=400, y=400)

def truyendulieu():
    global theta1_hientai, theta2_hientai, theta3_hientai, theta5_hientai, xungthuan, xungnghich
    #client = Client("opc.tcp://192.168.1.199:4840")
    try:
        client.connect()

        root = client.get_root_node()
        print("Objects root node is: ", root)
        b11 = abs((int(theta1_hientai * 16 * 100 / (1.8 * 14)))) * 100 + 2
        b12 = abs((int(theta2_hientai * 16 * 77 / (14 * 1.8)))) * 100 + 2
        b13 = abs((int(theta3_hientai * 20 * 61 / (14 * 1.8)))) * 100 + 2
        b14 = abs((int(theta5_hientai * 16 * 45 / (10 * 1.8)))) * 100 + 12
        xungthuan  = [b11, b12, b13, 0]
        xungnghich = [0, 0, 0, b14]

        t = time.time()  # phụ thuộc số thread của cpu....
        t1 = threading.Thread(target=write_value_int, args=([b11]))
        t2 = threading.Thread(target=write_value_int_1, args=([b12]))
        t3 = threading.Thread(target=write_value_int_2, args=([b13]))
        t4 = threading.Thread(target=write_value_int_3, args=([b14]))
        t1.start()
        t2.start()
        t3.start()
        t4.start()

    finally:
        client.disconnect()

#def truyendulieu2():
    #jfdnjndjdf()

def hambuxung():
    global theta1_hientai, theta2_hientai, theta3_hientai, theta5_hientai, xungthuan, xungnghich
    print("hay nhap toa doa moi")
    x = input()
    y = input()
    z = input()
    x = int(x)
    y = int(y)
    z = int(z)  # z = 100
    print(x, y, z)
    d1 = 231
    a2 = 221.12
    d4 = 225
    d6 = 145
    truyen1 = 0
    truyen2 = 0
    truyen3 = 0
    truyen5 = 0
    theta1 = math.atan2(-y, -x)
    k = x*math.cos(theta1) + y*math.sin(theta1)
    h = z - d1
    cos_t3 = (k**2 + h**2 - a2**2 - d4**2)/(2*a2*d4)
    sin_t3 = math.sqrt(1 - cos_t3**2)
    theta3 = math.atan2(sin_t3, cos_t3)
    m = d4*sin_t3
    n = a2 + d4*cos_t3
    sin_th2 = -(k*n + h*m)/(m**2 + n**2)
    cos_th2 = (h*n - k*m)/(m**2 + n**2)
    print("z=", z, k, h, m, n, sin_th2, cos_th2, sin_th2 / cos_th2)
    theta2 = math.atan2(-sin_th2, -cos_th2)
    theta2 = math.pi - abs(theta2)
    deltatheta1 = int(round((theta1*180/math.pi), 0)) - theta1_hientai
    deltatheta2 = int(round((theta2*180/math.pi), 0)) - theta2_hientai
    deltatheta3 = int(round((theta3*180/math.pi), 0)) - theta3_hientai
     # đổi tool từ 180 thành 90
    deltatheta5 = 90 - int(round((theta2*180/math.pi), 0)) - int(round((theta3*180/math.pi), 0)) - theta5_hientai
    theta1_hientai = int(round((theta1*180/math.pi), 0))
    theta2_hientai = int(round((theta2*180/math.pi), 0))
    theta3_hientai = int(round((theta3*180/math.pi), 0))
    theta5_hientai = 90 - theta2_hientai - theta3_hientai

    print("cac góc hiện tại: ")
    print(theta1_hientai, theta2_hientai, theta3_hientai, theta5_hientai)
    print(xungthuan, xungnghich)
    if deltatheta1 >= 0: # delta goc duong
        xungthuan[0] = xungthuan[0] + abs((int(deltatheta1 * 16 * 100 / (1.8 * 14)))) * 100
        truyen1 = xungthuan[0]
    if deltatheta2 >= 0:
        xungthuan[1] = xungthuan[1] + abs((int(deltatheta2 * 16 * 77 / (14 * 1.8)))) * 100
        truyen2 = xungthuan[1]
    if deltatheta3 >= 0:
        xungthuan[2] = xungthuan[2] + abs((int(deltatheta3 * 20 * 61 / (14 * 1.8)))) * 100
        truyen3 = xungthuan[2]
    if deltatheta5 >= 0:
        xungthuan[3] = xungthuan[3] + abs((int(deltatheta5 * 16 * 45 / (10 * 1.8)))) * 100 + 2
        truyen5 = xungthuan[3]

    if deltatheta1 < 0: # delta goc duong
        xungnghich[0] = xungnghich[0] + abs((int(deltatheta1 * 16 * 100 / (1.8 * 14)))) * 100 + 12
        truyen1 = xungnghich[0]
    if deltatheta2 < 0:
        xungnghich[1] = xungnghich[1] + abs((int(deltatheta2 * 16 * 77 / (14 * 1.8)))) * 100 + 12
        truyen2 = xungnghich[1]
    if deltatheta3 < 0:
        xungnghich[2] = xungnghich[2] + abs((int(deltatheta3 * 20 * 61 / (14 * 1.8)))) * 100 + 12
        truyen3 = xungnghich[2]
    if deltatheta5 < 0:
        xungnghich[3] = xungnghich[3] + abs((int(deltatheta5 * 16 * 45 / (10 * 1.8)))) * 100
        truyen5 = xungnghich[3]
    print("số xung tuyền: ")
    print(truyen1, truyen2, truyen3, truyen5)
    #truyendulieu2(truyen1, truyen2, truyen3, truyen5)

'''combo = Combobox(window, width=20)
combo.place(x=50, y=50)
def clicked():
    str = combo.get()
    if (ser.in_waiting > 0):
        data = ser.readline()
        sleep(0.1)
        print("receive:", str(data))
    else:
        # string = str + "\r"
        print("Sent!")
        ser.write(str.encode())
        sleep(0.5)
btn = Button(window, text="Transfer", command=clicked)
btn.place(x=50, y=20)'''

if __name__ == "__main__":
    global theta1_hientai, theta2_hientai,theta3_hientai, theta5_hientai, xungthuan, xungnghich
    xungthuan  = [0, 0, 0, 0]
    xungnghich = [0, 0, 0, 0]
    client = Client("opc.tcp://192.168.1.199:4840")
    connect_menu_init()
    video = cv.VideoCapture(0)  # Táº¡o khung camera trÃªn GUI
    canvas_w = video.get(cv.CAP_PROP_FRAME_WIDTH) // 2
    canvas_h = video.get(cv.CAP_PROP_FRAME_HEIGHT) // 2
    canvas = Canvas(window, width=canvas_w, height=canvas_h, bg="white")  # Táº¡o Ä‘á»“ há»a cÃ³ cáº¥u trÃºc
    canvas.place(x=40, y=100)
    photo = None
    update_frame()
    btn1 = Button(window, text="Detect Vật", command=image_saving)
    btn1.place(x=500, y=100)

    btn1 = Button(window, text="Detect Tool", command=image_savingtool)
    btn1.place(x=600, y=100)

    btn2 = Button(window, text="Truyen", command=truyendulieu)
    btn2.place(x=500, y=150)

    btn3 = Button(window, text="Bu xung", command=hambuxung)
    btn3.place(x=600, y=150)
window.mainloop()
