import torch
from torch.utils.data import Dataset
import scipy.io.wavfile as wavfile
import numpy as np
from PIL import Image


def get_mgrid(shape):
    '''Generates a flattened grid of (x,y,...) coordinates in a range of -1 to 1
    shape: tuple/list with desired dimensions of the grid 
    '''
    dim = len(shape)
    if dim < 2:
        return Exception("Dimension must be at least 2")
    
    tensors = tuple([torch.linspace(-1, 1, steps=s) for s in shape])
    mgrid = torch.stack(torch.meshgrid(*tensors), dim=-1)
    mgrid = mgrid.reshape(-1, dim)
    return mgrid


def laplace(y, x):
    grad = gradient(y, x)
    return divergence(grad, x)


def divergence(y, x):
    div = 0.
    for i in range(y.shape[-1]):
        div += torch.autograd.grad(y[..., i], x, torch.ones_like(y[..., i]), create_graph=True)[0][..., i:i+1]
    return div


def gradient(y, x, grad_outputs=None):
    if grad_outputs is None:
        grad_outputs = torch.ones_like(y)
    grad = torch.autograd.grad(y, [x], grad_outputs=grad_outputs, create_graph=True)[0]
    return grad

class ImageFitting(Dataset):
    def __init__(self, filename):
        super().__init__()
        pil_img = Image.open(filename)
        img = torch.from_numpy(np.array(pil_img))
        self.pixels = img.permute(1, 2, 0).view(-1, 1)
        self.coords = get_mgrid(img.shape, 2)

    def __len__(self):
        return 1

    def __getitem__(self, idx):
        if idx > 0: raise IndexError

        return self.coords, self.pixels
    

class AudioFile(Dataset):
    def __init__(self, filename):
        self.rate, self.data = wavfile.read(filename)
        self.data = self.data.astype(np.float32)
        self.timepoints = get_mgrid(len(self.data), 1)

    def get_num_samples(self):
        return self.timepoints.shape[0]

    def __len__(self):
        return 1

    def __getitem__(self, idx):
        amplitude = self.data
        scale = np.max(np.abs(amplitude))
        amplitude = (amplitude / scale)
        amplitude = torch.Tensor(amplitude).view(-1, 1)
        return self.timepoints, amplitude