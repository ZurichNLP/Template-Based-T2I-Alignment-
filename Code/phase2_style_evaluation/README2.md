# Image Generation Script for Multi-Style Dataset

## Overview
This script generates images using DALL-E 3 for a dataset of text samples, with each sample being rendered in 10 different artistic styles. The script includes robust error handling, progress tracking, and the ability to pause and resume generation.

## Prerequisites
- Python 3.8+
- OpenAI API key
- Required Python packages:
  ```
  openai
  aiohttp
  rich
  ```

## Directory Structure
```
phase2_style_evaluation/
├── code/
│   ├── image_generator_p2.ipynb
│   ├── refined_prompts_400.json
│   └── generation_state.json
└── images/
    ├── by_style/
    │   ├── cartoon/
    │   ├── realistic/
    │   ├── artistic/
    │   └── ...
    └── by_dataset/
        ├── wikipedia/
        ├── asset/
        ├── simpa/
        └── onestop/
```

## File Naming Convention
Generated images follow this naming pattern:
```
{dataset}_{sampleID}_{style}.png
Example: wikipedia_020_cartoon.png
```

## Features
- Asynchronous image generation and download
- Progress tracking with rich console output
- State persistence for pause/resume capability
- Error handling and automatic retries
- Rate limiting management
- Dual organization structure (by style and by dataset)
- Full-size HD image downloads
- Detailed statistics tracking

## Usage

1. Set up your OpenAI API key:
   ```bash
   export OPENAI_API_KEY='your-api-key-here'
   ```

2. Run the script in Jupyter Notebook:
   - Open `image_generator_p2.ipynb`
   - Run all cells

3. Monitor Progress:
   - The script shows a progress bar
   - Statistics are displayed after each chunk
   - Processing status is continuously saved

4. Pause/Resume:
   - You can interrupt the script at any time
   - Progress is automatically saved in `generation_state.json`
   - Rerunning the script will continue from the last saved state

## State Tracking
The script maintains state in `generation_state.json` with:
- List of completed samples
- Failed sample records
- Last processed chunk index
- Timestamp of last update

## Error Handling
- Automatic retry for failed downloads (max 3 attempts)
- Rate limit detection and waiting
- Connection error management
- Detailed error logging

## Statistics Tracked
- Total processing duration
- Number of attempts
- Successful downloads
- Failed downloads
- Rate limit hits
- Connection errors
- Success rate

## Output Files
1. Generated Images:
   - Saved in both style-based and dataset-based organizations
   - Full HD quality (1024x1024)

2. Processing Statistics:
   - Saved in `images/processing_stats.json`
   - Updated after completion

3. State File:
   - Saved in `code/generation_state.json`
   - Updated after each chunk
   - Used for resume capability

## Troubleshooting
1. If the script fails to start:
   - Verify OpenAI API key is set
   - Check all required packages are installed
   - Ensure proper directory structure exists

2. If downloads are failing:
   - Check internet connection
   - Verify API key has sufficient credits
   - Look for rate limiting messages

3. For resume issues:
   - Check if `generation_state.json` exists and is not corrupted
   - Verify file permissions in output directories

## Notes
- Each sample is processed in chunks of 5 to manage rate limits
- 2-second delay between chunks to prevent overwhelming the API
- Images are saved in both organization schemes for flexibility
- Progress can be monitored through the rich console interface