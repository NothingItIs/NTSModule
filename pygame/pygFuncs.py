import pygame
import sys, os
import platform
if platform.system() == "Windows":
    appendingSlash = "\\"
elif platform.system() == "Linux":
    appendingSlash = "/"
appendingSys: str = "/".join(str(os.path.dirname(os.path.realpath(__file__))).split(appendingSlash)[:-2])
sys.path.append(f"{appendingSys}")
appendingSys: str = "/".join(str(os.path.dirname(os.path.realpath(__file__))).split(appendingSlash)[:-1])
sys.path.append(f"{appendingSys}")
del appendingSys
from imports import *
from pygVariables import *

pygame.init()

# Functions
def variables() -> tuple[Coordinate, mousePress, pygameKeyCode]:
    mousePos = pygame.mouse.get_pos()
    mousePressed = pygame.mouse.get_pressed()
    keyPressed = pygame.key.get_pressed()
    return mousePos, mousePressed, keyPressed

@overload
def hoverColorFunc(rectColor: ColorRBG) -> ColorRBG: """Default function."""
@overload
def hoverColorFunc(rectColor: ColorRBG, addRed: int, addBlue: int, addGree: int) -> ColorRBG: """***KEYWORD ARGUMENTS RECOMMENDED*** Add a custom amount of a specific color."""
@overload
def hoverColorFunc(rectColor: ColorRBG, addColor: int, allColors: bool) -> ColorRBG: """***KEYWORD ARGUMENTS RECOMMENDED*** Add the same amount to all colors that are accessable, by default this is set to -25. 'allColors' defines whetehr all colors are affected or only colors that are below 255."""
def hoverColorFunc(
        rectColor: ColorRBG, 
        addRed: int = 0, 
        addGreen: int = 0, 
        addBlue: int = 0, 
        addColor: int = -25, 
        allColors: bool = False
) -> tuple[int,int,int]:
    if rectColor[0] == 255 and addRed == 0 and allColors == False:
        R = False
    else:
        R = True
    if rectColor[1] == 255 and addGreen == 0 and allColors == False:
        G = False
    else:
        G = True
    if rectColor[2] == 255 and addBlue == 0 and allColors == False:
        B = False
    else:
        B = True
    
    # Red
    if R:
        RedAfter = rectColor[0] + addColor
        RedAfter = RedAfter + addRed
        if RedAfter > 255:
            RedAfter = 255
        elif RedAfter < 0:
            RedAfter = 0
    else:
        RedAfter = 255
    
    # Green
    if G:
        GreenAfter = rectColor[1] + addColor
        GreenAfter = GreenAfter + addGreen
        if GreenAfter > 255:
            GreenAfter = 255
        elif GreenAfter < 0:
            GreenAfter = 0
    else:
        GreenAfter = 255
    
    # Blue
    if B:
        BlueAfter = rectColor[2] + addColor
        BlueAfter = BlueAfter + addBlue
        if BlueAfter > 255:
            BlueAfter = 255
        elif BlueAfter < 0:
            BlueAfter = 0
    else:
        BlueAfter = 255
    
    return (RedAfter, GreenAfter, BlueAfter)

if __name__ == '__main__':
    ...