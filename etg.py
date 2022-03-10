import pygame
from moviepy.editor import VideoFileClip


def run(SCREEN):
    clip = VideoFileClip('phostos/ENRICHEDTONINGGEL.mp4')
    clip.preview()
