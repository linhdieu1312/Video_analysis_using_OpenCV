# import cv2

# vid = cv2.VideoCapture('src\simpson_cut1.mp4')
# if vid.isOpened() == False:
#     print("Error")
# else:
#     #frame per second: tốc độ khung hình trên giây: Cap_prop_fps = 5
#     # "Property Frames Per Second" trong OpenCV: hằng số được sử dụng để xác định và truy cập thông số 
#     # về tốc độ khung hình của video
#     fps = vid.get(cv2.CAP_PROP_FPS)
#     vid1_width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
#     vid1_height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
#     print('Frames per second : ', fps,'FPS')

#     #count the number of frames in a video: số lượng khung hình: cap_prop_frame_count = 7
#     fpv = vid.get(cv2.CAP_PROP_FRAME_COUNT)
#     print('Frame count : ', fpv)
#     duration = int(fpv / fps)

#     print(f"Độ dài video: {duration} giây")

    
#     bitrate = vid.get(cv2.CAP_PROP_BITRATE) # 47
#     print("Bitrate: ", bitrate, "kbits/s")
    
#     pb = vid.get(cv2.VIDEOWRITER_PROP_FRAMEBYTES)
#     print("framebytes: ", pb)

# # while(vid.isOpened()):
# # 	# vid_capture.read() methods returns a tuple, first element is a bool 
# # 	# and the second is frame
# # 	ret, frame = vid.read()
# #     #Phương thức vid.read () trả về kết quả dạng tuple, trong đó phần tử đầu tiên kiểu boolean và 
# #     #phần tử tiếp theo là khung video thực tế. Khi phần tử đầu tiên là True có nghĩa là luồng video có chứa 
# #     # khung hình để đọc. Nếu có một khung hình để đọc, thì ta có thể sử dụng hàm imshow () để hiển thị khung hình
# #     # hiện tại trong một cửa sổ, nếu không thì thoát khỏi vòng lặp. Lưu ý rằng cũng có thể sử dụng hàm waitKey () 
# #     # để tạm dừng trong 20ms giữa các khung hình video. Gọi hàm waitKey () cho phép theo dõi nhập liệu bàn phím
# #     # từ người dùng. Trong trường hợp ví dụ thì nếu nhấn phím ‘q’ thì sẽ thoát khỏi vòng lặp.
# # 	if ret == True:
# # 		cv2.imshow('Frame',frame)
# # 		# 20 is in milliseconds, try to increase the value, say 50 and observe
# # 		key = cv2.waitKey(20)
		
# # 		if key == ord('q'):
# # 			break
# # 	else:
# # 		break

# # Release the video capture object
# vid.release()
# cv2.destroyAllWindows()

import cv2

# Đường dẫn của video
video_path = 'src/simpson_cut_2.mp4'

# Tạo đối tượng VideoCapture
cap = cv2.VideoCapture(video_path)

# Đọc một khung hình từ video
ret, frame = cap.read()

# Hiển thị ma trận điểm ảnh của frame
print("Ma trận điểm ảnh của frame:")
print(frame)

# Hiển thị khung hình
cv2.imshow('Video Frame', frame)
cv2.waitKey(0)  # Chờ đến khi có phản hồi từ người dùng
cv2.destroyAllWindows()

# Giải phóng tài nguyên
cap.release()
