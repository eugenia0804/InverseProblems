# Introduction

Quantifying the uncertainty in reconstructed images is crucial for computational imaging in both scientific and medical applications. In many imaging problems, such as medical image reconstruction, remote sensing, or materials science, it is essential not only to generate an image but also to understand how uncertain or confident we are about the reconstructed features. By incorporating uncertainty, we can better interpret the results, assess the reliability of the image features, and make informed decisions about further processing, diagnosis, or analysis.

## What is the posterior distribution

In the context of image reconstruction and uncertainty quantification, the posterior distribution represents the probability distribution of the reconstructed image given the observed data. It encapsulates all the information we have about the image after considering both the observed data and prior beliefs about the image. 

The posterior distribution is typically high-dimensional, as it represents the distribution over all pixels or parameters of the image. In practice, we are often interested in summary statistics such as the **mean** (expected reconstruction) and the **variance** (uncertainty about the reconstruction). 

## Classical Methods

### MCMC sampling

**Markov Chain Monte Carlo (MCMC)** methods are a family of algorithms used to sample from complex, high-dimensional probability distributions, particularly in situations where the distribution is difficult to sample from directly. One of the most popular MCMC algorithms is Metropolis-Hastings sampling, which is used to draw samples from a target distribution by generating a Markov Chain.

The math of the Metropolis-Hastings Algorithm can be expressed as follows:

Let $f(x)$ be a function that is proportional to the desired probability density function $P(x)$ (the target distribution)

1. Initialization: Choose an arbitrary point $x_t$ to be the first observation in the sample and choose a proposal funtion $g(x|y)$. $g$ is assumed to be symmetric.

2. For each itertaion $t$:
- Propose a candidate $x'$ for the next sample by picking from the distribution $g(x'|x_t)$
- Calculate the acceptance ratio $\alpha = f(x')/f(x_t)$, whcih will be used to decide whether to accept or reject the candidate. Because $f$ is proportional to the density of $P$, we have that $\alpha=f(x')/f(x_t)=P(x')/P(x_t)$.
- Accept or reject:
    - Generate a uniform random number $u\in[0,1]$
    - If $u\leq\alpha$, then accept the candidate by setting $x_{t+1}=x'$
    - If $u\geq\alpha$, then reject the candidate and set $x_{t+1}=x_t$ instead.


Example code and toy example can be found in `mcmc.ipynb`.


### Bayesian hypothesis testing

**Bayesian hypothesis testing** is a statistical framework that evaluates hypotheses in light of both prior information and observed data, with a primary goal of quantifying the likelihood of different hypotheses being true. In the context of computational imaging, Bayesian hypothesis testing can be particularly useful for evaluating competing hypotheses about the true underlying image or the nature of image reconstruction, where we wish to assess the most likely configuration of an image given the available data and prior knowledge.

In Bayesian hypothesis testing, the likelihood of a hypothesis $H_i$ is evaluated using the posterior probability given the observed data $D$, denoted as $P(H_i|D)$. This posterior is calculated using Bayes' Theorem, where we combine the prior belief about the hypothesis $P(H_i)$ with the likelihood of observing the data given that hypothesis $P(D|H_i)$. The resulting posterior probability provides a measure of how likely a given hypothesis is after incorporating the data.



### Variational Inference

**Variational Inference (VI)** is a technique for approximating complex posterior distributions in Bayesian inference by transforming the problem into an optimization task. This is particularly useful when dealing with high-dimensional, intractable posterior distributions, such as those arising in image reconstruction problems. The goal of VI is to find a simpler distribution that approximates the true posterior distribution as closely as possible, but with a computational cost that is significantly lower than traditional sampling methods like MCMC.

The basic idea behind Variational Inference is to find a distribution $q(x)$ from a family of distributions $Q$ (called the variational family) that minimizes the **Kullback-Leibler (KL) divergence** between the variational distribution $q(x)$ and the true posterior distribution $p(x∣D)$ , where $D$ represents the observed data. The KL divergence measures how much information is lost when using $q(x)$ to approximate $p(x∣D)$. The goal is to minimize this divergence:

$$KL(q(x)|p(x|D))=E_{q(x)}[log\frac{q(x)}{p(x|D)}]$$

VI typically requires fewer computational resources compared to MCMC and can handle large datasets or high-dimensional problems more efficiently. However, while MCMC provides exact samples from the posterior, VI provides an approximation, which is faster but might lose some precision.

Example code and toy example can be found in `vi.ipynb`.