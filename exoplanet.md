# EXOPLANET DETECTION WITH MACHINE LEARNING: NOISE AUGMENTATION


## 1 INTRODUCTION

- As we all know, there are lots of objects that exist in our universe, orbit, pull everything inside or burst. And, humanity wanted to understand the reason why they exist, the motion of them or the effects on the universe. The motion of the Earth, bursting of a star, or the structure of a black hole and its effects on spacetime. All of these made us curious and we did lots of observations with big telescopes or satellites. We analyzed these observations and saw exciting phenomena, the observation of different planets, special oscillations of the stars and merging of two black holes.

- But, in 1917, the first evidence was noted that a mass was outside of our solar system, it was also orbiting around a star, any confirmation did not pass into history. After years, 1992, that orbiting mass was confirmed that it exists in our universe. And they called it an “Exoplanet”.

- Detecting a planet has become a very extensive topic in astronomy since the first detection of an exoplanet. In time, astronomers developed some detection techniques for these masses such as transit method, radial velocity, gravitational microlensing and astrometry. First exoplanet was discovered with radial velocity, but the transit method is the most powerful method. 3421 exoplanets have been discovered by this method, totally 4528 of them are found with all these techniques.

### 1.1 Detection Methods 

#### 1.1.1 Transit Method

- When a planet passes directly between its orbiting star and an observer, it prevents us from observing the star’s light by a measurable amount. 

#### 1.1.2 Radial Velocity

- Orbiting planets cause stars to wobble in space, in other words it causes the color of the light astronomers. When it starts to move in the direction of the observer the star’s light spectrum shifts towards blue, if not, it towards red. With this method 879 exoplanets have been discovered.

#### 1.1.3 Direct Imaging

- By taking pictures and removing the overwhelming glare of the stars that they orbit. With this method 54 planets have been found.

#### 1.1.4 Gravitational Microlensing

- The coming light from a distant star is bent and focused by gravity as a planet passes between the star and the observer. The planets bend spacetime, due to this effect the light coming from a distant star and a closer star’s becomes together instantly and this creates a pick at the brightness curve, light curve. With that 116 planets have been found.


#### 1.1.5 Astrometry

- The existence of an exoplanet makes some perturbation of the stars’ oscillation by a small amount. With this method only one exoplanet was discovered.






- Nevertheless, the transit method seems so powerful, sometimes we cannot see that dim of the brightness of the star obviously or if the exoplanet does not pass between the Sun and the Earth while it is orbiting, we cannot detect the exoplanet easily. However, in recent years, machine learning has contributed to exoplanet detection, some projects have been done with light curve data, getting from TESS (Transiting Exoplanet Survey Satellite). 




### 1.2 Machine Learning

- Machine Learning became a very common and useful tool from, of course, computer science to natural sciences, even in arts, since it makes the heavy works lighter. For example, detecting small earthquakes can be too hard, but using Machine Learning, we can get some good results in an easier way, if you have a huge dataset. It is also used in Exoplanet Detection. In that case we need a “labeled” training dataset, because our aim is classifying whether there is an exoplanet or not. Once we have the training dataset we need to feed that data into artificial neural networks. In the training process, our machine learning model will try to decrease the “loss” as much as it can, the rest will be the “prediction” step, whether there exists an exoplanet or just a mass.


## 2 LIGHT CURVE DATA

- Detection of exoplanets requires, of course, data science and data analysis, and in this analysis astronomers use light curve data. Mainly, astronomers use two types of light curve data, which are Kepler light curve data and TESS light curve data. Their data formats are the same, the only difference is the light curve data is obtained in different ways, Kepler Space Telescope and Transiting Exoplanet Survey Satellite (TESS).  

- It contains information about time, the brightness (aperture photometry flux) and its error, moment-derived row/column centroid and their errors, aperture photometry flux after pre-search data conditioning and its error, column/row position correction based on bright stars, and finally, PSF (Probabilistic Spectrum Fitting) -fitted column/row centroid position correction based on bright stars. The unit of the data that is with flux is is e/s and the rest is in pixels. All of this information is located in “fits” light curve data format column by column. 

- According to these columns, we need to extract time domain features. In the previous works that are done with machine learning, Time Series Feature extraction based on scalable hypothesis tests (TSFresh) (Christ et al. 2018) is used. This process contains commonly used techniques such as Fourier Transform, resampling (with 1 hour interval), interpolation if the data is not complete and scaling. Once the time domain light curve data is extracted, we can start the machine learning stage.



## 3 PREVIOUS WORKS WITH MACHINE LEARNING

