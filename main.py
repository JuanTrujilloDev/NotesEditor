import functions as func
import preparators as prep

if __name__ == "__main__":
    root = prep.RootPreparator().prepare_root()
    menubar = prep.MenuPreparator().prepare_menu(root)
    input = prep.InputPreparator().prepare_input(root)
    bottom_box = prep.BottomBoxPreparator().prepare_bottom_box(root)
    words_length = prep.WordsLengthPreparator().prepare_words_length(bottom_box)
    prep.OSLabelPreparator().prepare_os_label(bottom_box)
    value = input.bind(
        "<KeyRelease>", func.InputChangeProcessor(input, words_length).get_input_length
    )

    root.config(menu=menubar)
    root.mainloop()
