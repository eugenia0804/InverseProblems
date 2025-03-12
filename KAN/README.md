# Kolmogorov-Arnold Network (KAN)

Kolmogorov-Arnold Networks (KANs) are a novel neural network architecture proposed in [2024 by Liu et al.](https://arxiv.org/abs/2404.19756) inspired by the Kolmogorov-Arnold representation theorem from mathematics. Unlike traditional neural networks with fixed activation functions, KANs learn both the weights between neurons and the activation functions themselves. Each neuron in a KAN can adapt its response function to the specific data patterns it encounters, essentially constructing a library of custom univariate functions. This approach allows KANs to approximate complex multivariate functions through compositions of these learned univariate functions, often requiring fewer parameters than conventional neural networks. Their adaptive nature makes KANs particularly effective at modeling intricate patterns across various domains, from signal processing to computer vision, offering enhanced expressivity while maintaining computational efficiency.

![image](https://private-user-images.githubusercontent.com/40363572/421528465-148e896c-fbce-4dbb-b41f-a171643d81e4.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDE3MTkyNDAsIm5iZiI6MTc0MTcxODk0MCwicGF0aCI6Ii80MDM2MzU3Mi80MjE1Mjg0NjUtMTQ4ZTg5NmMtZmJjZS00ZGJiLWI0MWYtYTE3MTY0M2Q4MWU0LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTAzMTElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwMzExVDE4NDkwMFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWQ3Yjc2Y2FlYjllNTVlYTVlZWExZmJhYmY3NjFiMzZkZmZiOTA4Zjc3ZWNlOTQ4MWM3ZmI2OWVjNDM5ZTFjNmUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.gd4lT-aMSvrcslCToxwpMiAJk-TW_3BLJvWvH8XMOSo)

## Tutorials
* [KAN-Tutorial](https://github.com/pg2455/KAN-Tutorial) - To gain a better understanding of how KANs work and how to build one I recommend working through the jupyter notebooks.
* [pykan tutorials](https://github.com/KindXiaoming/pykan/tree/master/tutorials/Example) - a folder of tutorials by the original authors of the paper using their library [pykan](https://kindxiaoming.github.io/pykan/intro.html)

## KANs and INRs

The following papers and projects using KANs to learn implicit neural representations:
* [Single-Layer Learnable Activation for Implicit Neural Representation (SL2A-INR)](https://arxiv.org/abs/2409.10836)
* [Implicit Neural Representations with Fourier Kolmogorov-Arnold Networks
](https://arxiv.org/abs/2409.09323) | [code](https://github.com/Ali-Meh619/FKAN)
* [implicit-kan](https://github.com/belkakari/implicit-kan)

The findings in these papers suggest that incorporating KAN layers into implicit neural representations may significantly improve the learning of Fourier features. KANs' ability to adaptively learn activation functions appears to help neural networks better capture both high and low-frequency components of signals, leading to faster convergence and improved reconstruction quality, especially for complex patterns and fine details.

## Other helpful Resources
### Articles
* [A Beginner-friendly Introduction to Kolmogorov Arnold Networks](https://www.dailydoseofds.com/a-beginner-friendly-introduction-to-kolmogorov-arnold-networks-kan/)
* [The Math Behind KAN](https://towardsdatascience.com/the-math-behind-kan-kolmogorov-arnold-networks-7c12a164ba95/)

### Youtube
* [KAN: Kolmogorov-Arnold Networks | Ziming Liu (author)](https://www.youtube.com/watch?v=AUDHb-tnlB0)
* [What are splines?](https://youtu.be/jvPPXbo87ds?si=CmZVMfFgOBvrkWO1) - An intuitive explanation of all things splines

* [B-Splines](https://www.youtube.com/live/qhQrRCJ-mVg?si=AQaK9X3wBtYCAVT3) - A lecture walking through the math of B-Splines and Bezier curves 

I recommend checking out the [awesome-kan](https://github.com/mintisan/awesome-kan?tab=readme-ov-file#table-of-contents) github page which aims to be a comprehensive and organized collection that will help researchers and developers in the world of KAN. It contains additional tutorials as well as tons of projects making use of KANs to some extent