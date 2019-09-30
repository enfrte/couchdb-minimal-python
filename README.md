# Couchdb with minimal Python

Using minimal Python to send data to CouchDB. Intended for use with IoT [pynus](https://github.com/aykevl/pynus) script which polls UART service output. This code sends data to CouchDB via HTTP request methods. 

### pynus.py

If you are using pynus.py you need to import simple_couchdb_requests and change on_notify()  

    # pynus.py
    
    import simple_couchdb_requests 

    def on_notify(characteristic, value):
        data = bytes(value).replace(b'\n', b'\r\n').decode('utf-8')
        
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        sensorId = hex(uuid.getnode())
        
        if (data[:5] == "temp="):
            # data looks like 'temp=-20\n\r'
            temperatureValue = data[5:].rstrip() # returns '-20'
        
        post_fields = {
            "sensorHumanId": "Leon",
            "sensorUuid": sensorId,
            "temperatureValue": float(temperatureValue),
            "recordedDate": timestamp
        } # Set POST fields here
        
        # disables SSL scanning
        #ssl._create_default_https_context = ssl._create_unverified_context
        
        simple_couchdb_requests.couchdb_connect('admin', 'password', 'http://192.168.1.109:5984')
        simple_couchdb_requests.couchdb_post('temperature', post_fields, True) 

### Working locally with CouchDB

In Fauxton, go to config.

Change the bind_address under [chttpd] and [httpd] from 127.0.0.1 to 0.0.0.0

Go to Control Panel > Windows Firewall > Advanced settings > Inbound rules > New rule

In the New rule settings

* Add the Program erl.exe in your CouchDB\erts-8.3\bin folder.
* Add the port 5984
* Select Public profile. 

Test the connection on another local device `curl http://YOUR-SERVER-IP:5984/`

Note, you might have to restart the CouchDB server. 

### Finishing up

Run the pynus.py script onthe RPi to get things moving. 

CouchDB has been quite fun to work with :)