from flask import Flask, render_template, Response, request
import imutils
import threading
from imutils.video import VideoStream
import time
import cv2
from pose_est import pose_det

# initialize the output frame and a lock used to ensure thread-safe
# exchanges of the output frames (useful when multiple browsers/tabs
# are viewing the stream)
outputFrame = None
lock = threading.Lock()
# initialize a flask object
app = Flask(__name__)

vs = VideoStream(src=1).start()
time.sleep(2.0)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/opencam', methods=['GET', 'POST'])
def index2():
    answer = request.form['response']
    return render_template('index.html', ans=answer)


# def generate():
#     """Video streaming generator function."""
#     cap = cv2.VideoCapture(1)
#     # Read until video is completed
#     while(cap.isOpened()):
#         # Capture frame-by-frame
#         ret, img = cap.read()
#
#         scale_percent = 130 # percent of original size
#         width = int(img.shape[1] * scale_percent / 100)
#         height = int(img.shape[0] * scale_percent / 100)
#         dim = (width, height)
#
#         if ret == True:
#             img = cv2.resize(img, dim)
#             img = pose_det(img)
#             frame = cv2.imencode('.jpg', img)[1].tobytes()
#             yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
#             time.sleep(0.1)
#         else:
#             break


def camera():
    global vs, outputFrame, lock
    # grab global references to the video stream, output frame, and
    # lock variables

    while True:
        # read the next frame from the video stream, resize it,
        frame = vs.read()
        frame = imutils.resize(frame, width=800)
        frame = pose_det(frame)

        # acquire the lock, set the output frame, and release the
        # lock
        with lock:
            outputFrame = frame.copy()


def generate():
    # grab global references to the output frame and lock variables
    global outputFrame, lock
    # loop over frames from the output stream
    while True:
        # wait until the lock is acquired
        with lock:
            # check if the output frame is available, otherwise skip
            # the iteration of the loop
            if outputFrame is None:
                continue
            # encode the frame in JPEG format
            (flag, encodedImage) = cv2.imencode(".jpg", outputFrame)
            # ensure the frame was successfully encoded
            if not flag:
                continue
        # yield the output frame in the byte format
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')


@app.route('/video_feed')
def video_feed():
    # return the response generated along with the specific media
    # type (mime type)
    return Response(generate(), mimetype="multipart/x-mixed-replace; boundary=frame")


if __name__ == '__main__':
    # construct the argument parser and parse command line arguments

    t = threading.Thread(target=camera)
    t.daemon = True
    t.start()
    # start the flask app
    app.run(debug=True, threaded=True, use_reloader=False)
# release the video stream pointer
vs.stop()
