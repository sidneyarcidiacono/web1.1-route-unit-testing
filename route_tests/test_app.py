import pytest

from .app import app

#######################
# Index Tests
# (there's only one here because there is only one possible scenario!)
#######################


def test_index():
    """Test that the index page shows 'Hello, World!'."""
    res = app.test_client().get("/")
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    expected_page_text = "Hello, World!"
    assert expected_page_text == result_page_text


#######################
# Color Tests
#######################


def test_color_results_blue():
    """Test color results if blue."""
    result = app.test_client().get("/color_results?color=blue")

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = "Wow, blue is my favorite color, too!"
    assert expected_page_text == result_page_text


def test_color_results_scenario1():
    """Test if color results works on black."""
    favorite_color = app.test_client().get("/color_results?color=black")

    assert favorite_color.status_code == 200

    result_page_text = favorite_color.get_data(as_text=True)
    expected_page_text = "Wow, black is my favorite color, too!"
    assert expected_page_text == result_page_text


def test_color_results_edgecase1():
    """Test if color results fails on edgecase empty string."""
    favorite_color = app.test_client().get("/color_results?color=")

    assert favorite_color.status_code == 200

    result_page_text = favorite_color.get_data(as_text=True)
    expected_page_text = "Wow,  is my favorite color, too!"
    assert expected_page_text == result_page_text


#######################
# Froyo Tests
#######################


def test_froyo_results_scenario1():
    """Test froyo results with vanilla and chocolate."""
    result = app.test_client().get(
        "/froyo_results?flavor=vanilla&toppings=chocolate"
    )

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = (
        "You ordered vanilla flavored Fro-Yo with toppings chocolate!"
    )
    assert expected_page_text == result_page_text


def test_froyo_results_scenario2():
    """Test froyo results for user input symbol."""
    result = app.test_client().get(
        "/froyo_results?flavor=Chocolate&toppings=m%26ms"
    )

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = (
        "You ordered Chocolate flavored Fro-Yo with toppings m&ms!"
    )
    assert expected_page_text == result_page_text


def test_froyo_results_edgecase1():
    """Test edgecase of white space in toppings."""
    result = app.test_client().get(
        "/froyo_results?flavor=Chocolate&toppings=%20"
    )

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = (
        "You ordered Chocolate flavored Fro-Yo with toppings  !"
    )
    assert expected_page_text == result_page_text


def test_froyo_results_edgecase2():
    """Test froyo results if user inputs hash character."""
    result = app.test_client().get(
        "/froyo_results?flavor=Chocolate&toppings=%2323"
    )

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = (
        "You ordered Chocolate flavored Fro-Yo with toppings #23!"
    )
    assert expected_page_text == result_page_text


#######################
# Reverse Message Tests
#######################


def test_message_results_helloworld():
    """Test that hello world is reversed."""
    form_data = {"message": "Hello World"}
    res = app.test_client().post("/message_results", data=form_data)
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    assert "dlroW olleH" in result_page_text


def test_message_results_scenario2():
    """Test if goodbye world is reversed."""
    form_data = {"message": "Goodbye World"}
    res = app.test_client().post("/message_results", data=form_data)
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    assert "dlroW eybdooG" in result_page_text


def test_message_results_edgecase1():
    """Test reverse on empty string."""
    form_data = {"message": ""}
    res = app.test_client().post("/message_results", data=form_data)
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    assert "" in result_page_text


#######################
# Calculator Tests
#######################


def test_calculator_results_scenario1():
    """Test calculator on adding one and 2."""
    result = app.test_client().get(
        "calculator_results?operand1=1&operation=add&operand2=2"
    )

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = "You chose to add 1 and 2. Your result is: 3"
    assert expected_page_text == result_page_text


def test_calculator_results_scenario2():
    """Test calculator on adding 15 and 17."""
    result = app.test_client().get(
        "calculator_results?operand1=15&operation=add&operand2=17"
    )

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = "You chose to add 15 and 17. Your result is: 32"
    assert expected_page_text == result_page_text


def test_calculator_results_scenario3():
    """Test calculator on multiply one and two."""
    result = app.test_client().get(
        "calculator_results?operand1=1&operation=multiply&operand2=2"
    )

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = "You chose to multiply 1 and 2. Your result is: 2"
    assert expected_page_text == result_page_text


def test_calculator_results_scenario4():
    """Test calculator on dividing 2 and 2."""
    result = app.test_client().get(
        "calculator_results?operand1=2&operation=divide&operand2=2"
    )

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = "You chose to divide 2 and 2. Your result is: 1.0"
    assert expected_page_text == result_page_text


def test_calculator_results_edgecase1():
    """Test calculator results with mispelled operator."""
    result = app.test_client().get(
        "calculator_results?operand1=2&operation=ad&operand2=2"
    )

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = "Incorrect operator"
    assert expected_page_text == result_page_text


def test_calculator_results_edgecase2():
    """Test calculator results with invalid operator."""
    result = app.test_client().get(
        "calculator_results?operand1=2&operation=mutiply&operand2=2"
    )

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = "Incorrect operator"
    assert expected_page_text == result_page_text


def test_calculator_results_subtraction():
    """Test calculator on subtracting 2 and 1."""
    result = app.test_client().get(
        "calculator_results?operand1=2&operation=subtract&operand2=1"
    )

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = "You chose to subtract 2 and 1. Your result is: 1"
    assert expected_page_text == result_page_text
