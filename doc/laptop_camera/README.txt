
Using the Laptop's Camera
=========================

Command Line
------------
Reference: https://askubuntu.com/questions/106770/take-a-picture-from-terminal#

Installation:
apt-get install fswebcam
apt-get install streamer

Sample Commands:
- Puts it in current directory

fswebcam -r 640x480 --jpeg 95 -D 3 web-cam-shot.jpg
fswebcam -r 640x480 --jpeg 85 -D 1 web-cam-shot.jpg

streamer -h                     # -s and ".jpg" do not seem to work
streamer -f jpeg -o image.jpeg


