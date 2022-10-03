# puppy

## Deployment

Clone this project

```bash
  cd <workspace_name>
  cd src
  git clone https://github.com/Ritesh-Gandhi24/Quadruped.git
```

Catkin build/make and source the folder

```bash
  cd <workspace_name>
  catkin build
  source devel/setup.bash
```
Launch the files

```bash
  cd src/Quadruped
  roslaunch Quadruped display.Launch
```
Open a new terminal 

```bash
  cd <package_name>
  cd src/Quadruped
  roslaunch qadruped gazebo.launch
```
