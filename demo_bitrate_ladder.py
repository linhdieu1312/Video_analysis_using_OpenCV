import cv2

def calculate_bitrate_ladder(video_path):
    # Đọc thông tin kích thước và tốc độ khung hình của video
    cap = cv2.VideoCapture(video_path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    cap.release()

    # Xác định bitrate tối thiểu và tối đa (đơn vị: kbps)
    min_bitrate = 500
    max_bitrate = 5000

    # Chia bitrate thành 3 lớp (ladder)
    bitrate_ladder = [min_bitrate, (min_bitrate + max_bitrate) // 2, max_bitrate]

    # In thông tin bitrate ladder
    print("Bitrate Ladder:")
    for i, bitrate in enumerate(bitrate_ladder):
        print(f"Level {i + 1}: {bitrate} kbps")

# Đường dẫn của video cần tính toán bitrate ladder
video_path = 'src/simpson_cut1.mp4'
calculate_bitrate_ladder(video_path)
