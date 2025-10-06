# Belkiss Souayed - Master's Thesis

## Overview
This repository contains the code and analysis for Belkiss Souayed's Master's thesis research conducted at the University of Zurich (UZH). The project develops a framework for generating accessible images from simplified text using structured prompt templates, specifically designed to help users with cognitive disabilities and learning difficulties through cognitively accessible AI-generated visual content.

## Repository Structure

```
Belkiss_ThesisFiles/
├── Code/
│   ├── annotation_analysis/          # Analysis of annotation data and inter-annotator agreement
│   │   ├── 100 score analysis/
│   │   ├── IAA/                     # Inter-Annotator Agreement calculations
│   │   ├── Style Recognition/
│   │   ├── best dataset and style/
│   │   ├── correlation study/
│   │   └── qualitative study/
│   ├── intermediate_exploration/     # Exploratory analysis and experiments
│   ├── phase1_template_selection/    # Phase 1: Template selection methodology
│   ├── phase2_style_evaluation/      # Phase 2: Style evaluation framework
│   └── phase3_label_studio/         # Phase 3: Label Studio annotation setup
└── required files/                  # Essential datasets and configuration files
    ├── complete_dataset_400.json
    ├── expert_distribution_mapping.csv
    ├── refined_prompts.json
    └── renamed_images_mapping.csv
```

## Data Availability
### Annotation Data and Images
Due to file size limitations, the annotation data and generated images are hosted on **SwissUbase**:

- **Annotation Data**: Contains individual annotator files.  
- **Generated Images**: Complete dataset of the generated images used in the study.  
- **Access**: [SwissUbase Dataset Link](https://www.swissubase.ch/en/share/eCTXtvik5Lr96iLcAk0nfnfSheu-QlACjK6TT-jZ6Q8c_ZOYu3VZfDaVF1AW9jsRRL8)



## Research Overview

### Dataset and Corpus
The research utilizes four established text simplification datasets:
- **OneStopEnglish**: News articles at different reading levels
- **SimPA**: Simplified text corpus  
- **Wikipedia**: Encyclopedic content simplification
- **ASSET**: Sentence-level text simplification

These datasets were combined to create a balanced corpus of **400 sentence pairs** covering news, web, and encyclopedic domains.

### Prompt Templates
Five structured prompt templates were developed, each following different layout logic based on cognitive accessibility principles:

1. **Basic Object Focus**: Simple, object-centered visual representations
2. **Contextual Scene**: Scene-based imagery with environmental context  
3. **Educational Layout**: Structured layouts optimized for learning
4. **Multi-Level Detail**: Hierarchical visual information presentation
5. **Grid Layout**: Organized grid-based visual arrangements

### Evaluation Methodology
- **Automatic metrics**: CLIP similarity scores for semantic alignment
- **Expert annotations**: Multi-dimensional human evaluation across accessibility criteria
- **Style analysis**: Assessment of visual styles impact on accessibility and clarity

## Research Phases

### Phase 1: Template Selection and Development
- **Objective**: Develop and select optimal prompt templates for accessibility-focused image generation
- **Key Files**: 
  - `phase1_template_selection/prompt_generator_p1.ipynb`
  - `phase1_template_selection/image_generator_p1.ipynb`
  - `phase1_template_selection/clip_evaluator_p1.ipynb`

### Phase 2: Style Evaluation and Testing
- **Objective**: Evaluate different visual styles across the five prompt templates for accessibility impact
- **Key Files**:
  - `phase2_style_evaluation/code/image_generator_p2.ipynb`
  - `phase2_style_evaluation/code/clip_evaluator_p2.ipynb`
  - `phase2_style_evaluation/code/p2_prompt_generator.ipynb`

### Phase 3: Human Annotation and Validation
- **Objective**: Conduct expert evaluation of generated images across multiple accessibility dimensions
- **Key Files**:
  - `phase3_label_studio/image_processing.ipynb`
  - `annotation_analysis/` (complete analysis suite)


## Citation

```bibtex
@mastersthesis{souayed2025thesis,
  title={Template-Based Text-to-Image Alignment for Language Accessibility: A Study on Visualizing Simplified Text},
  author={Souayed, Belkiss},
  year={2025},
  school={University of Zurich},
  type={Master's thesis}
}
```
## Data License and Source Acknowledgments

This dataset was developed as part of a research study exploring the alignment between simplified text and accessible image generation.  
The simplified sentences were sampled from four publicly available text simplification datasets:  
**ASSET**, **OneStopEnglish**, **SimPA**, and **Wikipedia**.

Only sentence sampling and minimal preprocessing (removal of artifacts, special characters, and formatting inconsistencies) were performed.  
No semantic modifications were made to the original texts.

The dataset also includes automatically generated text-to-image prompts for each sentence.  
No original datasets are redistributed in full.

---

## 📚 Source Datasets and Licenses

| Dataset | License | Link |
|----------|----------|------|
| **ASSET** | Creative Commons Attribution–NonCommercial 4.0 International (CC BY-NC 4.0) | [https://github.com/facebookresearch/asset/blob/main/LICENSE](https://github.com/facebookresearch/asset/blob/main/LICENSE) |
| **OneStopEnglish** | Creative Commons Attribution–ShareAlike 4.0 International (CC BY-SA 4.0) | [https://creativecommons.org/licenses/](https://creativecommons.org/licenses/) |
| **SimPA** | Freely available under a Creative Commons Licence (*SimPA: A Simplification Corpus for Arabic, English and Spanish*, LREC 2018) | [https://aclanthology.org/L18-1685/](https://aclanthology.org/L18-1685/) |
| **Wikipedia** | Creative Commons Attribution 4.0 International (CC BY 4.0) | [https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/) |

All listed licenses permit academic reuse with proper attribution.

## Contact

Belkiss Souayed
Email: [belkiss.souayed@uzh.ch]  
Institution: University of Zurich (UZH)  
Supervisor: Dr. Yingqiang Gao
Examiner: Prof. Dr. Sarah Ebling
---

*This research was conducted as part of a Master's thesis at the University of Zurich (UZH). For questions about data access or collaboration, please contact the author.*
