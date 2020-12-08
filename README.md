# Enode-URL-Generator
An ethereum enode URL generator

### How to start

- Clone this repo

  `git clone https://github.com/Dave0x21/Enode-URL-Generator.git`

- Move inside the repo directory

  `cd sendTx`

- Create a virtual env

  `python3 -m venv env`

- Use your virtual env

  `source env/bin/activate`

- Install requirements

  `pip install -r requirements.txt`
  
  ###### Basic Usage
  
`./enode.py privKey`

###### Example

`./enode.py 0x7400921efaf63382984b72d980341fc815d435814aec1728f2c2fb103d555260`

`Your enode url is: enode://e9042e87f502d6448321359e75316dcec97787a4cf29acf9814830ae0ab21911261ff10f8bf17dc9089647f09f97415130920e9e0e87f880d9557f4b910888f1@0.0.0.0:30303'


`./enode.py 0x7400921efaf63382984b72d980341fc815d435814aec1728f2c2fb103d555260 -i 192.168.1.1 -p 31303`

`Your enode url is: enode://e9042e87f502d6448321359e75316dcec97787a4cf29acf9814830ae0ab21911261ff10f8bf17dc9089647f09f97415130920e9e0e87f880d9557f4b910888f1@192.168.1.1:31303'

