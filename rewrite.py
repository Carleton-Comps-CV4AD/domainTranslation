#This code is primarily used to rewriet items in the .odgt files, feel free to ignore

import os

# Set the directory where the files are located
directory = "/Data/tangumaj/cv4ad_carla/Domain_Translation_Multi-weather_Restoration/dataset"

# Iterate over all files in the directory
for filename in os.listdir(directory):
    if "_" in filename:  # Only process files containing "_"
        new_filename = filename.replace("_", "-0")  # Replace underscores with hyphens
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_filename)
        
        # Rename the file
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} -> {new_filename}")

print("Renaming complete.")
