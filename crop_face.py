import cv2
import os
import numpy as np


def crop_face(image, cascade_path):
    cascade = cv2.CascadeClassifier(cascade_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    for s in np.arange(1. + 0.01, 2., 0.01):
        for n in range(5, 1, -1):
            faces = cascade.detectMultiScale(gray,
                                             scaleFactor=s,
                                             minNeighbors=n,
                                             minSize=(200, 200))
            if len(faces) == 0:
                continue
            else:
                if not len(faces) == 1:
                    faces = sorted(faces, key=lambda z: z[2] * z[3])
                    faces.reverse()
                x, y, w, h = faces[0]
                roi = image[y: y + h, x: x + w]
                return roi
    return None


def main():
    cascade = "lbpcascade_animeface.xml"
    root = "./cinderella/cards/"
    dst_root = "./cinderella/faces/"
    idols = os.listdir(root)
    src_dirs = [os.path.join(root, name) for name in idols]
    dst_dirs = [os.path.join(dst_root, name) for name in idols]

    for i in range(len(idols)):
        os.makedirs(dst_dirs[i], exist_ok=True)
        print("processing ", idols[i], "...")
        for index in range(len(os.listdir(src_dirs[i]))):
            src_path = os.path.join(src_dirs[i], "{}.jpg".format(index))
            dst_path = os.path.join(dst_dirs[i], "{}.jpg".format(index))
            image = cv2.imread(src_path)
            roi = crop_face(image, cascade)

            if roi is not None:
                cv2.imwrite(dst_path, roi)


if __name__ == "__main__":
    main()