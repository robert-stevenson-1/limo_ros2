# Introduction to developing with Docker and VS Code

You can watch a live demo of the [Visual Studio Code Remote - Containers](https://www.youtube.com/watch?v=TVcoGLL6Smo) on YouTube.

### Why Docker

[Docker](https://docs.docker.com/get-started/overview/) provides OS-level virtualisation, allowing for the deployment of software packages in isolated environments called containers. 

![Docker Architecture](./assets/docker_architecture.svg)

*Images are prepacked beforehand and become containers when run on Docker Engine*

### Docker vs virtual machines

Docker and virtual machines provide similar benefits, however, they are functionally different. 

![Docker VM Differences](./assets/docker_vm_diff.png)

### Visual Studio Code First Time Setup on Local PC

#### [Required extensions for VS Code](https://code.visualstudio.com/docs/editor/extension-marketplace)
* Remote Development
```bash
code  --install-extension ms-vscode-remote.vscode-remote-extensionpack
```

#### Connect to LIMO and start container

1. SSH into the LIMO using VS Code
    * In VS Code, Ctrl + Shift + P to bring up the command pallete
    * (Do once if static IP assigned) Search for "Remote-SSH: Add new SSH Host..."
    * ssh agilex@<limo_IP>
    * Bring up command pallete again, search for "Remote-SSH: Connect to Host..."
    * Once connected, "File" -> "Open Folder" and navigate to limo_ros2 workspace

2. Run docker image
    * Once in the workspace, VS Code should detect the Dockerfile and ask to build container
    * Alternatively, Ctrl + Shift + P to bring up the command pallete and search for Remote-Containers: Rebuild Container

### References
* [VS Code Remote Development](https://code.visualstudio.com/docs/remote/remote-overview)
* [Useful template for reference](https://github.com/athackst/vscode_ros2_workspace)