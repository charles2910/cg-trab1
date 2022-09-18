from scene import Scene
from shaders import Shader
from window import Window

import glfw
from OpenGL.GL import *

vertex_code = '''
    attribute vec2 position;

    void main() {
        gl_Position = vec4(position, 0.0, 1.0);
    }
    '''

fragment_code = '''
    uniform vec4 color;

    void main() {
        gl_FragColor = color;
    }
    '''

if __name__ == "__main__":
    window = Window(1200, 700, "Paisagem").window
    program = Shader(vertex_code, fragment_code).program

    scene = Scene(program)
    scene.prepare()

    glfw.show_window(window)

    while not glfw.window_should_close(window):
        glfw.poll_events()

        glClear(GL_COLOR_BUFFER_BIT)

        # Set sky color
        glClearColor(0.529, 0.808, 0.922, 1.0)

        scene.draw()

        glfw.swap_buffers(window)

    glfw.terminate()
