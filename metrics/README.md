# Introduction

The page provides a summary and code snippet of all relevant metrics in the reverse imaging problem space. 

## Peak-Signal-to-Noise Ratio (PSNR) $\uparrow$

Given a reference image $f$ and a test image $g$, both of size $M \times N$, the PSNR between $f$ and $g$ is defined by:

$$
PSNR(f, g) = 10 \log_{10} \left( \frac{255^2}{MSE(f, g)} \right)$$

where

$$MSE(f, g) = \frac{1}{MN} \sum^{M}_{i=1} \sum^{N}_{j=1} (f_{ij} - g_{ij})^2
$$

The PSNR value approaches infinity as the MSE approaches zero; this shows that a higher PSNR value provides a higher image quality. At the other end of the scale, a small value of the PSNR implies high numerical differences between images.

#### Implementation:

```python
from skimage.metrics import peak_signal_noise_ratio

def psnr(x, gt, data_range=None):
    if data_range is None:
        data_range = gt.max() - gt.min()
    return peak_signal_noise_ratio(x, gt, data_range=data_range)
```

## Structural Similarity Index Measure (SSIM) $\uparrow$

The SSIM is a well-known quality metric used to measure the similarity between two images and is considered to be correlated with the quality perception of the human visual system (HVS). Instead of using traditional error summation methods, the SSIM is designed by modeling any image distortion as a combination of three factors: loss of correlation, luminance distortion, and contrast distortion. The SSIM is defined as:

$$
SSIM(f, g) = l(f, g) \cdot c(f, g) \cdot s(f, g)
$$

where

$$
\begin{aligned}
    l(f, g) &= \frac{2 \mu_{f} \mu_{g} + C_1}{\mu_{f}^{2} + \mu_{g}^{2} + C_1} \\
    c(f, g) &= \frac{2 \sigma_{f} \sigma_{g} + C_2}{\sigma_{f}^{2} + \sigma_{g}^{2} + C_2} \\
    s(f, g) &= \frac{\sigma_{fg} + C_3}{\sigma_{f} \sigma_{g} + C_3}
\end{aligned}
$$

#### Implementation:

```python
from skimage.metrics import structural_similarity

def ssim(x, gt, data_range=None):
    if data_range is None:
        data_range = gt.max() - gt.min()
    return structural_similarity(x, gt, data_range=data_range)
```

## Uncertainty Quantification

When developing method with capability of uncertainty quantification, we want to further measure how well the recovered uncertainty space truely align with the real, unlike PSNR and SSIM which inputs are ground truth image and the reconstructed image, the input are either raw generated samples or their mean and standard deviation.

Compare to PSNR and SSIM, which are metrics dedicating to the imaging field and have readily available function in `skimage` package, metrics related to uncertainty quantification quality are more broadly applicable.

### Negative Log-Likelihood (NLL) $\downarrow$

The NLL metric estimates how well the predicted probability distribution matches the real distribution. It is normally used in classification tasks but can also be used as an uncertainty quantification metric. It is defined as:

$$H(p,\hat{p}) = -E_p[log\hat{p}] = -\sum^n_{i=1}p_ilog(\hat{p_i})= -log(\hat{p_j})$$

where $p_j=1$ is the ground truth and $\hat{p_j} = softmax_j(x)$. 


#### Implemenation:
```python
def nll(x, mean, std):
    nll = (x-mean) ** 2 / (2 * std ** 2) + 0.5 * np.log(2 * np.pi * std ** 2)
    return nll.mean().astype(float)
```
<!-- 
### Out of Distribution Rate (OODR)

#### Implemenation:
```python
def oodr(x, mean, std, threshold=4.0):
    ratio = np.abs(mean-x)/std
    return (ratio > threshold).mean()
``` -->

### Expected Calibration Error (ECE) $\downarrow$

ECE is defined as

$$ECE=E_{\hat{P}}[|P(\hat{Y}=y|\hat{P}=p)-p|]=\sum_p P(\hat{P}=p)|P(\hat{Y}=y|\hat{P}=p)-p|$$


