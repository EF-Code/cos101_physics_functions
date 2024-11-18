#Created by Francis Emmanuel

print("This program allows you to calculate the physics functions below:")
print("")

def calculate_force(mass, acceleration):
  #formula of force is F = MA
  force = mass * acceleration
  return force

def calculate_velocity(initial_velocity, acceleration, time):
  #formula of final velocity is v = u + at
  final_velocity = initial_velocity + acceleration * time
  return final_velocity

def calculate_kinetic_energy(mass, velocity):
  #formula for kinetic energy is KE = 0.5 * m * v^2
  kinetic_energy = 0.5 * mass * velocity**2
  return kinetic_energy

def calculate_potential_energy(mass, gravity, height):
  #formula for potential energy is PE = mgh
  potential_energy = mass * gravity * height
  return potential_energy

def calculate_work_done(force, displacement):
  #formula for work done is W = F * d * cos(theta)
  # Assuming force and displacement are in the same direction (theta = 0)
  work_done = force * displacement
  return work_done
  
print("")
print("1. Force")
print("2. Final Velocity")
print("3. Kinetic Energy")
print("4. Potential Energy")
print("5. Work Done")
print("")
print("Select the physics function to calculate (1-5): ")
reply = int(input())


if reply == 1:
  print("*****CALCULATION FOR FORCE SELECTED*****")
  print("The formula of force is F = MA ")
  print("Input the value for mass (M):")
  mass = int(input())
  print("Input the value for acceleration (A):")
  acceleration = int(input())
  force = calculate_force(mass, acceleration)
  print("Force (F):", force, "N")

elif reply == 2:
  print("*****CALCULATION FOR FINAL VELOCITY SELECTED*****")
  print("The formula of final velocity is v = u + at")
  print("")
  print("Input the value for initial velocity (u):")
  initial_velocity = int(input())
  print("Input the value for acceleration (a):")
  acceleration = int(input())
  print("Input the value for time (t):")
  time = int(input())
  final_velocity = calculate_velocity(initial_velocity, acceleration, time)
  print("Final Velocity (V):", final_velocity, "m/s")

elif reply == 3:
  print("*****CALCULATION FOR KINETIC ENERGY SELECTED*****")
  print("The formula for Kinetic Energy is KE = 0.5 * m * v^2")
  print("")
  print("Input the value for mass (m):")
  mass = int(input())
  print("Input the value for final velocity (v):")
  final_velocity = int(input())
  kinetic_energy = calculate_kinetic_energy(mass, final_velocity)
  print("Kinetic Energy (KE):", kinetic_energy, "J")

elif reply == 4:
  print("*****CALCULATION FOR POTENTIAL ENERGY SELECTED*****")
  print("The formula for Potential Energy is PE = mgh")
  print("")
  print("Input the value for mass (m):")
  mass = int(input())
  print("Input the value for gravity (g):")
  gravity = int(input())
  print(("Input the value for height (h):"))
  height = float(input())
  potential_energy = calculate_potential_energy(mass, gravity, height)
  print("Potential Energy (PE):", potential_energy, "J")

elif reply == 5:
  print("*****CALCULATION FOR WORK DONE SELECTED*****")
  print("The formula for Work Done is W = F * d * cos(theta)")
  print("")
  print("Input the value for force (F):")
  force = int(input())
  print("Input the value for displacement (D):")
  displacement = float(input())
  work_done = calculate_work_done(force, displacement)
  print("Work Done (W):", work_done, "J")

else:
  print("Invalid input provided try again.")





