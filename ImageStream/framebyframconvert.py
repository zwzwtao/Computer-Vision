import os
import cv2

string_table = 'E&M$BXG@#*%+-Q1+|__]._+^0}'

video = cv2.VideoCapture('video01.mp4')

return_val, frame_by_frame = video.read()

while return_val:
    string_img = ''
    grey_scale_img = cv2.cvtColor(frame_by_frame, cv2.COLOR_BGR2GRAY)
    grey_scale_img_resize = cv2.resize(grey_scale_img, (100, 30))

    for i in grey_scale_img_resize:
        for j in i:
            pixel_index = (int)(j / 255 * (len(string_table) - 1))
            string_img += string_table[pixel_index]
        string_img += '\n'
    os.system('cls')
    print(string_img)
    return_val, frame_by_frame = video.read()
    cv2.waitKey(5)














