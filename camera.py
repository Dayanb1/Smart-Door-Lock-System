#camera
import time
import picamera
import requests
from PIL import Image
import io
# Telegram bot API token
TOKEN = "7399602712:AAG3gZaeOvNcPiVI9ebsUWUNxzIvLRTwcrQ" # Chat ID of the recipient (your Telegram chat ID)
CHAT_ID = "1015944656" # Function to capture and compress the photo
def capture_photo():
with picamera.PiCamera() as camera:
# Set camera resolution
camera.resolution = (2592 , 1944)
# Create an in-memory stream for capturing the photo
stream = io.BytesIO()
# Capture the photo
camera.capture(stream, format='jpeg')
# Reset the stream position to the beginning
stream.seek(0)
# Open the image using PIL

image = Image.open(stream)
# Compress the image with JPEG format and quality of 80
compressed_stream = io.BytesIO()
image.save(compressed_stream, format='jpeg', quality=80)
# Reset the compressed stream position to the beginning
compressed_stream.seek(0)
return compressed_stream
# Function to send the photo to Telegram
def send_photo(photo):
url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto" # Create the HTTP request data
files = {"photo": photo}
data = {"chat_id": CHAT_ID}
# Send the request
response = requests.post(url, files=files, data=data)
# Check if the request was successful
if response.status_code == 200:
print("Photo sent successfully!")
else:
print("Failed to send photo.")
# Continuously capture and send photos
# Capture a photo
#photo_stream = capture_photo()
# Send the photo
#send_photo(photo_stream)
# Add a delay before capturing the next photo
#time.sleep(2) # Adjust the delay as needed

