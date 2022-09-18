from OpenGL.GL import *
import OpenGL.GL.shaders

class Shader:
    def __init__(self, vertex_code: str, fragment_code: str):
        self.program = glCreateProgram()
        vertex = glCreateShader(GL_VERTEX_SHADER)
        fragment = glCreateShader(GL_FRAGMENT_SHADER)

        glShaderSource(vertex, vertex_code)
        glShaderSource(fragment, fragment_code)

        glCompileShader(vertex)
        if not glGetShaderiv(vertex, GL_COMPILE_STATUS):
            error = glGetShaderInfoLog(vertex).decode()
            raise RuntimeError(error)

        glCompileShader(fragment)
        if not glGetShaderiv(fragment, GL_COMPILE_STATUS):
            error = glGetShaderInfoLog(fragment).decode()
            raise RuntimeError(error)

        glAttachShader(self.program, vertex)
        glAttachShader(self.program, fragment)

        glLinkProgram(self.program)
        if not glGetProgramiv(self.program, GL_LINK_STATUS):
            raise RuntimeError(glGetProgramInfoLog(self.program))

        glUseProgram(self.program)
