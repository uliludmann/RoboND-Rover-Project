import numpy as np
import time


# This is where you can build a decision tree for determining throttle, brake and steer
# commands based on the output of the perception_step() function
def decision_step(Rover):
    # Implement conditionals to decide what to do given perception data
    # Here you're all set up with some basic functionality but you'll need to
    # improve on this decision tree to do a good job of navigating autonomously!
    # Example:
    # Check if we have vision data to make decisions with
    if Rover.nav_angles is not None:
        # Check for Rover.mode status
        if Rover.mode == 'forward':
            print(Rover.mode)
            Rover.steer = 0
            # Check the extent of navigable terrain
            if len(Rover.nav_angles) >= Rover.stop_forward:
                # If mode is forward, navigable terrain looks good
                # and velocity is below max, then throttle
                if Rover.vel < Rover.max_vel:
                    # Set throttle value to throttle setting
                    Rover.throttle = Rover.throttle_set
                # Set steering to average angle clipped to the range +/- 15
                offset = 12
                Rover.steer = np.clip(np.mean(Rover.nav_angles * 180/np.pi) + offset, -15, 15)
            # If there's a lack of navigable terrain pixels then go to 'stop' mode
            elif len(Rover.nav_angles) < Rover.stop_forward:
                    # Set mode to "stop" and hit the brakes!
                    Rover.throttle = 0
                    # Set brake to stored brake value
                    Rover.brake = Rover.brake_set
                    Rover.steer = 0
                    Rover.mode = 'stop'
        #stuck?

        if Rover.throttle == 0.2 and abs(Rover.vel) < 0.2:
            print("Stuck?")
            if not Rover.start_time_stuck:
                Rover.start_time_stuck = Rover.total_time
            print(Rover.total_time - Rover.start_time_stuck)
            if Rover.total_time - Rover.start_time_stuck > 5:
                Rover.mode = 'stuck'


        # If we're already in "stop" mode then make different decisions
        elif Rover.mode == 'stop':
            print(Rover.mode)
            # If we're in stop mode but still moving keep braking
            if Rover.vel > 0.2:
                Rover.throttle = 0
                Rover.brake = Rover.brake_set
                Rover.steer = 0
            # If we're not moving (vel < 0.2) then do something else
            elif Rover.vel <= 0.2:
                # Now we're stopped and we have vision data to see if there's a path forward
                if len(Rover.nav_angles) < Rover.go_forward:
                    Rover.throttle = 0
                    # Release the brake to allow turning
                    Rover.brake = 0
                    # Turn range is +/- 15 degrees, when stopped the next line will induce 4-wheel turning
                    Rover.steer = -15 # Could be more clever here about which way to turn
                # If we're stopped but see sufficient navigable terrain in front then go!
                if len(Rover.nav_angles) >= Rover.go_forward:
                    # Set throttle back to stored value
                    Rover.throttle = Rover.throttle_set
                    # Release the brake
                    Rover.brake = 0
                    # Set steer to mean angle - some offset
                    Rover.steer = np.clip(np.mean(Rover.nav_angles * 180/np.pi ), -15, 15)
                    Rover.mode = 'forward'




    # If in a state where want to pickup a rock send pickup command
    if Rover.near_sample and Rover.vel == 0 and not Rover.picking_up:
        Rover.send_pickup = True

    if Rover.mode == 'stuck':
        print(Rover.mode)
        if not Rover.stuck_choice:
            #Rover.stuck_choice = True
            Rover.throttle = -0.2
            Rover.steer = -15
        if len(Rover.nav_angles) >= 2 * Rover.stop_forward and (Rover.total_time - Rover.start_time_stuck) > 13:
                Rover.mode = 'forward'
                Rover.start_time_stuck = None

    #if np.count_nonzero(Rover.vision_image[:,:, 1]) > 40:
    #    print("ich sehe einen Felsen!")
    #    Rover.brake = Rover.brake_set
    #    Rover.throttle = 0
    #    rover.steer = 0
    #    Rover.mode = 'rock'
        #if Rover.vel == 0:
        #    Rover.mode = 'approaching_rock'


    #if Rover.mode == 'rock':
    #    print(Rover.mode)
    #    Rover.steer = np.clip(np.mean(Rover.nav_angles[:, :, 1] * 180/np.pi ), -15, 15)

        #Rover.mode = 'forward'


    return Rover
