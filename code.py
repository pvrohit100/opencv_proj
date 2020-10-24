# import the opencv library 
import cv2 


# define a video capture object 
vid = cv2.VideoCapture(1)
setfps = vid.set(cv2.CAP_PROP_FPS, 5)
i=input()
bgret, defbg = vid.read()
print("bg capt")
#print(defbg)

while(True): 
    
    # Capture the video frame 
    # by frame 
    ret, frame = vid.read() 

    # Display the resulting frame 
    
    for i in range(480):
        for j in range(640):
            if frame[i][j][0]>150 and frame[i][j][1]>150 and frame[i][j][2]>150:
                
                frame[i][j][0]=defbg[i][j][0]
                frame[i][j][1]=defbg[i][j][1]
                frame[i][j][2]=defbg[i][j][2]
                '''
                frame[i][j][0]=0  #############replace white color
                frame[i][j][1]=0
                frame[i][j][2]=0
                '''
    cv2.imshow('frame', frame)
    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 
