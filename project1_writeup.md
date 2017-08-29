# Rover Sample Return Project
**Writeup for Project 1 - Udacity Robotics Nanodegree** Handed in by Ulrich Ludmann 2017/08/29

## Abstract
The Goal of this Project is to drive a rover around a simulated Environment. The Rover senses the Environment optically with a video camera.
We want to use this camera image to sense the environment and derive appropriate actions.

## Assignments
The following chapter describes how I mastered the project Assignments.
Generally I can say, that I tried really hard to get along without the Project-Walkthrough. But I some cases it was impossible for me to do it without.

### Jupyter Notebook functions

#### Perspective transform
Initially I forgot to implement the masking. After watching the walkthrough, it was clear to me.

#### Color thresh
These functions are slightly modified from the functions you provided.
In the rock detection function, I provide lower and upper thresholds for the color, parameters.

#### Process image function
I copied the scaffolding for this function from the walkthrough.
I struggled with the x and y axis (sometimes they were interchanged) and i forgot to implement the mask. So the results were really poor. Fortunately now I know.
Also I tried some things while populating  the map.


### decision.py functions
Most of the code is unchanged. Form the version that you provided with the assignment.
#### perception_step()
I implemented "wall-hugging" by adding a offset to the Rover.steer in line 27.

I implemented a function, that detects, if the rover is stuck. After this detection, the rover performs actions to escacpe this state.

I experimented a lot with rock detection. This works quiet well but i couldn't get the rover to drive near the rock and pick the rock up.

### percetion.py functions
This is mostly the implementation of the project walkthrough video. I edited the mapping so that the rover does only take the near pixels into account and not those, which are more distant to the camera. This improves the fidelity and its ability to navigate.


## Conclusion
Unfortunately I was not able to master this assignment running without the help of the project walkthrough. I learned a lot about image processing and of course numpy and python.
It was nice to see that the function which I implemented by myself (is the rover stuck?) worked.
I look forward to the next assignment.

*My code is optimized to run in 800x600 resolution and on quality level "good". FPS were between 10 and 30 *
