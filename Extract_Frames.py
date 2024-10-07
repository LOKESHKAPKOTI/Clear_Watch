import cv2
import os

def extract_frames(video_path, output_folder):
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Save frames as images
        frame_filename = os.path.join(output_folder, f"{video_name}_frame_{frame_count:04d}.jpg")
        cv2.imwrite(frame_filename, frame)
        frame_count += 1

    cap.release()

# Example usage
video_folder = 'Resized_Videos'
output_frame_folder = 'Extracted_Frames'
os.makedirs(output_frame_folder, exist_ok=True)

# video_path = 'Resized_Videos/RoadAccidents004_x264.mp4'
# extract_frames(video_path, output_frame_folder)

for video_file in os.listdir(video_folder):
    video_path = os.path.join(video_folder, video_file)
    extract_frames(video_path, output_frame_folder)
