import cv2

# import and show img, press any key to return
img = cv2.imread("img01.png")
resized_img = cv2.resize(img, (500, 300))
cv2.imshow("re_img01", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()



















