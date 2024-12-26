import cv2

frameWidth = 640
frameHeight = 360

#capturing video using webcam or the video file we have
cap = cv2.VideoCapture("Resources/Rohit_Pull.mp4")
#cap = cv2.VideoCapture(0)
#fps=cap.get(cv2.CAP_PROP_FPS)
fps=30
delay= int(1000/fps)
#cap.set(3,frameWidth)
#cap.set(4,frameHeight)

# while True:
#     success, img = cap.read()
#     img = cv2.resize(img,(frameWidth,frameHeight))
#     #img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
#     cv2.imshow("Video", img)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

#This code was written to display the video in grayscale and also save the grayscale video in a new file
#but the VideoWriter_fourcc function is not working in my device
outputfile="Resources/Rohit_Pull_Grey.mp4"
fourcc=1983148141
out = cv2.VideoWriter(outputfile,fourcc,fps,(frameWidth,frameHeight))
while cap.isOpened():
    success, img = cap.read()
    if not success:
        break
    img = cv2.resize(img,(frameWidth,frameHeight))
    g_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Video", g_img)
    out.write(g_img)
    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break