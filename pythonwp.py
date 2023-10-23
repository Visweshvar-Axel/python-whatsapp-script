"""
import pywhatkit as pw
from datetime import datetime, timedelta
import time

MobilenNo = "+91 77081 96973"

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
print("Current time (24-hour format):", current_time)

try:
    pw.sendwhatmsg(
        MobilenNo, "hey bro... \n message send by python ;)", hour, minute, 15
    )
except Exception as e:
    print(f"An error occurred while sending the image: {str(e)}")


# Define the path to the image you want to send
image_path = r"my pic.jpeg"

# Define the caption for the image
caption = "image by Python 'GOW' test1"

try:
    pw.sendwhats_image(MobilenNo, image_path, caption)
    print("Image sent successfully!")
except Exception as e:
    print(f"An error occurred while sending the image: {str(e)}")
"""

import pywhatkit as pw
from datetime import datetime, timedelta

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
MobilenNo = "+91 7339429677"

# pw.sendwhatmsg(
#     "+91 77081 96973", "hey bro...  \nmsg send by python ;)", hour, minute, 15
# )

pw.sendwhatmsg("+91 77081 96973", "               ", hour, minute, 15)

# Define the path to the image you want to send
image_path = r"D:\sample proj\wp\gow.png"

# Define the caption for the image
caption = "image by Python 'GOW' test1"

try:
    pw.sendwhats_image("+91 77081 96973", image_path, caption)
    print("Image sent successfully!")
except Exception as e:
    print(f"An error occurred while sending the image: {str(e)}")
