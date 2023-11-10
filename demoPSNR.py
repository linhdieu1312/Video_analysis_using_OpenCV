import cv2

# Đọc hai video cần so sánh
video1 = cv2.VideoCapture('src/simpson_cut1.mp4')
video2 = cv2.VideoCapture('src/simpson_cut_2.mp4')
# video1: width * height
vid1_width = int(video1.get(cv2.CAP_PROP_FRAME_WIDTH))
vid1_height = int(video1.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Kiểm tra xem video có mở thành công hay không
if not (video1.isOpened() and video2.isOpened()):
    print("Không thể mở video.")
    exit()

# Lấy thông số của video
fps = video1.get(cv2.CAP_PROP_FPS)
frame_count = int(video1.get(cv2.CAP_PROP_FRAME_COUNT))

# Tính toán PSNR cho từng khung hình
total_psnr = 0.0
for i in range(frame_count):
    ret1, frame1 = video1.read()
    ret2, frame2 = video2.read()

    # Kiểm tra xem video có kết thúc hay không
    if not (ret1 and ret2):
        break

    frame2 = cv2.resize(frame2, (vid1_width, vid1_height))
    # Tính toán PSNR cho từng khung hình và cộng vào tổng PSNR
    psnr_value = cv2.PSNR(frame1, frame2)
    total_psnr += psnr_value

# Tính toán PSNR trung bình
average_psnr = total_psnr / frame_count

print(f"PSNR trung bình giữa hai video là: {average_psnr} dB")

# Giải phóng tài nguyên
video1.release()
video2.release()
