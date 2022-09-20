#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Created By: Carlos Henrique Lima Melara (9805380) and Maíra Canal (11819403)
# Created Date: 18/09/2022
# ---------------------------------------------------------------------------

from scene import Scene
from shaders import Shader
from window import Window

import glfw
from OpenGL.GL import *

vertex_code = '''
    attribute vec2 position;
    uniform mat4 mat_transformation;

    void main() {
        gl_Position = mat_transformation * vec4(position, 0.0, 1.0);
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

    # Create and prepare all scene objects
    scene = Scene(program)
    scene.prepare()

    glfw.show_window(window)

    # Main window loop
    while not glfw.window_should_close(window):
        glfw.poll_events()

        glClear(GL_COLOR_BUFFER_BIT)

        # Set sky color
        glClearColor(0.529, 0.808, 0.922, 1.0)

        scene.draw()

        glfw.swap_buffers(window)

    glfw.terminate()
