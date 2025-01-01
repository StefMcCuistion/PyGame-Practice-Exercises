import datetime
import pygame as pg
import os
import ctypes
import json, re
from pygame_console import Console


class StefsGame:

    def find_ratio(self, x):
        """
        Finds ratio of 5120x2880 to the active resolution. Used in scaling backgrounds, sprites, and fonts.
        """
        ratio = x / 5120
        return ratio

    def scale_bg(self, name, screen):
        img = pg.image.load(f"img/bg_{name}.png").convert_alpha()  # Loads img
        x, y = screen.get_size()  # Retrieves screen size
        img = pg.transform.scale(img, (x, y))  # Resizes img to screen size
        return img

    def scale_spr(self, name, screen, pos):
        img = pg.image.load(f"img/spr_{name}.png")  # Loads img
        x, y = screen.get_size()  # Retrieves screen size
        w, h = img.get_size()  # Retrieves img dimensions
        ratio = self.find_ratio(x)
        # Uses ratio to resize img appropriately for current resolution
        img = pg.transform.scale(img, (w * ratio, h * ratio))
        surf, pos = img, (pos[0] * ratio, pos[1] * ratio)
        return surf, pos

    def scale_txt(self, surf, screen, pos):
        x, y = screen.get_size()
        w, h = surf.get_size()
        ratio = self.find_ratio(x)
        surf = pg.transform.scale(surf, (w * ratio, h * ratio))
        pos = (pos[0] * ratio, pos[1] * ratio)
        return surf, pos

    def get_res(self, settings):
        res = settings.get("Resolution")
        res = list(map(int, res.split("x")))  # turns string into a list of ints
        return res

    def set_res(self, settings):
        res = settings.get("Resolution")
        res = list(map(int, res.split("x")))  # turns string into a list of ints
        fullscreen = settings.get("Fullscreen")
        print(f"fullscreen = {fullscreen}")
        if fullscreen == "0":
            screen = pg.display.set_mode(res)
        else:
            screen = pg.display.set_mode(res, pg.FULLSCREEN)
        return screen

    def start_menu(self, settings):

        X, Y = (
            5120,
            2880,
        )  # The constant size of the 'canvas', which the image files are already
        # sized appropriately for before any scaling is done. Use this like a coordinate
        # system since it's constant, then run it thorugh scale functions for final
        # placement accounting for resolution.
        x, y = self.get_res(settings)  # The resolution selected in settings.
        w, h = (
            self.screen.get_size()
        )  # The actual resolution, which will differ from that in settings if fullscreen is enabled.

        clock = pg.time.Clock()

        font = pg.font.SysFont("Comic Sans", 100)
        header = font.render("Stef's test game", True, "Black")

        bg_start = self.scale_bg("start", self.screen)
        ground_surf, ground_pos = self.scale_spr("ground", self.screen, (0, Y - 320))
        protag_surf, protag_pos = self.scale_spr("protag", self.screen, (X * 0.1, Y - 860))
        txt_surf, txt_pos = self.scale_txt(
            header, self.screen, (X * 0.5 - (header.get_size()[0] * 0.5), Y * 0.02)
        )

        protag_x = 0

        while True:
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
                elif event.type == pg.KEYUP:
                    if event.key == pg.K_ESCAPE:
                        pg.quit()
                        exit()
                    elif event.key == pg.K_F1:
                        self.console.toggle()
            
            protag_x += w * 0.01
            if protag_x > w:
                protag_x = -w * 0.4
            self.screen.blit(bg_start, (0, 0))
            self.screen.blit(ground_surf, ground_pos)
            self.screen.blit(protag_surf, (protag_pos[0] + protag_x, protag_pos[1]))
            self.screen.blit(txt_surf, txt_pos)
            # Read and process events related to the console in case console is enabled
            self.console.update(events)	
            # Display the console if enabled or animation is still in progress
            self.console.show(self.screen)
            pg.display.update()
            clock.tick(60)

    def cons_get_pos(self):
        ''' Example of function that can be passed to console to show dynamic
        data in the console
        '''
        return str(self.pos)

    def cons_get_details(self):
        ''' Example of function that can be passed to console to show dynamic
        data in the console
        '''
        
        return str('Input text buffer possition: ' + str(self.console.console_input.buffer_position) + ' Input text position: ' + str(len(self.console.console_input.input_string)))

    def cons_get_input_spacing(self):
        return str('TextInput spacing: ' + str(self.console.console_input.line_spacing) + 
            ' Cursor pos: ' + str(self.console.console_input.cursor_position) +
            ' Buffer pos: ' + str(self.console.console_input.buffer_offset))

    def cons_get_time(self):
        ''' Example of function that can be passed to console to show dynamic
        data in the console
        '''
        return str(datetime.now())

    def main(self):
        os.environ["SDL_VIDEO_CENTERED"] = "1"  # centers window when not in fullscreen
        pg.init()
        pg.font.init()
        ctypes.windll.user32.SetProcessDPIAware()  # keeps Windows GUI scale settings from messing with resolution
        pg.display.set_caption("Stef's Practice Game")

        # Opens settings.csv and creates dictionary for settings
        settings = {}
        with open("settings.csv") as file:
            for line in file:
                key, value = line.split(": ")
                settings[key] = value

        self.clock = pg.time.Clock()
        self.screen = self.set_res(settings)
        console_config = self.get_console_config_json("console_config01.json")
        self.console = Console(self, self.screen.get_width(), console_config)

        self.start_menu(settings)

    def get_console_config_json(self, config_file_path: str):

        try:
            with open(config_file_path, 'r') as json_file:
                json_data = json_file.read()
                return json.loads(re.sub("[^:]//.*","", json_data, flags=re.MULTILINE)) # Remove C-style comments before processing JSON
        except FileNotFoundError:
            raise FileNotFoundError("Console configuration file not found.")

if __name__ == "__main__":
    game = StefsGame()
    game.main()
