import cv2

string_table = 'E&M$BXG@#*%+-Q1+|__]._+^0}'

img = cv2.imread('img02.png')

grey_scale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grey_scale_img_resize = cv2.resize(grey_scale_img, (180, 100))

new_string_img = ''

# traverse all the pixels
k = 0
for i in grey_scale_img_resize:
    k += 1
    for j in i:
        pixel_index = (int)(j / 255 * (len(string_table) - 1))
        new_string_img += string_table[pixel_index]
    new_string_img += '\n'

print(new_string_img)
print(k)
# cv2.imshow('gs_img01', grey_scale_img_resize)
# cv2.waitKey()
# cv2.destroyAllWindows()