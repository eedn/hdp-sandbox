# HDP-sandbox
Hortonworks sandbox containers simplified install.  
This was created for multiple people to use on a single computer for practice purposes.

## tl;dr:
   ```$ git clone https://github.com/eedn/hdp-sandbox.git```



## Requirements:
  - Docker
  - docker-compose
  - python3
    -  yaml
    -  argparse

## Run
To make personalized docker-compose-{user_id}.yml file,  
Execute :  

   ```$ python3 generate_compose.py {user_id}```  

   and run docker with :  

   ```$ docker-compose -f docker-compose-{user_id}.yml up -d ```

   ```$ docker exec -it sandbox-proxy-{user_id} nginx -s reload```

Ambari will be exposed in localhost __port {user_id}8080__  
(ex. In case user_id = 3, access with __localhost:38080__ )

### Log in to sandbox-hdp to reset admin password:

```$ docker exec -it sandbox-hdp bash```

Then:

```$ ambari-admin-password-reset```

## Stop
   ```$ docker-compose -f docker-compose-{user_id}.yml stop```

## Start
   ```$ docker-compose -f docker-compose-{user_id}.yml start```

## Remove
This command remove container. (Remove with data)  
   ```$ docker-compose -f docker-compose-{user_id}.yml down```