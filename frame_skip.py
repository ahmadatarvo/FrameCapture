import cv2
import os
import glob

# Define the input and output directories
input_folder = 'input_videos'  # Replace with your folder containing video files
output_folder = 'output_images'

# Create the output directory if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Find all .ts files in the input directory
video_files = glob.glob(os.path.join(input_folder, '*.ts'))

# Initialize a global frame count for naming
frame_count = 1

# Loop through each video file and extract frames
for video_file in video_files:
    # Open the video file
    cap = cv2.VideoCapture(video_file)

    # Check if the video opened successfully
    if not cap.isOpened():
        print(f"Error: Could not open video {video_file}")
        continue

    frame_index = 1  # Tracks the index of the current frame in the video

    # Loop through the video frames
    while True:
        ret, frame = cap.read()
        
        # Break the loop if there are no frames left to read
        if not ret:
            break
        
        # Save every 5th frame
        if frame_index % 5 == 0:
            frame_filename = os.path.join(output_folder, f"frame_other_{frame_count}.jpg")
            cv2.imwrite(frame_filename, frame, [int(cv2.IMWRITE_JPEG_QUALITY), 90])  # 90 is the quality factor
            print(f"Saved {frame_filename}")
            frame_count += 1
        
        frame_index += 1

    # Release the video capture object
    cap.release()
    print(f"Frame extraction complete for {video_file}!")

print("All .mp4 files have been processed.")
