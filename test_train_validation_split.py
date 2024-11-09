import os
import shutil
import random

# Define the base directory and target folders
base_dir = 'archive'
categories = ['Dolphin', 'Fish', 'Jelly_Fish', 'Turtle_Tortoise', 'Whale']
split_ratios = {'Train': 0.7, 'Validation': 0.15, 'Test': 0.15}

# Create Train, Validation, and Test directories
for split in split_ratios:
    for category in categories:
        os.makedirs(os.path.join(base_dir, split, category), exist_ok=True)

# Function to split images into Train, Validation, and Test
def split_images():
    for category in categories:
        # Define source directory
        src_dir = os.path.join(base_dir, category)
        
        # Get all image files in the source directory
        images = [img for img in os.listdir(src_dir) if os.path.isfile(os.path.join(src_dir, img))]
        
        # Shuffle images for randomness
        random.shuffle(images)
        
        # Calculate split indices
        train_count = int(len(images) * split_ratios['Train'])
        val_count = int(len(images) * split_ratios['Validation'])
        
        # Split images based on the calculated indices
        train_images = images[:train_count]
        val_images = images[train_count:train_count + val_count]
        test_images = images[train_count + val_count:]
        
        # Move images to the respective directories
        for img in train_images:
            shutil.move(os.path.join(src_dir, img), os.path.join(base_dir, 'Train', category, img))
        for img in val_images:
            shutil.move(os.path.join(src_dir, img), os.path.join(base_dir, 'Validation', category, img))
        for img in test_images:
            shutil.move(os.path.join(src_dir, img), os.path.join(base_dir, 'Test', category, img))

# Run the function to split images
split_images()
print("Images have been successfully split into Train, Validation, and Test folders.")
