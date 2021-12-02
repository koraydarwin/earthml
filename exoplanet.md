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

- According to these columns, we need to extract time domain features, and for training phase we will use the flux and time columns, like done in the previous works. But, there is another method that is used which is Time Series Feature extraction based on scalable hypothesis tests (TSFresh) (Christ et al. 2018). According to this method, they firstly extract the flux and time columns, then extracted some time domain data properties, like absolute energy. And, with this method they got better results compared to the previous works that TSFresh package was not used (A. Malik et al. 2021). This feature extraction process contains commonly used techniques such as Fourier Transform, resampling (with 1 hour interval), interpolation if the data is not complete and scaling.




## 3 PREVIOUS WORKS WITH MACHINE LEARNING

- Up to now, two main Exoplanet Detection with Machine Learning works exist with different light curve data which are Kepler Data (Shallue & Vanderburg, 2018) and TESS data (Yu et al. 2019). In all of these projects, a labeled training dataset is used. “PC” (Planet Candidate) labeled sample points counted as “1”, and the rest are counted as “0”. There is also one other project that is done with K2 photometry, after extracting features from photometry data, data points are labeled again like in the above condition (A. Malik et al. 2021)

### 3.1 Extraction of Features from Light Curve Data

- In the previous works, as said earlier, from light curve data, only flux and time data are extracted, and the machine learning  this process is done with a Python package, which is called TSFresh (Christ et al. 2018). This package is created in order to reduce time consumption for extracting features of data, especially for large data. It can extract various features like absolute maximum, Fourier entropy, skewness, standard deviation and so forth, it can extract 794 time series features. We can also arrange the features that will be extracted by specifying parameters. Also, for large datasets, TSFresh uses  Python’s “multiprocessing” function underhood; we can distribute the feature extraction to multiple cores. And the fallowings can be extracted from any time series data by using TSFresh. 

   - Absolute Energy 
   - Autocorrelation
   - Continuous Wavelet Transform Coefficients
   - Fourier Entropy 
   - Permutation Entropy
   - Time Reversal Asymmetry Statistic


<img src="https://github.com/koraydarwin/earthml/blob/master/img/tess_collage.png">

- *Samples of raw TESS and feature extracted (with respect to absolute value energy) TESS light curve data.*



### 3.2 Training Dataset 

#### 3.2.1 Kepler Data

- In this work (Shallue & Vanderburg, 2018), the training dataset is created with Kepler data by Kepler data pipeline methods (Jenkins et al. 2010). In other words, all of the data points are spaced with 29.4 minutes, also some preprocessing is done. For the labeled training dataset the Autovetter Planet Candidate Catalog is used (Catanzarite 2015). For the training process, as said earlier, “PC” is counted “1” and the rest “0”. In that training set, there are 12137 non-planet candidate samples and 3600 planet candidate samples. 80% of the data is used for training, 10% is used for testing and 10% is used for validating.


#### 3.2.2 TESS Data

- For this work, the pipeline is so similar to the previous one, they followed some set of rules in order to do labeling (Yu et al. 2019). And, again “PC” is counted “1” and the rest “0”. In that training set, 492 planet candidate and 15959 non-planet candidate data points exist. Again similarly, 80% of the data is used for training, 10% is used for testing and 10% is used for validating.

#### 3.2.3 K2 Photometry Data

- In this work (A. Malik et al. 2021), they procured K2 photometry data from the Mikulski Archive for Space Telescopes (MAST). And, they followed some proprocess procedures for light curve training dataset, and for the labeled training dataset. For the Machine Learning part, again PC” is counted “1” and the rest “0” regardless what the data point is. 3,937 data points belong to planet candidate out of 7873 data points. For the training process, 90% of the data is used, the rest is used for validation.


- In the previous works, (Shallue & Vanderburg, 2018) & (Yu et al. 2019) they trained the deep learning model with two different inputs by separating, binning, the light curve data. These are called "local view" and "global view", a local view shows the shape of the transit in detail in other words it is a close-up of the transit event, spanning no more than two transit durations on either side of the transit midpoint; and a global view shows the characteristics of the light curve over an entire orbital period. For the Kepler data, its period can converge to 4 years since its period may be too long, they grouped their phase-folded light curves into 2001 bins for the global view, and 201 bins for the local view. But, for the TESS data, since its period is around 27 days they grouped their phase folded light curves into 201 bins for the global view, and 61 bins for the local view.

