## Executing the script

### Native OS
1. `pip install requests`
2. `python costco.py`

### Container

1. [Install Docker](https://docs.docker.com/get-docker/)
2. Build the image  `docker build -t maysunfaisal/costco .`
3. Run the container (detach) `docker run -idt maysunfaisal/costco`
4. Check the container log `docker logs -f <Container ID>`. (Get the Container ID by executing `docker ps` to list the running containers)

TODO: expose the host sound device to the container, so that the `say` command works in a container as well