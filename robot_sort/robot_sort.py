class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"

    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"

    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    # helper function to return to start position
    def return_to_start_position(self):
        """
        Checks if their is space for robot to move to the left
        and moves the robot as far to the left as it can
        until it is back to the starting position
        """
        while self.can_move_left():
            self.move_left()

    # helper function to contain main logic (if that makes sense)
    def sort_main_loop(self):
        # Use something similar to Bubble Sort Logic
        # Use while loop because you are not allowed to access any instance variables directly
        # therefore, you can only use the helper functions provided and the ones you make yourself
        while self.can_move_right():
            '''Use swap_item() to swap the position of the list item the robot is holding
            with the list item at the robot's current position(index) on the list
            Pick up and hold the robot.item at the current index/position on the robot.list'''
            self.swap_item()
            '''Use move_right() to move the robot's position one index to the right'''
            self.move_right()

            '''Use compare_item() to compare the item the robot is holding
            to the item at the current position the robot is at on the list
            if compare_item() returns 1'''
            if self.compare_item() == 1:
                # print('1ST PRINT COMP:', robot._list)

                '''Use set_light_on() to turn the robot's light on'''
                self.set_light_on()
                # print('2ND PRINT ON:', robot._list)

                '''Use swap_item() to swap the position of the list item the robot is holding
                with the list item at the robot's current position(index) on the list
                Pick up and hold the robot.item at the current index/position on the robot.list'''
                self.swap_item()
                # print('3RD PRINT SWAP:', robot._list)

                '''Use move_left() to move the robot's position one index to the left'''
                self.move_left()
                # print('4th PRINT MOV_LEFT:', robot._list)

                '''Use swap_item() to swap the position of the list item the robot is holding
                with the list item at the robot's current position(index) on the list'''
                self.swap_item()
                # print('5TH PRINT SWAP:', robot._list)

                '''Use move_right() to move the robot's position one index to the right'''
                self.move_right()
                # print('6th PRINT MOV_RIGHT:', robot._list)

            else:
                '''Use move_left() to move the robot's position one index to the left'''
                self.move_left()
                # print('ELSE 7th PRINT MOV_LEFT:', robot._list)

                '''Use swap_item() to swap the position of the list item the robot is holding
                with the list item at the robot's current position(index) on the list'''
                self.swap_item()
                # print('ELSE 8TH PRINT SWAP:', robot._list)

                '''Use move_right() to move the robot's position one index to the right'''
                self.move_right()
                # print('ELSE 9th PRINT MOV_RIGHT:', robot._list)

        if self.light_is_on():
            '''Use return_to_start() to move the robot's position as far to the left as it will go'''
            self.return_to_start_position()
            '''Use set_light_off() to turn the robot's light off'''
            # print('RETURN TO START:', robot._list)
            self.set_light_off()
            # print('PRINT OFF:', robot._list)
        else:
            '''Use set_light_on() to turn the robot's light on'''
            self.set_light_on()
            # print('PRINT ON:', robot._list)

    def sort(self):
        """
        Sort the robot's list.
        """
        while not self.light_is_on():
            '''Use sort_main_loop() to move the robot thru a Bubble Sort type algorithm functionality'''
            self.sort_main_loop()


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    # l = [5, 4, 3, 2, 1]

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1,
         45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)
