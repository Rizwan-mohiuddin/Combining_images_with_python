import cv2

def combine_and_resize_images(image1_path, image2_path, target_size):
    # Read the images
    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)

    # Resize both images to the target size
    image1_resized = cv2.resize(image1, target_size)
    image2_resized = cv2.resize(image2, target_size)

    # Combine the images horizontally (side by side)
    combined_image = cv2.hconcat([image1_resized, image2_resized])

    return combined_image

# Example usage
image1_path = "man.jpg"
image2_path = "stw.jpg"
target_size = (200, 200)
combined_image = combine_and_resize_images(image1_path, image2_path, target_size)

# Display the combined and resized image
cv2.imshow("Combined and Resized Image", combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
