import sys
import numpy as np
import cv2
from PIL import Image, ImageFilter, ImageDraw
from rembg import remove, new_session

def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/prep_photo.py <photo.jpg>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = "data/source-prepped.png"

    session = new_session("isnet-general-use")
    img = Image.open(input_path).convert("RGBA")
    img_no_bg = remove(img, session=session)

    rgba = np.array(img_no_bg)

    alpha = rgba[:, :, 3]
    alpha = cv2.GaussianBlur(alpha, (7, 7), 0)
    rgba[:, :, 3] = alpha

    bgr = cv2.cvtColor(rgba, cv2.COLOR_RGBA2BGR)
    lab = cv2.cvtColor(bgr, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=4.0, tileGridSize=(8, 8))
    l = clahe.apply(l)
    lab = cv2.merge([l, a, b])
    bgr_clahe = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

    alpha_f = rgba[:, :, 3].astype(np.float32) / 255.0
    white = np.full_like(bgr_clahe, 255, dtype=np.uint8)
    for i in range(3):
        white[:, :, i] = (bgr_clahe[:, :, i] * alpha_f + white[:, :, i] * (1 - alpha_f)).astype(np.uint8)

    gray = cv2.cvtColor(white, cv2.COLOR_BGR2GRAY)

    # NO vignette — rembg already isolates the subject
    gray = cv2.convertScaleAbs(gray, alpha=1.4, beta=-20)

    cv2.imwrite(output_path, gray)
    print(f"Saved: {output_path}")

if __name__ == "__main__":
    main()
