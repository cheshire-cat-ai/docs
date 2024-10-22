# Errors

#### Why am I getting the error `RateLimitError` in my browser console?

Please check if you have a valid credit card connected or if you have used up all the credits of your OpenAI trial period.

#### Docker has no permissions to write

This is a matter with your docker installation or the user you run docker from. Usually you can resolve it by using **sudo** command before calling any docker command, but it's better to create a `docker` group on your Linux system and give [root-level privileges](https://docs.docker.com/engine/install/linux-postinstall/) to docker.

#### The Cat seems not to be working from inside a Virtual Machine

In VirtualBox, you can select Settings->Network, then choose NAT in the "Attached to" drop down menu. Select "Advanced" to configure the port forwarding rules. Assuming the guest IP of your VM is 10.0.2.15 (the default) and the ports configured in the .env files are the defaults, you have to set at least the following rule:

| Rule name | Protocol | Host IP     | Host Port | Guest IP   | Guest Port |
|-----------|----------|-------------|-----------|------------|------------|
| Rule 1    | TCP      | 127.0.0.1   | 1865      | 10.0.2.15  | 1865       |

If you want to work on the documentation of the Cat, you also have to add one rule for port 8000 which is used by `mkdocs`, and to configure `mkdocs` itself to respond to all requests (not only localhost as per the default).

#### Proxy HTTPS and Mixed content

I'm using the Cat behind an HTTPS proxy but the login page tries to load some assets over HTTP instead of HTTPS. It seems to be related to `url_for('core-static', ...)`.

![alt text](../assets/img/faq/https_mixed_content.png)

You need to configure the [`CCAT_HTTPS_PROXY_MODE`](../production/administrators/env-variables.md/?h=ccat_https_proxy_mode#ccat_https_proxy_mode) environment variable