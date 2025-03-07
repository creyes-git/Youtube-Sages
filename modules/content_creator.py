import replicate
import os
from dotenv import load_dotenv


load_dotenv()

api_token = os.getenv("REPLICATE_API_TOKEN")


#FLUX SCHNELL - 0.003/Image 
def flux_schnell_create_image(prompt, num_images = 1):
    
    response = replicate.run("black-forest-labs/flux-schnell",
                             input = {"prompt": prompt,
                                      "go_fast": True,
                                      "megapixels": "1",
                                      "num_outputs": num_images,
                                      "aspect_ratio": "16:9",
                                      "output_format": "png",
                                      "output_quality": 100,
                                      "num_inference_steps": 4
                                     })
    
    return response
    
    
#FLUX DEV - 0.025/Image   
def flux_dev_create_image(prompt, num_images = 1, reference_image = None, prompt_strength = 0.8):
    
    response = replicate.run("black-forest-labs/flux-dev",
                             input = {"image": reference_image,
                                      "prompt": prompt,
                                      "go_fast": True,
                                      "guidance": 3.5,
                                      "megapixels": "1",
                                      "num_outputs": num_images,
                                      "aspect_ratio": "16:9",
                                      "output_format": "png",
                                      "output_quality": 100,
                                      "prompt_strength": prompt_strength,
                                      "num_inference_steps": 50
                                     })
    
    return response


#FLUX 1.1 PRO - 0.04/Image
def flux_pro_create_image(prompt, reference_image = None):
    
    response = replicate.run("black-forest-labs/flux-1.1-pro",
                             input = {"image_prompt": reference_image,
                                      "prompt": prompt,
                                      "aspect_ratio": "16:9",
                                      "output_format": "jpg",
                                      "output_quality": 100,
                                      "safety_tolerance": 3,
                                      "prompt_upsampling": True
                                     }
                        )
    
    return response