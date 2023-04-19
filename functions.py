import platform

import views


class SystemOSProcessor:
    def get_os(self) -> str:
        return platform.system() + " " + platform.release()


class InputChangeProcessor:
    def __init__(self, input_box: views.InputBox, words_length: views.WordsLengthLabel):
        self.input_box = input_box
        self.words_length = words_length

    def get_input_length(self, event: views.tk.Event) -> None:
        """Get input length and update words length label."""
        words = self.input_box.get("1.0", "end-1c").split()
        self.words_length.configure(text=f"Words: {len(words)}")
