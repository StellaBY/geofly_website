---
title: "[Paper] ST-Cokriging: Assimilating Multi-Scale Remote Sensing for Enhanced Resolution"
excerpt_separator: "<!--more-->"
categories:
  - Blog
tags:
  - Post Formats
  - readability
  - standard
---
The paper introduces a spatio-temporal Cokriging (ST-Cokriging) method, addressing the limitations of individual satellite remote sensing systems that cannot provide Earth surface observations with high spatial and temporal resolutions simultaneously. Due to the inherent trade-off between satellite orbit revisit frequency and sensor spatial resolution, this new method aims to assimilate multi-scale remote sensing data acquired by various systems with diverse temporal sampling frequencies and spatial resolutions.

Extending the traditional Cokriging technique into the spatio-temporal domain, the ST-Cokriging algorithm considers spatial, temporal, and spatio-temporal covariance structures within and between different datasets. This approach explicitly incorporates spatial and temporal covariances, enabling accurate assimilation of remote sensing data with varying resolutions and temporal frequencies.

In comparison to previous downscaling methods like STARFM and FSDAF, the ST-Cokriging method offers more precise and reliable assimilation results, especially in heterogeneous regions, while providing associated uncertainty estimates. The researchers developed a Python-based software package within the ArcGIS environment to implement this method effectively.

To illustrate the method's effectiveness, the study assimilated MODIS images (daily, 250 m, and 500 m spatial resolution) and Landsat TM/ETM+ images (16 days revisit cycle, 30 m) to generate daily spectral bands and NDVI images at 30 m spatial resolution. Validation and accuracy assessments revealed that ST-Cokriging effectively mitigates data gaps caused by cloud cover, producing reliable assimilation outcomes and uncertainty estimates at both high spatial and temporal frequencies.

In summary, the ST-Cokriging method demonstrated substantial advancements in assimilating multi-scale remote sensing data, offering improved accuracy and reliability in generating high-resolution and high-frequency composite imagery while providing estimates of uncertainty.

[See original post](https://www.sciencedirect.com/science/article/abs/pii/S0034425720305630?via%3Dihub)
