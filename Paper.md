# Noise Augmentation

**Outline**

- **Sample histograms for distributions**
   - **Gaussian Distribution**
   - **Exponential Distribution**
   - **Poisson Distribution**
   - **Rayleigh Distribution**
   - **Gaussian and Poisson Distribution**
   - **Exponential and Poisson Distribution**

- **Visualizing noise distributions with example waveforms**
   - **Gaussian Distribution (Waveform status)**
   - **Exponential Distribution (Waveform status)**
   - **Poisson Distribution (Waveform status)**
   - **Rayleigh Distribution (Waveform status)**
   - **Gaussian and Poisson Distributio (Waveform status)n**
   - **Exponential and Poisson Distribution (Waveform status)**
   



- **Data augmentation are techniques to used for increasing the quantity of the data by applying some methods such as flipping, cropping, scaling, translating, and adding noise, but note that similar techniques can be seen on neural network architectures too, such as Dropout.**
 



- **These data augmentation techniques are generally used for photographs or audios in Deep Learning, but these techniques can be applied for earthquake data too. There is a model that does these techniques onto earthquake data, which is called EQTransformer.**





- **EQTransformer package uses additive Gaussian noise for waveform data. Our aim was changing the distribution function and the type of the noise, additive or multiplicative. Then, observing the change in the number of detection, detected events, root mean square error, and mean average error. The functions that are used are;**



 - **Exponential Distribution**


 - **Poisson Distribution**


 - **Rayleigh Distribution**


 - **Gaussian Distribution**
 
 
   - **And the graph for formulas and some properties of these distribution functions;**



<img src="https://github.com/koraydarwin/earthml/blob/master/img/formula_table.png">



 
 
 
- **To visualize the distributions, we create samples from each distribution using NumPy's random module and plot histograms**


## Sample histograms for distributions


### Gaussian Distribution


<img src="https://github.com/koraydarwin/earthml/blob/master/img/gaussian_plot.png">

   - *The above plot shows the Gaussian distribution function with a random scale, which is between 0.01 and 0.15, original EQTransformer noise augmentation parameters. And, the size is 60001.*




### Exponential Distribution


<img src="https://github.com/koraydarwin/earthml/blob/master/img/exponential_plot.png">

 
   
   - *As can be seen, the shape of the plot is similar to each other. In contrast, if we look at the y-axis of the plot we will see that the magnitude of the axis is decreased, it becomes broader.*


   
   
### Poisson Distribution
   
<img src="https://github.com/koraydarwin/earthml/blob/master/img/poisson_plot.png">



   - *As can be seen, the magnitude of the y-axis again changes, becomes broader. And, the shape changes a little bit as lambda value changes.*
   
   

### Rayleigh Distribution
   
<img src="https://github.com/koraydarwin/earthml/blob/master/img/rayleigh_plot.png">

   
   
   - *As can be seen, the scale factor alpha changes the magnitude of the y-axis, becomes broader, and the shape a little bit around the 5-10 interval on x-axis.*


   

### Gaussian and Poisson Distribution (Poisson is added directly onto Gaussian Distribution with same scale)

<img src="https://github.com/koraydarwin/earthml/blob/master/img/gausspois_plot.png">

 
   - *The scale of the y-axis is decreased, becomes broader, and mid of the plot is intense, like Gaussian Distribution.*




### Exponential and Poisson Distribution (Exponential is added directly onto Poisson Distribution with same scale)

<img src="https://github.com/koraydarwin/earthml/blob/master/img/expopois_plot.png">

   
   - *The scale of the y-axis is decreased, broader, and its shape is similar to Exponential Distribution.*
   
   

- **Also, the effect of the scale parameter can be shown as fallowing:**


<img src="https://upload.wikimedia.org/wikipedia/commons/d/d7/Effects_of_a_scale_parameter_on_a_positive-support_probability_distribution.gif" width="400" height="400" />

   - *That one shows the effect of a scale parameter over a probability distribution.*
   
 
 
