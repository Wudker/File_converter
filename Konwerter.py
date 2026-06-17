import os
import sys
import subprocess
def konvers():
    if len(sys.argv) != 3:
        print("[filename] .base_extention .target_extention \n [Example of usage]: Test .gif .png")
        sys.exit(1)

    folder_path = "YOUR_FOLDER_WITH FILE" #Converted file will be saved in the same place
    base = sys.argv[1]
    target = sys.argv[2]

    for filename in os.listdir(folder_path):
        if filename.endswith(base):
            input_file = os.path.join(folder_path, filename)
            output_file = os.path.join(folder_path, os.path.splitext(filename)[0] + target)

            subprocess.call(['ffmpeg', '-i', input_file, output_file])
    os.system("cls")
    print('Konvesion Succes!')
    
if __name__=="__main__":
  konvers()  

