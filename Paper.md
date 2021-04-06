# Noise Augmentation

**Outline**

- **Introduction**
  - **Additive Noise**
  - **Multiplicative Noise**
  - **The Distribution Functions That Are Used**

- **Sample histograms for distributions**
   - **Gaussian Distribution**
   - **Exponential Distribution**
   - **Poisson Distribution**
   - **Rayleigh Distribution**
   - **Gaussian and Poisson Distribution**
   - **Exponential and Poisson Distribution**

- **Visualizing noise distributions with example waveforms**
   - **Distribution Plots (in waveform status)**
   - **The Original Waveform (Raw) and Filtered Version**
   - **Augmented Versions of the Original Waveform**

- **Plots of the Augmented Waveforms (Experiments)**
   - **The Original Waveform**
   - **Gaussian Noise Augmented, EQTransformer's Noise Augmentation**
   - **Multiplicative Exponential Noise Augmented**
   - **Multiplicative  Poisson Noise Augmented**
   - **Multiplicative Rayleigh Noise Augmented**
   - **Additive Exponential Noise Augmented (Type-1)**
   - **Additive Exponential Noise Augmented (Type-2)**
   - **Additive Poisson Noise Augmented (Type-1)**
   - **Additive Poisson Noise Augmented (Type-2)**
   - **Additive Rayleigh Noise Augmented (Type-1)**
   - **Additive Rayleigh Noise Augmented (Type-2)**
   - **Additive Gaussian & Poisson Noise Augmented**
   - **Additive Exponential & Poisson Noise Augmented**

- **Comparison Between Models**
   - **Mean Absolure Error Comparison with Recpect to P - Arrival Time**
   - **Root Mean Square Error Comparison with Recpect to P - Arrival Time**
   - **Detection Presicion Comparison**
   - **Detection Recall Comparison**
   - **Comparison for Matched Event Numbers**
   - **Comparison for Detection Numbers**

   

## Introduction

- **Data augmentation are techniques to used for increasing the quantity of the data by applying some methods such as flipping, cropping, scaling, translating, and adding noise, but note that similar techniques can be seen on neural network architectures too, such as Dropout.**
 



- **These data augmentation techniques are generally used for photographs or audios in Deep Learning, but these techniques can be applied for earthquake data too. There is a model that does these techniques onto earthquake data, which is called EQTransformer.**





- **EQTransformer package uses additive Gaussian noise for waveform data. Our aim was changing the distribution function and the type of the noise, additive or multiplicative. Then, observing the change in the number of detection, detected events, root mean square error, and mean average error.**


- **Also, before moving to the functions that are used, we need to define the types of noise:**



### Additive Noise

- **Let <img src="https://render.githubusercontent.com/render/math?math=f(x)"> be our seismic signal, and <img src="https://render.githubusercontent.com/render/math?math=f(x)"> is composed of <img src="https://render.githubusercontent.com/render/math?math=g(x)"> and <img src="https://render.githubusercontent.com/render/math?math=n(x)"> where <img src="https://render.githubusercontent.com/render/math?math=n(x)"> is noise and <img src="https://render.githubusercontent.com/render/math?math=g(x)"> is our desired component of our signal. Then, <img src="https://render.githubusercontent.com/render/math?math=f(x) = g(x)+n(x)">. Gaussian noise is the most encountered noise class. In our research, the effect of the change in the distribution function is observed. EQTransformer also uses Gaussian Distribution.**






### Multiplicative Noise

- **The same logic is again valid, the formulation is a little bit different. It is <img src="https://render.githubusercontent.com/render/math?math=f(x)=g(x)*(1+n(x))">. Here  is again noise, but for this one, the most common variant is “speckle noise”. For remarking, speckle noise is generally seemed on coherent light imaging. And, again in the observation, <img src="https://render.githubusercontent.com/render/math?math=n(x)"> changed variously.**




### The Distribution Functions That Are Used



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
   
 

   
   
   
 ## Visualizing noise distributions with example waveforms
 
   
   
- **An earthquake data can be represented like an NumPy array since it is a signal. Also, the noise that are created by distribution functions can be also shown like a waveform signal because it is an array. And, here is the plots of the signals.**


### Distribution Plots (in waveform status)


<img src="https://github.com/koraydarwin/earthml/blob/master/img/waveform.png">  





- *All plots above belong to the previous distributions that are shown with histograms.*

- *On these plots, we can see the signal forms of the distributions with different scales on the same plot. Orange signals are created with greater scale value (8; orange signals), for some plots, we can see that greater scale dominates the other signal, which is created with lower scale value (5; blue signals).*





### The Original Waveform (Raw) and Filtered Version


- **In order to see the effect of the scale parameter, the distribution that are created above should be added onto original waveform.**


<img src="https://github.com/koraydarwin/earthml/blob/master/img/14.png"> 


  - *The above plot belongs to original waveform data, that already includes background noise (titled with "raw"). And, below the "raw" titled plot, we see that the filtered version of the raw waveform data. Also, note that this waveform is between the 10.55 and 11.05 interval, 26th of September 2019. (Network Name: KO, Station Name: SLVT)* 




### Augmented Versions of the Original Waveform
  
  
<img src="https://github.com/koraydarwin/earthml/blob/master/img/eqsigcollage.png"> 

   - *The above plots shows that the signals, that are shown in the previous sub-section, are added onto the original waveform. In other words, simply augmented versions are shown. You see some blue signals, which are augmented with lower scaled (5) signal. Orange signals are created with higher scale value (8).*



   
   
   
