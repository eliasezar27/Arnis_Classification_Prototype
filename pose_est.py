import cv2
import mediapipe as mp
from strikes import strike

mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils


def pose_det(frame):
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    h, w, c = frame.shape
    results = pose.process(imgRGB)

    # print(results.pose_landmarks)
    joints = {}
    if results.pose_landmarks:
        mpDraw.draw_landmarks(frame, results.pose_landmarks, mpPose.POSE_CONNECTIONS)

        for id, lm in enumerate(results.pose_landmarks.landmark):
            # print(id, lm)
            cx, cy, thr = int(lm.x * w), int(lm.y * h), lm.visibility

            if thr > 0.5:
                joints[id] = (cx, cy)
                print(id, cx, cy, 'th: ', thr)

    label = strike(joints)
    frame = cv2.flip(frame, 1)
    frame = cv2.rectangle(frame, (0, 550), (450, h), (255, 255, 255), cv2.FILLED)
    frame = cv2.putText(frame, label, (1, h - 15), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2, cv2.LINE_AA)


    return frame