- Up to now, two main Exoplanet Detection with Machine Learning works exist with different light curve data which are Kepler Data (Shallue & Vanderburg, 2018) and TESS data (Yu et al. 2019). In all of these projects, a labeled training dataset is used. “PC” (Planet Candidate) labeled sample points counted as “1”, and the rest are counted as “0”. There is also one other project that is done with K2 photometry, after extracting features from photometry data, data points are labeled again like in the above condition (A. Malik et al. 2021)

### 3.1 Extraction of Features from Light Curve Data

- As said earlier in the second section, light curve data consists of information about photometry flux, moment derived centroid and so forth. But, we cannot use this data directly in the machine learning phase. Thus, we should calculate some measures according to raw light curve data in order to “extract” the features of the data, such as absolute energy of the raw light curve data. With these features, we need to create an array whose indexes are these features. (Also, after the extraction of feature process, another preprocessing can be done, removing redundant features from the array.)

- In the previous works, this process is done with a Python package, which is called TSFresh (Christ et al. 2018). This package is created in order to reduce time consumption for extracting features of data, especially for large data. It can extract various features like absolute maximum, Fourier entropy, skewness, standard deviation and so forth, it can extract 794 time series features. We can also arrange the features that will be extracted by specifying parameters. Also, for large datasets, TSFresh uses  Python’s “multiprocessing” function underhood; we can distribute the feature extraction to multiple cores.

<img src="https://github.com/koraydarwin/earthml/blob/master/img/exo.png">

- *Samples of raw TESS and feature extracted TESS light curve data.*


### 3.2 Training Dataset 

#### 3.2.1 Kepler Data

- In this work (Shallue & Vanderburg, 2018), the training dataset is created with Kepler data by Kepler data pipeline methods (Jenkins et al. 2010). In other words, all of the data points are spaced with 29.4 minutes, also some preprocessing is done. For the labeled training dataset the Autovetter Planet Candidate Catalog is used (Catanzarite 2015). For the training process, as said earlier, “PC” is counted “1” and the rest “0”. In that training set, there are 12137 non-planet candidate samples and 3600 planet candidate samples. 80% of the data is used for training, 10% is used for testing and 10% is used for validating.


#### 3.2.2 TESS Data

- For this work, the pipeline is so similar to the previous one, they followed some set of rules in order to do labeling (Yu et al. 2019). And, again “PC” is counted “1” and the rest “0”. In that training set, 492 planet candidate and 15959 non-planet candidate data points exist. Again similarly, 80% of the data is used for training, 10% is used for testing and 10% is used for validating.

#### 3.2.3 K2 Photometry Data

- In this work (A. Malik et al. 2021), they procured K2 photometry data from the Mikulski Archive for Space Telescopes (MAST). And, they followed some proprocess procedures for light curve training dataset, and for the labeled training dataset. For the Machine Learning part, again PC” is counted “1” and the rest “0” regardless what the data point is. 3,937 data points belong to planet candidate out of 7873 data points. For the training process, 90% of the data is used, the rest is used for validation.



## 4 OUR METHOD (NOISE AUGMENTATION)

- Data augmentation is a technique that is used for increasing the amount of data that already exists. And, it has great importance in machine learning. Lack of data causes troubles because a machine learning model will not be capable of doing a great prediction, this makes the model untrustable unfortunately. 

- Cropping, flipping, rotating and adding noise are the most known methods in machine learning, they are mostly used for image data, but recently, especially noise augmentation, is applied for time domain data, also its effects are being researched (Wen et al. 2021). In that work, the effect of adding noise is observed, but only Gaussian distribution function is used as noise source. In our method, we use different probabilistic distribution functions as noise; Rayleigh, exponential and Gaussian with different effects (as additive and multiplicative). 

- Recently, creating fake data by using machine learning, via GANs (Goodfellow et al. 2014), has become common, e.g. creating fake face images. In our noise augmentation method, we also create noise using GANs. 


### 4.1  Introduction to Noise Augmentation with Previous Works

### 4.2  Probability Distribution Functions

- In statistics, a probability density function is defined as whose value at any given point in the point space can be interpreted as providing a relative likelihood that the value of the random variable would be close to that sample. The main usage of a probability distribution function is calculating the probability of a given point that is between a specified interval, in other words calculating the integral of the function with the bounds (our interval). If we let the bounds as $ - \inf $ and $ \inf $ our integral should be equal to 1. This was for the continuous case, but if our probability density function is discrete, we need to sum up the probabilities of a given point that is located between an interval, similarly the result will be again 1. 

- And, there are different distribution functions with different properties, discrete or continuous, symmetric or non-symmetric and so forth. Gaussian (continuous and symmetric),  Rayleigh (continuous), Bernoulli (discrete), Poisson (discrete) distributions can be given as examples.


### 4.3 GANs



## 5 RESULTS



## 6 DISCUSSION



## 7 CONCLUSIONS






