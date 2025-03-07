# InverseProblems
A repo dedicated to learning all about inverse problems and solutions using implicit neural representations (INRs)

## What is an inverse problem?


## Implicit Neural representations

Implicit Neural representations (INRs) are a paradigm in deep learing where continuous signals such as images, 3D shapes, or sound waves, or physical fields are represented as continuous functions through neural networks. Unlike traditional discrete representations (like pixel grids or voxels), INRs encode the entire signal within the weights of a neural network that maps coordinates to values. For example, mapping (x,y) coordinates to RGB values for an image, or (x,y,z) coordinates to volume for a 3D shape. This approach creates a continuous, fully differentiable representation that can be queried at any resolution. INRs have gained significant traction as an elegant way to solve inverse problems, where we aim to reconstruct unknown signals from limited, noisy, or indirect observations.

## Repo Guide

This page is a centralized document with information relating to inverse problems and INRs, including models, datasets, colab notebooks, and more. We also touch on Kolmogorov-Arnold Networks (KAN) which are a more recent network which are slowly becoming more popular and may be beneficial in creating more effective INRs.

### Medical Imaging

[Implicit Neural Representation in Medical Imaging: A Comparative Survey](https://arxiv.org/pdf/2307.16142)