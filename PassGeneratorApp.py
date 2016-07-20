import gi
from Generator import Generator
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

class Handler:

    def __init__(self, builder):
        self.builder = builder
        self.clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)

    def copy_password(self, button):
        self.clipboard.set_text(self.builder.get_object("generated_pass_txtbox").get_text(), -1)

    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def activate_sibling(self, sibling):
        #check sibling status: if editable then toggle_btn is true, else false
        sibling.set_editable(not sibling.get_editable())
        if not sibling.get_editable():
            sibling.set_text("")


    def on_generate_btn_clicked(self, button):
        letters_allowed = self.builder.get_object("letters_allowed_check_btn").get_active()
        numbers_allowed = self.builder.get_object("numbers_allowed_check_btn").get_active()
        caps_letters_allowed = self.builder.get_object("uppercase_letters_allowed_check_btn").get_active()
        special_characters_allowed = self.builder.get_object("simbols_allowed_check_btn").get_active()

        letters_required = int(self.builder.get_object("letters_required_spin_btn").get_value())
        numbers_required = int(self.builder.get_object("numbers_required_spin_btn").get_value())
        caps_letters_required = int(self.builder.get_object("uppercase_letters_required_spin_btn").get_value())
        special_characters_required = int(self.builder.get_object("simbols_required_spin_btn").get_value())

        characters_to_use = self.builder.get_object("characters_allowed_txtbox").get_text()

        length = int(self.builder.get_object("n_chars_spin_btn").get_value())

        min_num_of_letters = 0
        min_num_of_numbers = 0
        min_num_of_caps_letters = 0
        min_num_of_special_characters = 0
        if letters_allowed and letters_required > 0:
           min_num_of_letters = letters_required
        if numbers_allowed and numbers_required > 0:
            min_num_of_numbers = numbers_required
        if caps_letters_allowed and caps_letters_required > 0:
            min_num_of_caps_letters = caps_letters_required
        if special_characters_allowed and special_characters_required > 0:
            min_num_of_special_characters = special_characters_required

        g = Generator(length, letters_allowed, numbers_allowed, caps_letters_allowed, special_characters_allowed, min_num_of_letters, min_num_of_numbers, min_num_of_caps_letters, min_num_of_special_characters, allowed_chars = characters_to_use)
        password = g.generate()

        self.builder.get_object("generated_pass_txtbox").set_text(password)


builder = Gtk.Builder()
builder.add_from_file("./ui.glade")
window = builder.get_object("Main Window")
window.show_all()
builder.connect_signals(Handler(builder))
Gtk.main()
