#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_11():
    if not wall_is_above():
    move_up()
    fill_cell()
    move_down()
    move_right()
    
if __name__ == '__main__':
    run_tasks()
