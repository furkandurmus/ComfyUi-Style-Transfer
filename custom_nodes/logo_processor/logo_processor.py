import torch
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter, ImageOps

class VanGoghLogoPreprocessor:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "contrast": ("FLOAT", {
                    "default": 1.2,
                    "min": 0.5,
                    "max": 2.0,
                    "step": 0.1,
                    "round": 0.01,
                    "display": "slider"
                }),
                "saturation": ("FLOAT", {
                    "default": 1.3,
                    "min": 0.5,
                    "max": 2.0,
                    "step": 0.1,
                    "round": 0.01,
                    "display": "slider"
                }),

                "logo_emphasis": ("FLOAT", {
                    "default": 0.5,
                    "min": 0.0,
                    "max": 1.0,
                    "step": 0.1,
                    "round": 0.01,
                    "display": "slider"
                }),
                "background_fill": (["none", "white", "black", "auto"],),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "preprocess"
    CATEGORY = "image"

    def preprocess(self, image, contrast, saturation, logo_emphasis, background_fill):
        image = Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))
        
        # Logo-specific preprocessing
        if background_fill != "none":
            if background_fill == "auto":
                bg_color = image.getpixel((0, 0)) 
            elif background_fill == "white":
                bg_color = (255, 255, 255)
            else:  # black
                bg_color = (0, 0, 0)
            
            # Create a mask of the logo
            mask = Image.new("L", image.size, 0)
            for x in range(image.width):
                for y in range(image.height):
                    if image.getpixel((x, y)) != bg_color:
                        mask.putpixel((x, y), 255)
            
            # Expand the mask slightly to ensure full logo coverage
            mask = mask.filter(ImageFilter.MaxFilter(3))
            
            # Fill the background
            bg = Image.new("RGB", image.size, bg_color)
            image = Image.composite(image, bg, mask)
        
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(1 + logo_emphasis)
        
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(contrast)
        
        enhancer = ImageEnhance.Color(image)
        image = enhancer.enhance(saturation)
        
        
        result = np.array(image).astype(np.float32) / 255.0
        result = torch.from_numpy(result).unsqueeze(0)
        
        return (result,)

NODE_CLASS_MAPPINGS = {
    "VanGoghLogoPreprocessor": VanGoghLogoPreprocessor
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "VanGoghLogoPreprocessor": "Van Gogh Logo Preprocessor"
}