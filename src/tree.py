from object import Object

from OpenGL.GL import *
import numpy as np

class ScotchPineTree(Object):
    def __init__(self, program):
        super().__init__(program, None)

    def create(self):
        vertices = np.zeros(13, [("position", np.float32, 2)])
        # Add componente randômica para diferenciar árvores
        largura_tronco = np.random.rand()/50.0 - 0.01
        largura_folhagem = np.random.rand()/30.0 - 0.0167
        altura_folhagem = np.random.rand()/20.0 - 0.025
        print(largura_tronco, largura_folhagem, altura_folhagem)
        vertices['position'] = [
            # Tronco
            (-0.04 + largura_tronco, -0.2),
            (-0.04 + largura_tronco, -0.0),
            (-0.08 - largura_tronco, -0.0),
            (-0.08 - largura_tronco, -0.2),

            # Folhagem
            (-0.18,-0.00),
            (-0.06, 0.24),
            ( 0.06, 0.00),
            (-0.18, 0.08),
            (-0.06, 0.32),
            ( 0.06, 0.08),
            (-0.18, 0.16),
            (-0.06, 0.40),
            ( 0.06, 0.16),
        ]
        #print(vertices)
        return vertices

    def draw(self):
        glBindVertexArray(self.vao)
        glUniform4f(glGetUniformLocation(self.program, "color"), 0.4, 0.2, 0.0, 1.0)
        glDrawArrays(GL_POLYGON, 0, 4)
        glUniform4f(glGetUniformLocation(self.program, "color"), 0.0, 0.5, 0.0, 1.0)
        glDrawArrays(GL_POLYGON, 4, 3)
        glDrawArrays(GL_POLYGON, 7, 3)
        glDrawArrays(GL_POLYGON, 10, 3)
        glBindVertexArray(0)

class SugarPineTree(Object):
    def __init__(self, program):
        super().__init__(program, None)

    def create(self):
        vertices = np.zeros(7, [("position", np.float32, 2)])
        # Add componente randômica para diferenciar árvores
        largura_tronco = np.random.rand()/50.0 - 0.01
        largura_folhagem = np.random.rand()/30.0 - 0.0167
        altura_folhagem = np.random.rand()/20.0 - 0.025
        vertices['position'] = [
            # Tronco
            (0.65 + largura_tronco, 0.0),
            (0.65 + largura_tronco, 0.12),
            (0.71 - largura_tronco, 0.12),
            (0.71 - largura_tronco, 0.0),

            # Folhagem
            (0.80 + largura_folhagem, 0.12),
            (0.56 - largura_folhagem, 0.12),
            (0.68, 0.5 + altura_folhagem),
        ]
        return vertices

    def draw(self):
        glBindVertexArray(self.vao)
        glUniform4f(glGetUniformLocation(self.program, "color"), 0.4, 0.2, 0.0, 1.0)
        glDrawArrays(GL_TRIANGLE_FAN, 0, 4)
        glUniform4f(glGetUniformLocation(self.program, "color"), 0.0, 0.5, 0.0, 1.0)
        glDrawArrays(GL_TRIANGLES, 4, 3)
        glBindVertexArray(0)
