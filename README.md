# NVCIM

## Set Up Environments

#### For Linux or WSL
1. Set up environment variable.

```shell
export NVCIM_HOME=/root/directory/of/this/project
```

2. Run the following command to install required packages.

```makefile
make requires
```

3. Run the following command to install python module `maptools`.

```makefile
make maptools
```

#### For Windows

1. Set up environment variable.

```powershell
$env:NVCIM_HOME=/root/directory/of/this/project
```

2. Run the following commands to install required pip packages.

```
pip install -U -r requirements.txt
```

Then, install `graphviz` on the client side.

3. Run the following command to install python module `maptools`.

```powershell
.\make.sh
```