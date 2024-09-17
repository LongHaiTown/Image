import matplotlib.pyplot as plt
import cv2

# Read the image in color mode
image = cv2.imread('img/CornerLine.jpg')

# Split the image into its color channels
b, g, r = cv2.split(image)

# Merge the channels back together in BGR order
imgMerged = cv2.merge((b, g, r))

# Plot the individual channels and the merged image
plt.figure(figsize=(12, 6))
plt.subplot(141); plt.imshow(b, cmap='Blues'); plt.title("Blue channel")
plt.subplot(142); plt.imshow(g, cmap=None); plt.title("Green channel")
plt.subplot(143); plt.imshow(r, cmap=None); plt.title("Red channel")

# Convert the BGR image to RGB for correct color display
imgMerged_rgb = cv2.cvtColor(imgMerged, cv2.COLOR_BGR2RGB)
plt.subplot(144); plt.imshow(imgMerged_rgb); plt.title("Merged Output")

plt.show()
