import os
from datetime import date
import time

today = date.today()
date_of_scan = today.strftime("%Y-%m-%d")

dog_id = input("Enter the dog id: ")
output_path = r'C:\Users\LDOG_experimenter\Desktop\emergency_rec'
if os.path.exists(output_path) == False:
       os.makedirs(output_path)
dog_id = r'C:\Users\LDOG_experimenter\Desktop\emergency_rec\%s\%s' % (dog_id, date_of_scan)
if os.path.exists(dog_id) == False:
       os.makedirs(dog_id)

for i in range(100):
       get_input_name = input("PupilPhoto emergency recorder\n1- pupil_LightFlux_1-6Hz_RightEyeStim_01\n2- pupil_RodMel_1-6Hz_RightEyeStim_02\n3- pupil_LplusS_1-6Hz_RightEyeStim_03\n4- pupil_LightFlux_1-6Hz_LeftEyeStim_04\n5- pupil_RodMel_1-6Hz_LeftEyeStim_05\n6- pupil_LplusS_1-6Hz_LeftEyeStim_06\n7- pupil_LightFlux_1-6Hz_RightEyeStim_07\n8- pupil_RodMel_1-6Hz_RightEyeStim_08\n9- pupil_LplusS_1-6Hz_RightEyeStim_09\n10- pupil_LightFlux_1-6Hz_LeftEyeStim_10\n11- pupil_RodMel_1-6Hz_LeftEyeStim_11\n12- pupil_LplusS_1-6Hz_LeftEyeStim_12\n13- pupil_LightFlux_1-6Hz_RightEyeStim_13\n14- pupil_RodMel_1-6Hz_RightEyeStim_14\n15- pupil_LplusS_1-6Hz_RightEyeStim_15\n16- pupil_LightFlux_1-6Hz_LeftEyeStim_16\n17- pupil_RodMel_1-6Hz_LeftEyeStim_17\n18- pupil_LplusS_1-6Hz_LeftEyeStim_18\n\nSelect the number corresponding to the acquisition. Enter break to stop the program:")
       print("selected %s" % get_input_name)

       if get_input_name == '1':
              saven = 'pupil_LightFlux_1-6Hz_RightEyeStim_01'
       elif get_input_name == '2':
              saven = 'pupil_RodMel_1-6Hz_RightEyeStim_02'
       elif get_input_name == '3':
              saven = 'pupil_LplusS_1-6Hz_RightEyeStim_03'
       elif get_input_name == '4':
              saven = 'pupil_LightFlux_1-6Hz_LeftEyeStim_04'
       elif get_input_name == '5':
              saven = 'pupil_RodMel_1-6Hz_LeftEyeStim_05'
       elif get_input_name == '6':
              saven = 'pupil_LplusS_1-6Hz_LeftEyeStim_06'
       elif get_input_name == '7':
              saven = 'pupil_LightFlux_1-6Hz_RightEyeStim_07'
       elif get_input_name == '8':
              saven = 'pupil_RodMel_1-6Hz_RightEyeStim_08'
       elif get_input_name == '9':
              saven = 'pupil_LplusS_1-6Hz_RightEyeStim_09'
       elif get_input_name == '10':
              saven = 'pupil_LightFlux_1-6Hz_LeftEyeStim_10'
       elif get_input_name == '11':
              saven = 'pupil_RodMel_1-6Hz_LeftEyeStim_11'
       elif get_input_name == '12':
              saven = 'pupil_LplusS_1-6Hz_LeftEyeStim_12'
       elif get_input_name == '13':
              saven = 'pupil_LightFlux_1-6Hz_RightEyeStim_13'
       elif get_input_name == '14':
              saven = 'pupil_RodMel_1-6Hz_RightEyeStim_14'
       elif get_input_name == '15':
              saven = 'pupil_LplusS_1-6Hz_RightEyeStim_15'
       elif get_input_name == '16':
              saven = 'pupil_LightFlux_1-6Hz_LeftEyeStim_16'
       elif get_input_name == '17':
              saven = 'pupil_RodMel_1-6Hz_LeftEyeStim_17'
       elif get_input_name == '18':
              saven = 'pupil_LplusS_1-6Hz_LeftEyeStim_18'
       elif get_input_name == 'break':
              print('Breaking the loop')
              break             
       else:
              print('That is an unrecognized number')

       output_path =  r'%s\%s.mov' % (dog_id,saven)
       cmd = 'ffmpeg -f dshow -rtbufsize 1500M -i video="Decklink Video Capture":audio="Decklink Audio Capture" -c:v mjpeg -q:v 0 -y -vf scale=640x780 -r 29.97 -t 00:06:00 %s' % output_path
       os.system(cmd)
