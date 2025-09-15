import pyautogui as gui
import keyboard
import time


def get_px(img, x, y):
    px = img.load()
    return px[x, y]


def get_px(img, x, y):
    px = img.load()
    return px[x, y]


def get_game_region():
    print("Move your mouse to the TOP-LEFT corner of the game and press 's'")
    while True:
        if keyboard.is_pressed('s'):
            x1, y1 = gui.position()
            time.sleep(1)
            break

    print("Now move to the BOTTOM-RIGHT corner of the game and press 'e'")
    while True:
        if keyboard.is_pressed('e'):
            x2, y2 = gui.position()
            time.sleep(1)
            break

    x = x1
    y = y1
    w = x2 - x1
    h = y2 - y1
    print(f"Game region: x={x}, y={y}, w={w}, h={h}")
    return x, y, w, h


# Get linear interpolation
def lerp(a, b, t):
    return a + (b - a) * t


# def is_moon_color(rgb):
#     r, g, b = rgb
#     return r > 130 and g > 130 and b > 130


def is_bird_pixel(rgb, is_night):
    r, g, b = rgb
    if is_night:
        return r > 200 and g > 200 and b > 200
    return r < 100 and g < 100 and b < 100
    

def start():
    # Screenshot game area
    x, y, w, h = get_game_region()

    FPS = 60
    INITIAL_SPEED = 6.0
    MAX_SPEED = 13.0
    FRAME_INCREMENT = 0.001
    MIN_PX_CNT = 30

    x_start_pct = 0.26
    x_end_pct   = 0.30
    y_cactus_top_pct = 0.64
    y_cactus_bottom_pct = 0.75
    y_bird_top_pct = 0.48
    y_bird_bottom_pct = 0.52
    max_lookahead_start_pct = 0.15
    max_lookahead_pct = 0.45
    jump_trigger_start_pct = 0.45
    jump_trigger_end_pct = 0.31
    duck_trigger_start_pct = 0.55
    duck_trigger_end_pct = 0.38
    duck_time_min = 0.2
    duck_time_max = 0.45
    y_moon_bottom_pct = 0.40

    # Cactus and bird checking window
    x_s = int(x_start_pct * w)
    x_e = int(x_end_pct * w)
    y_cactus_bottom = int(y_cactus_bottom_pct * h)
    y_cactus_top = int(y_cactus_top_pct * h)
    y_bird_bottom = int(y_bird_bottom_pct * h)
    y_bird_top = int(y_bird_top_pct * h)
    y_moon_bottom = int(y_moon_bottom_pct * h)

    speed = INITIAL_SPEED
    frame_count = 0
    frame_interval = 1.0 / FPS 
    last_frame_time = time.time()

    # Interface switch delay
    # time.sleep(3)

    # Start logic
    print("Press 'z' to start the game!")
    while True:
        if keyboard.is_pressed('z'):
            break

    print("Game started!")
    print("Press 'q' to stop!")

    # Game loop
    while True:
        t1 = time.time()

        # Exit on 'q'
        if keyboard.is_pressed('q'):
            break

        img = gui.screenshot(region=(x, y, w, h))
        img.save("dino.jpg")

        # Get background color
        bg_color = get_px(img, 10, 10)
        is_night = sum(bg_color) < 100

        # Normalize the speed
        speed_norm = (speed - 6) / (MAX_SPEED - 6)

        # Update checking window
        x_s_pct = lerp(x_start_pct, max_lookahead_start_pct, speed_norm)
        x_e_pct = lerp(x_end_pct, max_lookahead_pct, speed_norm)
        x_s = int(x_s_pct * w)
        x_e = int(x_e_pct * w)

        # Update jump trigger
        jump_trigger_pct = lerp(jump_trigger_end_pct, jump_trigger_start_pct, speed_norm)
        x_jump_trigger = int(jump_trigger_pct * w)
        
        # Update duck trigger
        duck_trigger_pct = lerp(duck_trigger_end_pct, duck_trigger_start_pct, speed_norm)
        x_duck_trigger = int(duck_trigger_pct * w)

        # Update duck under sleep time
        duck_time = lerp(duck_time_max, duck_time_min, speed_norm)

        bird_px_cnt = 0
        
        for i in reversed(range(x_s, x_e)):
            # Detect bird
            bottom_color = get_px(img, i, y_bird_bottom)
            top_color = get_px(img, i, y_bird_top)
            if is_bird_pixel(bottom_color, is_night) and is_bird_pixel(top_color, is_night):
                bird_px_cnt+=1

                if bird_px_cnt >= MIN_PX_CNT and i <= x_duck_trigger:
                    bird_px_cnt = 0
                    keyboard.press('down')
                    time.sleep(duck_time)
                    keyboard.release('down')
                    break

            # Detect cactus
            if get_px(img, i, y_cactus_bottom) != bg_color or get_px(img, i, y_cactus_top) != bg_color:
                if i <= x_jump_trigger: 
                    keyboard.press('space')
                    break

        current_time = time.time()
    
        # Update frames passed since last loop
        frames_passed = int((current_time - last_frame_time) / frame_interval)
        frame_count += frames_passed
        last_frame_time = current_time

        # Update speed based on frame count
        speed = 6.0 + frame_count * FRAME_INCREMENT
        if speed > MAX_SPEED:
            speed = MAX_SPEED


if __name__ == "__main__":
    start()