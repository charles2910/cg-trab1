import glfw
from OpenGL.GL import *
from houses import RedHouse, GreenHouse
from sun import Sun
from field import Field
from river import River
from shaders import Shader
from window import Window

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

    sun = Sun(program)
    sun.prepare()

    river = River(program)
    river.prepare()

    field = Field(program)
    field.prepare()

    redHouse = RedHouse(program)
    redHouse.prepare()

    yellowHouse = GreenHouse(program)
    yellowHouse.prepare()

    glfw.show_window(window)

    while not glfw.window_should_close(window):
        glfw.poll_events()

        glClear(GL_COLOR_BUFFER_BIT)

        # Set sky color
        glClearColor(0.529, 0.808, 0.922, 1.0)

        sun.draw()
        river.draw()
        field.draw()
        redHouse.draw()
        yellowHouse.draw()

        glfw.swap_buffers(window)

    glfw.terminate()
