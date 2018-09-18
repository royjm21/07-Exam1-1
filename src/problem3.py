"""
Exam 1, problem 3.

Authors: David Mutchler, Vibha Alangar, Valerie Galluzzi, Mark Hays,
         Amanda Stouder, their colleagues and Jeremy Roy.
"""  # done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem3()


def run_test_problem3():
    """ Tests the   problem3  function. """
    print()
    print('--------------------------------------------------')
    print('Testing the  problem3  function:')
    print('  See the graphics windows that pop up.')
    print('--------------------------------------------------')

    # ONE test on this window:
    title = 'Test 1 of problem3'
    window = rg.RoseWindow(450, 250, title)

    problem3(rg.Point(10, 20), 200, 25, window)
    window.close_on_mouse_click()

    # TWO tests on ONE window.
    title = 'Tests 2, 3 and 4 of problem3'
    window = rg.RoseWindow(450, 250, title)

    problem3(rg.Point(15, 30), 100, 20, window)
    window.continue_on_mouse_click()

    problem3(rg.Point(250, 10), 90, 45, window)
    window.continue_on_mouse_click()

    problem3(rg.Point(250, 125), 80, 45, window)
    window.close_on_mouse_click()


def problem3(point, length, delta, window):
    """
    See   problem3_picture.pdf   in this project for pictures
    that may help you better understand the following specification:

    What comes in:
      -- An rg.Point.
      -- Two positive integers
      -- An rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:  Draws, on the given rg.RoseWindow:

      -- A VERTICAL rg.Line for which:
           -- Its topmost point is the given point.
           -- Its length is the given length.
           -- Its color is 'black'.
           -- Its thickness is 3.

      -- Several HORIZONTAL rg.Lines such that:
           -- All the horizontal lines have their leftmost point
                on the vertical line.  SEE THE PICTURES.
           -- For the FIRST of these HORIZONTAL lines:
                -- Its leftmost point is the given point.
                -- Its length is the given length.
           -- Each SUBSEQUENT HORIZONTAL rg.Line is  delta  pixels
                directly below the previous rg.Line (where delta is a parameter)
                and 20 pixels longer than the previous rg.Line.
           -- All the HORIZONTAL lines have thickness 3.
           -- The 1st, 4th, 7th, etc rg.Lines have color 'magenta',
              The 2nd, 5th, 8th, etc rg.Lines have color 'cyan'
              The 3rd, 6th, 9th, etc rg.Lines have color 'spring green'

      NOTE: The NUMBER of lines to draw is determined by the facts that:
        -- The vertical line has the given length.
        -- All horizontal lines have their left endpoint on the vertical line.
        -- The distance between horizontal lines is the given delta.

      Must render but   ** NOT close **   the window.

    Type hints:
      :type point:   rg.Point
      :type length:  int
      :type delta:   int
      :type window:  rg.RoseWindow
    """
    # --------------------------------------------------------------------------
    # TODO: 2. Implement and test this function.
    # TODO (continued):  IMPORTANT: Use this ITERATIVE ENHANCEMENT PLAN:
    # TODO (continued):    1. Make the sole VERTICAL line appear,
    # TODO (continued):         with thickness 3.
    # TODO (continued):    2. Make the FIRST horizontal line appear.
    # TODO (continued):    3. Make MORE horizontal lines appear,
    # TODO (continued):         each delta below the previous one.
    # TODO (continued):    4. Make each successive horizontal line
    # TODO (continued):         20 pixels longer than the previous one.
    # TODO (continued):    5. Make the right NUMBER of horizontal lines.
    # TODO (continued):    6. Make the horizontal lines each have thickness 3
    # TODO (continued):         and colors per the specified pattern.
    #          Tests have been written for you (above).
    # --------------------------------------------------------------------------
    vertical_end = rg.Point(point.x, point.y + length)
    vertical_line = rg.Line(point, vertical_end)
    vertical_line.color = 'black'
    vertical_line.thickness = 3
    vertical_line.attach_to(window)
    thickness = 3
    horizontal1_end = rg.Point(point.x + length, point.y)
    horizontal_line = rg.Line(point, horizontal1_end)
    horizontal_line.color = 'magenta'
    horizontal_line.attach_to(window)
    horizontal_line.thickness = thickness
    horizontal_line2_start = rg.Point(point.x, point.y + delta)
    horizontal_line2_end = rg.Point(point.x + length + 20, point.y + delta)
    horizontal_line2 = rg.Line(horizontal_line2_start, horizontal_line2_end)
    horizontal_line2.color = 'cyan'
    horizontal_line2.thickness = thickness
    horizontal_line2.attach_to(window)
    line3_start = rg.Point(point.x, point.y + 2*delta)
    line3_end = rg.Point(point.x + length + 40, point.y + 2*delta)
    line3 = rg.Line(line3_start, line3_end)
    line3.color = 'spring green'
    line3.thickness = thickness
    line3.attach_to(window)
    line4_start = rg.Point(point.x, point.y + 3*delta)
    line4_end = rg.Point(point.x + length + 60, point.y + 3*delta)
    line4 = rg.Line(line4_start, line4_end)
    line4.thickness = thickness
    line4.color = "magenta"
    line4.attach_to(window)
    line5_start = rg.Point(point.x, point.y + 4*delta)
    line5_end = rg.Point(point.x + length + 80, point.y + 4*delta)
    line5 = rg.Line(line5_start, line5_end)
    line5.thickness = thickness
    line5.color = 'cyan'
    line5.attach_to(window)
    line6_start = rg.Point(point.x, point.y + 5*delta)
    line6_end = rg.Point(point.x + length + 100, point.y + 5*delta)
    line6 = rg.Line(line6_start, line6_end)
    line6.thickness = thickness
    line6.color = 'spring green'
    line6.attach_to(window)
    line7_start = rg.Point(point.x, point.y + 6*delta)
    line7_end = rg.Point(point.x + length + 120, point.y + 6*delta)
    line7 = rg.Line(line7_start, line7_end)
    line7.thickness = thickness
    line7.color = 'magenta'
    line7.attach_to(window)
    line8_start = rg.Point(point.x, point.y + 7*delta)
    line8_end = rg.Point(point.x + length + 140, point.y + 7*delta)
    line8 = rg.Line(line8_start, line8_end)
    line8.thickness = thickness
    line8.color = 'cyan'
    line8.attach_to(window)
    line9_start = rg.Point(point.x, point.y + 8*delta)
    line9_end = rg.Point(point.x + length + 160, point.y + 8*delta)
    line9 = rg.Line(line9_start, line9_end)
    line9.thickness = thickness
    line9.color = 'spring green'
    line9.attach_to(window)
    window.render()

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
