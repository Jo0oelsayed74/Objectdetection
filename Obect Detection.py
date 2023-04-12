import cv2
image = cv2.imread('D:\Object counter3.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
count = 0
for c in contours:
    area = cv2.contourArea(c)
    if area > 1000:
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        count += 1
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, 'Number of objects: ' + str(count), (10, 30), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', 800, 600)
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
