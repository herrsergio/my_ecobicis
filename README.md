# my-ecobicis

Get the status of my most used bike stations using serverless (Lambda service in AWS). Steps to install:

 1. Clone this repo.
 2. Install the `serverless` tool.
 
`sudo npm install -g serverless`
    
 3. `cd my-ecobicis`

 4. Execute the following commands:

`virtualenv env`

`source env/bin/activate`

`pip install httplib2`

`pip freeze > requirements.txt`

`npm init `

`npm install --save serverless-python-requirements`

5. `serverless deploy`
