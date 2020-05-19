import cv2

string_table = 'EMBXG98654321@#%&||()_+*^$}'

img = cv2.imread('img01.png')

grey_scale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grey_scale_img_resize = cv2.resize(grey_scale_img, (100, 30))

cv2.imshow('gs_img01', grey_scale_img_resize)
cv2.waitKey()
cv2.destroyAllWindows()