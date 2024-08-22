from ultralytics import YOLO
import cv2
import cvzone
import math
from sort import *
import numpy as np



cap = cv2.VideoCapture("../Videos/koy4.mp4")
model = YOLO("../Yolo-Weights/yolov8n.pt")
mask = cv2.imread("mask3.png")
mask = cv2.resize(mask, (int(cap.get(3)), int(cap.get(4))))



classNames = ['sheep']

tracker = Sort(max_age=20, min_hits=3, iou_threshold=0.3)
limits = [100, 400, 1300, 400]
totalCount = []

while True:
    success, img = cap.read()

    if not success:
        break

    # Display the main image
    cv2.line(img, (limits[0], limits[1]), (limits[2], limits[3]), (242, 242, 242), 1)

    imgRegion = cv2.bitwise_and(img, mask)
    results = model(imgRegion, stream=True)
    detections = np.empty((0, 5))

    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2 - x1, y2 - y1
            conf = math.ceil((box.conf[0] * 100)) / 100
            cls = 0
            currentClass = classNames[cls]

            if currentClass == "sheep" and conf > 0.5:
                currentArray = np.array([x1, y1, x2, y2, conf])
                detections = np.vstack((detections, currentArray))

    resultsTracker = tracker.update(detections)

    for result in resultsTracker:
        x1, y1, x2, y2, id = result
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        w, h = x2 - x1, y2 - y1
        cx, cy = x1 + w // 2, y1 + h // 2

        cvzone.cornerRect(img, (x1, y1, w, h), l=9, rt=2, colorR=(255, 0, 255))
        cvzone.putTextRect(img, f' {int(id)}', (max(0, x1), max(35, y1)),
                           scale=2, thickness=3, offset=10)

        cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)

        if limits[0] < cx < limits[2] and limits[1] - 15 < cy < limits[1] + 15:
            if totalCount.count(id) == 0:
                totalCount.append(id)
                cv2.line(img, (limits[0], limits[1]), (limits[2], limits[3]), (0, 255, 0), 5)

    cv2.putText(img, f'Count: {len(totalCount)}', (50, 50), cv2.FONT_HERSHEY_PLAIN, 5, (50, 50, 255), 8)
    cv2.imshow("Image", img)

    key = cv2.waitKeyEx(1)
    if key == ord('q'):
        break
    elif key == ord('s'):
        cap.set(cv2.CAP_PROP_POS_FRAMES, max(0, cap.get(cv2.CAP_PROP_POS_FRAMES) + 20))
    elif key == 32:  # ASCII code for spacebar
        cv2.waitKey(0)  # Wait indefinitely until a key is pressed
        continue

cv2.destroyAllWindows()
cap.release()