import cv2
import streamlink

# Nhập URL của video live stream
url = "https://www.youtube.com/watch?v=hSAuaNyIuhc"
streams = streamlink.streams(url)

# Lấy stream video live từ YouTube
stream_url = streams["best"].url

print(stream_url)
# Mở stream video từ URL
cap = cv2.VideoCapture(stream_url)

while True:
    # Đọc frame từ stream video
    ret, frame = cap.read()

    if not ret:
        break
    frame = cv2.resize(frame, (720, 480))
    # Hiển thị frame
    cv2.imshow('Live Stream', frame)

    # Nhấn 'q' để thoát
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng tài nguyên
cap.release()
cv2.destroyAllWindows()
