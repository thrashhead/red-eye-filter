#!/usr/bin/env python3

from copy import deepcopy
from re import A
from typing import List, Union
from utils.pixel import Pixel
from utils.function_tracer import FunctionTracer
from utils.image import PackedImage, StrideImage
from utils.eye_pattern import ALL_EYE_PATTERNS
from utils.resolution import Resolution

EYE_SIZE = 5

def compute_solution(images: List[Union[PackedImage, StrideImage]]):
    ft = FunctionTracer("compute_solution", "seconds")    

    new_images = []
    for image in images:
        for x, y, eye_indexes in convolve(image, EYE_SIZE):
            eye = [image.pixels[k] for k in eye_indexes]
            for eye_pattern in ALL_EYE_PATTERNS:
                if eye_matches_pattern(eye, eye_pattern):
                    reduced_eye = reduce_redness(eye, eye_pattern)
                    replace_eye(x, y, image, reduced_eye, EYE_SIZE)
                    break

        new_images.append(image)
    del ft

    return new_images


def convolve(image, kernel_size):
    width = image.resolution.width
    height = image.resolution.height

    for x in range(height - kernel_size + 1): 
        for y in range(width - kernel_size + 1):
            kernel_indexes = get_kernel_indexes(x, y, height, kernel_size)
            yield x, y, kernel_indexes


def get_kernel_indexes(x, y, height, kernel_size):
    kernel_indexes = []
    for i in range(x, x + kernel_size): # red
        for j in range(y, y + kernel_size): # colona
            kernel_indexes.append(i * height + j)

    return kernel_indexes
            

def eye_matches_pattern(eye, pattern):
    mask = []
    for pixel, char in list(zip(eye, pattern)):
        if char == ' ':
            continue

        if pixel.red < 200:
            return False

    return True


def reduce_redness(eye, eye_pattern):
    def reduce_redness_pixel(pixel):
        return Pixel(red=pixel.red - 150, green=pixel.green, blue=pixel.blue, alpha=pixel.alpha)

    reduced_eye = []
    print(eye_pattern)
    for char, pixel in zip(eye_pattern, eye):
        if char != ' ':
            reduced_eye.append(reduce_redness_pixel(pixel))
        else:
            reduced_eye.append(pixel)

    return reduced_eye


def replace_eye(x, y, image, eye, eye_size):
    height = image.resolution.height
    width = image.resolution.width

    cnt = 0
    for i in range(x, x + eye_size):
        for j in range(y, y + eye_size):
            image.pixels[i * width + j] = eye[cnt]
            cnt += 1
