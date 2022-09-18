import glfw

class Window:
    def __init__(self, x: int, y: int, name: str):
        glfw.init()
        glfw.window_hint(glfw.VISIBLE, glfw.FALSE)
        self.window = glfw.create_window(x, y, name, None, None)
        glfw.make_context_current(self.window)
