##  Introduction

In simple words, **normalizing flows** is a series of simple functions which are invertible, or the analytical inverse of the function can be calculated. For example, f(x) = x + 2 is a reversible function because for each input, a unique output exists and vice-versa whereas f(x) = x² is not a reversible function. Such functions are also known as bijective functions.

## Types of Normalizing Flows:

An overview of different types of normalizing flows can be found [here](https://arxiv.org/pdf/1908.09257). 

- Linear Flows (Diagonal, Triangular, Permutation and Orthogonal, Factoriza, Convolution)
- Planar and Radial Flows
- Coupling and Autoregressive Flows
- Residual Flows
- Infinitesimal (Continuous) Flows

Normalizing flows are an active field of research, some newer models includes: Affine Flow, Neural Spline Flow, Glow Flow, etc.

Detailed implementation of those models can be found [here](https://github.com/VincentStimper/normalizing-flows).


### Advantages of Normalizing Flows:

- The normalizing flow models do not need to put noise on the output and thus can have much more powerful local variance models.
- The training process of a flow-based model is very stable compared to GAN training of GANs, which requires careful tuning of hyperparameters of both generators and discriminators.
- Normalizing flows are much easier to converge when compared to GANs and VAEs.

### Disadvantages of Normalizing Flows:

- Due to the lackluster performance of flow models on tasks such as density estimation, it is regarded that they are not as expressive as other approaches.
- One of the two things required for flow models to be bijective is the volume preservation over transformations, which often leads to very high dimensional latent space, which is usually harder to interpret.
- The samples that are generated through flow-based models are not as good when compared to GANs and VAEs.

## References:

Aryansh Omray. (2021, July 16). Introduction to Normalizing Flows | Towards Data Science. Towards Data Science. https://towardsdatascience.com/introduction-to-normalizing-flows-d002af262a4b/



IBM. (2020). GitHub - IBM/controlled-peptide-generation at 1ba3ce8b024e0701f28828a02666b0518ef20370. GitHub. https://github.com/IBM/controlled-peptide-generation/tree/1ba3ce8b024e0701f28828a02666b0518ef20370


Normalizing Flow Models. (2018). Github.io. https://deepgenerativemodels.github.io/notes/flow/

