# Conv-INR 

Most INR models utilize a multilayer perceptron with sinusoidal activations, however, in [CONV-INR: Convolutional Implicit Neural Representation For
Multimodal Vision Signals [1]](https://arxiv.org/abs/2406.04249) the author looks uses a CNN for image reconstruction tasks. 

## Key Innovations of Conv-INR
Traditional INR approaches using MLPs face two significant challenges:

1. __Isolated coordinate processing:__ MLP-based INRs process each coordinate independently, ignoring relationships between neighboring points.
2. __Spectral bias:__ MLPs naturally converge to low-frequency components faster while struggling to learn high-frequency details.

Conv-INR addresses these limitations by leveraging convolutional neural networks instead of MLPs as the backbone for implicit neural representations

## How Conv-INR Processes Inputs Differently
Unlike traditional MLP-based INRs that reshape coordinates into a matrix of size (W×H)×2 for images, Conv-INR handles inputs in a fundamentally different way:

1. It arranges the coordinates as a 3D tensor of size W×H×C (where C is the coordinate dimension, typically 2 for images).
2. This preserves the spatial arrangement of the input signal, allowing the network to directly output a tensor of the same spatial dimensions as the target signal.
3. The convolution operation naturally incorporates local information by using a sliding window approach (typically with 3×3 kernels) that considers patches of adjacent coordinates together.

## Overcoming Spectral Bias
Conv-INR naturally addresses the spectral bias problem without requiring additional techniques like positional encoding or specialized activation functions:

1. Convolution operations inherently have the ability to represent both low and high-frequency signals due to their shift-invariant property.
2. The sliding window mechanism of convolution effectively acts as a form of shift-invariant operation over the input domain, similar to what positional encoding tries to achieve but in a more direct way.

## Broader Implications
This paper appears to be one of the first explorations of using convolutional networks for implicit neural representations. Given the impressive results, this direction warrants further investigation, particularly in:

1. Exploring different convolutional architectures and their impact on representation quality
2. Applying Conv-INR to additional domains beyond images, CT/MRI, and NeRF
3. Investigating hybrid approaches that combine the benefits of convolution and other INR advancements

## References
[1] Z. Cai, “Conv-INR: Convolutional Implicit Neural Representation for Multimodal Visual Signals,” Jun. 06, 2024, arXiv: arXiv:2406.04249. doi: 10.48550/arXiv.2406.04249.
