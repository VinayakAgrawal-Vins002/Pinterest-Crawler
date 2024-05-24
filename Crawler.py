## Imports
import os
import time
import shutil
import subprocess


# Fixed Variables
source_folder = "io\\output" # Create an Empty Directory till output
crawler = "pinterest-crawler --keywords "
base_path = "C:\\03_VS Code Files\\AutoWallpaper\\" # Replace with Your Base Folder

## Editable Lists
Titles = ["Art landscape", "Animated Night", "HD Animated", "Cityscape", "Dream Animated", "Vibrant Animated", "Dreamy art", "RoomScapes", "Fantasy Landscapes", "Animated Landscapes"]
Folders = ["LandScape", "NightScape", "HD", "CityScape", "DreamScape", "VibrantScape", "DreamArt", "RoomScape", "FantasyScapes", "AnimatedScapes"]
''' 
Replace the Above List Elements with your Pinterest Search Strings in the Titles List & Their Respective Folder Names in Folders.
Best to Keep the Strings of Maximum  2 Words for Best Search Results.
Remember [len(Titles) == len(Folders)] 

'''

## Destination folders [Replace with your Respective Destination Folder Path To Store The Images]
destination_folders = "Wallpapers\\"  
source = base_path+source_folder
counts = 100 # No of Images To Download per Search (Approx)
index = -1


## Function To Move Files To an Organized Location
def move_files(source_folder, destination_folder):
    
    # Ensure the destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Iterate over all files in the source folder
    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)

        # Check if it's a file (not a directory)
        if os.path.isfile(source_path):
            shutil.move(source_path, destination_path)
    

## Looping For Downloads
for title in Titles:
    
    index = index + 1
    command = crawler + title
    dest = destination_folders+Folders[index]

    # Start the command in a subprocess
    process = subprocess.Popen(command, shell=True)

    # Looping For Individual Search Downloads
    try:
        while True:
            # Count the number of images in the folder
            image_count = len([name for name in os.listdir(source) if os.path.isfile(os.path.join(source, name))])
            
            # Check if the number of images has reached req count
            if image_count >= counts:
                
                # Stop the subprocess
                process.terminate()
                process.wait()
                break
            
            # Wait for a short period before checking again
            time.sleep(3)

    except Exception as e:
        print("Encountered Error: Stopping Downloads")
        print(e)

    # Ensure the subprocess is terminated if it's still running
    finally:
        if process.poll() is None:
            process.terminate()
            process.wait()
        
        print("Downloaded: " + str(len([name for name in os.listdir(source)])) + " For '" + title + "' :")
            
        # Move Files
        try:
            move_files(source, dest)
        
        except Exception as e:
            print("Encountered Error: Moving Files")
            print(e)
        
        print("Moved Files: " + str(len([name for name in os.listdir(dest) if os.path.isfile(os.path.join(dest, name))])) + " For '" + title + "' :")
        
