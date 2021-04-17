from pynput import mouse
import time

start = time.time()
period = 10.0
f = open('log.txt', 'w')

def on_move(x, y):
    f.write('Pointer moved to {0}. Time: {1}\n'.format(
        (x, y), time.time()-start))
    if time.time()-start>=period:
        listener.stop()
        f.close()
        exit()

def on_click(x, y, button, pressed):
    button_clicked = ''
    if button == mouse.Button.right:
        button_clicked = 'Right'
    elif button == mouse.Button.left:
        button_clicked = 'Left'
    elif button == mouse.Button.middle:
        button_clicked = 'Middle'
    f.write('{0} at {1}. Time: {2}\n'.format(
        button_clicked,
        (x, y), time.time()-start))
    if time.time()-start>=period:
        listener.stop()
        f.close()
        exit()

def on_scroll(x, y, dx, dy):
    f.write('Scrolled {0} at {1}. Time: {2}\n'.format(
        'down' if dy < 0 else 'up',
        (x, y), time.time()-start))
    if time.time()-start>=period:
        listener.stop()
        f.close()
        exit()


listener = mouse.Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll)
listener.start()