<img src="https://github.com/koraydarwin/earthml/blob/master/img/glob_loc.png">

- *Samples of local and global views, PC: Planet Candidate; EB: Eclipsary Binary.*



## 4 OUR METHOD (NOISE AUGMENTATION)

- Data augmentation is a technique that is used for increasing the amount of data that already exists. And, it has great importance in machine learning. Lack of data causes troubles because a machine learning model will not be capable of doing a great prediction, this makes the model untrustable unfortunately. 

- Cropping, flipping, rotating and adding noise are the most known methods in machine learning, they are mostly used for image data, but recently, especially noise augmentation, is applied for time domain data, also its effects are being researched (Wen et al. 2021). In that work, the effect of adding noise is observed, but only Gaussian distribution function is used as noise source. In our method, we use different probabilistic distribution functions as noise; Rayleigh, exponential and Gaussian with different effects (as additive and multiplicative). 

- Recently, creating fake data by using machine learning, via GANs (Goodfellow et al. 2014), has become common, e.g. creating fake face images. In our noise augmentation method, we also create noise using GANs. 



<img src="https://render.githubusercontent.com/render/math?math=p(x) = \frac{1}{\sqrt{2\pi \sigma^2}} e^{\frac{-(x-\mu)^2}{2 \sigma^2}}">

  - *Gaussian Distribution Function <img src="https://render.githubusercontent.com/render/math?math=\mu"> is the mean <img src="https://render.githubusercontent.com/render/math?math=\sigma"> is the standard deviation*

<img src="https://render.githubusercontent.com/render/math?math=f(x, \frac{1}{\beta}) = \frac{1}{\beta} e^{\frac{-x}{\beta}}">

  - *Exponential Distribution Function <img src="https://render.githubusercontent.com/render/math?math=\beta"> is the scale value*

<img src="https://render.githubusercontent.com/render/math?math=P(x, \sigma) = \frac{x}{\sigma^2} e^{\frac{-x^2}{2\sigma^2}}">

  - *Rayleigh Distribution Function, <img src="https://render.githubusercontent.com/render/math?math=\sigma"> is the scale value*




### 4.1  Introduction to Noise Augmentation with Previous Works

- Noise augmentation is a fundamental tool because it encourages the model to learn the various aspects of each class by occluding random features, also, augmentation of any noise type makes the model more robust against the occurrence of that particular noise over the input data. And, there is no certainly accepted procedure to incorporate it with machine learning frameworks. According to the previous works, moise models that are distributed with different density functions are used for especially image training datasets, for Two Dimensional Convolutional Neural Networks. In the previous works Gaussian and the mixture of Gaussian and Poisson distribution functions are used in order to augment (Bovik, 2015), and their effect are explained in a positive way (Yin et al., 2015). Adding noise to the training data is not a unique procedure to the training of deep learning architectures: additive and multiplicative noise has long been used in signal processing for regression-based methods, in order to create more robust models. But, up to now, there is no systematic work done for time series data. It has been used, but the observation of its effect has not been done yet, our primary aim will be investigating its effects.

### 4.2  Probability Distribution Functions

- In statistics, a probability density function is defined as whose value at any given point in the point space can be interpreted as providing a relative likelihood that the value of the random variable would be close to that sample, simply, a probability distribution function that gives the probabilities of occurrence of different possible outcomes for an experiment. And, they can be classified in two classes which are discrete probability distribution and continuous probability distribution.

- From the definition, if the outcome of our experiment is dicrete, in other words, if we cannot have any value between the outcomes, then the counts of the events are discrete functions. Binomial distribution, Poisson distribution can be given as examples. But, if the outcome of our experiment may be observed between an interval, not only the bounds of the experiment, then the events are continuous function, and these functions are also known as probability density functions (PDF). Gaussian distribution, exponential distribution can be given as examples. The sum of the probabilities in continuous distribution function is one, the integral of the function with the bounds as <img src="https://render.githubusercontent.com/render/math?math=-\infty"> and <img src="https://render.githubusercontent.com/render/math?math=\infty"> is one.

