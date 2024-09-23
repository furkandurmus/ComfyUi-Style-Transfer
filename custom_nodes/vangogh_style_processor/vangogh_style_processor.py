import torch
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter

class VanGoghPreprocessor:
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
                "brush_stroke_sim": ("INT", {
                    "default": 3,
                    "min": 0,
                    "max": 10,
                    "step": 1,
                    "display": "slider"
                }),
                "tint_color": (["none", "yellow", "blue", "both"],),
                "tint_strength": ("FLOAT", {
                    "default": 0.1,
                    "min": 0.0,
                    "max": 0.5,
                    "step": 0.01,
                    "round": 0.01,
                    "display": "slider"
                })
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "preprocess"
    CATEGORY = "image/preprocessing"


    def preprocess(self, image, contrast, saturation, brush_stroke_sim, tint_color, tint_strength):
        image = Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))
        
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(contrast)
        
        enhancer = ImageEnhance.Color(image)
        image = enhancer.enhance(saturation)
        
        for _ in range(brush_stroke_sim):
            image = image.filter(ImageFilter.EDGE_ENHANCE)
            image = image.filter(ImageFilter.GaussianBlur(radius=1))
        
        if tint_color in ["yellow", "both"]:
            yellow_overlay = Image.new("RGB", image.size, (255, 255, 200))
            image = Image.blend(image, yellow_overlay, tint_strength)
        if tint_color in ["blue", "both"]:
            blue_overlay = Image.new("RGB", image.size, (200, 200, 255))
            image = Image.blend(image, blue_overlay, tint_strength)
        
        
        result = np.array(image).astype(np.float32) / 255.0
        result = torch.from_numpy(result).unsqueeze(0)
        
        return (result,)

NODE_CLASS_MAPPINGS = {
    "VanGoghPreprocessor": VanGoghPreprocessor
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "VanGoghPreprocessor": "Van Gogh Image Preprocessor"
}
