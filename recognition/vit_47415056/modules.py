import torch
from timm import create_model  # Import `create_model` directly from timm

# Configure the device to use GPU if available, otherwise use CPU
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def create_model(num_classes=2):
    """
    Creates and returns a Vision Transformer (ViT) model.

    Parameters:
    - num_classes (int): Number of output classes for the model. Default is 2.

    Returns:
    - model (torch.nn.Module): ViT model initialized with the specified number of output classes.
    """
    
    # Initialize the ViT model using `vit_tiny_patch16_224`
    model = create_model('vit_tiny_patch16_224', pretrained=False, num_classes=num_classes)
    
    return model.to(DEVICE)