<img src="https://upload.wikimedia.org/wikipedia/commons/3/36/Effect_of_a_scale_parameter_over_a_mixture_of_two_normal_probability_distributions.gif" width="400" height="400" />


   - *And, this one shows the effect of a scale parameter over a mixture of two probability distributions.*
   
   
   
 ## Visualizing noise distributions with example waveforms
 
   
   
- **An earthquake data can be represented like an NumPy array since it is a signal. Also, the noise that are created by distribution functions can be also shown like a waveform signal because it is an array. And, here is the plots of the signals.**


### Gaussian Distributions (Waveform status)


<img src="https://github.com/koraydarwin/earthml/blob/master/img/original_sig.png">  



### Exponential Distributions (Waveform status)


<img src="https://github.com/koraydarwin/earthml/blob/master/img/nosig_expo.png">  

   
   
### Poisson Distributions (Waveform status)

<img src="https://github.com/koraydarwin/earthml/blob/master/img/nosig_pois.png"> 



### Rayleigh Distributions (Waveform status)

<img src="https://github.com/koraydarwin/earthml/blob/master/img/nosig_ray.png"> 
 


### Gaussian and Poisson Distributions (Waveform status)
   
<img src="https://github.com/koraydarwin/earthml/blob/master/img/nosig_gausspois.png"> 



### Exponential and Poisson Distributions (Waveform status)

<img src="https://github.com/koraydarwin/earthml/blob/master/img/nosig_expopois.png"> 



- *All plots above belong to the previous distributions that are shown with histograms.*

- *On these plots, we can see the signal forms of the distributions with different scales on the same plot. Orange signals are created with greater scale value, for some plots, we can see that greater scale dominates the other signal, which is created with lower scale value.*




- **In order to see the effect of the scale parameter, the distribution that are created above should be added onto original waveform.**


### The Original Waveform


<img src="https://github.com/koraydarwin/earthml/blob/master/img/original_wave.png"> 


  - *The above plot belongs to original waveform data, that already includes background noise. Also, this waveform is between the 10.55 and 11.05 interval, 26th of September 2019. (Network Name: KO, Station Name: SLVT)*
  
  
  
<img src="https://github.com/koraydarwin/earthml/blob/master/img/scale_ex_1.png"> 

   - *The above plot shows mixture of the original waveform and first exponential distribution, since the magnitude of the original waveform is too much, noise could not show its effect.*


<img src="https://github.com/koraydarwin/earthml/blob/master/img/scale_ex_2.png"> 

   - *The above plot shows mixture of the original waveform and second exponential distribution, since the magnitude of the original waveform is too much, noise could not show its effect, again.*
   

<img src="https://github.com/koraydarwin/earthml/blob/master/img/scale_poi_1.png"> 

   - *The above plot shows mixture of the original waveform and first Poisson distribution, since the magnitude of the original waveform is too much, noise could not show its effect, again.*
   

<img src="https://github.com/koraydarwin/earthml/blob/master/img/scale_poi_2.png">

   - *The above plot shows mixture of the original waveform and second Poisson distribution, since the magnitude of the original waveform is too much, noise could not show its effect, again.*


<img src="https://github.com/koraydarwin/earthml/blob/master/img/scale_ray_1.png"> 

   - *The above plot shows mixture of the original waveform and first Rayleigh distribution, since the magnitude of the original waveform is too much, noise could not show its effect, again.*
   

<img src="https://github.com/koraydarwin/earthml/blob/master/img/scale_ray_2.png"> 

   - *The above plot shows mixture of the original waveform and second Rayleigh distribution, since the magnitude of the original waveform is too much, noise could not show its effect, again.*
   

<img src="https://github.com/koraydarwin/earthml/blob/master/img/scale_sevde1_1.png"> 

   - *The above plot shows mixture of the original waveform and first Gaussian & Poisson distribution, since the magnitude of the original waveform is too much, noise could not show its effect, again.*
   

<img src="https://github.com/koraydarwin/earthml/blob/master/img/scale_sevde1_2.png"> 

   - *The above plot shows mixture of the original waveform and second Gaussian & Poisson distribution, since the magnitude of the original waveform is too much, noise could not show its effect, again.*
   

