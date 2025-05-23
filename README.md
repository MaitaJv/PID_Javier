# Proyecto de investigacion y desarrollo - Facultad Regional Buenos Aires
> Estación de recepción de señales electromagnéticas satelitales y terrestres para monitoreo y educación en la Facultad Regional Buenos Aires
Participación de Javier Maita 

# Images processing
This python program add to a crude image, received by NOAA sats (NOAA 15, NOAA 18, NOAA 19), information of the capture, like capture time, capture date, and the NOAA that made the capture.
Pillow library is need to run successfully the program, you can install it executing  this command in the terminal
```sh
pip install pillow
```

#### Parameters 
To execute successfully the program, this will wait for 1 parameter, the rute of the image
```sh
python3 addData.py image-path/image.png
```