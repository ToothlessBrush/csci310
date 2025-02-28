# Authors: Group 11 (Thomas Herold, John Klein, Logan Oslund)
# File: merger.py

import os # Provides functions for filesystem interaction
import glob # Helps find files

def merge_files_by_category(base_dir): # Merge files by category to get an output of {category}.txt
    categories = ["backward", "forward", "land", "left", "right", "takeoff"] # Define categories
    
    for category in categories: # Process each category
        category_path = os.path.join(base_dir, category)
        if not os.path.isdir(category_path): # Check to see if directory exists (error checking)
            print(f"Skipping {category_path}, directory not found.")
            continue
        
        print(f"Processing category: {category}") # Display processing message for readability
        output_file = os.path.join(category_path, f"{category}.txt") # Builds the corresponding path inside each category directory
        
        with open(output_file, "a", encoding="utf-8") as outfile: # Open the output file in append mode ("a")
                                                                  # Append mode prevents overwriting existing data
            # Get a list of all subdirectories inside the category folder
            subdirs = [d for d in os.listdir(category_path) if os.path.isdir(os.path.join(category_path, d))]
            
            for subdir in sorted(subdirs):  # Sort for chronological order
                subdir_path = os.path.join(category_path, subdir) # Construct full path for the subdirectory
                
                # Get all .txt, .cw, and .csw files in the subdirectory; sort further
                data_files = sorted(glob.glob(os.path.join(subdir_path, "*.txt")) +
                                   glob.glob(os.path.join(subdir_path, "*.cw")) + # Unique cases since there is only
                                   glob.glob(os.path.join(subdir_path, "*.csw"))) # one .cw file and one .csw file
                
                for data_file in data_files: # Iteration
                    print(f"Merging: {data_file} into {output_file}") # Display merging message to show progress
                    
                    # Open and read ("r") each file, then append it to the output file
                    with open(data_file, "r", encoding="utf-8") as infile: # Encode in utf-8 (likely not needed)
                        outfile.write(infile.read()) # Write to corresponding output file
                        outfile.write("\n")  # Newline between merged files
    
                # Remove processed data files after merging
                for data_file in data_files:
                    os.remove(data_file) # Remove the file
                
                # Remove subdirectory if it is empty after file deletion
                if not os.listdir(subdir_path):
                    os.rmdir(subdir_path) # Remove the directory
    
    print("Merging completed for all categories!") # Final print message to show program termination

if __name__ == "__main__":
    base_directory = "data" # Defines directory name
    merge_files_by_category(base_directory) # Call function with base directory
