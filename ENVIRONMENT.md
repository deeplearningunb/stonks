## Environment

Anaconda an open-source package manager, environment manager. We gonna use to meet the library installation needs and functionality that needed to run stonk scripts.

__OBS: This tutorial is to linux distributions__

### Step 1 - Retrieve the Latest Version of Anaconda

Go to website to download the latest version.

    https://www.anaconda.com/distribution/

### Step 2 — Download the Anaconda Bash Script

Copy the sh file and go to directory /tmp and paste

Or you can it with curl

    $ cd /tmp
    $ curl -O https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh

### Step 3 — Verify the Data Integrity of the Installer

Ensure the integrity of the installer with cryptographic hash verification through SHA-256 checksum:

    $ sha256sum Anaconda3-2019.10-Linux-x86_64.sh
    

    output
    46d762284d252e51cd58a8ca6c8adc9da2eadc82c342927b2f66ed011d1d8b53  Anaconda3-2019.10-Linux-x86_64.sh

### Step 4 — Run the Anaconda Script

    $ bash Anaconda3-2019.10-Linux-x86_64.sh

This step its to do the installation, so just accept the recomendations to complete the installation.

__OBS: If you are using any different shell, you need to start the installation from it, not bash__

    $ zsh Anaconda3-2019.10-Linux-x86_64.sh

### Step 5 — Activate Installation

To activate the installation command, just run:

    $ source ~/.bashrc

### Step 6 - Test your installation

    $ conda list

You'll receive a list of packages avaliable through anaconda.

### Step 7 — Set Up Anaconda Environments

Go to folder where you want to create the environment and run the command:

    $ conda create --name my_env python=3

and the anaconda will create the environment

### Step 8 - Activate/deactivate the environment

To activate the environment just run the command:

    $ conda activate my_env

And to deactivate:

    $ conda deactivate
