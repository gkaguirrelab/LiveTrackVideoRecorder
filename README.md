# LiveTrackVideoRecorder
Python code that operates under Windows to record video input via ffmpeg commands

This python code starts a GUI program which interacts with ffmpeg and allows users to input recording parameters such as video name, save path, video length, video format, scale, and framerate easily. The browse button allows inputting json protocol files which can be used to auto assign some of the variables according to an MRI scan or experimental protocol. If a protocol file is selected, switch between the runs specified in the json file can be achieved with the right and left arrows. The length adapts automatically when another run is selected via the arrows.

# Equipment configuration

VIDEO

An IR camera (Cambridge systems) is connected to an MRI video filter. A BNC splitter splits the video feed that comes out of the filter into two and two different A/D converter receives the feed. One of these converters is used as a recording device while the other is used only to view the feed during recording.

AUDIO

TTL pulses that are received from the MRI scanner is converted to audio via a TTL-Audio box designed by UPenn Electronic Shop. Audio pulses are then transferred to the audio channel of the A/D converter.

# Software Requirements 
-ffmpeg 4.1.1 

-python 3 

-IP Camera Viewer - for viewing the feed with a different A/D 

-pyautogui package https://pypi.org/project/PyAutoGUI/  -  can be installed with: pip install pyautogui
