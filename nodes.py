import os, argparse
import sys
from .scripts.gradio.i2v_test import Image2Video
sys.path.insert(1, os.path.join(sys.path[0], 'lvdm'))

resolutions=["576_1024","320_512","256_256"]

class DynamiCrafterLoader:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "resolution": (resolutions,{"default":"576_1024"}),
            }
        }

    RETURN_TYPES = ("DynamiCrafter",)
    RETURN_NAMES = ("model",)
    FUNCTION = "run_inference"
    CATEGORY = "DynamiCrafter"

    def run_inference(self,resolution):
        image2video = Image2Video('./tmp/', resolution=resolution)
        return (image2video,)

class DynamiCrafterSimple:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "model": ("DynamiCrafter",),
                "image": ("IMAGE",),
                "prompt": ("STRING", {"default": ""}),
                "steps": ("INT", {"default": 50}),
                "cfg_scale": ("FLOAT", {"default": 7.5}),
                "eta": ("FLOAT", {"default": 1.0}),
                "motion": ("INT", {"default": 3}),
                "seed": ("INT", {"default": 123}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "run_inference"
    CATEGORY = "DynamiCrafter"

    def run_inference(self,model,image,prompt,steps,cfg_scale,eta,motion,seed):
        image = 255.0 * image[0].cpu().numpy()
        #image = Image.fromarray(np.clip(image, 0, 255).astype(np.uint8))
        
        imgs= image2video.get_image(image, prompt, steps, cfg_scale, eta, motion, seed)
        return imgs


NODE_CLASS_MAPPINGS = {
    "DynamiCrafterLoader":DynamiCrafterLoader,
    "DynamiCrafter Simple":DynamiCrafterSimple,
}
