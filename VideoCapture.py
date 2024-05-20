import cv2
import time
import keyboard

last_print_time = time.time()

def process_image(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, (320, 320))
    image = cv2.GaussianBlur(image, (5, 5), 0)
    image = cv2.Canny(image, 120, 200)
    image = cv2.dilate(image, None, iterations=2)
    image = cv2.erode(image, None, iterations=2)

    _, thresh = cv2.threshold(image, 200, 255, cv2.THRESH_BINARY)

    # Count White Lines Of The Images
    contours, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # Filter out small contours and count the remaining ones
    lines = [c for c in contours if cv2.boundingRect(c)[3] > 15 and cv2.boundingRect(c)[3] < 40]
    number_of_lines = len(lines)

    # Draw the contours on the original image
    image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)

    cv2.drawContours(image, lines, -1, (0, 255, 0), 3)      # Draw the contours With The Green Color
    return image, number_of_lines, lines

# Create a VideoCapture object
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    processed_frame, number_of_lines, contours = process_image(frame)

    # Draw the contours on the original frame
    cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)

    # Display the resulting frame
    cv2.imshow('Original Frame', frame)

    # Print the number of lines every 5 seconds
    current_time = time.time()
    if current_time - last_print_time >= 5:
        print(f'Number of lines: {number_of_lines}')
        last_print_time = current_time

    # Break the loop on 'q' key press
    if cv2.waitKey(1) and (keyboard.is_pressed('q')):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()