<img src="https://github.com/koraydarwin/earthml/blob/master/img/scale_sevde2_1.png"> 

   - *The above plot shows mixture of the original waveform and first Poisson & exponential distribution, since the magnitude of the original waveform is too much, noise could not show its effect, again.*
   
   
<img src="https://github.com/koraydarwin/earthml/blob/master/img/scale_sevde2_2.png"> 

   - *The above plot shows mixture of the original waveform and second Poisson & exponential distribution, since the magnitude of the original waveform is too much, noise could not show its effect, again.*

   
   
   




- **Up to that point, the mathematical explanation of the distribution functions with formulas, the difference between  them, the effect of the values that are used (scale) are shown by signal plots.**


- **The purpose of the task is adding or multiply the signals that are created by NumPy modules with our original earthquake signal, and training with augmented noise, nine different augmentation effect will be shown.**


- **Now, the effect of the different noise signals will be shown with the plots. Also, we will compare the noise signal with the natural background noise, car traffic, wind and so on.**






#### Additive Noise

- **Let $f(x)$ be our seismic signal, and $f(x)$ is composed of g(x) and $n(x)$ where $n(x)$ is noise and $g(x)$ is our desired component of our signal. Then, $ f(x) = g(x) + n(x)$. Gaussian noise is the most encountered noise class. In our research, the effect of the change in the distribution function is observed. EQTransformer also uses Gaussian Distribution.**


#### Multiplicative Noise

- **The same logic is again valid, the formulation is a little bit different. It is $f(x) = g(x) . (1 + n(x))$. Here $n(x)$ is again noise, but for this one, the most common variant is “speckle noise”. For remarking, speckle noise is generally seemed on coherent light imaging. And, again in the observation, $n(x)$ changed variously.**


- **Before the augmentation, let's see the original waveform again.**




### The Original Waveform


<img src="https://github.com/koraydarwin/earthml/blob/master/img/original_wave.png"> 


  - *The above plot belongs to original waveform data, that already includes background noise. Also, this waveform is between the 10.55 and 11.05 interval, 26th of September 2019. (Network Name: KO, Station Name: SLVT)*
  
  
- **Now, the fallowing plots shows the augmented version of the original waveform, additive or multiplicative noise are taken into account.**



## Results


### Gaussian Noise Augmented, EQTransformer's Noise Augmentation

<img src="https://github.com/koraydarwin/earthml/blob/master/img/original_augmented.png">
  
   - *The left and the right sides of the augmented waveform plot are amplified a little bit.*
   
<img src="https://github.com/koraydarwin/earthml/blob/master/img/original_spec.png">

   - *The spectrogram of the augmented waveform data (10.55 - 11.05 26th of September 2019)* 
   
   
- **And the augmentation function is here;**




```json
def _add_noise(self, data, snr, rate):
        'Randomly add Gaussian noie with a random SNR into waveforms'
        
        data_noisy = np.empty((data.shape))
        if np.random.uniform(0, 1) < rate and all(snr >= 10.0): 
            data_noisy = np.empty((data.shape))
            data_noisy[:, 0] = data[:,0] + np.random.normal(0, np.random.uniform(0.01, 0.15)*max(data[:,0]), data.shape[0])
            data_noisy[:, 1] = data[:,1] + np.random.normal(0, np.random.uniform(0.01, 0.15)*max(data[:,1]), data.shape[0])
            data_noisy[:, 2] = data[:,2] + np.random.normal(0, np.random.uniform(0.01, 0.15)*max(data[:,2]), data.shape[0])    
        else:
            data_noisy = data
        return data_noisy   
```





### Multiplicative Exponential Noise Augmented

<img src="https://github.com/koraydarwin/earthml/blob/master/img/expo_mul.png">

   - *As can be seen, the scale of the plot changed and during the mid of the plot, the shape also changed.*
   
<img src="https://github.com/koraydarwin/earthml/blob/master/img/multi-expo.png">

   - *The spectrogram of the augmented waveform data (10.55 - 11.05 26th of September 2019)* 
   
   
   
- **And the augmentation function is here;**




