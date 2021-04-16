def noise_aug(nois_type):
    
    
    
    noise_type = input()
    
    --------------"noise type can be"-----------------
    
    "expo_mul: multiplicative exponential"
    "pois_mul: multiplicative Poisson"
    "ray_mul: multiplicative Rayleigh"
    "add_expo: additive exponential"
    "add_pois: additive Poisson"
    "add_ray: additive Rayleigh"
    "gauss_pois: additive Gaussian and Poisson"
    "expo_pois: additive exponential and Poisson"
    
    ---------------------------------------------------
    
    
   
    -----"expo_mul"------
    
    if noise_type == "expo_mul":
        
        f = open("EqT_utils.py", "r")

        lst = []
        for x in f:
            lst.append(x)
            
            
     mulexpo = ["    def _add_noise(self, data, snr, rate): \n",
          "        'Randomly add Gaussian noie with a random SNR into waveforms' \n",
          "",
          "        data_noisy = np.empty((data.shape)) \n",
          "        if np.random.uniform(0, 1) < rate and all(snr >= 10.0): \n",
          "            data_noisy = np.empty((data.shape)) \n",
          "            data_noisy[:, 0] = data[:,0] * (1 + np.random.exponential(np.random.randint(0,10), data.shape[0])) \n",
          "            data_noisy[:, 1] = data[:,1] * (1 + np.random.exponential(np.random.randint(0,10), data.shape[0])) \n",
          "            data_noisy[:, 2] = data[:,2] * (1 + np.random.exponential(np.random.randint(0,10), data.shape[0])) \n",
          "        else: \n",
          "            data_noisy = data \n",
          "        return data_noisy \n  "]
            
            
        for i in range(218,230):
            lst[i] = lst[i].replace(lst[i], mulexpo[i-218])
    
    
        for i in range(724,736):
            lst[i] = lst[i].replace(lst[i], mulexpo[i-724])
    
    
        for i in range(1156,1166):
            lst[i] = lst[i].replace(lst[i], mulexpo[i-1156])
            
        with open("expo_mul.py", 'w') as output:
            for row in lst:
                output.write(str(row))
                
                
                
    -----"pois_mul"------ 
    
    
    elif noise_type == "pois_mul":
        
        f = open("EqT_utils.py", "r")

        lst = []
        for x in f:
            lst.append(x)
            
            
        mulpois = ["    def _add_noise(self, data, snr, rate): \n",
          "        'Randomly add Gaussian noie with a random SNR into waveforms' \n",
          "",
          "        data_noisy = np.empty((data.shape)) \n",
          "        if np.random.uniform(0, 1) < rate and all(snr >= 10.0):  \n",
          "            data_noisy = np.empty((data.shape)) \n",
          "            data_noisy[:, 0] = data[:,0] * (1 + np.random.poisson(np.random.randint(0,10), data.shape[0])) \n",
          "            data_noisy[:, 1] = data[:,1] * (1 + np.random.poisson(np.random.randint(0,10), data.shape[0])) \n",
          "            data_noisy[:, 2] = data[:,2] * (1 + np.random.poisson(np.random.randint(0,10), data.shape[0])) \n",
          "        else: \n",
          "            data_noisy = data \n",
          "        return data_noisy \n  "]

            
        for i in range(218,230):
            lst[i] = lst[i].replace(lst[i], mulpois[i-218])
    
    
        for i in range(724,736):
            lst[i] = lst[i].replace(lst[i], mulpois[i-724])
    
    
        for i in range(1156,1166):
            lst[i] = lst[i].replace(lst[i], mulpois[i-1156])
            
        with open("pois_mul.py", 'w') as output:
            for row in lst:
                output.write(str(row))
                
                
                
    -----"ray_mul"------
    
    
    elif noise_type == "ray_mul":
        
        f = open("EqT_utils.py", "r")

        lst = []
        for x in f:
            lst.append(x)
            
            
            
        mulray = ["    def _add_noise(self, data, snr, rate): \n",
          "        'Randomly add Gaussian noie with a random SNR into waveforms' \n",
          "",
          "        data_noisy = np.empty((data.shape)) \n",
          "        if np.random.uniform(0, 1) < rate and all(snr >= 10.0):  \n",
          "            data_noisy = np.empty((data.shape)) \n",
          "            data_noisy[:, 0] = data[:,0] * (1 + np.random.rayleigh(np.random.randint(0,10), data.shape[0])) \n",
          "            data_noisy[:, 1] = data[:,1] * (1 + np.random.rayleigh(np.random.randint(0,10), data.shape[0])) \n",
          "            data_noisy[:, 2] = data[:,2] * (1 + np.random.rayleigh(np.random.randint(0,10), data.shape[0])) \n",
          "        else: \n",
          "            data_noisy = data \n",
          "        return data_noisy \n  "]
        
            
        for i in range(218,230):
            lst[i] = lst[i].replace(lst[i], mulray[i-218])
    
    
        for i in range(724,736):
            lst[i] = lst[i].replace(lst[i], mulray[i-724])
    
    
        for i in range(1156,1166):
            lst[i] = lst[i].replace(lst[i], mulray[i-1156])
            
        with open("ray_mul.py", 'w') as output:
            for row in lst:
                output.write(str(row))   
                
                
                
                
    -----"add_expo"------
    
    
    elif noise_type == "add_expo":
        
        f = open("EqT_utils.py", "r")

        lst = []
        for x in f:
            lst.append(x)
            
            
        add_expo = ["    def _add_noise(self, data, snr, rate): \n",
          "        'Randomly add Gaussian noie with a random SNR into waveforms' \n",
          "",
          "        data_noisy = np.empty((data.shape)) \n",
          "        if np.random.uniform(0, 1) < rate and all(snr >= 10.0): \n",
          "            data_noisy = np.empty((data.shape)) \n",
          "            data_noisy[:, 0] = data[:,0] + np.random.exponential(int(np.random.randint(0,10)*max(data[:,0])), data.shape[0]) \n",
          "            data_noisy[:, 1] = data[:,1] + np.random.exponential(int(np.random.randint(0,10)*max(data[:,1])), data.shape[0]) \n",
          "            data_noisy[:, 2] = data[:,2] + np.random.exponential(int(np.random.randint(0,10)*max(data[:,2])), data.shape[0]) \n",
          "        else: \n",
          "            data_noisy = data \n",
          "        return data_noisy \n  "]
            
        for i in range(218,230):
            lst[i] = lst[i].replace(lst[i], add_expo[i-218])
    
    
        for i in range(724,736):
            lst[i] = lst[i].replace(lst[i], add_expo[i-724])
    
    
        for i in range(1156,1166):
            lst[i] = lst[i].replace(lst[i], add_expo[i-1156])
            
        with open("add_expo.py", 'w') as output:
            for row in lst:
                output.write(str(row))   
                
                
                
    -----"add_pois"------
    
    
    elif noise_type == "add_pois":
        
        f = open("EqT_utils.py", "r")

        lst = []
        for x in f:
            lst.append(x)
            
            
        add_pois = ["    def _add_noise(self, data, snr, rate): \n",
          "        'Randomly add Gaussian noie with a random SNR into waveforms' \n",
          "",
          "        data_noisy = np.empty((data.shape)) \n",
          "        if np.random.uniform(0, 1) < rate and all(snr >= 10.0): \n",
          "            data_noisy = np.empty((data.shape)) \n",
          "            data_noisy[:, 0] = data[:,0] + np.random.poisson(int(np.random.randint(0,10)*max(data[:,0])), data.shape[0]) \n",
          "            data_noisy[:, 1] = data[:,1] + np.random.poisson(int(np.random.randint(0,10)*max(data[:,1])), data.shape[0]) \n",
          "            data_noisy[:, 2] = data[:,2] + np.random.poisson(int(np.random.randint(0,10)*max(data[:,2])), data.shape[0]) \n",
          "        else: \n",
          "            data_noisy = data \n",
          "        return data_noisy \n  "]
            
        for i in range(218,230):
            lst[i] = lst[i].replace(lst[i], add_pois[i-218])
    
    
        for i in range(724,736):
            lst[i] = lst[i].replace(lst[i], add_pois[i-724])
    
    
        for i in range(1156,1166):
            lst[i] = lst[i].replace(lst[i], add_pois[i-1156])
            
        with open("add_pois.py", 'w') as output:
            for row in lst:
                output.write(str(row))   
                
                
                
                
    -----"add_ray"------     
    
    
    elif noise_type == "add_ray":
        
        f = open("EqT_utils.py", "r")

        lst = []
        for x in f:
            lst.append(x)
            
            
        add_ray = ["    def _add_noise(self, data, snr, rate): \n",
          "        'Randomly add Gaussian noie with a random SNR into waveforms' \n",
          "",
          "        data_noisy = np.empty((data.shape)) \n",
          "        if np.random.uniform(0, 1) < rate and all(snr >= 10.0): \n",
          "            data_noisy = np.empty((data.shape)) \n",
          "            data_noisy[:, 0] = data[:,0] + np.random.rayleigh(int(np.random.randint(0,10)*max(data[:,0])), data.shape[0]) \n",
          "            data_noisy[:, 1] = data[:,1] + np.random.rayleigh(int(np.random.randint(0,10)*max(data[:,1])), data.shape[0]) \n",
          "            data_noisy[:, 2] = data[:,2] + np.random.rayleigh(int(np.random.randint(0,10)*max(data[:,2])), data.shape[0]) \n",
          "        else: \n",
          "            data_noisy = data \n",
          "        return data_noisy \n  "]
            
        for i in range(218,230):
            lst[i] = lst[i].replace(lst[i], add_ray[i-218])
    
    
        for i in range(724,736):
            lst[i] = lst[i].replace(lst[i], add_ray[i-724])
    
    
        for i in range(1156,1166):
            lst[i] = lst[i].replace(lst[i], add_ray[i-1156])
            
        with open("add_ray.py", 'w') as output:
            for row in lst:
                output.write(str(row))   
                
                
                
    -----"gauss_pois"------
    
    
    elif noise_type == "gauss_pois ":
        
        f = open("EqT_utils.py", "r")

        lst = []
        for x in f:
            lst.append(x)
            
            
        gauss_pois = ["    def _add_noise(self, data, snr, rate): \n",
          "        'Randomly add Gaussian noie with a random SNR into waveforms' \n",
          "",
          "        data_noisy = np.empty((data.shape)) \n",
          "        if np.random.uniform(0, 1) < rate and all(snr >= 10.0):  \n",
          "            data_noisy = np.empty((data.shape)) \n",
          "            data_noisy[:, 0] = data[:,0] + np.random.normal(0, np.random.uniform(0.01, 0.1)*max(data[:,0]), data.shape[0]) + np.random.poisson(np.random.uniform(0.01, 0.1)*max(data[:,0]), data.shape[0]) \n",
          "            data_noisy[:, 1] = data[:,1] + np.random.normal(0, np.random.uniform(0.01, 0.1)*max(data[:,1]), data.shape[0]) + np.random.poisson(np.random.uniform(0.01, 0.1)*max(data[:,1]), data.shape[0]) \n",
          "            data_noisy[:, 2] = data[:,2] + np.random.normal(0, np.random.uniform(0.01, 0.1)*max(data[:,2]), data.shape[0]) + np.random.poisson(np.random.uniform(0.01, 0.1)*max(data[:,2]), data.shape[0]) \n",
          "        else: \n",
          "            data_noisy = data \n",
          "        return data_noisy \n  "]
            
        for i in range(218,230):
            lst[i] = lst[i].replace(lst[i], gauss_pois[i-218])
    
    
        for i in range(724,736):
            lst[i] = lst[i].replace(lst[i], gauss_pois[i-724])
    
    
        for i in range(1156,1166):
            lst[i] = lst[i].replace(lst[i], gauss_pois[i-1156])
            
        with open("gauss_pois.py", 'w') as output:
            for row in lst:
                output.write(str(row))   
                
                
                
                
                
                
                
    -----"expo_pois"------
    
    
    elif noise_type == "expo_pois":
        
        f = open("EqT_utils.py", "r")

        lst = []
        for x in f:
            lst.append(x)
            
            
        expo_pois = ["    def _add_noise(self, data, snr, rate): \n",
          "        'Randomly add Gaussian noie with a random SNR into waveforms' \n",
          "",
          "        data_noisy = np.empty((data.shape)) \n",
          "        if np.random.uniform(0, 1) < rate and all(snr >= 10.0): \n",
          "            data_noisy = np.empty((data.shape)) \n",
          "            data_noisy[:, 0] = data[:,0] + np.random.exponential(np.random.uniform(0.01, 0.15)*max(data[:,0]), data.shape[0]) + np.random.poisson(np.random.uniform(0.01, 0.15)*max(data[:,0]), data.shape[0]) \n",
          "            data_noisy[:, 1] = data[:,1] + np.random.exponential(np.random.uniform(0.01, 0.15)*max(data[:,1]), data.shape[0]) + np.random.poisson(np.random.uniform(0.01, 0.15)*max(data[:,1]), data.shape[0]) \n",
          "            data_noisy[:, 2] = data[:,2] + np.random.exponential(np.random.uniform(0.01, 0.15)*max(data[:,2]), data.shape[0]) + np.random.poisson(np.random.uniform(0.01, 0.15)*max(data[:,2]), data.shape[0]) \n",
          "        else: \n",
          "            data_noisy = data \n",
          "        return data_noisy \n  "]
            
        for i in range(218,230):
            lst[i] = lst[i].replace(lst[i], expopois[i-218])
    
    
        for i in range(724,736):
            lst[i] = lst[i].replace(lst[i], expopois[i-724])
    
    
        for i in range(1156,1166):
            lst[i] = lst[i].replace(lst[i], expopois[i-1156])
            
        with open("expo_pois.py", 'w') as output:
            for row in lst:
                output.write(str(row))    
                
                
                
    f = open("trainer.py", "r")
    lst = []
    for x in f:
        lst.append(x)
    

        
    new = "from" + " " +  noise_type + " " + "import DataGenerator, _lr_schedule, cred2, PreLoadGenerator, data_reader \n"
    lst[26] = lst[26].replace(lst[26], new)
    
    with open(noise_type + "_train.py", 'w') as output:
        for row in lst:
            output.write(str(row)) 
            
            
    #from noise_type_train import noise_aug
    
   
    
         
