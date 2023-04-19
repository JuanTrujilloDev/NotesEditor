import functions
import views


class MenuPreparator:
    def prepare_menu(self, root: views.MainWindow) -> views.Menu:
        """Prepare and returns menu bar widget"""
        menubar = views.Menu(root)
        root_color = root.cget("bg")
        menubar.config(background=root_color)

        return menubar


class InputPreparator:
    def prepare_input(self, root: views.MainWindow) -> views.InputBox:
        """Renders Input widget and returns it"""
        return views.InputBox(root)


class BottomBoxPreparator:
    def prepare_bottom_box(self, root: views.MainWindow) -> views.BottomBox:
        """Displays BottomBox widget and returns it"""
        bottom_box = views.BottomBox(root)
        views.SeparatorInfo(bottom_box)

        return bottom_box


class WordsLengthPreparator:
    def prepare_words_length(
        self, bottom_box: views.BottomBox
    ) -> views.WordsLengthLabel:
        """Displays WordsLengthLabel widget and returns it"""
        return views.WordsLengthLabel(bottom_box, text=f"Words: 0")


class OSLabelPreparator:
    def prepare_os_label(
        self, bottom_box: views.BottomBox
    ) -> views.OperativeSystemLabel:
        """Gest's current os and displays it through
        OperativeSystemLabel widget and returns it"""
        current_os = functions.SystemOSProcessor().get_os()
        return views.OperativeSystemLabel(bottom_box, text=f"{current_os}")


class RootPreparator:
    def prepare_root(self) -> views.MainWindow:
        """Prepare and returns root widget"""
        root = views.MainWindow()

        return root
