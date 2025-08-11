# Image Annotation Study: Stylistic Variation Recognition

## Project Overview

This project involves setting up an image annotation study with 4 expert annotators. The dataset consists of 2000 images generated from 200 simplified sentences with 10 different styles for each sentence. The study aims to evaluate Inter-Annotator Agreement (IAA) by having all experts annotate the same core set of 200 images, plus additional unique images per expert.

## Directory Structure

phase3_label_studio/
├── all_images/                  # Original image collection (3935 images)
├── 2000_set_shuffled/           # Selected 2000 images maintaining 10 styles per base image
├── 2000_set_renamed/            # Images with simplified names (just sequence numbers)
├── IAA_set/                     # 200 selected images for IAA evaluation
├── Expert_distribution/         # Individual folders for each expert
│   ├── Martin Kappus/
│   │   ├── IAA_set/             # The 200 core images for IAA
│   │   └── unique_set/          # Martin's 450 unique images
│   ├── Luisa Carrer/
│   │   ├── IAA_set/             # The 200 core images for IAA
│   │   └── unique_set/          # Luisa's 450 unique images
│   ├── Katrin Andermatt/
│   │   ├── IAA_set/             # The 200 core images for IAA
│   │   └── unique_set/          # Katrin's 450 unique images
│   └── Alexa Lintner/
│       ├── IAA_set/             # The 200 core images for IAA
│       └── unique_set/          # Alexa's 450 unique images
└── code/                        # Scripts and mapping files
├── renamed_images_mapping.csv  # Mapping between simplified and original filenames
└── expert_distribution_mapping.csv  # Mapping with IAA and expert assignments



## Process Steps

### Step 1: Initial Dataset Analysis

- Started with 3935 images in the original dataset
- Each image filename follows the pattern: `####_dataset_dataset_ID_style.png`
- Confirmed 4 datasets and 10 styles per base image

### Step 2: Creating the 2000-Image Set

- Selected 200 base images that had all 10 style variations (total 2000 images)
- Created a new folder "2000_set_shuffled" containing these images
- Created a mapping file to track the selected images

### Step 3: Simplifying Filenames

- Renamed all images to use just their sequential numbers
- Created a mapping file to track the relationship between:
  - New filenames (e.g., "0001.png")
  - Original filenames (e.g., "0001_simpa_simpa_173_artistic.png")
  - Dataset, prompt ID, and style information
- Stored these simplified images in "2000_set_renamed"

### Step 4: Creating IAA Image Set

- Selected 20 base images (200 images total) for Inter-Annotator Agreement (IAA) evaluation
- Added "_IAA" suffix to these images to clearly identify them (e.g., "0001_IAA.png")
- Moved these to a dedicated "IAA_set" folder

### Step 5: Distributing Images to Experts

- Created 4 expert folders, each with two subfolders:
  - IAA_set: Contains copies of all 200 IAA images (same for all experts)
  - unique_set: Contains 450 unique images assigned only to that expert
- Distributed the remaining 180 base images (1800 images) among 4 experts (45 base images = 450 images per expert)
- Verified that no expert shares unique images with any other expert

## Annotation Task Details

For the annotation study, each expert will:
1. Evaluate all 200 core IAA images
2. Evaluate their assigned 450 unique images
3. Identify which style best matches each image (without knowing the actual style)
4. Provide other annotations as specified in the study guidelines

## Analysis Plan

After collecting annotations, the mapping files will be used to:
1. Measure Inter-Annotator Agreement on the core images
2. Analyze style recognition accuracy
3. Evaluate consistency across datasets and styles
4. Generate comprehensive statistics on annotation quality

## Notes

- All image filenames visible to annotators have been anonymized to remove style information
- The mapping files should be kept private (not shared with annotators)
- The original image naming pattern was: dataset_dataset_ID_style.png