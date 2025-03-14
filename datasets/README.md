# Datasets

## FastMRI
The the fastMRI dataset and information about it can be found [here](https://fastmri.med.nyu.edu/)
* To download the dataset, scroll to the bottom of the page and enter your electronic signature. An email will be sent to you with links to the downloads

For more information on how to structure and use the fastmri data check out the [fastMRI github](https://github.com/facebookresearch/fastMRI)

The mri files provided are in k wave space or k-space. To better understand k-space I recommend watching [this video](https://www.youtube.com/watch?v=GF7Z8Sd9qYE) by LOFT lab

## COSMOS

The COSMOS real galaxy dataset is extracted from the HST COSMOS survey for use with GalSim. It can be found [here](https://zenodo.org/records/3242143#.Ytjzki-KFAY)


## NeRF
NERF (Neural Radiance Fields) is a computer vision technique that represents 3D scenes as continuous volumetric functions using neural networks. Unlike traditional 3D reconstruction methods that use meshes or point clouds, NERF learns to model how light rays interact with scene geometry and appearance to generate photorealistic novel views of a scene from a set of input images.

The NERF dataset consists of multiple images of a scene captured from different viewpoints, along with corresponding parameters $(x, y, z, \theta, \phi) \rightarrow (r,g,b,\sigma)$. Where $\theta$ is the camera angle, $\phi$ is the tilt, and $\sigma$ is the volume of the rendered ray at a given pixel.

* [Dataset used in the orignal NeRF paper](https://drive.google.com/drive/folders/1cK3UDIJqKAAm7zyrxRYVFJ0BRMgrwhh4)

* [The NeRF project page](https://www.matthewtancik.com/nerf)

For a pytorch implementation of the nerf model check out [yenchenlin's repo](https://github.com/yenchenlin/nerf-pytorch)


## Kodak images

The [Kodak dataset](datasets/kodak) is commonly used for simple image reconstruction tasks, useful as a baseline test to compare reconstruction scores and metrics across different model architectures.