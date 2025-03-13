# Sinusoidal Representation Network (SIREN)

### [Paper](https://arxiv.org/abs/2006.09661) | [Project Page](https://www.vincentsitzmann.com/siren/) | [Github](https://github.com/vsitzmann/siren)

SIRENs have shown to be one of the most effective neural network models for implicit neural representations and have began to become widely adopted. This is due to their remarkable ability to represent complex signals with high fidelity across a variety of domains. The sinusoidal activation functions at the core of SIRENs enable them to capture fine details and high-frequency information that traditional networks with ReLU or tanh activations struggle to model.
The key advantages that have driven SIREN adoption include:

1. Superior representation of complex signals with sharp discontinuities
2. Ability to model higher-order derivatives accurately
3. Faster convergence during training
4. Natural representation of periodic functions
5. Excellent performance in tasks requiring differential constraints

SIRENs excel particularly in applications like image and audio reconstruction, 3D shape representation, physics-informed neural networks, and other scenarios where capturing high-frequency details or honoring differential equations is crucial.

### Other Resources

* [Notebook training a SIREN from the original authors](models/SIREN/explore_siren.ipynb)

* [Understanding Fourier Features](https://sair.synerise.com/fourier-feature-encoding/)

* [An Interactive Guide to the Fourier Transform](https://betterexplained.com/articles/an-interactive-guide-to-the-fourier-transform/)
