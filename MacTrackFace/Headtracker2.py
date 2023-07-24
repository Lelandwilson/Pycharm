"""Human facial landmark detector based on Convolutional Neural Network."""
import cv2
import numpy as np
import tensorflow as tf
from tensorflow import keras
import math
import time
import pyautogui

import calibrateHead3

tf.get_logger().setLevel('INFO')

lastDirection = 0
newDirection = 0

topScreenMiddle = [781.9244384765625, -522.343994140625]
bottomScreenMiddle = [757.5992431640625, 510.1078186035156]

startup = True
calibrationLoop = 1
monitors = []
calibratedPositions = []

class FaceDetector:
    """Detect human face from image"""

    def __init__(self,
                 dnn_proto_text='models/deploy.prototxt',
                 dnn_model='models/res10_300x300_ssd_iter_140000.caffemodel'):
        """Initialization"""
        self.face_net = cv2.dnn.readNetFromCaffe(dnn_proto_text, dnn_model)
        self.detection_result = None

    def get_faceboxes(self, image, threshold=0.5):
        """
        Get the bounding box of faces in image using dnn.
        """
        rows, cols, _ = image.shape

        confidences = []
        faceboxes = []

        self.face_net.setInput(cv2.dnn.blobFromImage(
            image, 1.0, (300, 300), (104.0, 177.0, 123.0), False, False))
        detections = self.face_net.forward()

        for result in detections[0, 0, :, :]:
            confidence = result[2]
            if confidence > threshold:
                x_left_bottom = int(result[3] * cols)
                y_left_bottom = int(result[4] * rows)
                x_right_top = int(result[5] * cols)
                y_right_top = int(result[6] * rows)
                confidences.append(confidence)
                faceboxes.append(
                    [x_left_bottom, y_left_bottom, x_right_top, y_right_top])

        self.detection_result = [faceboxes, confidences]

        return confidences, faceboxes

    def draw_all_result(self, image):
        """Draw the detection result on image"""
        for facebox, conf in self.detection_result:
            cv2.rectangle(image, (facebox[0], facebox[1]),
                          (facebox[2], facebox[3]), (0, 255, 0))
            label = "face: %.4f" % conf
            label_size, base_line = cv2.getTextSize(
                label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)

            cv2.rectangle(image, (facebox[0], facebox[1] - label_size[1]),
                          (facebox[0] + label_size[0],
                           facebox[1] + base_line),
                          (0, 255, 0), cv2.FILLED)
            cv2.putText(image, label, (facebox[0], facebox[1]),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))


class MarkDetector:
    """Facial landmark detector by Convolutional Neural Network"""

    def __init__(self, saved_model='models/pose_model'):
        """Initialization"""
        # A face detector is required for mark detection.
        self.face_detector = FaceDetector()

        self.cnn_input_size = 128
        self.marks = None

        # Restore model from the saved_model file.
        # self.model = keras.models.load_model(saved_model)
        self.model = tf.saved_model.load(saved_model)

    @staticmethod
    def draw_box(image, boxes, box_color=(255, 255, 255)):
        """Draw square boxes on image"""
        for box in boxes:
            cv2.rectangle(image,
                          (box[0], box[1]),
                          (box[2], box[3]), box_color, 3)

    @staticmethod
    def move_box(box, offset):
        """Move the box to direction specified by vector offset"""
        left_x = box[0] + offset[0]
        top_y = box[1] + offset[1]
        right_x = box[2] + offset[0]
        bottom_y = box[3] + offset[1]
        return [left_x, top_y, right_x, bottom_y]

    @staticmethod
    def get_square_box(box):
        """Get a square box out of the given box, by expanding it."""
        left_x = box[0]
        top_y = box[1]
        right_x = box[2]
        bottom_y = box[3]

        box_width = right_x - left_x
        box_height = bottom_y - top_y

        # Check if box is already a square. If not, make it a square.
        diff = box_height - box_width
        delta = int(abs(diff) / 2)

        if diff == 0:  # Already a square.
            return box
        elif diff > 0:  # Height > width, a slim box.
            left_x -= delta
            right_x += delta
            if diff % 2 == 1:
                right_x += 1
        else:  # Width > height, a short box.
            top_y -= delta
            bottom_y += delta
            if diff % 2 == 1:
                bottom_y += 1

        # Make sure box is always square.
        assert ((right_x - left_x) == (bottom_y - top_y)), 'Box is not square.'

        return [left_x, top_y, right_x, bottom_y]

    @staticmethod
    def box_in_image(box, image):
        """Check if the box is in image"""
        rows = image.shape[0]
        cols = image.shape[1]
        return box[0] >= 0 and box[1] >= 0 and box[2] <= cols and box[3] <= rows

    def extract_cnn_facebox(self, image):
        """Extract face area from image."""
        _, raw_boxes = self.face_detector.get_faceboxes(
            image=image, threshold=0.5)
        a = []
        for box in raw_boxes:
            # Move box down.
            # diff_height_width = (box[3] - box[1]) - (box[2] - box[0])
            offset_y = int(abs((box[3] - box[1]) * 0.1))
            box_moved = self.move_box(box, [0, offset_y])

            # Make box square.
            facebox = self.get_square_box(box_moved)

            if self.box_in_image(facebox, image):
                a.append(facebox)

        return a

    def detect_marks(self, image_np):
        """Detect marks from image"""

        # # Actual detection.
        predictions = self.model.signatures["predict"](
            tf.constant(image_np, dtype=tf.uint8))

        # Convert predictions to landmarks.
        marks = np.array(predictions['output']).flatten()[:136]
        marks = np.reshape(marks, (-1, 2))

        return marks

    @staticmethod
    def draw_marks(image, marks, color=(255, 255, 255)):
        """Draw mark points on image"""
        for mark in marks:
            cv2.circle(image, (int(mark[0]), int(
                mark[1])), 2, color, -1, cv2.LINE_AA)


