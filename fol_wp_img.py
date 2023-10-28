import pywhatkit as pw
from datetime import datetime, timedelta
import os
import time


def get_image_file_names(folder_path):
    image_files = [
        f
        for f in os.listdir(folder_path)
        if f.lower().endswith((".jpg", ".jpeg", ".png", ".gif"))
    ]
    return image_files


directory_path = r"D:\sample proj\wp\image_folder"
folder_names = [
    folder
    for folder in os.listdir(directory_path)
    if os.path.isdir(os.path.join(directory_path, folder))
]

for folder in folder_names:
    MobilenNo = "+91 " + folder
    folder_path = directory_path + "/" + folder
    image_names = get_image_file_names(folder_path)
    count = 1

    # Get the current date and time
    current_time = datetime.now()

    # Extract hours and minutes
    current_hour = current_time.hour
    current_minute = current_time.minute

    # Add one minute
    new_time = current_time + timedelta(minutes=1)

    # Extract the updated hours and minutes
    hour = new_time.hour
    minute = new_time.minute

    pw.sendwhatmsg(MobilenNo, "               ", hour, minute, 15)
    for names in image_names:
        image_path = folder_path + "\\" + names
        try:
            pw.sendwhats_image(MobilenNo, image_path, str(count))
            print("Image sent successfully!")
        except Exception as e:
            print(f"An error occurred while sending the image: {str(e)}")
        count += 1
        time.sleep(10)

    # Get the current date and time
    current_time = datetime.now()

    # Extract hours and minutes
    current_hour = current_time.hour
    current_minute = current_time.minute

    # Add one minute
    new_time = current_time + timedelta(minutes=1)

    # Extract the updated hours and minutes
    hour = new_time.hour
    minute = new_time.minute

    pw.sendwhatmsg(
        MobilenNo,
        "Images are send by AI powered bot...\n Enjoy your clicks",
        hour,
        minute,
        15,
    )