```json
def _add_noise(self, data, snr, rate):
        'Randomly add Gaussian noie with a random SNR into waveforms'
        
        data_noisy = np.empty((data.shape))
        if np.random.uniform(0, 1) < rate and all(snr >= 10.0): 
            data_noisy = np.empty((data.shape))
            data_noisy[:, 0] = data[:,0] * (1 + np.random.exponential(np.random.randint(0,10), data.shape[0]))
            data_noisy[:, 1] = data[:,1] * (1 + np.random.exponential(np.random.randint(0,10), data.shape[0]))
            data_noisy[:, 2] = data[:,2] * (1 + np.random.exponential(np.random.randint(0,10), data.shape[0]))    
        else:
            data_noisy = data
        return data_noisy    
```


   
   
   
   
### Multiplicative Poisson Noise Augmented

<img src="https://github.com/koraydarwin/earthml/blob/master/img/poisson_mul.png">

   - *As can be seen, the scale of the plot changed and during the mid of the plot, the shape also changed.*
   
<img src="https://github.com/koraydarwin/earthml/blob/master/img/multi-poi.png">

   - *The spectrogram of the augmented waveform data (10.55 - 11.05 26th of September 2019)* 
   
   
   
- **And the augmentation function is here;**




```json
def _add_noise(self, data, snr, rate):
        'Randomly add Gaussian noie with a random SNR into waveforms'
        
        data_noisy = np.empty((data.shape))
        if np.random.uniform(0, 1) < rate and all(snr >= 10.0): 
            data_noisy = np.empty((data.shape))
            data_noisy[:, 0] = data[:,0] * (1 + np.random.poisson(np.random.randint(0,10), data.shape[0]))
            data_noisy[:, 1] = data[:,1] * (1 + np.random.poisson(np.random.randint(0,10), data.shape[0]))
            data_noisy[:, 2] = data[:,2] * (1 + np.random.poisson(np.random.randint(0,10), data.shape[0]))  
        else:
            data_noisy = data
        return data_noisy   
```


   
   
   
   
### Multiplicative Rayleigh Noise Augmented

<img src="https://github.com/koraydarwin/earthml/blob/master/img/ray_mul.png">

   - *Again, as can be seen, the scale of the plot changed and during the mid of the plot, the shape also changed.*

<img src="https://github.com/koraydarwin/earthml/blob/master/img/multi-ray.png">

   - *The spectrogram of the augmented waveform data (10.55 - 11.05 26th of September 2019)* 
   
- **And the augmentation function is here;**




```json
def _add_noise(self, data, snr, rate):
        'Randomly add Gaussian noie with a random SNR into waveforms'
        
        data_noisy = np.empty((data.shape))
        if np.random.uniform(0, 1) < rate and all(snr >= 10.0): 
            data_noisy = np.empty((data.shape))
            data_noisy[:, 0] = data[:,0] * (1 + np.random.rayleigh(np.random.randint(0,10), data.shape[0]))
            data_noisy[:, 1] = data[:,1] * (1 + np.random.rayleigh(np.random.randint(0,10), data.shape[0]))
            data_noisy[:, 2] = data[:,2] * (1 + np.random.rayleigh(np.random.randint(0,10), data.shape[0]))  
        else:
            data_noisy = data
        return data_noisy     
```


   
      
   

   
   
### Additive Exponential Noise Augmented (Type-1)

<img src="https://github.com/koraydarwin/earthml/blob/master/img/expo_add_1.png">

   - *The scale did not change, and the shape of the new augmented waveform is similar to the original one.*

<img src="https://github.com/koraydarwin/earthml/blob/master/img/expo-typ1.png">

   - *The spectrogram of the augmented waveform data (10.55 - 11.05 26th of September 2019)* 
   
   
- **And the augmentation function is here;**




```json
def _add_noise(self, data, snr, rate):
        'Randomly add Gaussian noie with a random SNR into waveforms'
        
        data_noisy = np.empty((data.shape))
        if np.random.uniform(0, 1) < rate and all(snr >= 10.0): 
            data_noisy = np.empty((data.shape))
            data_noisy[:, 0] = data[:,0] + np.random.exponential(np.random.randint(0,10), data.shape[0])
            data_noisy[:, 1] = data[:,1] + np.random.exponential(np.random.randint(0,10), data.shape[0])
            data_noisy[:, 2] = data[:,2] + np.random.exponential(np.random.randint(0,10), data.shape[0])   
        else:
            data_noisy = data
        return data_noisy       
```


   
      
      