- Python's NumPy package also has the property of random number generator with its "random" function according to the probability distribution function that we specified. Our approach is using that NumPy function, and generate random number, in our case these random numbers are "noise", with only continuous distribution functions (Gaussian, Rayleight and exponential). And, augmenting the light curve data with that noise with additive approach or multiplicative approach.


### 4.3 GANs

- Machine learning has been improving as time passes away, it has been used in many areas from science to economics. We solved prediction and classifying problems. We also created new data from a training dataset, Autoencoders and Variational Autoencoders, actually for a data analysis technique which is called “denoising”. But, in 2014, a new type of machine learning concept was designed which is called “General Adversarial Networks”, shortly GANs, by Ian Goodfellow. For any given training set, this method learns to generate new data with the same statistics as the training set. We have seen fake face photos everywhere, in this example GANs are used.

- GANs have mainly two components which are called “generator” and “discriminator”, both are classical deep learning models, but the main difference is that they are trained simultaneously by adversarial process. Generator model produces new data from a seed, i.e. random noise, by upsampling until we get the dimension that we want. And, the discriminator classifies the produced new data is whether fake or real. Discriminator will give negative output for fake data and positive output for real data. Until the losses of both discriminator and generator decays to some equilibrium point, the training process will continue.

- For its applications, it has been used for fashion, art and science, modeling the distribution of dark matter in a particular direction; fake faces are the most common one. Our approach is creating noise from noise, our training set will be noise instead of a fake image data. And, we will augment our light curve data with the noise that is produced by the output of our GAN models.

- In out case, we produced noise by using the "noise" data in the training light curve data, which are labeled as "0". To do we upsampled the training dataset in generator part, with Conv1D's Transpose, and the discriminator evaulated the generated data whether it is fake or not, with Conv1D. After the training phase, noise creation via GANs, we get the noise that can be added to the training dataset with appropriate dimensions.

<img src="https://github.com/koraydarwin/earthml/blob/master/img/generator.png">

- *The schematic version of the Generator.*

<img src="https://github.com/koraydarwin/earthml/blob/master/img/discriminator.png">

- *The schematic version of the Discriminator.*


## 5 RESULTS

- In the previous work that is done with TESS light curve data (Yu et al. 2019), they used Conv1D and simple Dense layers as a deep learning model, and they got 97.4% accuracy and 65% presicion in Triage mode, it classifies whether the data is an exoplanet or not, in Vetting mode, it classifies whether the data is an exoplanet or an eclipsing binaries or not, 97.8%. After this work, there is another work that uses gradient boosted tree (GBT) model via XGBoost package, which ensures us better results, 84% presicion. In these works, there is no data augmentation process, adding noise. In our approach, we firstly added two types of noises to TESS training dataset, noise that is created by GANs and noise which is the output of classical probability distribution functions. Secondly, we extracted the features from the noise augmented data. Finally, we tried various deep learning models that is produced by two packages which are Tensorflow and XGBoost. 


### 5.1 Architecture of the Previous Works


<img src="https://github.com/koraydarwin/earthml/blob/master/img/original_yu.png">

- *In this model, for the first input (i.e. global view) the number of the first One Dimensional Convolutional Neural Networks' filter size is 16 with 2 filter factor, 2 block size, 5 kernel size, 5 pooling size, 2 pool strides. For the second input (i.e. local view) the number of the first One Dimensional Convolutional Neural Networks' filter size is 16 with 2 filter factor, 2 block size, 5 kernel size, 7 pooling size, 2 pool strides.*


### 5.1 Experiments (--- Draft ---)

<img src="https://github.com/koraydarwin/earthml/blob/master/img/mod1.png">

- *First architecture.*

<img src="https://github.com/koraydarwin/earthml/blob/master/img/mod2.png">

- *Second architecture.*

<img src="https://github.com/koraydarwin/earthml/blob/master/img/mod3.png">

- *Third architecture.*
- 
<img src="https://github.com/koraydarwin/earthml/blob/master/img/mod4.png">

- *Fourth architecture.*

- *In all of these models (created with Tensorflow layers), we got 97% accuracy, 0% recall.*








## 6 DISCUSSION



## 7 CONCLUSIONS






