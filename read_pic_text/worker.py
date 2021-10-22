#!/bin/env python
# -*- coding: utf-8 -*-.
import os
import asyncio

import pyocr as pyocr

from config import FOLDER_PATH, TEXT
import docx
import pytesseract
from PIL import Image


async def list_sorted_pic_folder(FOLDER_PATH) -> list[str]:
    list_sorted = []
    for pic in os.listdir(FOLDER_PATH):
        list_sorted.append(pic)
    filename = sorted(list_sorted)
    return filename
    # вернул отсортированый список по имени файла


async def gen_read_pic():
    filename = await list_sorted_pic_folder(FOLDER_PATH)
    for file in filename:
        if '.jpg' or '.png' in filename:
            img_path = os.path.join(FOLDER_PATH, file)
            img = Image.open(img_path)
            text = TEXT + pytesseract.image_to_string(img,
                                                      lang="rus",
                                                      config='--oem 1',
                                                      builder=pyocr.builders.WordBoxBuilder()
                                                      ).strip()
            yield text


async def write_file_to_doc():
    async for return_value in gen_read_pic():
        print(return_value)
        print(f'page', 20 * '#')
        with open('output.txt', mode="a+", encoding="utf-8") as file_write_name:
            file_write_name.write(return_value)




async def main() -> None:
    await write_file_to_doc()



if __name__ == '__main__':
    asyncio.run(main())