### Additive Exponential Noise Augmented (Type-2)

<img src="https://github.com/koraydarwin/earthml/blob/master/img/expo_add_2.png">

   - *The scale and the shape is changed too much.*

<img src="https://github.com/koraydarwin/earthml/blob/master/img/expo-typ2.png">

   - *The spectrogram of the augmented waveform data (10.55 - 11.05 26th of September 2019)* 
   
   
- **And the augmentation function is here;**




```json
def _add_noise(self, data, snr, rate):
        'Randomly add Gaussian noie with a random SNR into waveforms'
        
        data_noisy = np.empty((data.shape))
        if np.random.uniform(0, 1) < rate and all(snr >= 10.0): 
            data_noisy = np.empty((data.shape))
            data_noisy[:, 0] = data[:,0] + np.random.exponential(int(np.random.randint(0,10)*max(data[:,0])), data.shape[0])
            data_noisy[:, 1] = data[:,1] + np.random.exponential(int(np.random.randint(0,10)*max(data[:,1])), data.shape[0])
            data_noisy[:, 2] = data[:,2] + np.random.exponential(int(np.random.randint(0,10)*max(data[:,2])), data.shape[0])    
        else:
            data_noisy = data
        return data_noisy   
```


   
      
   


### Additive Poisson Noise Augmented (Type-1)

<img src="https://github.com/koraydarwin/earthml/blob/master/img/poisson_add_1.png">

   - *The scale did not change, and the shape of the new augmented waveform is similar to the original one.*

<img src="https://github.com/koraydarwin/earthml/blob/master/img/poi-typ1.png">

   - *The spectrogram of the augmented waveform data (10.55 - 11.05 26th of September 2019)* 
   
   
- **And the augmentation function is here;**




```json
 def _add_noise(self, data, snr, rate):
        'Randomly add Gaussian noie with a random SNR into waveforms'
        
        data_noisy = np.empty((data.shape))
        if np.random.uniform(0, 1) < rate and all(snr >= 10.0): 
            data_noisy = np.empty((data.shape))
            data_noisy[:, 0] = data[:,0] + np.random.poisson(np.random.randint(0,10), data.shape[0])
            data_noisy[:, 1] = data[:,1] + np.random.poisson(np.random.randint(0,10), data.shape[0])
            data_noisy[:, 2] = data[:,2] + np.random.poisson(np.random.randint(0,10), data.shape[0])    
        else:
            data_noisy = data
        return data_noisy   
```


   
      
   


### Additive Poisson Noise Augmented (Type-2)

<img src="https://github.com/koraydarwin/earthml/blob/master/img/poisson_add_2.png">

   - *The scale changed, but the shape is again similar to the original.*

<img src="https://github.com/koraydarwin/earthml/blob/master/img/poi-typ2.png">

   - *The spectrogram of the augmented waveform data (10.55 - 11.05 26th of September 2019)* 
   
   
   
- **And the augmentation function is here;**




```json
def _add_noise(self, data, snr, rate):
        'Randomly add Gaussian noie with a random SNR into waveforms'
        
        data_noisy = np.empty((data.shape))
        if np.random.uniform(0, 1) < rate and all(snr >= 10.0): 
            data_noisy = np.empty((data.shape))
            data_noisy[:, 0] = data[:,0] + np.random.poisson(int(np.random.randint(0,10)*max(data[:,0])), data.shape[0])
            data_noisy[:, 1] = data[:,1] + np.random.poisson(int(np.random.randint(0,10)*max(data[:,1])), data.shape[0])
            data_noisy[:, 2] = data[:,2] + np.random.poisson(int(np.random.randint(0,10)*max(data[:,2])), data.shape[0])   
        else:
            data_noisy = data
        return data_noisy   
```


   
      
   


