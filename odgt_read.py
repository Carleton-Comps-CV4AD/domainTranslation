import json
import os
import shutil

def read_odgt_file(odgt_file):
    """
    Reads the ODG file (line by line) and extracts image paths from each line.
    :param odgt_file: Path to the ODG file.
    :return: List of image paths.
    """
    image_paths = []
    with open(odgt_file, 'r') as file:
        for line in file:
            try:
                data = json.loads(line)  # Load the JSON object from each line
                image_paths.append(data['fpath_img'])  # Extract the image path
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
            except KeyError as e:
                print(f"KeyError: Missing expected key in JSON object: {e}")
    return image_paths

def get_unique_filename(destination_folder, filename):
    """
    Ensures the filename is unique in the destination folder by appending a counter if needed.
    :param destination_folder: The folder where the image will be copied.
    :param filename: The original filename.
    :return: A unique filename.
    """
    base, ext = os.path.splitext(filename)
    counter = 1
    new_filename = filename

    while os.path.exists(os.path.join(destination_folder, new_filename)):
        # If the file exists, add a counter to the filename
        new_filename = f"{base}_{counter}{ext}"
        counter += 1

    return new_filename

def copy_images_to_folder(image_paths, destination_folder):
    """
    Copies images from the provided paths to the destination folder, ensuring unique filenames.
    :param image_paths: List of image paths to copy.
    :param destination_folder: The folder to copy images into.
    """
    # Ensure destination folder exists
    os.makedirs(destination_folder, exist_ok=True)

    for img_path in image_paths:
        # Check if the image file exists
        if os.path.exists(img_path):
            # Get the filename from the full path
            filename = os.path.basename(img_path)
            
            # Get a unique filename if the file already exists
            unique_filename = get_unique_filename(destination_folder, filename)
            
            destination_path = os.path.join(destination_folder, unique_filename)
            
            # Copy the image to the new folder
            shutil.copy(img_path, destination_path)
            print(f"Copied: {img_path} to {destination_path}")
        else:
            print(f"Warning: File does not exist {img_path}")

def main():
    # Path to the ODG file
    odgt_file = '/Data/tangumaj/cv4ad_carla/Domain_Translation_Multi-weather_Restoration/foggy(test.odgt)'
    
    # Destination folder to store the images
    destination_folder = '/Data/tangumaj/cv4ad_carla/Domain_Translation_Multi-weather_Restoration/dataset'

    # Read the ODG file and get image paths
    image_paths = read_odgt_file(odgt_file)
    
    # Copy images to the specified folder
    copy_images_to_folder(image_paths, destination_folder)

if __name__ == "__main__":
    main()