We approximate the probability distribution by a histogram with $B$ bins. Then $P(\hat{P}=p)=\frac{n_b}{N}$ where $n_b$ is the number of probabilities in bin $b$ and $N$ is the size of the dataset. Since we put $n_b$ probabilities into one bin, $p$ is not a single value. Therefore, a representative value $p=\sum_{\hat{p_i}\in b}\frac{\hat{p_i}}{n_b}=conf(b)$ is necessary. Similarly, we can set $P(\hat{Y}=y|\hat{P}=p)=\sum_{\hat{p_i}\in b}\frac{1(y_i=\hat{y_i})}{n_b}=acc(b)$ where $\hat{y_i}$ is obtained from the highest probability (arg max). $\hat{p_i}$ is also the highest probability (max).

ECE is then defined as follows:

$$ECE(B)=\sum^B_{b=1}\frac{n_b}{N}|acc(b)-conf(b)|=\frac{1}{N}\sum_{b\in B}|\sum_{(\hat{p_i}, \hat{y_i})\in b}1(y_i=\hat{y_i})-\hat{p_i}|$$

The accuracy $acc(b)$ is also called “observed relative frequency”, while the confidence $conf(b)$ is a synonym fo “average predicted frequency”.

#### Implemenation:
```python
def ece(samples, gt, percent_diff=0.05):
    
    if isinstance(samples, np.ndarray):
        samples = torch.from_numpy(samples)
    if isinstance(gt, np.ndarray):
        gt = torch.from_numpy(gt)
        
    percentages = [round(percent, 2) for percent in np.arange(0, 1, percent_diff)]

    deltas = np.append(np.logspace(-20, -1, 21), 0)
    delta_vals = []
    best_delta = 0
    best_ece = np.inf
    for delta in deltas:
        ece = 0
        for percent in percentages:
            lb = torch.quantile(samples, 0.5 - percent / 2, dim=0, keepdim=True)
            ub = torch.quantile(samples, 0.5 + percent / 2, dim=0, keepdim=True)
            mean_pt = ((gt > lb - delta) & (gt < ub + delta)).float().mean()
            ece += abs(mean_pt - percent) * percent_diff
        delta_vals.append(ece)
        if ece < best_ece:
            best_delta = delta
            best_ece = ece

    ece = 0
    for percent in percentages:
        lb = torch.quantile(samples, 0.5 - percent / 2, dim=0, keepdim=True)
        ub = torch.quantile(samples, 0.5 + percent / 2, dim=0, keepdim=True)
        mean_pt = ((gt > lb - best_delta) & (gt < ub + best_delta)).float().mean()
        ece += abs(mean_pt - percent) * percent_diff

    return ece.item()
```

A more detailed explanation on the calibration process can be found [here](https://towardsdatascience.com/expected-calibration-error-ece-a-step-by-step-visual-explanation-with-python-code-c3e9aa12937d/
).


## References:

Guo, C., Pleiss, G., Sun, Y., & Weinberger, K. Q. (2017, July). On calibration of modern neural networks. In International conference on machine learning (pp. 1321-1330). PMLR.

Hore, A., & Ziou, D. (2010). Image quality metrics: PSNR vs. SSIM. In 2010 20th International Conference on Pattern Recognition (pp. 2366–2369). IEEE. https://doi.org/10.1109/ICPR.2010.579 (If available, replace with actual DOI or link to proceedings.)

Nieradzik, L. (n.d.). Metrics for uncertainty estimation. Retrieved March 6, 2025, from https://lars76.github.io/2020/08/07/metrics-for-uncertainty-estimation.html

Pavlovic, M. (2025, January). Expected calibration error (ECE): A step-by-step visual explanation. Towards Data Science. https://towardsdatascience.com/expected-calibration-error-ece-a-step-by-step-visual-explanation-with-python-code-c3e9aa12937d/
