from tkinter import Tk as make_screen, Canvas

class Screen :
    def __init__(self, _width, _height, _bias_list=[[1,-1],[1,-1],[1,-1]], _scale_size=1):
        self.screen = make_screen()
        self.canvas = Canvas(width = _width, height = _height)
        self.canvas.pack()
        self.screen.update()
        self.bg = self.canvas.create_rectangle(0, 0, _width, _height,
                                               fill ="white", outline = "")
        self.points = list()
        self.lines = list()

        self.bias_list = _bias_list
        self.scale_size = _scale_size

    def background(self, color):
        self.canvas.itemcget(self.bg, fill=color)

    def mainloop(self):
        self.screen.mainloop()

    def drawPoint(self, x, y, psize):
        self.points.append(self.canvas.create_oval(x, y, x + psize, y + psize,
                                                   fill = "blue", outline = ""))

    def drawline(self, x1, y1, x2, y2):
        self.lines.append(self.canvas.create_line(x1, y1, x2, y2))

    def draw_non_opt_points(self, points, point_size) :
        for coords in points :
            self.drawPoint(
                (coords[0]+abs(self.bias_list[0][1]))*self.scale_size,
                (coords[1]+abs(self.bias_list[1][1]))*self.scale_size,
                (coords[2]+point_size))

    def draw_opt_points(self, points, point_size) :
        for cornode in points :
            axislist = cornode.getXList()
            for x in axislist :
                self.drawPoint(
                    (x+abs(self.bias_list[0][1]))*self.scale_size,
                    (cornode()+abs(self.bias_list[1][1]))*self.scale_size,
                    (point_size))