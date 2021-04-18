import cv2
import mediapipe as mp
from strikes import strike, joint_angles

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
    lab_len = int(len(label) * 26.5)
    if lab_len > 450:
        lab_len = 480
    frame = cv2.flip(frame, 1)
    frame = cv2.rectangle(frame, (0, h), (lab_len, h-45), (255, 255, 255), cv2.FILLED)
    frame = cv2.putText(frame, label, (1, h - 15), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2, cv2.LINE_AA)


    return frame

def angle_det(frame):
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

    joints_angles = joint_angles(joints)

    if 14 in joints:
        frame = cv2.putText(frame, str(joints_angles['right elbow']), joints[14], cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1, cv2.LINE_AA)

    if 12 in joints:
        frame = cv2.putText(frame, str(joints_angles['right shoulder']), joints[12], cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1, cv2.LINE_AA)

    if 24 in joints:
        frame = cv2.putText(frame, str(joints_angles['right hip']), joints[24], cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1, cv2.LINE_AA)

    if 26 in joints:
        frame = cv2.putText(frame, str(joints_angles['right knee']), joints[26], cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1, cv2.LINE_AA)

    if 13 in joints:
        frame = cv2.putText(frame, str(joints_angles['left elbow']), joints[13], cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1, cv2.LINE_AA)

    if 11 in joints:
        frame = cv2.putText(frame, str(joints_angles['left shoulder']), joints[11], cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1, cv2.LINE_AA)

    if 23 in joints:
        frame = cv2.putText(frame, str(joints_angles['left hip']), joints[23], cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1, cv2.LINE_AA)

    if 25 in joints:
        frame = cv2.putText(frame, str(joints_angles['left knee']), joints[25], cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1, cv2.LINE_AA)


    return frame, joints_angles