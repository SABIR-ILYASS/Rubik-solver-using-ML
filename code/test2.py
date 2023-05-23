import pygame
from pygame.locals import *
import os


class FirstPage:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 600))
        pygame.display.set_caption("Rubik's cube solver")
        icon = pygame.image.load("C:/Users/sabir/Desktop/rubik_solver/Images/logo.png")
        pygame.display.set_icon(icon)

        self.clock = pygame.time.Clock()
        self.running = True

        self.background = pygame.image.load("C:/Users/sabir/Desktop/rubik_solver/Images/background.jpg")
        self.background = pygame.transform.scale(self.background, (1200, 600))

        self.font_title = pygame.font.Font("C:/Users/sabir/Desktop/rubik_solver/Images/font/Gabriola.ttf", 100)
        self.font_subtitle = pygame.font.Font("C:/Users/sabir/Desktop/rubik_solver/Images/font/Gabriola.ttf", 30)

        self.show_Window_title()
        self.show_help_button1()
        self.show_manualy_button()

        self.rubik_3D = None
        self.white_widget = None

        self.list_buttons = []
        self.list_buttons_colors = []
        self.MOVES = ["up", "down", "right", "left"]
        self.COLORS = ["White", "Yellow", "Red", "Orange", "Blue", "Green"]
        self.show_help_button1()

    def show_Window_title(self, title_index=True):
        title_text = "Rubik's Cube Solver" if title_index else "Rotate the cube."
        title_surf = self.font_title.render(title_text, True, (163, 249, 255))
        title_rect = title_surf.get_rect(center=(600, 250) if title_index else (835, 105))
        self.screen.blit(title_surf, title_rect)
        print("hello")

    def show_help_button1(self):
        help_button = pygame.Surface((80, 25))
        help_button.fill((163, 249, 255))
        help_button_rect = help_button.get_rect(topleft=(1100, 20))
        self.screen.blit(help_button, help_button_rect)

        help_text = self.font_subtitle.render("Help!", True, (8, 27, 42))
        help_text_rect = help_text.get_rect(center=help_button_rect.center)
        self.screen.blit(help_text, help_text_rect)

    def show_manualy_button(self):
        button2 = pygame.image.load("C:/Users/sabir/Desktop/rubik_solver/Images/manually.png")
        button2_rect = button2.get_rect(center=(600, 425))
        self.screen.blit(button2, button2_rect)

        button2_text = self.font_subtitle.render("Add the faces manually.", True, (8, 27, 42))
        button2_text_rect = button2_text.get_rect(center=(600, 425))
        self.screen.blit(button2_text, button2_text_rect)

    def show_help(self):
        # Display help dialog
        help_dialog = pygame.Surface((400, 200))
        help_dialog.fill((255, 255, 255))
        help_dialog_rect = help_dialog.get_rect(center=(600, 300))
        self.screen.blit(help_dialog, help_dialog_rect)

        help_text = "This is some help text. Click the close button to close this window."
        help_font = pygame.font.Font(None, 20)
        help_text_render = help_font.render(help_text, True, (0, 0, 0))
        help_text_rect = help_text_render.get_rect(center=(600, 300))
        self.screen.blit(help_text_render, help_text_rect)

    def show_white_widget(self):
        self.hide_window_title()
        self.hide_manually_button()

        if self.white_widget is None:
            self.white_widget = pygame.Surface((580, 500))
            self.white_widget.fill((255, 255,255))
            self.white_widget_rect = self.white_widget.get_rect(topleft=(10, 10))
            self.screen.blit(self.white_widget, self.white_widget_rect)
            self.show_buttons()
            self.show_colors()

    def show_buttons(self):
            self.show_Window_title(False)

            iteration = 2
            for name in self.MOVES:
                button = pygame.image.load("C:/Users/sabir/Desktop/rubik_solver/Images/{}.png".format(name))
                button_rect = button.get_rect(center=(850, 100 * iteration))
                self.screen.blit(button, button_rect)

                button_text = self.font_subtitle.render("Rotate the cube to {}".format(name), True, (8, 27, 42))
                button_text_rect = button_text.get_rect(center=(850, 100 * iteration))
                self.screen.blit(button_text, button_text_rect)

                iteration += 1
                self.list_buttons.append(button_rect)

    def show_colors(self):
            title_color = self.font_subtitle.render("Choose the color:", True, (163, 249, 255))
            title_color_rect = title_color.get_rect(topleft=(10, 520))
            self.screen.blit(title_color, title_color_rect)

            iteration = 1
            for color in self.COLORS:
                button = pygame.Surface((60, 30))
                button.fill(self.get_color_rgb(color))
                button_rect = button.get_rect(topleft=(40 + 80 * iteration, 535))
                self.screen.blit(button, button_rect)

                button_text = self.font_subtitle.render("{}".format(color), True, (0, 0, 0))
                button_text_rect = button_text.get_rect(center=button_rect.center)
                self.screen.blit(button_text, button_text_rect)

                iteration += 1
                self.list_buttons_colors.append(button_rect)

    def get_color_rgb(self, color):
            if color == "White":
                return (255, 255, 255)
            elif color == "Yellow":
                return (255, 255, 0)
            elif color == "Red":
                return (255, 0, 0)
            elif color == "Orange":
                return (255, 165, 0)
            elif color == "Blue":
                return (0, 0, 255)
            elif color == "Green":
                return (0, 128, 0)

    def hide_window_title(self):
            pass

    def hide_help_button1(self):
            pass

    def hide_camera_button(self):
            pass

    def hide_manually_button(self):
            pass


    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.blit(self.background, (0, 0))
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()


if __name__ == "__main__":
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    app = FirstPage()
    app.run()

