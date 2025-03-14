# InverseProblems
A repo dedicated to learning all about inverse problems and solutions using implicit neural representations (INRs)

## What is an inverse problem?

An inverse problem involves reconstructing an unknown signal, image, or multidimensional volume from observed data. These observations are typically related to the unknown through a forward process, which is often non-invertible, making the problem ill-posed. This means that solutions may not exist, may not be unique, or may not depend continuously on the data.

Examples of Inverse Problems:

- Deblurring: Recovering a clear image from a blurred one.
- Deconvolution: Extracting original signals from convoluted measurements.
- Inpainting: Filling in missing or damaged parts of an image.
- Compressed Sensing: Reconstructing high-dimensional signals from fewer measurements than traditionally required.
- Superresolution: Enhancing the resolution of imaging systems beyond their original capabilities.

Mathematical Definition:

Mathematically, we can define a forward model as:

$$\mathbf{y} = A(\mathbf{x}) + \mathbf{n}$$


Here, $A: \mathbb{R}^n \rightarrow \mathbb{R}^m$ denotes the forward operator, which can be linear or nonlinear, and $\mathbf{n} \in \mathbb{R}^m$ represents random measurement noise. This formulation illustrates that the observed data are a noisy transformation of the true image, and the goal is to infer $\mathbf{x}$ from $\mathbf{y}$.



## Implicit Neural representations

Implicit Neural representations (INRs) are a paradigm in deep learing where continuous signals such as images, 3D shapes, or sound waves, or physical fields are represented as continuous functions through neural networks. Unlike traditional discrete representations (like pixel grids or voxels), INRs encode the entire signal within the weights of a neural network that maps coordinates to values. For example, mapping (x,y) coordinates to RGB values for an image, or (x,y,z) coordinates to volume for a 3D shape. This approach creates a continuous, fully differentiable representation that can be queried at any resolution. INRs have gained significant traction as an elegant way to solve inverse problems, where we aim to reconstruct unknown signals from limited, noisy, or indirect observations.

## INR Use Cases

__3D Scene Representation:__ INRs excel at representing complex 3D scenes through models like NeRF (Neural Radiance Fields), enabling photorealistic novel view synthesis from a sparse set of input images.

__Medical Imaging:__ INRs can compactly represent CT and MRI scans, supporting super-resolution, noise reduction, and reconstruction from limited data—particularly valuable when dealing with sparse or incomplete medical data.

__Signal Compression:__ By encoding images, audio, or video as compact neural networks rather than discrete samples, INRs achieve impressive compression ratios while preserving high-frequency details that traditional methods might lose.

__Physics Simulation:__ INRs can represent solutions to partial differential equations, enabling efficient simulation of physical phenomena like fluid dynamics or heat transfer with continuous outputs at arbitrary resolution.

__Shape Representation:__ Using signed distance functions (SDFs), INRs can represent complex 3D geometries with smooth surfaces and sharp features, useful for computer graphics, CAD, and digital fabrication.

## Repo Guide

* #### [Datasets](datasets/README.md)
    * fastMRI
    * NeRF
    * GALAXY?
    * kodak

* #### Models
    * Diffusion
    * [SIREN](models/SIREN/README.md)
        * [siren pytorch](models/SIREN/siren.py)
        * [training a SIREN](models/SIREN/explore_siren.ipynb)
    * [WIRE](models/WIRE/README.md)
    * [ConvINR](models/ConvINR/README.md)
        * [training a ConvINR](models/ConvINR/train_cnn_inr.ipynb)

* #### [Metrics](metrics/README.md)
    * Peak-Signal-to-Noise Ratio (PSNR)
    * Structural Similarity Index Measure (SSIM)
    * Uncertainty Quantification
    * Negative Log-Likelihood (NLL)
    * Expected Calibration Error (ECE)

* #### Slide decks
    * [KANs and INRs](slides/KANs%20and%20INRs.pdf)
    * [Unsupervised DL Methods in Inverse Imaging Problems](slides/Unsupervised%20DL%20Methods%20in%20Inverse%20Imaging%20Problems.pdf)

## Other Resources

Be sure to check out the __[awesome-implicit-representations repo](https://github.com/vsitzmann/awesome-implicit-representations)__ for more resources on implicit neural representations
