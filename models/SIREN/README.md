# Sinusoidal Representation Network (SIREN)

SIRENs have shown to be one of the most effective neural network models for implicit neural representations and have began to become widely adopted. This is due to their remarkable ability to represent complex signals with high fidelity across a variety of domains. The sinusoidal activation functions at the core of SIRENs enable them to capture fine details and high-frequency information that traditional networks with ReLU or tanh activations struggle to model.
The key advantages that have driven SIREN adoption include:

1. Superior representation of complex signals with sharp discontinuities
2. Ability to model higher-order derivatives accurately
3. Faster convergence during training
4. Natural representation of periodic functions
5. Excellent performance in tasks requiring differential constraints

SIRENs excel particularly in applications like image and audio reconstruction, 3D shape representation, physics-informed neural networks, and other scenarios where capturing high-frequency details or honoring differential equations is crucial.

### Link to the github of the original SIREN paper:
[SIREN Github](https://github.com/vsitzmann/siren)

### Other Resources helpful for understanding SIREN and related topics

* [A helpful walkthrough for setting up and running a SIREN model from the original authors of the SIREN paper](models/SIREN/explore_siren.ipynb)

* [A website explaining fourier features](https://sair.synerise.com/fourier-feature-encoding/)

* [An Interactive Guide to the Fourier Transform](https://betterexplained.com/articles/an-interactive-guide-to-the-fourier-transform/)
