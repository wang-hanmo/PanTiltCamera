#coding=utf-8
import cv2
import time
def get_img_from_camera_net(folder_path, f_w, f_h):
    cap = cv2.VideoCapture('rtsp://admin:admin@192.168.42.108:554/cam/realmonitor?channel=1&subtype=0')#获取云台摄像机主视频流
    #cap = cv2.VideoCapture('rtsp://admin:admin@192.168.42.108:554/cam/realmonitor?channel=1&subtype=1')#获取云台摄像机辅助视频流一
    #cap = cv2.VideoCapture('rtsp://admin:admin@192.168.42.108:554/cam/realmonitor?channel=1&subtype=2')#获取云台摄像机辅助视频流二
    #cap = cv2.VideoCapture(0) #默认本地视频
    vid = cv2.VideoWriter('./output.avi', cv2.VideoWriter_fourcc('X','V','I','D'), 20, (f_w,f_h))
    record = False
    while cap.isOpened():
        ret, frame = cap.read()
        if ret==True:
            frame = cv2.resize(frame,(f_w, f_h))
            cv2.imshow("capture", frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == ord('c'):
                tid = time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime(time.time()))
                cv2.imwrite(folder_path + tid + '.png',frame)
            elif key == ord('k'):
                record =True
            
            if record:
                vid.write(frame)

    cap.release()
    vid.release()
    cv2.destroyAllWindows()
 
# 测试
if __name__ == '__main__':
    folder_path = './imgs/'
    width = 1024
    height = 768
    import os
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    get_img_from_camera_net(folder_path,width,height)
    
