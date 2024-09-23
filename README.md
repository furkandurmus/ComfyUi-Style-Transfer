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

- Linux system 
- Python 3.10+
- CUDA-compatible GPU (for optimal performance)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/furkandurmus/ComfyUi-Style-Transfer.git
   ```
2 Clone custom node repositories to enhance usability of Comfy:
   ```
   cd ComfyUi-Style-Transfer/custom_nodes
   git clone https://github.com/ltdrdata/ComfyUI-Manager.git
   git clone https://github.com/cubiq/ComfyUI_IPAdapter_plus.git
   git clone https://github.com/Fannovel16/comfyui_controlnet_aux.git
   ```
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Download the required models:
   - [Juggernaut XL](https://civitai.com/models/133005/juggernaut-xl) and put into /models/checkpoints
   - [diffusers_xl_depth_full.safetensors](https://comfyui-wiki.com/resource/controlnet-models/controlnet-sdxl) and put into /models/controlnet
   - [clip vision](https://huggingface.co/laion/CLIP-ViT-H-14-laion2B-s32B-b79K) and put into /models/clip_vision
   - [ipadapter](https://huggingface.co/h94/IP-Adapter/blob/main/sdxl_models/ip-adapter_sdxl_vit-h.safetensors) and put into /models/ipadapter (create if not exists)
   - [vae](https://huggingface.co/hskWih/tmp_model/blob/2709fed9dcafe28f48d2cf798802206204f66889/tmpvae_XL/xlVAEC_f1.safetensors) and put into /models/vae


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

