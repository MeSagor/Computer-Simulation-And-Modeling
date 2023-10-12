import random
import numpy as np
import matplotlib.pyplot as plt

bomber_x_positions = [25]
bomber_y_positions = [25]
fighter_x_positions = [1]
fighter_y_positions = [45]
bomber_velocity = 7
fighter_velocity = 2

window_x = 50
window_y = 50
plt.figure(figsize=(7, 6))
plt.axis([0, window_x, 0, window_y])
plt.title('Pure Pursuit')
plt.ion() 
plt.show()

total_time = 0
while True:
    total_time += 1
    x_rand = random.randint(-bomber_velocity, bomber_velocity)
    y_rand = random.randint(-bomber_velocity, bomber_velocity)
    # x_rand = bomber_velocity * random.choice([-1, 1])
    # y_rand = bomber_velocity * random.choice([-1, 1])
    
    new_x = max(0, min(window_x, (bomber_x_positions[-1] + x_rand)))
    new_y = max(0, min(window_y, (bomber_y_positions[-1] + y_rand)))
    bomber_x_positions.append(new_x)
    bomber_y_positions.append(new_y)

    distance = np.sqrt((bomber_x_positions[-1] - fighter_x_positions[-1])**2 + 
                       (bomber_y_positions[-1] - fighter_y_positions[-1])**2) 

    new_fighter_x = fighter_x_positions[-1] + fighter_velocity * (bomber_x_positions[-1] - fighter_x_positions[-1])/distance
    new_fighter_y = fighter_y_positions[-1] + fighter_velocity * (bomber_y_positions[-1] - fighter_y_positions[-1])/distance
    fighter_x_positions.append(new_fighter_x)
    fighter_y_positions.append(new_fighter_y)

    colors0 = (['blue'] * (len(bomber_x_positions)-1)) + ['green']
    colors1 = (['red'] * (len(bomber_x_positions)-1)) + ['cyan']
    plt.scatter(bomber_x_positions, bomber_y_positions, marker='o', color=colors0, linestyle='dashed')
    plt.plot(bomber_x_positions, bomber_y_positions, color='blue', linestyle='dashed')
    plt.scatter(fighter_x_positions, fighter_y_positions, marker='o', color=colors1, linestyle='dashed') 
    plt.plot(fighter_x_positions, fighter_y_positions, color='red', linestyle='dashed') 
    plt.draw()
    plt.pause(0.7)
 
    print(f'distance: {distance:.2f}')
    if distance < 6:
        plt.text(30, 47, f'Bomber destroyed at: {total_time}', fontsize=12)
        plt.pause(6)
        break
    elif distance > 27 and total_time > 10:
        plt.text(30, 47, f'Bomber escaped at: {total_time}', fontsize=12)
        plt.pause(6)
        break
