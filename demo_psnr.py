import cv2

video1 = cv2.VideoCapture('src\simpson_cut1.mp4')
vid1_width = int(video1.get(cv2.CAP_PROP_FRAME_WIDTH))
vid1_height = int(video1.get(cv2.CAP_PROP_FRAME_HEIGHT))

#fps cua video 1:
if not video1.isOpened():
    print("Error video!!!!")
else: 
    fps = video1.get(cv2.CAP_PROP_FPS)
    print("Frame per second: ", fps, "kbps")
    print("Resolusion:", vid1_width, "x", vid1_height)

# chuyen do phan giai cua video nay sang do phan giai khac
vid2_width = 640
vid2_height = 480
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video2 = cv2.VideoWriter('src\simpson_cut1.mp4', fourcc, fps, (vid2_width, vid2_height))

# Đọc từng khung hình, thay đổi độ phân giải và ghi vào video đầu ra
while True:
    ret, frame = video1.read()
    if not ret:
        break

    # Thay đổi độ phân giải của khung hình
    frame_resized = cv2.resize(frame, (vid2_width, vid1_height))

    # Ghi khung hình đã thay đổi vào video đầu ra
    video2.write(frame_resized)

# Giải phóng tài nguyên
video1.release()
video2.release()
cv2.destroyAllWindows()

