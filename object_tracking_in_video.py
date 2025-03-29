import cv2

video = cv2.VideoCapture(0)

tracker = cv2.TrackerCSRT_create()  

ret, frame = video.read()
bbox = cv2.selectROI("select object",frame,False)

tracker.init(frame, bbox)

while(True):
    ret, frame = video.read()
    if not ret:
        break

    success, bbox = tracker.update(frame)

    if(success):
        x_cor, y_cor, width, height = [int(i) for i in bbox]
        cv2.rectangle(frame, (x_cor, y_cor), (x_cor + width, y_cor + height), (0, 255, 0), 2)

    cv2.imshow("Object tracking: ", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

video.release()
cv2.destroyAllWindows()


