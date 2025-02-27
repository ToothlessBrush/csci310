# Authors: Group 11 (Thomas Herold, John Klein, Logan Oslund)
# File: merger.py

import os # Provides functions for filesystem interaction
import glob # Helps find files

def merge_files_by_category(base_dir): # Merge files by category to get an ouput of {category}.txt
    categories = ["backward", "forward", "land", "left", "right", "takeoff"] # Define categories
    
    for category in categories: # Process each category
        category_path = os.path.join(base_dir, category)
        if not os.path.isdir(category_path): # Check to see if directory exists (error checking)
            print(f"Skipping {category_path}, directory not found.")
            continue
        
        print(f"Processing category: {category}") # Display processing message for readability
        output_file = os.path.join(base_dir, f"{category}.txt") # Builds the corresponding path
        
        with open(output_file, "a", encoding="utf-8") as outfile: # Open the output file in append mode ("a")
                                                                  # Append mode prevents overwriting existing data
            # Find all subdirectories in the category folder
            subdirs = [d for d in os.listdir(category_path) if os.path.isdir(os.path.join(category_path, d))]
            
            for subdir in sorted(subdirs):  # Sort for chronological order
                subdir_path = os.path.join(category_path, subdir) # Construct full path for the subdirectory
                
                # Get all .txt files in the subdirectory
                txt_files = sorted(glob.glob(os.path.join(subdir_path, "*.txt"))) # glob.glob() finds all txt files
                
                for txt_file in txt_files: # Iteration
                    print(f"Merging: {txt_file} into {output_file}") # Display merging message to show progress
                    
                    # Open and read ("r") each file, then append it to the output file
                    with open(txt_file, "r", encoding="utf-8") as infile:
                        outfile.write(infile.read()) # Write to corresponding output file
                        outfile.write("\n")  # Newline between merged files
    
    print("Merging completed for all categories!") # Final print message to show program termination

if __name__ == "__main__":
    base_directory = "data" # Defines directory name
    merge_files_by_category(base_directory) # Call function with base directory