### Additive Rayleigh Noise Augmented (Type-1)

<img src="https://github.com/koraydarwin/earthml/blob/master/img/ray_add_1.png">

   - *The scale did not change, and the shape of the new augmented waveform is similar to the original one.*

<img src="https://github.com/koraydarwin/earthml/blob/master/img/ray-typ1.png">

   - *The spectrogram of the augmented waveform data (10.55 - 11.05 26th of September 2019)* 
   
   
   
- **And the augmentation function is here;**




```json
def _add_noise(self, data, snr, rate):
        'Randomly add Gaussian noie with a random SNR into waveforms'
        
        data_noisy = np.empty((data.shape))
        if np.random.uniform(0, 1) < rate and all(snr >= 10.0): 
            data_noisy = np.empty((data.shape))
            data_noisy[:, 0] = data[:,0] + np.random.rayleigh(np.random.randint(0,10), data.shape[0])
            data_noisy[:, 1] = data[:,1] + np.random.rayleigh(np.random.randint(0,10), data.shape[0])
            data_noisy[:, 2] = data[:,2] + np.random.rayleigh(np.random.randint(0,10), data.shape[0]) 
        else:
            data_noisy = data
        return data_noisy   
```


   
      
   


### Additive Rayleigh Noise Augmented (Type-2)

<img src="https://github.com/koraydarwin/earthml/blob/master/img/ray_add_2.png">
   
   - *The scale and the shape is changed too much.*
   

<img src="https://github.com/koraydarwin/earthml/blob/master/img/ray-typ2.png">

   - *The spectrogram of the augmented waveform data (10.55 - 11.05 26th of September 2019)* 
   
   
- **And the augmentation function is here;**




```json
def _add_noise(self, data, snr, rate):
        'Randomly add Gaussian noie with a random SNR into waveforms'
        
        data_noisy = np.empty((data.shape))
        if np.random.uniform(0, 1) < rate and all(snr >= 10.0): 
            data_noisy = np.empty((data.shape))
            data_noisy[:, 0] = data[:,0] + np.random.rayleigh(int(np.random.randint(0,10)*max(data[:,0])), data.shape[0])
            data_noisy[:, 1] = data[:,1] + np.random.rayleigh(int(np.random.randint(0,10)*max(data[:,1])), data.shape[0])
            data_noisy[:, 2] = data[:,2] + np.random.rayleigh(int(np.random.randint(0,10)*max(data[:,2])), data.shape[0])    
        else:
            data_noisy = data
        return data_noisy   
```


   
      
   
### Additive Gaussian & Poisson Noise Augmented


<img src="https://github.com/koraydarwin/earthml/blob/master/img/sevde_augmented_1.png">

   - *The amplitude is increased with respect to original waveform.*
   
   
<img src="https://github.com/koraydarwin/earthml/blob/master/img/sevde_spectrogram_1.png">

   - *The spectrogram of the augmented waveform data (10.55 - 11.05 26th of September 2019)* 
   
   
- **And the augmentation function is here;**


```json
def _add_noise(self, data, snr, rate):
        'Randomly add Gaussian noie with a random SNR into waveforms'
        
        data_noisy = np.empty((data.shape))
        if np.random.uniform(0, 1) < rate and all(snr >= 10.0): 
            data_noisy = np.empty((data.shape))

            max_data0 = max(data[:,0])
            data_noisy[:, 0] = data[:,0] + np.random.normal(0, np.random.uniform(0.01, 0.1) * max_data0, data.shape[0]) + np.random.poisson(np.random.uniform(0.01, 0.1) * max_data0, data.shape[0])
            
            max_data1 = max(data[:,1])
            data_noisy[:, 1] = data[:,1] + np.random.normal(0, np.random.uniform(0.01, 0.1) * max_data1, data.shape[0]) + np.random.poisson(np.random.uniform(0.01, 0.1) * max_data1, data.shape[0])

            max_data2 = max(data[:,2])
            data_noisy[:, 2] = data[:,2] + np.random.normal(0, np.random.uniform(0.01, 0.1) * max_data2, data.shape[0]) + np.random.poisson(np.random.uniform(0.01, 0.1) * max_data2, data.shape[0])

        else:
            data_noisy = data
        return data_noisy  
```





