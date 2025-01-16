### Image Processing with OpenCV

#### Requirements
Ensure you have the following libraries installed:
- OpenCV
- NumPy

To install them, use:
```bash
pip install opencv-python numpy
```

#### How to Run the Script
1. Save the `ImageProcessing.py` script in your working directory.
2. Ensure the `Resources` folder contains the input image (e.g., `lords.png`).
3. Open a terminal or command prompt and navigate to the script's directory.
4. Run the script using:
```bash
python ImageProcessing.py
```
5. The following actions will occur:
   - The original and grayscale images will be displayed in separate windows.
   - The processed grayscale image will be saved in the `Resources` folder as `GreyLords.png`.

#### Notes
- Ensure the `Resources` folder is in the same directory as the script.
- Images will close automatically after 5 seconds.

---

### Video Capture with OpenCV

#### Requirements
Ensure you have the following libraries installed:
- OpenCV

To install it, use:
```bash
pip install opencv-python
```

#### How to Run the Script
1. Save the `VideoCapture.py` script in your working directory.
2. Ensure the `Resources` folder contains the input video file (e.g., `Rohit_Pull.mp4`).
3. Open a terminal or command prompt and navigate to the script's directory.
4. Run the script using:
```bash
python VideoCapture.py
```
5. The following actions will occur:
   - The grayscale version of the video will be displayed in a window.
   - The processed video will be saved in the `Resources` folder as `Rohit_Pull_Grey.mp4` (if `VideoWriter` works).

#### Exit
Press the 'q' key to exit the program.

#### Notes
- Ensure the `Resources` folder is in the same directory as the script.
- If `VideoWriter` doesn't work on your device, the video will not be saved.

---

### Hand Detection with MediaPipe

#### Requirements
Ensure you have the following libraries installed:
- OpenCV
- MediaPipe
- NumPy

To install them, use:
```bash
pip install opencv-python mediapipe numpy
```

#### How to Run the Script
1. Save the `HandDetection.py` script in your working directory.
2. Connect your webcam to your computer.
3. Open a terminal or command prompt and navigate to the script's directory.
4. Run the script using:
```bash
python HandDetection.py
```
5. A window will open displaying the video feed with hand detection.
   - A red circle will be drawn on the index finger tip.
   - The terminal will print "Pinching" if the thumb and index finger tips are less than 40 pixels apart, otherwise "Not Pinching".

#### Exit
Press the 'q' key to exit the program.

#### Notes
- Ensure the webcam has proper lighting for accurate hand detection.
- The script processes only one hand at a time.
