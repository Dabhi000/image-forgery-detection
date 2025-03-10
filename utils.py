import cv2
import numpy as np
from sklearn.cluster import KMeans

def detect_forgery(image_path):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        return False, "Invalid image"

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect edges (for tampering detection)
    edges = cv2.Canny(gray, 100, 200)

    # Analyze edges for tampering
    edge_pixels = np.sum(edges) / 255  # Count edge pixels
    total_pixels = edges.size
    edge_ratio = edge_pixels / total_pixels

    # Simple threshold-based forgery detection
    if edge_ratio > 0.05:  # Adjust threshold as needed
        return True, "Image may be forged (high edge density)"
    else:
        return False, "Image appears authentic"