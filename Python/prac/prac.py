"""
    Based on the combination of vehicle type and light color, determine the maximum speed the vehicle can travel through the intersection.

    Vehicle Types:
        private ( cars, trucks )
        public ( busses )
        emergency ( ambulance, fire )
        human ( bicycle )

    Lights:
        green
        yellow
        red
        white

    Specs:
        For white lights, only public and emergency vehicles can go.
        Public vehicles can go up to their max speed of 30mph through white lights. But must stop for any other lights.
        At yellow lights, private vehicles must slow to 20 and emergency vehicles must slow to 30.
        Other than emergency vehicles, all vehicles must stop at a red light.
        At green lights, allowed vehicles can maintain their speed.
        Emergency vehicles must slow to 20 at red lights.
        Human vehicles must stop at yellow and red lights.
        stopped == 0
"""

speed = 50 # this is what should be changed
vehicle_type = "private"
light_color = "yellow"

# Your code goes here
if light_color == "green":
    speed = 50
    print(f"The speed is: {speed}")
elif light_color == "yellow":
    speed = 20
    print(f"The speed is: {speed}")
else:
    speed = 0
    print(f"The speed is:{speed}")