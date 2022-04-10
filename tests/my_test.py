import pytest
import src.my_code

inp_1 = ["No", "No"]
out_1 = "Sleep in? No!"

inp_2 = ["No", "Yes"]
out_2 = "Sleep in? Yes!"

inp_3 = ["Yes", "Yes"]
out_3 = "Sleep in? Yes!"

inp_4 = ["Yes", "No"]
out_4 = "Sleep in? Yes!"


# run the test function for each input/output pair
@pytest.mark.parametrize("test_input, expected", [(inp_1, out_1), (inp_2, out_2), (inp_3, out_3), (inp_4, out_4)])
def test_capture_stdout(capsys, test_input, expected):
    # Load the test input for the program execution:
    def mock_input(s):
        return test_input.pop(0)

    src.my_code.input = mock_input

    # Execute the student program, and capture the output (print statements):
    src.my_code.main()
    out, err = capsys.readouterr()

    # Test the actual program output against the anticipated program output:
    assert out.strip() == expected
