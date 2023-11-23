import student.student_frame_factory as sff

def go_to_register_card(frame) -> None:
    sff.StudentFrameFactory.get_frame("RegisterCardFrame", frame.window)
    frame.destroy()