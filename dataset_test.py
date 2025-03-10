from os import listdir
from os.path import join
import cv2
import torch
import torch.utils.data as data
import torchvision.transforms as transforms

from utils import is_image_file

class DatasetFromFolder_Test(data.Dataset):
    def __init__(self, image_dir):
        super(DatasetFromFolder_Test, self).__init__()
        self.path = image_dir
        self.image_filenames = [x for x in listdir(self.path) if is_image_file(x)]
        print(self.path)
        print(self.image_filenames)

        transform_list = [transforms.ToTensor(),
                          transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))]
        self.transform = transforms.Compose(transform_list)

    def __getitem__(self, index):
        image_path = join(self.path, self.image_filenames[index])
        print(f"Loading image: {image_path}")
        
        # Attempt to load the image
        image = cv2.imread(image_path)
        
        # Check if the image was successfully loaded
        if image is None:
            error_msg = f"Error: Unable to read image at path: {image_path}"
            print(error_msg)
            # Option 1: Raise an error if you want to stop execution
            raise FileNotFoundError(error_msg)
            # Option 2: Return a placeholder image (e.g., a black image)
            # image = np.zeros((256, 256, 3), dtype=np.uint8)
        
        # Resize to 256x256 regardless of original size
        image_resized = cv2.resize(image, (256, 256), interpolation=cv2.INTER_AREA)
        image_tensor = self.transform(image_resized)
        return image_tensor, self.image_filenames[index]

    def __len__(self):
        return len(self.image_filenames)
