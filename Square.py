import time

from flyt_python import api
drone = api.navigation()

time.sleep(3.0)
drone.access_resquest()

print("Taking Off")
drone.take_off(5.0)

print("Projecting the trajectory")
drone.position_set(6.5, 0, 0, relative=True)
drone.position_set(0, 6.5, 0, relative=True)
drone.position_set(-6.5, 0, 0, relative=True)
drone.position_set(0, -6.5, 0, relative=True)

print("Landing")
drone.land(async=False)

# shutdown the instance
drone.disconnect()
