import glfw
from shaders import Shader
from window import Window

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

    glfw.show_window(window)

    while not glfw.window_should_close(window):
        glfw.poll_events()

    glfw.terminate()
