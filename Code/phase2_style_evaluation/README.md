# Phase 2: Style Evaluation

This phase focuses on evaluating different visual styles using the winning "Basic Object Focus" template from Phase 1.

## Directory Structure
```
phase2_style_evaluation/
├── code/
│   ├── p2_prompt_generator.py      # Generates prompts for different styles
│   ├── p2_image_generator.py       # Generates images with style variations
│   └── p2_clip_evaluator.py        # Evaluates style performance
├── output_files/
│   ├── generated_prompts_p2.json   # Generated prompts for each style
│   └── clip_analysis_p2/           # Style evaluation results
└── images/
    ├── by_style/                   # Images organized by style
    └── by_dataset/                 # Images organized by dataset
```

## Styles Being Evaluated
1. Cartoon
2. Realistic
3. Artistic
4. Minimalistic
5. Digital Art
6. 3D Rendered
7. Geometric
8. Retro
9. Storybook
10. Technical

## Methodology
- Uses winning "Basic Object Focus" template from Phase 1
- Samples 400 texts (100 from each dataset)
- Generates 10 style variations per sample
- Total planned images: 4000 (400 × 10 styles)
- CLIP score target: 0.23 or better

## Analysis Goals
1. Per-style CLIP scores
2. Per-dataset performance
3. Style rankings
4. Analysis visualizations:
   - 4 histograms (one per dataset)
   - 5 histograms per dataset showing style distribution

## Image Labeling
Each generated image includes:
- Template name
- Style name
- Image index
- Dataset identifier

## Dataset Distribution
Random sampling of 100 entries from each source:
- Wikipedia simplified articles
- ASSET dataset
- OneStop English
- SIMPA corpus