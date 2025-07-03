---
title: "[Paper] Spatio-Temporal Fusion Enhances Crime Prediction Using Multi-Source Data"
excerpt_separator: "<!--more-->"
categories:
  - Blog
tags:
  - Post Formats
  - readability
  - standard
---
The study proposes a novel method for crime prediction by merging historical crime data with transitional zones identified from VIIRS nightlight imagery. Crime prediction plays a crucial role in optimizing police resource allocation for crime prevention. While existing approaches focus on historical crime or environmental variables linked to criminal patterns, this research introduces a novel spatio-temporal Cokriging algorithm blending multi-source data for more accurate crime forecasting.

Utilizing time-series historical crime data as the primary variable and urban transitional zones derived from nightlight imagery as the secondary co-variable, the algorithm was implemented to predict street crimes and hotspots in Cincinnati, Ohio, on a weekly basis. Validation techniques, including statistical tests, Predictive Accuracy Index (PAI), and Predictive Efficiency Index (PEI) tests, were employed to assess prediction accuracy compared to a control group not using the co-variable.

The findings highlight the algorithm's effectiveness, revealing a notable improvement in prediction accuracy. Statistical tests indicated an increase of 5.4% in the correlation coefficient for weekdays and 12.3% for weekends when utilizing the proposed method. Moreover, in hotspot tests, the algorithm exhibited higher hit rates measured by PAI/PEI, further confirming its predictive efficacy.

This innovative spatio-temporal Cokriging approach demonstrates promising results in enhancing crime prediction accuracy by incorporating transitional zones from nightlight imagery alongside historical crime data. The method's ability to improve correlation coefficients and achieve higher hit rates in predicting crime hotspots signifies its potential for optimizing law enforcement strategies by providing more precise crime forecasts. Overall, this research introduces a promising avenue for advancing crime prediction models by leveraging multi-source data integration in spatio-temporal domains.

[See original post](https://www.tandfonline.com/doi/full/10.1080/13658816.2020.1737701)