## Plots of the Augmented Waveforms (Experiments)



- **Up to that point, the mathematical explanation of the distribution functions with formulas, the difference between  them, the effect of the values that are used (scale) are shown by signal plots.**


- **The purpose of the task is adding or multiply the signals that are created by NumPy modules with our original earthquake signal, and training with augmented noise, nine different augmentation effect will be shown.**


- **Now, the effect of the different noise signals will be shown with the plots. Also, we will compare the noise signal with the natural background noise, car traffic, wind and so on.**






- **Before the augmentation, let's see the original waveform again.**




### The Original Waveform


<img src="https://github.com/koraydarwin/earthml/blob/master/img/1.png"> 



  - *The above plot belongs to original waveform data, that already includes background noise. Also, this waveform is between the 10.55 and 11.05 interval, 26th of September 2019. (Network Name: KO, Station Name: SLVT).*
  
  
- **Now, the fallowing plots shows the augmented version of the original waveform and its augmented spectrogram, additive or multiplicative noise are taken into account.**





### Gaussian Noise Augmented, EQTransformer's Noise Augmentation

<img src="https://github.com/koraydarwin/earthml/blob/master/img/2.png">
  
   - *The left and the right sides of the augmented waveform plot are amplified a little bit.*
   
   
   
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

<img src="https://github.com/koraydarwin/earthml/blob/master/img/3.png">

   - *As can be seen, the scale of the plot changed and during the mid of the plot, the shape also changed.*
   
   
   
   
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

<img src="https://github.com/koraydarwin/earthml/blob/master/img/4.png">

   - *As can be seen, the scale of the plot changed and during the mid of the plot, the shape also changed.*
   
   
   
   
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

<img src="https://github.com/koraydarwin/earthml/blob/master/img/5.png">

   - *Again, as can be seen, the scale of the plot changed and during the mid of the plot, the shape also changed.*


   
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

<img src="https://github.com/koraydarwin/earthml/blob/master/img/6.png">

   - *The scale did not change, and the shape of the new augmented waveform is similar to the original one.*
 
   
   
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

<img src="https://github.com/koraydarwin/earthml/blob/master/img/7.png">

   - *The scale and the shape is changed too much.*


   
   
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

<img src="https://github.com/koraydarwin/earthml/blob/master/img/8.png">

   - *The scale did not change, and the shape of the new augmented waveform is similar to the original one.*


   
   
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

<img src="https://github.com/koraydarwin/earthml/blob/master/img/9.png">

   - *The scale changed, but the shape is again similar to the original.*


   
   
   
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

<img src="https://github.com/koraydarwin/earthml/blob/master/img/10.png">

   - *The scale did not change, and the shape of the new augmented waveform is similar to the original one.*


   
   
   
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

<img src="https://github.com/koraydarwin/earthml/blob/master/img/11.png">
   
   - *The scale and the shape is changed too much.*
   


   
   
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


<img src="https://github.com/koraydarwin/earthml/blob/master/img/12.png">

   - *The amplitude is increased with respect to original waveform.*
   
   

   
   
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


<img src="https://github.com/koraydarwin/earthml/blob/master/img/13.png">

   - *The amplitude is increased, and the silhouette is similar to the original waveform, but more noisy.*
   
   
   
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






## Comparison Between Models
   
   
   
- **Up to that point, the effect of the noise augmentation with different noise types, different distribution functions. From that point, the waveform data is trained by EQTransformer's Trainer function, with microSTEAD data. Another model is also created which is original EQTransformer's noised. And, the machine learning model (h5 file format) is released.**



- **The next step that needed to be done is detecting. In order to do it, EQTransformer's mseed predictor should be used with the model that is created. The rest is completely comparison with respect to earthquake catalog, of course the difference between the machine learning models can be observed according to root mean square error and mean average error. But, in order to get these errors, EQTransformer's Tester function whose output is a csv file, includes  some errors.**

  
   
 
 
### Mean Absolute Error Comparison with Recpect to P - Arrival Time

<img src="https://github.com/koraydarwin/earthml/blob/master/img/pmaef.png">

   - *As can be seen, we have less error compared to original model.*
   
### Root Mean Square Error Comparison with Recpect to P - Arrival Time

<img src="https://github.com/koraydarwin/earthml/blob/master/img/prmsef.png">

   - *As can be seen, we have less error compared to original model, again.*
   
   
### Detection Presicion Comparison

<img src="https://github.com/koraydarwin/earthml/blob/master/img/det_pre.png">



### Detection Recall Comparison


<img src="https://github.com/koraydarwin/earthml/blob/master/img/recall.png">



- **The previous plots shows the comparison between models according to errors. Now, the comparison for the number of detected event numbers and the number of matched event numbers with the catalog. As be said before, you need to use mseed predictor function whose output is a csv file which contains event start time, P wave arrival time, S wave arrival time and so on.**



### Comparison for Matched Event Numbers

<img src="https://github.com/koraydarwin/earthml/blob/master/img/match_final.png">

   - *The comparison with the catalog is done according to P wave arrival time.*
   

### Comparison for Detection Numbers

<img src="https://github.com/koraydarwin/earthml/blob/master/img/detection_final.png">

   - *More events is detected rather than the original model.*
   
   


