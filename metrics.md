# Introduction

The page provides a summary and code snippet of all relevant metrics in the reverse imaging problem space. The Jupyter notebook version of this section can be found in `notebooks/metrics.ipynb`.

## Peak-Signal-to-Noise Ratio (PSNR)

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

## Structural Similarity Index Measure (SSIM)

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

### Negative Log-Likelihood (NLL)




#### Implemenation:
```python
def nll(x, mean, std):
    nll = (x-mean) ** 2 / (2 * std ** 2) + 0.5 * np.log(2 * np.pi * std ** 2)
    return nll.mean().astype(float)
```

### Out of Distribution Rate (OODR)

#### Implemenation:
```python
def oodr(x, mean, std, threshold=4.0):
    ratio = np.abs(mean-x)/std
    return (ratio > threshold).mean()
```

### Expected Calibration Error (ECE)

ECE approximates by partitioning predictions into M equally-spaced bins (similar to the reliability diagrams) and taking a weighted average of the bins’ accuracy/confidence
difference. More precisely,

$$ECE = \sum_{m=1}^{M} \frac{|B_m|}{n} \left| \text{acc}(B_m) - \text{conf}(B_m) \right|$$

where $n$ is the number of samples. The difference between
$acc$ and $conf$ for a given bin represents the calibration gap.

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

A more detailed 

Citation:

@misc{Pavlovic_2025, title={Expected calibration error (ECE): A step-by-step visual explanation}, url={https://towardsdatascience.com/expected-calibration-error-ece-a-step-by-step-visual-explanation-with-python-code-c3e9aa12937d/}, journal={Towards Data Science}, author={Pavlovic, Maja}, year={2025}, month={Jan}} 

@inproceedings{hore2010image,
  title={Image quality metrics: PSNR vs. SSIM},
  author={Hore, Alain and Ziou, Djemel},
  booktitle={2010 20th international conference on pattern recognition},
  pages={2366--2369},
  year={2010},
  organization={IEEE}
}

@misc{towardsdatascienceExpectedCalibration,
	author = {Maja Pavlovic},
	title = {{E}xpected {C}alibration {E}rror ({E}{C}{E}): {A} {S}tep-by-{S}tep {V}isual {E}xplanation | {T}owards {D}ata {S}cience --- towardsdatascience.com},
	howpublished = {\url{https://towardsdatascience.com/expected-calibration-error-ece-a-step-by-step-visual-explanation-with-python-code-c3e9aa12937d/}},
	year = {},
	note = {[Accessed 06-03-2025]},
}

@misc{arxiv,
	author = {},
	title = {arxiv.org},
	howpublished = {\url{https://arxiv.org/pdf/1706.04599}},
	year = {},
	note = {[Accessed 06-03-2025]},
}