# Function to be called when looking upwards
def topSelect():
    pyautogui.moveTo(topScreenMiddle, duration=0)
    pyautogui.click()
    # print("Looking at screen 2")

# Function to be called when looking downwards
def bottomSelect():
    pyautogui.moveTo(bottomScreenMiddle, duration=0)
    pyautogui.click()
    # print("Looking at screen 1")

def rangeOF(a1, c1):
    calibrationStep = 6
    if (a1[0] > (c1[0]-calibrationStep)) and (a1[0] < (c1[0]+calibrationStep))\
            or (a1[1] > (c1[1] - calibrationStep)) and (a1[1] < (c1[1] + calibrationStep)):
        # if (a1[1] > (c1[1] - 1)) and (a1[1] < (c1[1] + 1)):
        return True

    # print("False")
    return False

mark_detector = MarkDetector()
cap = cv2.VideoCapture(0)
ret, img = cap.read()
size = img.shape
font = cv2.FONT_HERSHEY_SIMPLEX
# 3D model points.
model_points = np.array([
    (0.0, 0.0, 0.0),  # Nose tip
    (0.0, -330.0, -65.0),  # Chin
    (-225.0, 170.0, -135.0),  # Left eye left corner
    (225.0, 170.0, -135.0),  # Right eye right corne
    (-150.0, -150.0, -125.0),  # Left Mouth corner
    (150.0, -150.0, -125.0)  # Right mouth corner
])

# Camera internals
focal_length = size[1]
center = (size[1] / 2, size[0] / 2)
camera_matrix = np.array(
    [[focal_length, 0, center[0]],
     [0, focal_length, center[1]],
     [0, 0, 1]], dtype="double"
)


while True:
    ret, img = cap.read()
    if ret:
        faceboxes = mark_detector.extract_cnn_facebox(img)
        for facebox in faceboxes:
            face_img = img[facebox[1]: facebox[3],
                       facebox[0]: facebox[2]]
            face_img = cv2.resize(face_img, (128, 128))
            face_img = cv2.cvtColor(face_img, cv2.COLOR_BGR2RGB)
            marks = mark_detector.detect_marks([face_img])
            marks *= (facebox[2] - facebox[0])
            marks[:, 0] += facebox[0]
            marks[:, 1] += facebox[1]
            shape = marks.astype(np.uint)

            image_points = np.array([
                shape[30],  # Nose tip
                shape[8],  # Chin
                shape[36],  # Left eye left corner
                shape[45],  # Right eye right corner
                shape[48],  # Left Mouth corner
                shape[54]  # Right mouth corner
            ], dtype="double")

            p1 = (int(image_points[0][0]), int(image_points[0][1]))

            # begin calibration
            if startup:
                # Detect number of monitors & monitor details: returns a dictionary of monitors
                print("Position Collected")
                monitors = calibrateHead3.DetectMonitors().detect_monitors()
                calibratedPositions.append(calibrateHead3.run(p1, calibrationLoop, monitors))
                print("Move head")

                calibrationLoop = calibrationLoop+1

                # Exit calibration loop
                if len(monitors) == len(calibratedPositions):
                    print(calibratedPositions)
                    print("Exit calibration mode")
                    startup = False

            else:
                # print(ang1, ang2)

                # User is looking at screen 1
                if (rangeOF(p1, calibratedPositions[0][0])):
                    newDirection = 1
                    if lastDirection != newDirection:
                        # topSelect()
                        bottomSelect()


                # User is looking at screen 2
                elif (rangeOF(p1, calibratedPositions[1][0])):
                    # User is looking at screen 2
                    newDirection = -1
                    if lastDirection != newDirection:
                        # bottomSelect()
                        topSelect()

            lastDirection = newDirection

        # cv2.imshow('img', img)
        time.sleep(0.1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    else:
        time.sleep(0.1)
        break

cv2.destroyAllWindows()
cap.release()
