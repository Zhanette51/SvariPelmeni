#!/usr/bin/env python3
"""
Точка входа в игру "Свари пельмени!"
"""
import pygame
import sys
from game.main import Game

def main():
    try:
        game = Game()
        game.run()
    except Exception as e:
        print(f"Ошибка запуска игры: {e}")
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    main()
