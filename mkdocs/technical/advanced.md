# &#128008; Advanced

##  &#128272; API Authentication

In order to authenticate endpoints, it is necessary to include the `API_KEY=your-key-here` variable in the `.env` file. Multiple keys can be accepted by separating them with a pipe (`|`) as follows: `API_KEY=your-key-here|secondary_client_key`.

After configuration, all endpoints will require an `access_token` header for authentication, such as `access_token: your-key-here`. Failure to provide the correct access token will result in a 403 error.

!!! warning

    This kind of athentication is weak and it's intended for machine to machine communication, please do not rely on it and enforce other kind of stronger authentication such as OAuth2 for the client side.

!!! example
    **Authenticated API call:**
    === "Python"
        ```python
        import requests

        server_url = 'http://localhost:1865/'
        api_key = 'your-key-here'
        access_token = {'access_token': api_key}
        
        response = requests.get(server_url, headers=access_token)
        
        if response.status_code == 200:
            print(response.text)
        else:
            print('Error occurred: {}'.format(response.status_code))
        ```
    === "Node"
        ```javascript
        const request = require('request');
        
        const serverUrl = 'http://localhost:1865/';
        const apiKey = 'your-key-here';
        const access_token = {'access_token': apiKey};
        
        request({url: serverUrl, headers: access_token}, (error, response, body) => {
            if (error) {
                console.error(error);
            } else {
                if (response.statusCode === 200) {
                    console.log(body);
                } else {
                    console.error(`Error occurred: ${response.statusCode}`);
                }
            }
        });
        ```   

By adding the variable to the `.env` file, all Swagger endpoints (`localhost:1865/docs`) will require authentication and can be accessed on the top right-hand corner of the page through the green **Authorize** button.

## &#128300; Testing

To run tests, start the Cat as usual.  
Tests will run on the same containers you already launched, but with mock databases and plugin folder.
End to end (e2e) tests are found in `tests/routes`, while all the other folders contain unit tests and mocks / utilities.

### Run all tests

Open another terminal (in the same folder from where you start the Cat) and launch:

```bash
docker exec cheshire_cat_core python -m pytest --color=yes .
```

### Run a specific test file

If you want to run specific test files and not the whole suite, just specify the path:

```bash
docker exec cheshire_cat_core python -m pytest --color=yes tests/routes/memory/test_memory_recall.py
```

### Run a specific test function in a specific test file

You can also launch only one specific test function, using the `::` notation and the name of the function:

```bash
docker exec cheshire_cat_core python -m pytest --color=yes tests/routes/memory/test_memory_recall.py::test_memory_recall_with_k_success
```

## &#128450;&#65039; Memory Backup

### Create a full backup

To create a complete backup for the memories of your Cheshire Cat, you simply need to copy the `long_term_memory` folder located in the root directory. This will allow you to later load all the (declarative and episodic) memories into a new instance whenever you wish.   

### Restore a full backup

To load your backup into a clean installation of Cheshire Cat, you just need to copy the `long_term_memory` folder into the root directory at the same level as the `core` folder. In case you've already started an instance of Cheshire Cat, you will find the `long_term_memory` folder there; you can safely overwrite it.

!!! warning
    The `long_term_memory` folder will be protected, and you might need to use the admin permissions of your system to access it.

The terminal command to perform this operation is as follows:

```bash
sudo cp -r /path/to/source/cheshire_cat/long_term_memory /path/to/destination/cheshire_cat
```
