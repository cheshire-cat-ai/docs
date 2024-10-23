The Cat installation is open by default, which means that all APIs are publicly accessible.  
Below is a summary of the steps necessary to secure the installation.

* Change the password for all the users using via Admin Portal

* Secure the REST APIs and WebSocket by setting the following [environment](http://127.0.0.1:8000/docs/production/administrators/env-variables/) variables:
```bash
CCAT_API_KEY=a-very-long-and-alphanumeric-secret
CCAT_API_KEY_WS=another-very-long-and-alphanumeric-secret
```
* Set a JWT hash secret to encrypt user data:
```bash
CCAT_JWT_SECRET=yet-another-very-long-and-alphanumeric-secret
```