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

    def disable_required_field(self, check_btn):
        sibling_name = Gtk.Buildable.get_name(check_btn).replace("allowed", "required")
        sibling_widget = self.builder.get_object(sibling_name)

        allowed = check_btn.get_active()
        required = sibling_widget.get_active()

        if not allowed and required:
            sibling_widget.set_active(False)

    def check_if_toggable(self, check_btn):
        sibling_name = Gtk.Buildable.get_name(check_btn).replace("required", "allowed")
        sibling_widget = self.builder.get_object(sibling_name)

        allowed = sibling_widget.get_active()

        if not allowed:
            sibling_widget.set_active(True)

    def on_generate_btn_clicked(self, button):
        letters_allowed = self.builder.get_object("letters_allowed_check_btn").get_active()
        numbers_allowed = self.builder.get_object("numbers_allowed_check_btn").get_active()
        caps_letters_allowed = self.builder.get_object("uppercase_letters_allowed_check_btn").get_active()
        special_characters_allowed = self.builder.get_object("simbols_allowed_check_btn").get_active()

        letters_required = self.builder.get_object("letters_required_check_btn").get_active()
        numbers_required = self.builder.get_object("numbers_required_check_btn").get_active()
        caps_letters_required = self.builder.get_object("uppercase_letters_required_check_btn").get_active()
        special_characters_required = self.builder.get_object("simbols_required_check_btn").get_active()

        length = int(self.builder.get_object("n_chars_spin_btn").get_value())

        min_num_of_letters = 0
        min_num_of_numbers = 0
        min_num_of_caps_letters = 0
        min_num_of_special_characters = 0
        if letters_allowed and letters_required:
           min_num_of_letters += 1
        if numbers_allowed and numbers_required:
            min_num_of_numbers += 1
        if caps_letters_allowed and caps_letters_required:
            min_num_of_caps_letters += 1
        if special_characters_allowed and special_characters_required:
            min_num_of_special_characters += 1

        g = Generator(length, letters_allowed, numbers_allowed, caps_letters_allowed, special_characters_allowed, min_num_of_letters, min_num_of_numbers, min_num_of_caps_letters, min_num_of_special_characters)
        password = g.generate()

        self.builder.get_object("generated_pass_txtbox").set_text(password)


builder = Gtk.Builder()
builder.add_from_file("./ui.glade")
window = builder.get_object("Main Window")
window.show_all()
builder.connect_signals(Handler(builder))
Gtk.main()
