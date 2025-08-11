import os
import sys
from pathlib import Path

# Add this script's directory to Python path so we can import the functions
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(script_dir)

# Import the analysis functions from naming-analysis.py
# Make sure naming-analysis.py is in the same directory as this script
from naming_analysis import analyze_image_structure, verify_image_completeness

# Define paths using Path for cross-platform compatibility
base_image_dir = r"C:\Users\SouayedBelkiss\OneDrive - gae\Desktop\Thesis\phase2_style_evaluation\images\all_images"
output_dir = r"C:\Users\SouayedBelkiss\OneDrive - gae\Desktop\Thesis\phase2_style_evaluation\analysis_results"

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Define expected datasets and styles
expected_datasets = [
    "wikipedia_wikipedia", 
    "asset_asset", 
    "onestopenglish_onestopenglish", 
    "simpa_simpa"
]

expected_styles = [
    "Cartoon",
    "Realistic",
    "Artistic",
    "Minimalistic",
    "Digital Art",
    "3D Rendered",
    "Geometric",
    "Retro",
    "Storybook",
    "Technical"
]

# Run analysis
print("Analyzing image structure...")
stats = analyze_image_structure(base_image_dir, output_dir)

print("\nVerifying image completeness...")
completeness = verify_image_completeness(base_image_dir, expected_datasets, expected_styles, output_dir)

# Print summary
print("\nAnalysis Summary:")
print(f"Total images found: {stats['total_images']}")
print(f"Images with standard naming: {stats['by_naming_pattern']['standard']}")
print(f"Images with non-standard naming: {stats['by_naming_pattern']['non_standard']}")
print("\nDataset distribution:")
for dataset, count in stats['datasets'].items():
    print(f"  - {dataset}: {count} images")

print("\nStyle distribution:")
for style, count in stats['styles'].items():
    print(f"  - {style}: {count} images")

print(f"\nCompleteness rate: {completeness['completeness_rate']:.2f}%")
print(f"Missing combinations: {len(completeness['missing_combinations'])}")
print(f"Extra combinations: {len(completeness['extra_combinations'])}")

print(f"\nResults saved to {output_dir}")