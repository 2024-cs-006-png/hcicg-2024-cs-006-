
import glfw
from OpenGL.GL import *

def main():
    # Initialize GLFW
    if not glfw.init():
        return

    # Create a window (800x600)
    window = glfw.create_window(800, 600, "Lab 01 - First Window", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    # Print OpenGL Version
    version = glGetString(GL_VERSION)
    print("OpenGL Version:", version.decode('utf-8'))

    # Main Render Loop
    while not glfw.window_should_close(window):
        # Background color (R, G, B, Alpha)
        glClearColor(0.2, 0.4, 0.6, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()