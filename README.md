# puppy

## Deployment

Clone this project

```bash
  cd <workspace_name>
  cd src
  git clone https://github.com/Ritesh-Gandhi24/puppy.git
```

Catkin build/make and source the folder

```bash
  cd <workspace_name>
  catkin build
  source devel/setup.bash
```
Launch the files

```bash
  cd src/puppy
  roslaunch puppy display.Launch
```
Open a new terminal 

```bash
  cd <package_name>
  cd src/puppy
  roslaunch puppy gazebo.launch
```
