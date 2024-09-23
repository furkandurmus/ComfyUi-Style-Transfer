# ComfyUi-Style-Transfer
Apply Style Transfer with Diffusion Models on ComfyUi Tool
# Advanced Image Style Transfer with ComfyUI

## Project Overview

This repository contains an implementation of an advanced image style transfer tool using ComfyUI, a powerful interface for Stable Diffusion models. The project aims to apply artistic styles from reference images to target images, with a particular focus on handling complex scenarios including images with text.

## Features

- Style transfer using state-of-the-art Stable Diffusion models
- Integration with IPAdapter for enhanced style adaptation
- Custom preprocessing for images containing text (OCR)
- Flexible workflow allowing for easy experimentation and modification

## Prerequisites

- Python 3.10+
- CUDA-compatible GPU (for optimal performance)
- ComfyUI (latest version)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/furkandurmus/ComfyUi-Style-Transfer.git
   cd comfyui
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Download the required models:
   - Juggernaut XL
   - Diffusers XL Depth
   (Provide links or instructions for downloading these models)

4. Place the downloaded models in the appropriate ComfyUI directories.

## Usage

1. Start ComfyUI:
   ```
   python /comfyui/main.py
   ```

2. In the ComfyUI interface, load the provided workflow file: `style_transfer_workflow.json`

3. Upload your reference style image and target image to the respective nodes.

4. Adjust parameters as needed (see 'Configuration' section below).

5. Run the workflow and retrieve your styled image from the output node.

## Configuration

- **IPAdapter Settings**: Adjust strength to control the intensity of style transfer.
- **ControlNet Settings**: Modify the influence of the depth map on the style transfer process.
- **KSampler Settings**: 
  - Adjust steps (recommended: 20-30) 
  - Set an appropriate CFG Scale (recommended: 7-8)
  - Modify denoise strength (recommended: 0.5-0.7) to balance between preserving original content and applying new style.

## Custom OCR Preprocessing

For images containing text:

1. Enable the custom OCR preprocessing node in the workflow.
2. Adjust the preprocessing parameters based on the characteristics of your text-containing image.

## Examples

XXXX

## Limitations

- The current implementation may struggle with maintaining text integrity in logos or text-heavy images.
- Performance may vary depending on the complexity of the input images and chosen styles.