### Additive Exponential & Poisson Noise Augmented


<img src="https://github.com/koraydarwin/earthml/blob/master/img/sevde_augmented_2.png">

   - *The amplitude is increased, and the silhouette is similar to the original waveform, but more noisy.*
   
   
<img src="https://github.com/koraydarwin/earthml/blob/master/img/sevde_spectrogram_2.png">

   - *The spectrogram of the augmented waveform data (10.55 - 11.05 26th of September 2019)* 
   
   
- **And the augmentation function is here;**


```json
def _add_noise(self, data, snr, rate):
        'Randomly add Gaussian noie with a random SNR into waveforms'
        
        data_noisy = np.empty((data.shape))
        if np.random.uniform(0, 1) < rate and all(snr >= 10.0): 
            data_noisy = np.empty((data.shape))

            data_noisy[:, 0] = data[:,0] + np.random.exponential(np.random.uniform(0.01, 0.15)*max(data[:,0]), data.shape[0]) + np.random.poisson(np.random.uniform(0.01, 0.15)*max(data[:,0]), data.shape[0])
            data_noisy[:, 1] = data[:,1] + np.random.exponential(np.random.uniform(0.01, 0.15)*max(data[:,1]), data.shape[0]) + np.random.poisson(np.random.uniform(0.01, 0.15)*max(data[:,1]), data.shape[0])
            data_noisy[:, 2] = data[:,2] + np.random.exponential(np.random.uniform(0.01, 0.15)*max(data[:,2]), data.shape[0]) + np.random.poisson(np.random.uniform(0.01, 0.15)*max(data[:,2]), data.shape[0])   
        else:
            data_noisy = data
        return data_noisy   
```








  

- **As you all know, car traffic, wind or ocean currents may affect the waveform that we took from a seismogram. If you look at a waveform data that are taken from two different located seismograms, also the time is same, you will realize that the waveform differs because of these effects. Now, that background noise will be compared with our artificial noise. And here is the original background noise.**



<img src="https://github.com/koraydarwin/earthml/blob/master/img/original_noise.png">

   - *You can see the difference between the background and artificial noise, scale and shape are too different.*
   
   
   
   
- **Up to that point, the effect of the noise augmentation with different noise types, different distribution functions and the difference between artificial and our artificial noise are shown. From that point, the waveform data is trained by EQTransformer's Trainer function, with microSTEAD data. Another model is also created which is original EQTransformer's noised. And, the machine learning model (h5 file format) is released.**



- **The next step that needed to be done is detecting. In order to do it, EQTransformer's mseed predictor should be used with the model that is created. The rest is completely comparison with respect to earthquake catalog, of course the difference between the machine learning models can be observed according to root mean square error and mean average error. But, in order to get these errors, EQTransformer's Tester function whose output is a csv file, includes  some errors.**

  
   
 
 
### Mean Average Error Comparison

<img src="https://github.com/koraydarwin/earthml/blob/master/img/pmaef.png">

   - *As can be seen, we have less error compared to original model.*
   
### Root Mean Square Error Comparison

<img src="https://github.com/koraydarwin/earthml/blob/master/img/prmsef.png">

   - *As can be seen, we have less error compared to original model, again.*
   
   
### Detection Presicion Comparison

<img src="https://github.com/koraydarwin/earthml/blob/master/img/det_pre.png">



- **The previous plots shows the comparison between models according to errors. Now, the comparison for the number of detected event numbers and the number of matched event numbers with the catalog. As be said before, you need to use mseed predictor function whose output is a csv file which contains event start time, P wave arrival time, S wave arrival time and so on.**



### Comparison for Matched Event Numbers

<img src="https://github.com/koraydarwin/earthml/blob/master/img/match_final.png">

   - *The comparison with the catalog is done according to P wave arrival time.*
   

### Comparison for Detection Numbers

<img src="https://github.com/koraydarwin/earthml/blob/master/img/detection_final.png">

   - *More events is detected rather than the original model.*
   
   


```python

```
