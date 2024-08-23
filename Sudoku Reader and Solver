import cv2
import numpy as np
import pytesseract

# Path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Nateb\PycharmProjects\Tesseract\tesseract.exe'


def preprocess_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image not found or unable to load: {image_path}")

    image = cv2.resize(image, (1200, 1200))
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Denoise image
    gray = cv2.fastNlMeansDenoising(gray, None, 30, 7, 21)

    # Adjust contrast (if needed)
    alpha = 1.5  # Contrast control
    beta = 0  # Brightness control
    contrast_img = cv2.convertScaleAbs(gray, alpha=alpha, beta=beta)

    # Adaptive thresholding
    thresh = cv2.adaptiveThreshold(contrast_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

    # Apply morphological transformations
    kernel = np.ones((4, 4), np.uint8)
    morphed_img = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    return morphed_img


def find_sudoku_grid(thresh_image):
    contours, _ = cv2.findContours(thresh_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        raise ValueError("No contours found in the image")

    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    sudoku_contour = contours[0]
    epsilon = 0.02 * cv2.arcLength(sudoku_contour, True)
    approx = cv2.approxPolyDP(sudoku_contour, epsilon, True)
    x, y, w, h = cv2.boundingRect(approx)
    return x, y, w, h


def extract_cells(image, x, y, w, h):
    cells = []
    cell_size = w // 9
    zoom_factor = 1  # Increase zoom factor for better OCR

    for i in range(9):
        row_cells = []
        for j in range(9):
            x1 = x + j * cell_size + 17  # Left padding
            y1 = y + i * cell_size + 20 # Top padding
            x2 = x1 + cell_size - 10 # Right padding
            y2 = y1 + cell_size  - 19 # Bottom padding

            cell_img = image[y1:y2, x1:x2]
            if cell_img.size == 0:
                row_cells.append(-1)
                continue

            # Resize to a larger size to zoom in
            new_size = (cell_size * zoom_factor, cell_size * zoom_factor)
            cell_img_resized = cv2.resize(cell_img, new_size, interpolation=cv2.INTER_CUBIC)

            # Apply adaptive thresholding and sharpen
            cell_img_thresh = cv2.adaptiveThreshold(cell_img_resized, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                                    cv2.THRESH_BINARY_INV, 15, 5)

            # Optional: Apply sharpening filter
            kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
            cell_img_sharpened = cv2.filter2D(cell_img_thresh, -1, kernel)

            # Print the resized and thresholded cell image
            cv2.imshow(f'Cell ({i}, {j})', cell_img_sharpened)
            cv2.waitKey(0)  # Wait for a key press to close the window

            # Perform OCR
            text = pytesseract.image_to_string(cell_img_sharpened, config='--psm 6 --oem 3 outputbase digits').strip()

            if text:
                try:
                    row_cells.append(int(text))
                except ValueError:
                    row_cells.append(-1)
            else:
                row_cells.append(-1)

        cells.append(row_cells)

    cv2.destroyAllWindows()  # Close all OpenCV windows
    return cells


def read_sudoku_image(image_path):
    thresh_image = preprocess_image(image_path)
    x, y, w, h = find_sudoku_grid(thresh_image)
    sudoku_grid = extract_cells(thresh_image, x, y, w, h)
    return sudoku_grid


#----------------------------------------------------------------------------------- INPUT PATH FOR UNSOLVED SUDOKU IMAGE -------------------------------------------------------------------------------------------

# Path to the Sudoku image
image_path = r'(INPUT PATH HERE (ETC. C:/user.....))'



line = '---------------------------'
try:
    sudoku_grid = read_sudoku_image(image_path)
    sudoku_in_unsolved_form = []
    for row in sudoku_grid:
        sudoku_in_unsolved_form.append(row)
    print(f" Unsolved Sudoku: \n {sudoku_in_unsolved_form[0]} \n {sudoku_in_unsolved_form[1]} \n {sudoku_in_unsolved_form[2]} \n {line} \n {sudoku_in_unsolved_form[3]} \n {sudoku_in_unsolved_form[4]} \n {sudoku_in_unsolved_form[5]} \n {line} \n {sudoku_in_unsolved_form[6]} \n {sudoku_in_unsolved_form[7]} \n {sudoku_in_unsolved_form[8]}" )
except Exception as e:
    print(f"An error occurred: {e}")




########### down below is where it solves and prints the solved sudoku
# This part was derived from the file "Sudoku Solver.py"




def find_next_empty(puzzle):
    # this will find the next row, column thats not filled (replaces with -1)
    # return row, col val (can be none if there is none
    for r in range(9):  # because they can only have numbers 0-9
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c

    return None, None  # for if it is empty


def is_valid(puzzle, guess, row, col):  # this will check the guess to make sure its valid
    # we must check the row, col, and square its in (normal sudoku rules)
    # this will check tot values in the given row (a simple check compared to the folling check portion because the row is easily defined)
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    # the following will check the column and add it to a list so that we can compare it to the guess
    col_vals = []
    for i in range(9):
        col_vals.append(puzzle[i][col])
    if guess in col_vals:
        return False

    # the following will check the square (3x3) portion that the guess is located in
    row_start = (row // 3) * 3  # so if the row is 2 and you do '//' it will equal 0 AKA 2 // 3 = 0
    col_start = (
                            col // 3) * 3  # same thing as before, but the * 3 part it there to get the first inner square(1x1) of te big square (3x3)

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    # at this point, it is valid
    return True


def solve_sudoku(puzzle):
    # this will solve sudoku by using backtracking
    # Step 1: Choose a starting point to make a guess
    row, col = find_next_empty(puzzle)

    # Step 1.1: if there is nowehere left to go, then that means that we are done because it will only use valid input
    if row is None:
        return True

    # Step 2: make a guess between 1-9
    for guess in range(1, 10):  # this makes the 'guess' variable be a number starting a 1 and goes to 9
        # Step 3: we have to check if the guess is a valid number or not
        if is_valid(puzzle, guess, row, col):
            # step 3.1: if valid, add it to the puzzle
            puzzle[row][col] = guess
            # step 4: recurively call the puzzle
            if solve_sudoku(puzzle):
                return (
                    f" \n Solved Sudoku: \n {puzzle[0]} \n {puzzle[1]} \n {puzzle[2]} \n {line} \n {puzzle[3]} \n {puzzle[4]} \n {puzzle[5]} \n {line} \n {puzzle[6]} \n {puzzle[7]} \n {puzzle[8]} ")

        # step 5: what happens if its not valid
        puzzle[row][col] = -1  # reset the guess

    # step 6: Declare unsolvable if not working
    return False

    # To make a manual implimentation where you put all the numbers down at once, make the sudoku puzzle (like the ones below) with the blank spaces as -1 and change the code above
#    print(solve_sudoku(example_board))
#    print(f" {example_board[0]}  \n {example_board[1]}  \n {example_board[2]} \n {example_board[3]}  \n {example_board[4]} \n {example_board[5]} \n {example_board[6]}\n {example_board[7]} \n {example_board[8]}")

print(solve_sudoku(sudoku_in_unsolved_form))
input("Press 'Enter' to close.")
