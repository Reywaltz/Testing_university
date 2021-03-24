from internal.gui import test_gui
from internal.additions import additions


valid_input = "Сложное предложение - это"
test_data = "Каждый охотник желает знать, где сидит фазан"

def test_normal_input_GUI():
    root = test_gui.tk.Tk()
    top = test_gui.Test_GUI(root)
    root.update_idletasks()
    top.Input_field.insert(1.0, valid_input)
    correct_res = additions.sentence_transform(additions.prepare_input(valid_input))
    callback = list(top.Button1.invoke())
    root.destroy()
    assert callback == correct_res

def test_empty_input_GUI():
    root = test_gui.tk.Tk()
    top = test_gui.Test_GUI(root)
    root.update_idletasks()
    callback = list(top.Button1.invoke())
    root.destroy()
    assert callback == []

def test_button_press():
    root = test_gui.tk.Tk()
    top = test_gui.Test_GUI(root)
    root.update_idletasks()
    top.Input_field.insert(1.0, test_data)
    button_press = top.Button1.invoke()
    assert top.Input_field.get(1.0, "end-1c") == test_data 
