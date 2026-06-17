#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Background import Background
from const import WIN_WIDTH, WIN_HEIGHT


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'c1_bg':
                list_bg = []
                for i in range(3):
                    list_bg.append(Background(f'c1_bg{i}', (0, 0)))
                    list_bg.append(Background(f'c1_bg{i}', (WIN_WIDTH, 0)))
                return list_bg

